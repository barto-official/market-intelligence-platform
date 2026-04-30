"""Example API module for docstring rendering tests.

This module intentionally includes a variety of Python constructs and docstring
patterns to validate MkDocs + docstring renderers (e.g., mkdocstrings).

Conventions used here are compatible with Google-style docstrings.
"""

from __future__ import annotations

import time
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import (
    Any,
    TypeVar,
)

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        Sum of a and b.

    Examples:
        >>> add(2, 3)
        5
    """
    return a + b


class ValidationError(ValueError):
    """Raised when input validation fails."""


def slugify(text: str, *, max_length: int = 64) -> str:
    """Convert text into a URL-safe slug.

    This function is intentionally simple and deterministic to make it easy
    to test doc rendering.

    Args:
        text: Source text.
        max_length: Maximum length of the returned slug. Must be positive.

    Returns:
        A lowercase slug consisting of alphanumerics and hyphens.

    Raises:
        ValidationError: If `text` is empty or `max_length` is not positive.

    Examples:
        >>> slugify("Hello, World!")
        'hello-world'
        >>> slugify("A  B   C", max_length=3)
        'a-b'
    """
    if not text.strip():
        raise ValidationError("text must be non-empty")
    if max_length <= 0:
        raise ValidationError("max_length must be positive")

    slug = []
    prev_hyphen = False
    for ch in text.strip().lower():
        if ch.isalnum():
            slug.append(ch)
            prev_hyphen = False
        elif not prev_hyphen and slug:
            slug.append("-")
            prev_hyphen = True

    out = "".join(slug).strip("-")
    return out[:max_length].strip("-")


def chunked(items: Sequence[T], size: int) -> list[list[T]]:
    """Split a sequence into fixed-size chunks.

    Args:
        items: Input sequence.
        size: Chunk size. Must be >= 1.

    Returns:
        A list of chunks. The final chunk may be shorter.

    Raises:
        ValidationError: If `size` is less than 1.

    Examples:
        >>> chunked([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    if size < 1:
        raise ValidationError("size must be >= 1")

    return [list(items[i : i + size]) for i in range(0, len(items), size)]


def merge_maps(*maps: Mapping[K, V], conflict: str = "right") -> dict[K, V]:
    """Merge multiple mappings into one dict.

    Args:
        *maps: Any number of mappings to merge.
        conflict: Conflict resolution strategy:
            - `"right"`: later mappings win (default)
            - `"left"`: first mapping wins

    Returns:
        A new dict containing all keys from all mappings.

    Raises:
        ValidationError: If `conflict` is not supported.
    """
    if conflict not in {"right", "left"}:
        raise ValidationError("conflict must be 'right' or 'left'")

    out: dict[K, V] = {}
    if conflict == "right":
        for m in maps:
            out.update(m)
    else:
        for m in maps:
            for k, v in m.items():
                out.setdefault(k, v)

    return out


def utc_now() -> datetime:
    """Return the current UTC timestamp (timezone-aware).

    Returns:
        A timezone-aware `datetime` in UTC.
    """
    return datetime.now(UTC)


@dataclass(frozen=True, slots=True)
class User:
    """A simple user model.

    Args:
        id: Unique identifier.
        email: Email address.
        display_name: Optional human-readable name.
    """

    id: int
    email: str
    display_name: str | None = None

    @property
    def initials(self) -> str:
        """Derive initials from `display_name` (or email local-part as fallback).

        Returns:
            Uppercase initials, e.g. `"Ada Lovelace" -> "AL"`.
        """
        base = (self.display_name or self.email.split("@", 1)[0]).strip()
        parts = [p for p in base.replace("_", " ").split() if p]
        if not parts:
            return "?"
        return "".join(p[0].upper() for p in parts[:2])


@dataclass
class CacheStats:
    """Simple cache statistics container."""

    hits: int = 0
    misses: int = 0

    @property
    def total(self) -> int:
        """Return total lookups (hits + misses)."""
        return self.hits + self.misses

    @property
    def hit_rate(self) -> float:
        """Return the hit rate as a float in [0.0, 1.0].

        Returns:
            Hit rate; returns 0.0 if there are no lookups.
        """
        return (self.hits / self.total) if self.total else 0.0


class TTLCache(Iterable[tuple[str, Any]]):
    """A tiny in-memory cache with a fixed TTL.

    This class is intentionally minimal; it supports get/set and iteration.
    It is useful for documenting:
    - constructor args
    - methods
    - properties
    - iteration protocol

    Args:
        ttl_seconds: Time-to-live for entries in seconds. Must be positive.

    Raises:
        ValidationError: If `ttl_seconds` is not positive.
    """

    def __init__(self, ttl_seconds: float) -> None:
        if ttl_seconds <= 0:
            raise ValidationError("ttl_seconds must be positive")
        self._ttl = ttl_seconds
        self._data: dict[str, tuple[float, Any]] = {}
        self.stats: CacheStats = CacheStats()

    @property
    def ttl_seconds(self) -> float:
        """Configured TTL in seconds."""
        return self._ttl

    def set(self, key: str, value: Any, *, now: float | None = None) -> None:
        """Store an item in the cache.

        Args:
            key: Cache key.
            value: Value to store.
            now: Override the clock for tests (epoch seconds).
        """
        ts = time.time() if now is None else now
        self._data[key] = (ts, value)

    def get(self, key: str, default: Any = None, *, now: float | None = None) -> Any:
        """Retrieve an item if present and not expired.

        Args:
            key: Cache key.
            default: Returned if missing or expired.
            now: Override the clock for tests (epoch seconds).

        Returns:
            Cached value or `default`.
        """
        ts_now = time.time() if now is None else now
        if key not in self._data:
            self.stats.misses += 1
            return default

        ts_set, value = self._data[key]
        if (ts_now - ts_set) > self._ttl:
            self._data.pop(key, None)
            self.stats.misses += 1
            return default

        self.stats.hits += 1
        return value

    def purge(self, *, now: float | None = None) -> int:
        """Remove expired entries.

        Args:
            now: Override the clock for tests (epoch seconds).

        Returns:
            Number of entries removed.
        """
        ts_now = time.time() if now is None else now
        to_delete = [k for k, (ts, _) in self._data.items() if (ts_now - ts) > self._ttl]
        for k in to_delete:
            self._data.pop(k, None)
        return len(to_delete)

    def __iter__(self) -> Iterator[tuple[str, Any]]:  # noqa: D
        """Iterate over unexpired items as ``(key, value)`` pairs."""

        # Note: intentionally not purging; docs can describe this nuance.
        for k, (_, v) in self._data.items():
            yield (k, v)

    def __len__(self) -> int:
        """Return the number of currently stored entries (including possibly expired)."""
        return len(self._data)


class FileSession:
    """Context manager that opens a file and ensures it is closed.

    This is a good docstring test for context managers and attributes.

    Args:
        path: Path to the file.
        mode: File open mode, e.g. `"r"` or `"w"`.
        encoding: Encoding used for text modes.

    Attributes:
        path: The file path.
        mode: The open mode.
        encoding: The encoding.
        handle: The active file handle after entering the context.

    Examples:
        >>> with FileSession("example.txt", "w") as s:
        ...     _ = s.handle.write("hello")
    """

    def __init__(self, path: str | Path, mode: str = "r", encoding: str = "utf-8") -> None:
        self.path = Path(path)
        self.mode = mode
        self.encoding = encoding
        self.handle = None  # type: ignore[assignment]

    def __enter__(self) -> FileSession:
        self.handle = Path(self.path).open(self.mode, encoding=self.encoding)
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        if self.handle:
            self.handle.close()
        # Returning False propagates exceptions.
        return False


@dataclass
class Task:
    """A simple task record.

    Args:
        title: Short name.
        done: Whether the task is completed.
        tags: Optional tags.
    """

    title: str
    done: bool = False
    tags: list[str] = field(default_factory=list)


class TaskManager:
    """Manage tasks in memory.

    Provides examples of instance methods, classmethods, and staticmethods.

    Args:
        tasks: Optional initial tasks.
    """

    def __init__(self, tasks: Iterable[Task] | None = None) -> None:
        self._tasks: list[Task] = list(tasks) if tasks else []

    def add(self, title: str, *, tags: Iterable[str] | None = None) -> Task:
        """Add a new task.

        Args:
            title: Task title.
            tags: Optional tags.

        Returns:
            The created `Task`.
        """
        t = Task(title=title, tags=list(tags) if tags else [])
        self._tasks.append(t)
        return t

    def complete(self, index: int) -> Task:
        """Mark a task complete.

        Args:
            index: 0-based index.

        Returns:
            The updated `Task`.
        """
        t = self._tasks[index]
        t.done = True
        return t

    def find(self, predicate: Callable[[Task], bool]) -> list[Task]:
        """Return all tasks matching a predicate.

        Args:
            predicate: Function that returns True for tasks to include.

        Returns:
            A list of matching tasks.
        """
        return [t for t in self._tasks if predicate(t)]

    @classmethod
    def from_titles(cls, titles: Iterable[str]) -> TaskManager:
        """Create a manager from task titles.

        Args:
            titles: Task titles.

        Returns:
            A `TaskManager` with one task per title.
        """
        return cls(Task(title=t) for t in titles)

    @staticmethod
    def validate_title(title: str) -> None:
        """Validate a task title.

        Args:
            title: Proposed title.

        Raises:
            ValidationError: If the title is invalid.
        """
        if not title.strip():
            raise ValidationError("title must be non-empty")

    def __len__(self) -> int:
        """Return the number of tasks."""
        return len(self._tasks)

    def __iter__(self) -> Iterator[Task]:
        """Iterate over tasks in insertion order."""
        return iter(self._tasks)
