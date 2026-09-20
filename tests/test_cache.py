import json
from pathlib import Path

import pytest
from pytest import MonkeyPatch

from seriousdb.cache import Cache


def boom(*args, **kwargs):
    raise RuntimeError("simulated crash mid-flush")


def test_flush_failure_does_not_corrupt_existing_file(
    tmp_path: Path, monkeypatch: MonkeyPatch
):
    db_file = tmp_path / ".sdb"
    cache = Cache()
    cache.load(str(db_file))
    cache.insert("name", "Alice")
    cache.flush()
    original_content = db_file.read_bytes()

    cache.insert("name", "Bob")

    monkeypatch.setattr(json, "dumps", boom)

    with pytest.raises(RuntimeError):
        cache.flush()

    assert db_file.read_bytes() == original_content
