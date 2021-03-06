"""Add Many2Many between Venue & Artist:
1) Add junction (association) table venue_artist
2) Add Artist.venues & Venue.artists colleciton (via backref on Artist)

Revision ID: 9f38f2acf7de
Revises: 77cf86ea78fb
Create Date: 2020-04-22 16:48:43.691815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f38f2acf7de'
down_revision = '77cf86ea78fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venue_artist',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], ),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venue_artist')
    # ### end Alembic commands ###
