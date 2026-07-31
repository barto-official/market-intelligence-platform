"""Smoke tests for the mip package."""

import mip
from mip.hello import add


def test_package_exports_add() -> None:
    """The package root re-exports add from hello."""
    assert mip.add is add


def test_add() -> None:
    """add returns the sum of two integers."""
    assert add(2, 3) == 5
