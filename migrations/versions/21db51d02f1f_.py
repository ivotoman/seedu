"""empty message

Revision ID: 21db51d02f1f
Revises: 1c6377177a51
Create Date: 2015-10-15 23:50:54.631320

"""

# revision identifiers, used by Alembic.
revision = '21db51d02f1f'
down_revision = '1c6377177a51'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schools')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schools',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=180), autoincrement=False, nullable=True),
    sa.Column('given_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('family_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('pw_hash', sa.VARCHAR(length=600), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'schools_pkey'),
    sa.UniqueConstraint('name', name=u'schools_name_key')
    )
    ### end Alembic commands ###