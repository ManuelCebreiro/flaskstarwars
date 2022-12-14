"""empty message

Revision ID: ff7986dea7b0
Revises: 71c4bc1b3723
Create Date: 2022-08-09 11:38:06.748820

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ff7986dea7b0'
down_revision = '71c4bc1b3723'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planets', sa.Column('name', sa.String(length=250), nullable=True))
    op.add_column('planets', sa.Column('population', sa.Integer(), nullable=True))
    op.add_column('planets', sa.Column('climate', sa.String(length=250), nullable=True))
    op.add_column('planets', sa.Column('terrain', sa.String(length=250), nullable=True))
    op.add_column('planets', sa.Column('rotation_period', sa.Integer(), nullable=True))
    op.add_column('planets', sa.Column('orbital_period', sa.Integer(), nullable=True))
    op.drop_column('planets', 'Rotation_period')
    op.drop_column('planets', 'Terrain')
    op.drop_column('planets', 'Orbital_period')
    op.drop_column('planets', 'Climate')
    op.drop_column('planets', 'Population')
    op.drop_column('planets', 'Name')
    op.add_column('vehicles', sa.Column('name', sa.String(length=250), nullable=True))
    op.add_column('vehicles', sa.Column('model', sa.String(length=250), nullable=True))
    op.add_column('vehicles', sa.Column('vehicles_class', sa.String(length=250), nullable=True))
    op.add_column('vehicles', sa.Column('length', sa.String(length=250), nullable=True))
    op.add_column('vehicles', sa.Column('cargo_capacity', sa.String(length=250), nullable=True))
    op.add_column('vehicles', sa.Column('max_Speed', sa.Integer(), nullable=True))
    op.drop_column('vehicles', 'Name')
    op.drop_column('vehicles', 'Cargo_capacity')
    op.drop_column('vehicles', 'Max_Speed')
    op.drop_column('vehicles', 'Vehicles_class')
    op.drop_column('vehicles', 'Length')
    op.drop_column('vehicles', 'Model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vehicles', sa.Column('Model', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('vehicles', sa.Column('Length', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('vehicles', sa.Column('Vehicles_class', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('vehicles', sa.Column('Max_Speed', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('vehicles', sa.Column('Cargo_capacity', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('vehicles', sa.Column('Name', mysql.VARCHAR(length=250), nullable=True))
    op.drop_column('vehicles', 'max_Speed')
    op.drop_column('vehicles', 'cargo_capacity')
    op.drop_column('vehicles', 'length')
    op.drop_column('vehicles', 'vehicles_class')
    op.drop_column('vehicles', 'model')
    op.drop_column('vehicles', 'name')
    op.add_column('planets', sa.Column('Name', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('planets', sa.Column('Population', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('planets', sa.Column('Climate', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('planets', sa.Column('Orbital_period', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('planets', sa.Column('Terrain', mysql.VARCHAR(length=250), nullable=True))
    op.add_column('planets', sa.Column('Rotation_period', mysql.VARCHAR(length=250), nullable=True))
    op.drop_column('planets', 'orbital_period')
    op.drop_column('planets', 'rotation_period')
    op.drop_column('planets', 'terrain')
    op.drop_column('planets', 'climate')
    op.drop_column('planets', 'population')
    op.drop_column('planets', 'name')
    # ### end Alembic commands ###
