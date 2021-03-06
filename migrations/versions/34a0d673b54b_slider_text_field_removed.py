"""slider_text_field_removed

Revision ID: 34a0d673b54b
Revises: 1c82ae10d083
Create Date: 2020-07-28 14:19:58.586180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34a0d673b54b'
down_revision = '1c82ae10d083'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Slider_Text_key', 'Slider', type_='unique')
    op.drop_column('Slider', 'Text RU')
    op.drop_column('Slider', 'Text')
    op.drop_column('Slider', 'Text UK')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Slider', sa.Column('Text UK', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('Slider', sa.Column('Text', sa.TEXT(), autoincrement=False, nullable=False))
    op.add_column('Slider', sa.Column('Text RU', sa.TEXT(), autoincrement=False, nullable=True))
    op.create_unique_constraint('Slider_Text_key', 'Slider', ['Text'])
    # ### end Alembic commands ###
