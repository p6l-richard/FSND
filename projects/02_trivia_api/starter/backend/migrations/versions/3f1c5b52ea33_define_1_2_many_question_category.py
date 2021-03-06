"""Define 1-2-many: Question <> Category

Revision ID: 3f1c5b52ea33
Revises: 06be5f9a43d5
Create Date: 2020-05-12 10:00:35.386474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f1c5b52ea33'
down_revision = '06be5f9a43d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_table('categories')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('question', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('answer', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('difficulty', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name='category_id', onupdate='CASCADE', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='questions_pkey')
    )
    op.alter_column('questions', 'category', _type=Integer)
    op.create_table('categories',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='categories_pkey')
    )
    # ### end Alembic commands ###
