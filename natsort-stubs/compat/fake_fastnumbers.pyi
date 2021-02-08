# stdlib
from typing import Any, Optional

# this package
from natsort.unicode_numbers import decimal_chars as decimal_chars

NAN_INF: Any
ASCII_NUMS: str
POTENTIAL_FIRST_CHAR: Any

def fast_float(
		x: Any,
		key: Any = ...,
		nan: Optional[Any] = ...,
		_uni: Any = ...,
		_nan_inf: Any = ...,
		_first_char: Any = ...
		): ...

def fast_int(x: Any, key: Any = ..., _uni: Any = ..., _first_char: Any = ...): ...
