# stdlib
from typing import Any, Callable, Iterable, List, Optional, Tuple, TypeVar, overload

# this package
from natsort import utils as utils
from natsort.ns_enum import NS_DUMB as NS_DUMB
from natsort.ns_enum import ns as ns

_T = TypeVar("_T")

def decoder(encoding: str) -> Callable: ...  # TODO: perhaps overloaded Callback Protocol?

@overload
def as_ascii(s: bytes) -> str: ...

@overload
def as_ascii(s: object) -> object: ...

@overload
def as_utf8(s: bytes) -> str: ...

@overload
def as_utf8(s: object) -> object: ...

def natsort_keygen(key: Optional[Callable[[Any], Any]] = ..., alg: ns = ...) -> Callable: ...

natsort_key: Callable  # TODO: matches rtype of above

def natsorted(
		seq: Iterable[_T],
		key: Optional[Callable[[Any], Any]] = ...,
		reverse: bool = ...,
		alg: ns = ...,
		) -> List[_T]: ...

def humansorted(
		seq: Iterable[_T],
		key: Optional[Callable[[Any], Any]] = ...,
		reverse: bool = ...,
		alg: ns = ...,
		) -> List[_T]: ...

def realsorted(
		seq: Iterable[_T],
		key: Optional[Callable[[Any], Any]] = ...,
		reverse: bool = ...,
		alg: ns = ...,
		) -> List[_T]: ...

def index_natsorted(
		seq: Iterable,
		key: Optional[Callable[[Any], Any]] = ...,
		reverse: bool = ...,
		alg: ns = ...,
		) -> Tuple[int, ...]: ...

def index_humansorted(
		seq: Iterable,
		key: Optional[Callable[[Any], Any]] = ...,
		reverse: bool = ...,
		alg: ns = ...
		) -> Tuple[int, ...]: ...

def index_realsorted(
		seq: Iterable,
		key: Optional[Callable[[Any], Any]] = ...,
		reverse: bool = ...,
		alg: ns = ...,
		) -> Tuple[int, ...]: ...

@overload
def order_by_index(
		seq: List[_T],
		index: Iterable[int],
		iter: bool = ...,  # noqa: A002
		) -> List[_T]: ...

@overload
def order_by_index(
		seq: Iterable[_T],
		index: Iterable[int],
		iter: bool = ...,  # noqa: A002
		) -> Iterable[_T]: ...

def numeric_regex_chooser(alg: ns) -> str: ...
def os_sort_keygen(key: Optional[Any] = ...) -> Callable: ...

os_sort_key = Callable  # TODO: matches rtype of above

def os_sorted(seq: Iterable[_T], key: Optional[Callable[[Any], Any]] = ..., reverse: bool = ...) -> List[_T]: ...
