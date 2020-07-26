"""novation_table

Revision ID: 4429a94265cd
Revises: a9eeccc7a4a0
Create Date: 2020-07-25 13:32:49.237535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4429a94265cd'
down_revision = 'a9eeccc7a4a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Novation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Background', sa.Unicode(length=128), nullable=False),
    sa.Column('Title', sa.String(length=80), nullable=False),
    sa.Column('Title RU', sa.String(length=80), nullable=True),
    sa.Column('Title UK', sa.String(length=80), nullable=True),
    sa.Column('Text', sa.TEXT(), nullable=False),
    sa.Column('Text RU', sa.TEXT(), nullable=True),
    sa.Column('Text UK', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Text'),
    sa.UniqueConstraint('Title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Novation')
    # ### end Alembic commands ###
