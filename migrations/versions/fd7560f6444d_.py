"""empty message

Revision ID: fd7560f6444d
Revises: 
Create Date: 2024-03-16 00:30:19.558153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd7560f6444d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('bedrooms', sa.Integer(), nullable=True),
    sa.Column('bathrooms', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.Column('photo_filename', sa.String(length=160), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property')
    # ### end Alembic commands ###