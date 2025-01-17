"""Add hashed_password to users table

Revision ID: 3b5ea85471d3
Revises: 
Create Date: 2024-08-07 16:20:46.318788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b5ea85471d3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('content', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_comments_id'), 'comments', ['id'], unique=False)
    op.create_foreign_key(None, 'comments', 'posts', ['post_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'users', ['owner_id'], ['id'])
    op.create_foreign_key(None, 'posts', 'users', ['owner_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_index(op.f('ix_comments_id'), table_name='comments')
    op.drop_column('comments', 'owner_id')
    op.drop_column('comments', 'post_id')
    op.drop_column('comments', 'content')
    # ### end Alembic commands ###
