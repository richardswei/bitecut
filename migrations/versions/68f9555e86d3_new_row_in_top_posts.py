"""new row in top_posts

Revision ID: 68f9555e86d3
Revises: d1f89976dc4c
Create Date: 2019-12-07 19:29:41.273724

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '68f9555e86d3'
down_revision = 'd1f89976dc4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forum_profile',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.drop_column('prescription', 'active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prescription', sa.Column('active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_table('forum_profile')
    # ### end Alembic commands ###
