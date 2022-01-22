"""Initial Migration

Revision ID: 0aac2a6637e0
Revises: 
Create Date: 2022-01-22 07:57:07.523639

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0aac2a6637e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('server',
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('updated', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.VARCHAR(length=63), nullable=False),
    sa.Column('version', sa.VARCHAR(length=12), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('server')
    # ### end Alembic commands ###