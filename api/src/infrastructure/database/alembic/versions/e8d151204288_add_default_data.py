"""add default data

Revision ID: e8d151204288
Revises: fdd0bb2cb836
Create Date: 2024-08-04 09:42:31.169327

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e8d151204288"
down_revision: Union[str, None] = "fdd0bb2cb836"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO people (id, name, email) VALUES
        (1, 'Jorge Perez', 'jperez@example.com'),
        (2, 'Alberto Ramirez', 'aramirez@example.com')
        """
    )

    op.execute(
        """
        INSERT INTO vehicles (id, license_plate, brand, color, owner_id) VALUES
        (1, 'AAA111', 'Toyota', 'Rojo', 1),
        (2, 'BBB222', 'Honda', 'Azul', 2),
        (3, 'CCC333', 'Ford', 'Rojo', 2)
        """
    )


def downgrade() -> None:
    op.execute(
        "DELETE FROM vehicles WHERE license_plate IN ('AAA111', 'BBB222', 'CCC333')"
    )
    op.execute(
        "DELETE FROM people WHERE email IN ('jperez@example.com', 'aramirez@example.com')"
    )
