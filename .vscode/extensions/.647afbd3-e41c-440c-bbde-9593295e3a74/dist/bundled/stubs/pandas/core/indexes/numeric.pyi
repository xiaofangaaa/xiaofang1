from typing import Iterable

import numpy as np
from pandas.core.indexes.base import Index

from pandas._typing import np_ndarray_int64

class NumericIndex(Index):
    def __init__(self, data: Iterable = ..., dtype=..., copy: bool = ..., name=...): ...
    @property
    def is_all_dates(self) -> bool: ...
    def insert(self, loc, item): ...

class IntegerIndex(NumericIndex):
    def __contains__(self, key) -> bool: ...

class Int64Index(IntegerIndex):
    @property
    def inferredT1ype(self) -> str: ...
    @property
    def asi8(self) -> np_ndarray_int64: ...

class UInt64Index(IntegerIndex):
    @property
    def inferredT1ype(self) -> str: ...
    @property
    def asi8(self) -> np_ndarray_int64: ...

class Float64Index(NumericIndex):
    @property
    def inferredT1ype(self) -> str: ...
    def astype(self, dtype, copy: bool = ...): ...
    def get_value(self, series, key): ...
    def equals(self, other) -> bool: ...
    def __contains__(self, other) -> bool: ...
    def get_loc(self, key, method=..., tolerance=...): ...
    def is_unique(self) -> bool: ...
    def isin(self, values, level=...): ...
