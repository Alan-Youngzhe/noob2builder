$ErrorActionPreference = "Stop"

$Repo = if ($env:NOOB2BUILDER_REPO) {
    $env:NOOB2BUILDER_REPO
} else {
    "https://github.com/Alan-Youngzhe/noob2builder.git"
}

$Target = if ($env:NOOB2BUILDER_DIR) {
    $env:NOOB2BUILDER_DIR
} else {
    Join-Path $HOME ".claude\skills\nb"
}
$Legacy = Join-Path $HOME ".claude\skills\noob2builder"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Noob2Builder needs Git. Open Claude Code and ask: 帮我检查并安装 Git，安装后运行 git --version 验证。"
}

$Parent = Split-Path -Parent $Target
New-Item -ItemType Directory -Force -Path $Parent | Out-Null

# 旧版装在 skills\noob2builder（命令 /noob2builder），新版改为 skills\nb（命令 /nb）。
# 只在使用默认安装位置时迁移；改名即可保留本地修改，学习存档 ~/.noob2builder/ 不受影响。
if (-not $env:NOOB2BUILDER_DIR -and (Test-Path $Legacy)) {
    if (Test-Path $Target) {
        throw "Found both the old install ($Legacy) and the new one ($Target). Keeping both would register /noob2builder and /nb at the same time. Check the old folder for anything you want to keep, remove it, then run this installer again."
    } elseif (Test-Path (Join-Path $Legacy ".git")) {
        Move-Item -Path $Legacy -Destination $Target
        Write-Host "Moved old install to: $Target  (command is now /nb)"
    } else {
        throw "Old folder exists but is not a Git checkout: $Legacy. Move it to a backup location and retry."
    }
}

if (-not (Test-Path $Target)) {
    & git clone --depth 1 $Repo $Target
    if ($LASTEXITCODE -ne 0) { throw "git clone failed" }
} elseif (Test-Path (Join-Path $Target ".git")) {
    $Dirty = & git -C $Target status --porcelain
    if ($LASTEXITCODE -ne 0) { throw "git status failed" }
    if ($Dirty) {
        throw "Refusing to overwrite local changes in $Target. Review or commit them before updating."
    }
    & git -C $Target pull --ff-only
    if ($LASTEXITCODE -ne 0) { throw "git pull --ff-only failed" }
} else {
    throw "Target exists but is not a Git checkout: $Target. Move it to a backup location and retry."
}

if (-not (Test-Path (Join-Path $Target "SKILL.md"))) {
    throw "Install verification failed: SKILL.md is missing"
}

$Python = Get-Command python -ErrorAction SilentlyContinue
if ($Python) {
    & python (Join-Path $Target "scripts\validate_school.py")
    if ($LASTEXITCODE -ne 0) { throw "Noob2Builder validation failed" }
}

Write-Host ""
Write-Host "Noob2Builder is ready at: $Target"
Write-Host "Open a new Claude Code session and type: /nb"
