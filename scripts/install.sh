#!/usr/bin/env bash
set -euo pipefail

repo="${NOOB2BUILDER_REPO:-https://github.com/Alan-Youngzhe/noob2builder.git}"
target="${NOOB2BUILDER_DIR:-$HOME/.claude/skills/noob2builder}"

if ! command -v git >/dev/null 2>&1; then
  echo "Noob2Builder needs Git for safe install and updates." >&2
  echo "Open Claude Code and ask: 帮我检查并安装 Git，安装后运行 git --version 验证。" >&2
  exit 1
fi

mkdir -p "$(dirname "$target")"

if [ ! -e "$target" ]; then
  git clone --depth 1 "$repo" "$target"
elif [ -d "$target/.git" ]; then
  if [ -n "$(git -C "$target" status --porcelain)" ]; then
    echo "Refusing to overwrite local changes in: $target" >&2
    echo "Ask Claude Code to review or commit those changes before updating." >&2
    exit 1
  fi
  git -C "$target" pull --ff-only
else
  echo "Target exists but is not a Git checkout: $target" >&2
  echo "Move it to a backup location, then run this installer again." >&2
  exit 1
fi

test -f "$target/SKILL.md"

if command -v python3 >/dev/null 2>&1; then
  python3 "$target/scripts/validate_school.py"
fi

echo
echo "Noob2Builder is ready at: $target"
echo "Open a new Claude Code session and say: 带我学 AI"
