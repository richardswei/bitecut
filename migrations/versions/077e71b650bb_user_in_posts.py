"""user in posts

Revision ID: 077e71b650bb
Revises: 7ce0749575e3
Create Date: 2019-12-05 20:40:15.383052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '077e71b650bb'
down_revision = '7ce0749575e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'user_id')
    # ### end Alembic commands ###
