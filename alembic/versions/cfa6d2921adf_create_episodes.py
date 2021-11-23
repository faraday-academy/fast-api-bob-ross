"""create episodes

Revision ID: cfa6d2921adf
Revises: 
Create Date: 2021-11-23 09:08:49.872045

"""
import os
import json
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfa6d2921adf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    episodes = op.create_table(
        'episodes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(100), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('season', sa.Integer, nullable=False),
        sa.Column('date', sa.String(25), nullable=False),
    )

    with open(os.path.join(os.path.dirname(__file__), "../data/episodes.json")) as f:
        episode_data = f.read()

    op.bulk_insert(episodes, json.loads(episode_data))


def downgrade():
    op.drop_table('episodes')
