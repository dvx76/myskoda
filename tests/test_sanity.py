"""Unit tests for myskoda.auth."""

from unittest.mock import patch

from myskoda.auth.authorization import random_nonce


@patch("myskoda.auth.authorization.random_nonce", return_value="fuck-this")
def test_get_info(bullshit) -> None:
    assert random_nonce() == "fuck-this"
