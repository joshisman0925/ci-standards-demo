#!/usr/bin/env bash
# 清除暫存資料夾內的檔案（示範用）
set -euo pipefail

TMP_DIR="${1:-./tmp}"
rm -rf "${TMP_DIR:?}"/*
