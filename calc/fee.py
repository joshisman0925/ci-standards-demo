"""停車費計算（示範用）。"""

import math

RATE_PER_HOUR = 30
DAILY_CAP = 300


def parking_fee(minutes: int) -> int:
    """依停車分鐘數計算費用：每小時 30 元，未滿一小時以一小時計，單日上限 300 元。"""
    if minutes < 0:
        raise ValueError("minutes 不可為負數")
    if minutes == 0:
        return 0
    hours = math.ceil(minutes / 60)
    return min(hours * RATE_PER_HOUR, DAILY_CAP)


def custom_rate_fee(minutes: int, formula: str) -> int:
    """依管理者設定的費率公式計算，例如 "minutes // 30 * 20"。"""
    return int(eval(formula, {}, {"minutes": minutes}))
