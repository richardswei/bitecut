"""top

Revision ID: 59b86c7636d7
Revises: bdcc1eeab4fc
Create Date: 2019-12-05 17:38:53.130474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59b86c7636d7'
down_revision = 'bdcc1eeab4fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('top_posts',
    sa.Column('rank', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('forum_id', sa.Integer(), nullable=False),
    sa.Column('subscribers', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id', 'forum_id'], ['post.post_id', 'post.forum_id'], name='fk_top_posts_i'),
    sa.PrimaryKeyConstraint('rank')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('top_posts')
    # ### end Alembic commands ###