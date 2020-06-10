try:
    from contextlib import asynccontextmanager
except ImportError:  # pragma: no cover
    # Python 3.6
    from async_generator import asynccontextmanager  # type: ignore  # noqa: F401
