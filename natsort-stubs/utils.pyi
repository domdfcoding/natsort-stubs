# stdlib
import pathlib
from typing import (
		Any,
		Callable,
		Iterable,
		Iterator,
		List,
		Match,
		Optional,
		Pattern,
		Tuple,
		TypeVar,
		Union,
		overload
		)

# this package
from natsort.compat.fastnumbers import fast_float as fast_float
from natsort.compat.fastnumbers import fast_int as fast_int
from natsort.compat.locale import get_decimal_point as get_decimal_point
from natsort.compat.locale import get_strxfrm as get_strxfrm
from natsort.compat.locale import get_thousands_sep as get_thousands_sep
from natsort.ns_enum import NS_DUMB as NS_DUMB
from natsort.ns_enum import ns as ns
from natsort.unicode_numbers import digits_no_decimals as digits_no_decimals
from natsort.unicode_numbers import numeric_no_decimals as numeric_no_decimals

_T = TypeVar("_T")

class NumericalRegularExpressions:
	numeric: str = ...
	digits: str = ...
	exp: str = ...
	float_num: str = ...

	@classmethod
	def int_sign(cls) -> Pattern: ...

	@classmethod
	def int_nosign(cls) -> Pattern: ...

	@classmethod
	def float_sign_exp(cls) -> Pattern: ...

	@classmethod
	def float_nosign_exp(cls) -> Pattern: ...

	@classmethod
	def float_sign_noexp(cls) -> Pattern: ...

	@classmethod
	def float_nosign_noexp(cls) -> Pattern: ...

def regex_chooser(alg: ns) -> Pattern: ...

def natsort_key(
		val: Union[str, bytes, int, float, Iterable],
		key: Optional[Callable],
		string_func: Callable[..., Tuple],
		bytes_func: Callable[..., Tuple],
		num_func: Callable[..., Tuple],
		) -> Tuple: ...

def parse_bytes_factory(alg: ns) -> Callable[[bytes], Tuple[bytes, ...]]: ...
def parse_number_or_none_factory(alg: ns, sep: str, pre_sep: str) -> Callable[[float], Tuple]: ...

def parse_string_factory(
		alg: ns,
		sep: str,
		splitter: Callable[[str], Iterable[str]],
		input_transform: Callable[..., str],
		component_transform: Callable[[str], Union[str, float]],
		final_transform: Callable[[Tuple, str], Tuple]
		) -> Callable[[str], Tuple]: ...

def parse_path_factory(str_split: Callable[[str], Tuple]): ...
def sep_inserter(iterable: Iterable[_T], sep: str) -> Iterator[Union[_T, str]]: ...
def input_string_transform_factory(alg: ns) -> Callable[..., str]: ...
def string_component_transform_factory(alg: ns) -> Callable[[str], Union[str, float]]: ...
def final_data_transform_factory(alg: ns, sep: str, pre_sep: str) -> Callable[[Tuple, str], Tuple]: ...

lower_function: Callable[..., Any]

def groupletters(x: str, _low: Callable[..., Any] = ...) -> str: ...
def chain_functions(functions: List[Callable[[Any], Any]]) -> Callable[[Any], Any]: ...

@overload
def do_decoding(s: bytes, encoding: str) -> str: ...

@overload
def do_decoding(s: object, encoding: str) -> object: ...

def path_splitter(
		s: Union[str, pathlib.Path],
		_d_match: Callable[[str, int, int], Optional[Match[str]]] = ...,
		) -> Tuple: ...
