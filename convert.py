from typing import Iterable
from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class Base_10_Number:
    integer_part: int
    fractional_part: int


@dataclass(frozen=True)
class Base_N_Number:
    base: int
    integer_part: Iterable[int]
    fractional_part: Iterable[int]


def to_base_10(n: Base_N_Number):
    result_integer_part = 0
    mult = 1
    for d in n.integer_part[::-1]:
        assert 0 <= d < n.base
        result_integer_part += d * mult
        mult *= n.base

    result_fractional_part = 0
    mult = 1 / n.base
    for d in n.fractional_part:
        assert 0 <= d < n.base
        result_fractional_part += d * mult
        mult /= n.base

    return Base_10_Number(result_integer_part, result_fractional_part)


def from_base_10(n: Base_10_Number, to_base: int, max_num_fraction_digits: int):
    integer_part = n.integer_part
    fractional_part = n.fractional_part

    result_integer_part = deque()
    while integer_part != 0:
        quotient = integer_part // to_base
        remainder = integer_part - quotient * to_base
        result_integer_part.appendleft(remainder)
        integer_part = quotient

    result_fractional_part = deque()
    for _ in range(max_num_fraction_digits):
        mult_result = fractional_part * to_base
        mult_result_integer_part = int(mult_result // 1)
        result_fractional_part.append(mult_result_integer_part)

        mult_result_fractional_part = mult_result - mult_result_integer_part
        fractional_part = mult_result_fractional_part
        if fractional_part == 0:
            break

    return Base_N_Number(to_base, result_integer_part, result_fractional_part)
