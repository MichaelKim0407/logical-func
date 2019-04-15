from ._base import (
    Function as _Function,
)

true = _Function(lambda *args, **kwargs: True)
false = ~true

is_true = _Function(lambda x: x is True)
is_false = _Function(lambda x: x is False)

eval_true = _Function(bool)
eval_false = ~eval_true
