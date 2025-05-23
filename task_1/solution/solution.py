####################################### Вариант 1 #######################################
from types import FunctionType
from functools import wraps

def strict(func: FunctionType):
    @wraps(func)
    def wrapper(*args, **kwargs):
        keys = tuple(func.__annotations__.keys())
        for item in enumerate(args):
            if not isinstance(item[1], func.__annotations__.get(keys[item[0]])):
                raise TypeError(f"{item[1]} is not of the type {func.__annotations__.get(keys[item[0]])}")

        for k, v in kwargs.items():
            if not isinstance(v, func.__annotations__.get(k)):
                raise TypeError(f"{v[1]} is not of the type {func.__annotations__.get(k)}")

        return func(*args, **kwargs)

    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

# функция для теста декоратора для str
@strict
def say_hello(a: str, b: str) -> str:
    return f"Hello, {a} {b}!"


####################################### Вариант 2 #######################################
# проверка на соответствие типов переданных с помощью Annotated и get_type_hints
# from typing import Annotated, get_type_hints
# from functools import wraps
#
# def strict(func):
#     @wraps(func)
#     def wrapped(*args, **kwargs):
#         type_hints = get_type_hints(func, include_extras=True)
#         type_check = type_hints['return']
#         for item in tuple(args):
#             if type(item) != type_check:
#                 raise TypeError(f"{item} is not of the type {type_check}")
#
#         for item in tuple(kwargs):
#             if type(item) != type_check:
#                 raise TypeError(f"{item} is not of the type {type_check}")
#
#         return func(*args, **kwargs)
#
#     return wrapped
#
#
# @strict
# def sum_two(a: Annotated[int, int], b: Annotated[int, int]) -> int:
#     return a + b
#
# # функция для теста на соответствие типов на примере str
# @strict
# def say_hello(a: Annotated[str, str], b: Annotated [str, str]) -> str:
#     return f"Hello, {a} {b}!"





