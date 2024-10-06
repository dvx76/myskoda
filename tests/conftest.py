"""Test helpers."""

from collections.abc import AsyncGenerator, Generator
from typing import Any
from unittest.mock import patch

import pytest
from aioresponses import aioresponses


@pytest.fixture(name="responses")
def aioresponses_fixture() -> Generator[aioresponses, None, None]:
    """Return aioresponses fixture."""
    with aioresponses() as mocked_responses:
        yield mocked_responses


@pytest.fixture(name="nonce")
def _mock_nonce() -> Generator[Any, None, None]:
    """Mock nonce."""
    print("PATCH CALLED!")
    with patch(
        "myskoda.auth.authorization.random_nonce",
        return_value="f0a57298-a276-4b3f-8bc1-c5f97f23d681",
    ) as patched:
        yield patched


@pytest.fixture(name="verifier")
async def _mock_verifier() -> AsyncGenerator[None, None]:
    """Mock verifier."""
    with patch("myskoda.auth.authorization.random_verifier", return_value="abcdefghabcdefgh"):
        yield
