"""停車費計算（示範用）。"""

import ast
import math
import operator

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


_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
}
_UNARY_OPS = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def _eval_node(node: ast.AST, minutes: int) -> int:
    if isinstance(node, ast.Expression):
        return _eval_node(node.body, minutes)
    if isinstance(node, ast.Constant) and type(node.value) is int:
        return node.value
    if isinstance(node, ast.Name) and node.id == "minutes":
        return minutes
    if isinstance(node, ast.BinOp) and type(node.op) in _BIN_OPS:
        left = _eval_node(node.left, minutes)
        right = _eval_node(node.right, minutes)
        return _BIN_OPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPS:
        return _UNARY_OPS[type(node.op)](_eval_node(node.operand, minutes))
    raise ValueError(f"費率公式含不允許的語法：{ast.dump(node)}")


def custom_rate_fee(minutes: int, formula: str) -> int:
    """依管理者設定的費率公式計算，例如 "minutes // 30 * 20"。

    公式只允許整數、變數 minutes 與 + - * // % 運算；不使用 eval，
    避免公式被塞入任意程式碼執行。
    """
    if minutes < 0:
        raise ValueError("minutes 不可為負數")
    try:
        tree = ast.parse(formula, mode="eval")
    except SyntaxError as exc:
        raise ValueError(f"費率公式語法錯誤：{formula!r}") from exc
    return int(_eval_node(tree, minutes))
