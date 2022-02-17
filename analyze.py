from macros_sdk import *


def analyze(tree: Program) -> None:
    """Add your AST analysis code here."""
    declared_globals: set[str] = set()

    for node in tree.body:
        match node:
            case VarDeclaration(name=name_token):
                name = name_token.string

                if name_token.string in declared_globals:
                    add_issue("LX-001", f"Redeclared global {name!r}", node=node)
                else:
                    declared_globals.add(name)
