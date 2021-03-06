"""hi

Revision ID: d1a2745dfc73
Revises: ef80c6169104
Create Date: 2019-12-07 22:02:06.074530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1a2745dfc73'
down_revision = 'ef80c6169104'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prescription', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('prescription', sa.Column('notify', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('prescription', 'notify')
    op.drop_column('prescription', 'active')
    # ### end Alembic commands ###
