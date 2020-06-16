"""catalog table

Revision ID: e6204b388f2d
Revises: 
Create Date: 2020-06-16 12:23:37.561873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6204b388f2d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Catalog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('Name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Catalog')
    # ### end Alembic commands ###