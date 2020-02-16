"""try again

Revision ID: 473018675535
Revises: 05a918b0a9de
Create Date: 2019-12-05 15:26:58.978316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '473018675535'
down_revision = '05a918b0a9de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forum_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_forum_role_default'), 'forum_role', ['default'], unique=False)
    op.create_table('forum_members',
    sa.Column('forum_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('anonymous', sa.Boolean(), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['forum_id'], ['forum.forum_id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['forum_role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('forum_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('forum_members')
    op.drop_index(op.f('ix_forum_role_default'), table_name='forum_role')
    op.drop_table('forum_role')
    # ### end Alembic commands ###