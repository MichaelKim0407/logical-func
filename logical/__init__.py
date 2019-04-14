from ._base import (
    BaseFunction as _BaseFunction,
)

__version__ = '1.0'


class Function(_BaseFunction):
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return self.__func(*args, **kwargs)
