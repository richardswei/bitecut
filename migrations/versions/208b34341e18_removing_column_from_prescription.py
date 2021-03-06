"""removing column from prescription

Revision ID: 208b34341e18
Revises: 09cc8b4ebe0d
Create Date: 2019-12-11 20:28:44.926040

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '208b34341e18'
down_revision = '09cc8b4ebe0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('prescription', 'frequency')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prescription', sa.Column('frequency', mysql.VARCHAR(length=32), nullable=False))
    # ### end Alembic commands ###
