$ErrorActionPreference = "Stop"

$Repo = if ($env:NOOB2BUILDER_REPO) {
    $env:NOOB2BUILDER_REPO
} else {
    "https://github.com/Alan-Youngzhe/noob2builder.git"
}

$Target = if ($env:NOOB2BUILDER_DIR) {
    $env:NOOB2BUILDER_DIR
} else {
    Join-Path $HOME ".claude\skills\noob2builder"
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Noob2Builder needs Git. Open Claude Code and ask: 帮我检查并安装 Git，安装后运行 git --version 验证。"
}

$Parent = Split-Path -Parent $Target
New-Item -ItemType Directory -Force -Path $Parent | Out-Null

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
Write-Host "Open a new Claude Code session and say: 带我学 AI"
