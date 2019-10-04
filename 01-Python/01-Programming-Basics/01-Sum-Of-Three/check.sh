#!/usr/bin/env bash
CURRENT_DIR=$(pwd)
cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1
find . -iname "*.py" -not -path "./tests/*" | xargs pylint --output-format=colorized
PYTHONDONTWRITEBYTECODE=1 pytest -v --color=yes
cd $CURRENT_DIR
