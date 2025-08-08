"""Create weather_requests table

Revision ID: f1c5c2cb484d
Revises: 
Create Date: 2025-08-07 17:15:37.318313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'f1c5c2cb484d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table('weather_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_weather_requests_id'), 'weather_requests', ['id'], unique=False)



def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(op.f('ix_weather_requests_id'), table_name='weather_requests')
    op.drop_table('weather_requests')

