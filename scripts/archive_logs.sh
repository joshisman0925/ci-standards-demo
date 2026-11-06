#!/usr/bin/env bash
# 將指定資料夾的紀錄檔壓縮備份（示範用）
set -euo pipefail

LOG_DIR="${1:-./logs}"
tar -czf logs-backup.tar.gz -- "$LOG_DIR"
