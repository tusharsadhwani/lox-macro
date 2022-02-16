from ast import *
from typing import Optional

from helper import make_issue


def add_issue(
    issue_code: str,
    issue_msg: str,
    *,
    node: Optional[AST] = None,
    line: Optional[int] = None,
    col: Optional[int] = None,
) -> None:
    """Adds a new issue to report."""
    from helper import ISSUES, get_current_filepath

    if node is not None:
        if not isinstance(node, AST):
            raise ValueError("'node' must be an AST node")

        line, col = node.lineno, node.col_offset

    if line is None or col is None:
        raise ValueError(
            "Must provide either ast node or line and column to raise issue"
        )

    filepath = get_current_filepath()
    issue = make_issue(issue_code, issue_msg, filepath, line, col)
    ISSUES.append(issue)


__all__ = [
    # AST classes
    "AST",
    "Add",
    "And",
    "AnnAssign",
    "Assert",
    "Assign",
    "AsyncFor",
    "AsyncFunctionDef",
    "AsyncWith",
    "Attribute",
    "AugAssign",
    "AugLoad",
    "AugStore",
    "Await",
    "BinOp",
    "BitAnd",
    "BitOr",
    "BitXor",
    "BoolOp",
    "Break",
    "Bytes",
    "Call",
    "ClassDef",
    "Compare",
    "Constant",
    "Continue",
    "Del",
    "Delete",
    "Dict",
    "DictComp",
    "Div",
    "Ellipsis",
    "Eq",
    "ExceptHandler",
    "Expr",
    "Expression",
    "ExtSlice",
    "FloorDiv",
    "For",
    "FormattedValue",
    "FunctionDef",
    "FunctionType",
    "GeneratorExp",
    "Global",
    "Gt",
    "GtE",
    "If",
    "IfExp",
    "Import",
    "ImportFrom",
    "In",
    "Index",
    "IntEnum",
    "Interactive",
    "Invert",
    "Is",
    "IsNot",
    "JoinedStr",
    "LShift",
    "Lambda",
    "List",
    "ListComp",
    "Load",
    "Lt",
    "LtE",
    "MatMult",
    "Match",
    "MatchAs",
    "MatchClass",
    "MatchMapping",
    "MatchOr",
    "MatchSequence",
    "MatchSingleton",
    "MatchStar",
    "MatchValue",
    "Mod",
    "Module",
    "Mult",
    "Name",
    "NameConstant",
    "NamedExpr",
    "NodeTransformer",
    "NodeVisitor",
    "Nonlocal",
    "Not",
    "NotEq",
    "NotIn",
    "Num",
    "Or",
    "Param",
    "Pass",
    "Pow",
    "RShift",
    "Raise",
    "Return",
    "Set",
    "SetComp",
    "Slice",
    "Starred",
    "Store",
    "Str",
    "Sub",
    "Subscript",
    "Suite",
    "Try",
    "Tuple",
    "TypeIgnore",
    "UAdd",
    "USub",
    "UnaryOp",
    "While",
    "With",
    "Yield",
    "YieldFrom",
    "alias",
    "arg",
    "arguments",
    "auto",
    "boolop",
    "cmpop",
    "comprehension",
    "contextmanager",
    "copy_location",
    "dump",
    "excepthandler",
    "expr",
    "expr_context",
    "keyword",
    "match_case",
    "mod",
    "nullcontext",
    "operator",
    "parse",
    "pattern",
    "slice",
    "stmt",
    "type_ignore",
    "unaryop",
    "withitem",
    # Functions to expose
    "walk",
    "add_issue",
]
