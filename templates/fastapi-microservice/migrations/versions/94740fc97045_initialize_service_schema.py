"""initialize service schema

Revision ID: 94740fc97045
Revises:
Create Date: 2026-09-17 21:56:10.349048

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "94740fc97045"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""
