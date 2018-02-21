import ast
import sys

from niveristand import errormessages
from niveristand.exceptions import TranslateError
from niveristand.translation import utils
from niveristand.translation.py2rtseq import validations


def try_transformer(node, resources):
    _validate_restrictions(node)
    for stmt in node.body:
        utils.generic_ast_node_transform(stmt, resources)
    resources.set_current_block(resources.get_rtseq().Code.CleanUp)
    for stmt in node.finalbody:
        utils.generic_ast_node_transform(stmt, resources)


def except_transformer(node, resources):
    raise TranslateError(errormessages.invalid_try_except_orelse)


def _validate_restrictions(node):
    if sys.version_info > (3, 0):
        if node.handlers or node.orelse:
            raise TranslateError(errormessages.invalid_try_except_orelse)
    if validations.check_if_any_in_block(ast.Return, node.body) or \
            validations.check_if_any_in_block(ast.Return, node.finalbody):
            raise TranslateError(errormessages.return_not_supported_in_try_finally)
    validations.check_try_in_node_body(node.body)