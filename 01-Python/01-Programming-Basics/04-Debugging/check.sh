#!/usr/bin/env bash
CURRENT_DIR=$(pwd)
cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1
find . -iname "*.py" | xargs pylint --output-format=colorized
PYTHONDONTWRITEBYTECODE=1 pytest --color=yes
cd $CURRENT_DIR
