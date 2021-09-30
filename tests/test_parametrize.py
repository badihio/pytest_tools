import dataclasses

from pytest_tools import pytest_generate_tests  # noqa: I023, I005


@dataclasses.dataclass
class SumTestData:
    x: int
    y: int
    z: int
    expected: int
    id: str


sum_tests = [
    SumTestData(
        x=1,
        y=2,
        z=3,
        expected=2,
        id='all-positive-numbers',
    ),
]


@pytest_generate_tests.parametrize(
    sum_tests,
)
def test_sum(
    numbers,
    expected,
):
    assert sum(numbers) == expected
