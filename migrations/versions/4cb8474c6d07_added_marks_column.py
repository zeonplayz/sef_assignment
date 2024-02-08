"""Added marks column

Revision ID: 4cb8474c6d07
Revises: 742dcad5ea9e
Create Date: 2024-02-08 19:00:39.211228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cb8474c6d07'
down_revision = '742dcad5ea9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.add_column(sa.Column('marks', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('submission', schema=None) as batch_op:
        batch_op.drop_column('marks')

    # ### end Alembic commands ###
