from typing import Optional

from pylox import get_snippet_line_col
from pylox.nodes import *
from pylox.utils import walk

from helper import ISSUES, get_current_filepath, get_current_source, make_issue


def add_issue(
    issue_code: str,
    issue_msg: str,
    *,
    node: Optional[Node] = None,
    line: Optional[int] = None,
    col: Optional[int] = None,
) -> None:
    """Adds a new issue to report."""
    if node is not None:
        if not isinstance(node, Node):
            raise ValueError("'node' must be an AST node")

        source = get_current_source()
        line, col, _ = get_snippet_line_col(source, node.index)

    if line is None or col is None:
        raise ValueError(
            "Must provide either ast node or line and column to raise issue"
        )

    filepath = get_current_filepath()
    issue = make_issue(issue_code, issue_msg, filepath, line, col)
    ISSUES.append(issue)


__all__ = [
    # AST classes
    "Assignment",
    "Binary",
    "Block",
    "Call",
    "Declaration",
    "Expr",
    "ExprStmt",
    "For",
    "FunctionDef",
    "Grouping",
    "If",
    "Literal",
    "Node",
    "Print",
    "Program",
    "ReturnStmt",
    "Stmt",
    "Token",
    "Unary",
    "VarDeclaration",
    "Variable",
    "While",
    # Functions to expose
    "walk",
    "add_issue",
]
