"""Renaming students to scholars

Revision ID: 224d6045bdc6
Revises: 791279dd0760
Create Date: 2023-10-18 21:57:21.212869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '224d6045bdc6'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
