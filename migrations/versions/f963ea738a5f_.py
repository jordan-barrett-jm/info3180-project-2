"""empty message

Revision ID: f963ea738a5f
Revises: 73026ef6e568
Create Date: 2022-04-21 17:51:12.830431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f963ea738a5f'
down_revision = '73026ef6e568'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('make', sa.String(length=80), nullable=True),
    sa.Column('model', sa.String(length=80), nullable=True),
    sa.Column('colour', sa.String(length=80), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('year', sa.String(length=80), nullable=True),
    sa.Column('transmission', sa.String(length=80), nullable=True),
    sa.Column('car_type', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=80), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('date_joined', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('biography', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profiles')
    op.drop_table('cars')
    # ### end Alembic commands ###
