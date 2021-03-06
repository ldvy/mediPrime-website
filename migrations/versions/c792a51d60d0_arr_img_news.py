"""arr_img/news

Revision ID: c792a51d60d0
Revises: 55bf43952107
Create Date: 2020-07-14 20:48:44.084614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c792a51d60d0'
down_revision = '55bf43952107'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Model', sa.Column('Brand', sa.String(length=80), nullable=True))
    op.add_column('Model', sa.Column('Brand RU', sa.String(length=80), nullable=True))
    op.add_column('Model', sa.Column('Brand UK', sa.String(length=80), nullable=True))
    op.add_column('Model', sa.Column('Country', sa.String(length=80), nullable=True))
    op.add_column('Model', sa.Column('Country RU', sa.String(length=80), nullable=True))
    op.add_column('Model', sa.Column('Country UK', sa.String(length=80), nullable=True))
    op.add_column('NewsOn', sa.Column('Text', sa.TEXT(), nullable=True))
    op.add_column('NewsOn', sa.Column('Text RU', sa.TEXT(), nullable=True))
    op.add_column('NewsOn', sa.Column('Text UK', sa.TEXT(), nullable=True))
    op.add_column('NewsOn', sa.Column('Title RU', sa.String(length=80), nullable=True))
    op.add_column('NewsOn', sa.Column('Title UK', sa.String(length=80), nullable=True))
    op.drop_column('NewsOn', 'category_id')
    op.drop_column('NewsOn', 'text')
    op.drop_constraint('reagent_Method RU_key', 'reagent', type_='unique')
    op.drop_constraint('reagent_Method Uk_key', 'reagent', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('reagent_Method Uk_key', 'reagent', ['Method Uk'])
    op.create_unique_constraint('reagent_Method RU_key', 'reagent', ['Method RU'])
    op.add_column('NewsOn', sa.Column('text', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('NewsOn', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('NewsOn', 'Title UK')
    op.drop_column('NewsOn', 'Title RU')
    op.drop_column('NewsOn', 'Text UK')
    op.drop_column('NewsOn', 'Text RU')
    op.drop_column('NewsOn', 'Text')
    op.drop_column('Model', 'Country UK')
    op.drop_column('Model', 'Country RU')
    op.drop_column('Model', 'Country')
    op.drop_column('Model', 'Brand UK')
    op.drop_column('Model', 'Brand RU')
    op.drop_column('Model', 'Brand')
    # ### end Alembic commands ###
