import ast

from pylox.lexer import Lexer
from pylox.parser import Parser

import analyze
from helper import (
    CODEPATH,
    ISSUES,
    get_files,
    prepare_result,
    publish_results,
    set_current_filepath,
    set_current_source,
)


def run_analysis(filepath: str) -> None:
    with open(filepath) as file:
        source = file.read()

    set_current_source(source)
    if hasattr(analyze, "analyze") and callable(analyze.analyze):
        tokens = Lexer(source).tokens
        tree, errors = Parser(tokens).parse()
        if not errors:
            analyze.analyze(tree)

    if hasattr(analyze, "analyze_source") and callable(analyze.analyze_source):
        analyze.analyze_source(source)


if __name__ == "__main__":
    for filepath in get_files(CODEPATH):
        if not filepath.endswith(".lox"):
            continue

        set_current_filepath(filepath)
        run_analysis(filepath)

    result = prepare_result(ISSUES)
    publish_results(result)
