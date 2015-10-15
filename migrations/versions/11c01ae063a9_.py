"""empty message

Revision ID: 11c01ae063a9
Revises: 2015-10-14 22:34:54.420245
Create Date: 2015-10-15 00:41:29.356092

"""

# revision identifiers, used by Alembic.
revision = '11c01ae063a9'
down_revision = '2015-10-14 22:34:54.420245'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'family_name',
               existing_type=sa.VARCHAR(length=120))
    op.alter_column('users', 'given_name',
               existing_type=sa.VARCHAR(length=50))
    op.alter_column('users', 'pw_hash',
               existing_type=sa.VARCHAR(length=600))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'pw_hash',
               existing_type=sa.VARCHAR(length=600),
               nullable=True)
    op.alter_column('users', 'given_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('users', 'family_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    ### end Alembic commands ###
