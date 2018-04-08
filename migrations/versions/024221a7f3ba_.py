"""empty message

Revision ID: 024221a7f3ba
Revises: 970367203e61
Create Date: 2018-02-22 07:41:27.090270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '024221a7f3ba'
down_revision = '970367203e61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('msg', sa.String(), nullable=True),
    sa.Column('todo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['todo_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todolist')
    # ### end Alembic commands ###