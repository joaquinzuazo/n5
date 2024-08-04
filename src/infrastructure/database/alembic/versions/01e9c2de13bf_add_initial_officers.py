"""add initial officers

Revision ID: 01e9c2de13bf
Revises: e8d151204288
Create Date: 2024-08-04 17:09:10.947168

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "01e9c2de13bf"
down_revision: Union[str, None] = "e8d151204288"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        INSERT INTO officers (id, name, badge_number, hashed_password) VALUES
        (1, 'Nico Paz', '12345', '$2b$12$CoAqpJl5XHVizb5ApjtKHOijHH.RIIpR0RFyF5ucRen7TMOLOrbkS'),
        (2, 'Leo Messi', '67890', '$2b$12$vV5GRy6xseu9RYQsr8meauqH6QKH8L6PXo0NJ3X6pWhYis5R31zMG')
        """
    )


def downgrade() -> None:
    op.execute("DELETE FROM officers WHERE badge_number IN ('12345', '67890')")