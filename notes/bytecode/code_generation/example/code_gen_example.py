import dis
import io
from types import CodeType, FunctionType
from typing import Any, Callable, List, NamedTuple, Tuple


# Opcodes
_LOAD_FAST = dis.opname.index('LOAD_FAST')
_LOAD_CONST = dis.opname.index('LOAD_CONST')
_COMPARE_OP = dis.opname.index('COMPARE_OP')
_JUMP_IF_FALSE_OR_POP = dis.opname.index('JUMP_IF_FALSE_OR_POP')
_RETURN_VALUE = dis.opname.index('RETURN_VALUE')


class Comparison(NamedTuple):
    variable_index: int
    comparison_op: int
    test_value: Any


def make_fast_comparator(
    num_args: int,
    comparisons: List[Comparison],
    filename: str = '__generated-code__',
    func_name: str = '_compiled_CompareKey',
) -> Callable:
    constants: Tuple[Any, ...]
    if not comparisons:
        # If no comparisons, we return True
        constants = (None, True)
        bytecode = bytes([_LOAD_CONST, 1, _RETURN_VALUE, 0])
        line_no_tab = bytes([0, 1])
    else:
        constants = (None, *(compare[2] for compare in comparisons))

        COMPARISON_LENGTH = 4 * 2
        writer = io.BytesIO()
        return_address = COMPARISON_LENGTH * len(comparisons) - 2
        if return_address > 255:
            raise RuntimeError(
                'Handling jumps of more than 255 bytes would require more '
                'complex code'
            )
        
        line_no_writer = io.BytesIO()
        last_line_start = 0

        def increment_line() -> None:
            nonlocal last_line_start
            curr_pos = writer.tell()
            line_no_writer.write(bytes([curr_pos - last_line_start, 1]))
            last_line_start = curr_pos
        
        for op_num, comparison in enumerate(comparisons):
            index, cmp_op, _ = comparison
            if index < 0 or index >= num_args:
                raise ValueError(
                    f'Got bad index {index} for comparison request with only '
                    f'{num_args} arguments.'
                )
            if cmp_op < 0 or cmp_op >= len(dis.cmp_op) - 1:
                raise ValueError(f'Got bad comparison operation {cmp_op}')
            
            increment_line()
            writer.write(
                bytes([_LOAD_FAST, index, _LOAD_CONST, op_num + 1, _COMPARE_OP, cmp_op])
            )

            if op_num != len(comparisons) - 1:
                writer.write(bytes([_JUMP_IF_FALSE_OR_POP, return_address]))
            else:
                increment_line()
                writer.write(bytes([_RETURN_VALUE, 0]))
        
        bytecode = writer.getvalue()
        line_no_tab = line_no_writer.getvalue()
    
    print(bytecode)

    code = CodeType(
        num_args,                                     # argcount,             #   integer
        0,                                            # kwonlyargcount,       #   integer
        num_args,                                     # nlocals,              #   integer
        2,                                            # stacksize,            #   integer
        0,                                            # flags,                #   integer
        bytecode,                                     # codestring,           #   bytes
        constants,                                    # consts,               #   tuple
        tuple(),                                      # names,                #   tuple
        tuple(f'arg{i}' for i in range(num_args)),    # varnames,             #   tuple
        tuple(),                                      # freevars,             #   tuple
        tuple(),                                      # cellvars              #   tuple
        filename,                                     # filename,             #   string
        func_name,                                    # name,                 #   string
        0,                                            # firstlineno,          #   integer
        line_no_tab,                                  # lnotab,               #   bytes
    )

    return FunctionType(code, {})
