"""update models

Revision ID: 73569fa807f1
Revises: 0c63a13675f3
Create Date: 2023-03-08 15:39:05.410972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73569fa807f1'
down_revision = '0c63a13675f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=200), server_default='', nullable=False),
    sa.Column('body', sa.Text(), server_default='', nullable=False),
    sa.Column('dt_created', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('dt_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article')
    op.drop_table('author')
    # ### end Alembic commands ###