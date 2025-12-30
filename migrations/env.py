"""Env for alembic."""  # noqa: INP001

from alembic import context
from sqlalchemy import create_engine, pool
from time_flow.db.metadata import metadata
from time_flow.utils import get_settings

settings = get_settings()
target_metadata = metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(  # pylint: disable=no-member
        url=settings.DB.url_sync,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        compare_server_default=True,
    )

    with context.begin_transaction():  # pylint: disable=no-member
        context.run_migrations()  # pylint: disable=no-member


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        settings.DB.url_sync,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(  # pylint: disable=no-member
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            compare_server_default=True,
        )

        with context.begin_transaction():  # pylint: disable=no-member
            context.run_migrations()  # pylint: disable=no-member


if context.is_offline_mode():  # pylint: disable=no-member
    run_migrations_offline()
else:
    run_migrations_online()
