"""empty message

Revision ID: 40a4ee01e3c9
Revises: f35c79d4e439
Create Date: 2020-03-12 21:23:18.427246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40a4ee01e3c9'
down_revision = 'f35c79d4e439'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.create_foreign_key(None, 'todos', 'categories', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.create_foreign_key(None, 'todos', 'todos', ['category_id'], ['id'])
    # ### end Alembic commands ###
