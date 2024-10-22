"""initial models

Revision ID: fdd0bb2cb836
Revises:
Create Date: 2024-08-03 19:42:15.204117

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "fdd0bb2cb836"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "officers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("badge_number", sa.String(), nullable=True),
        sa.Column("hashed_password", sa.String(), nullable=True),
        sa.Column(
            "role",
            sa.Enum("ADMIN", "OFFICER", name="roleenum"),
            nullable=False,
            server_default="OFFICER",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_officers_badge_number"), "officers", ["badge_number"], unique=True
    )
    op.create_index(op.f("ix_officers_id"), "officers", ["id"], unique=False)
    op.create_index(op.f("ix_officers_name"), "officers", ["name"], unique=False)
    op.create_table(
        "people",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_people_email"), "people", ["email"], unique=True)
    op.create_index(op.f("ix_people_id"), "people", ["id"], unique=False)
    op.create_index(op.f("ix_people_name"), "people", ["name"], unique=False)
    op.create_table(
        "vehicles",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("license_plate", sa.String(), nullable=True),
        sa.Column("brand", sa.String(), nullable=True),
        sa.Column("color", sa.String(), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["owner_id"], ["people.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_vehicles_brand"), "vehicles", ["brand"], unique=False)
    op.create_index(op.f("ix_vehicles_color"), "vehicles", ["color"], unique=False)
    op.create_index(op.f("ix_vehicles_id"), "vehicles", ["id"], unique=False)
    op.create_index(
        op.f("ix_vehicles_license_plate"), "vehicles", ["license_plate"], unique=True
    )
    op.create_table(
        "infractions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("license_plate", sa.String(), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("comments", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["license_plate"], ["vehicles.license_plate"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_infractions_id"), "infractions", ["id"], unique=False)
    op.create_index(
        op.f("ix_infractions_license_plate"),
        "infractions",
        ["license_plate"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_infractions_license_plate"), table_name="infractions")
    op.drop_index(op.f("ix_infractions_id"), table_name="infractions")
    op.drop_table("infractions")
    op.drop_index(op.f("ix_vehicles_license_plate"), table_name="vehicles")
    op.drop_index(op.f("ix_vehicles_id"), table_name="vehicles")
    op.drop_index(op.f("ix_vehicles_color"), table_name="vehicles")
    op.drop_index(op.f("ix_vehicles_brand"), table_name="vehicles")
    op.drop_table("vehicles")
    op.drop_index(op.f("ix_people_name"), table_name="people")
    op.drop_index(op.f("ix_people_id"), table_name="people")
    op.drop_index(op.f("ix_people_email"), table_name="people")
    op.drop_table("people")
    op.drop_index(op.f("ix_officers_name"), table_name="officers")
    op.drop_index(op.f("ix_officers_id"), table_name="officers")
    op.drop_index(op.f("ix_officers_badge_number"), table_name="officers")
    op.drop_table("officers")
    op.execute("DROP TYPE roleenum")
    # ### end Alembic commands ###
