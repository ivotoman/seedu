"""empty message

Revision ID: 4a4973a84764
Revises: 366e57f72b33
Create Date: 2015-11-01 19:02:18.263897

"""

# revision identifiers, used by Alembic.
revision = '4a4973a84764'
down_revision = '366e57f72b33'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('curricula_schools')
    op.add_column('curricula', sa.Column('customization_table', postgresql.JSON(), nullable=True))
    op.add_column('curricula', sa.Column('school', sa.Integer(), nullable=True))
    op.add_column('curricula', sa.Column('standardcurriculum', sa.Integer(), nullable=True))
    op.drop_constraint(u'curricula_standardcurriculum_id_fkey', 'curricula', type_='foreignkey')
    op.create_foreign_key(None, 'curricula', 'standardCurricula', ['standardcurriculum'], ['id'])
    op.create_foreign_key(None, 'curricula', 'schools', ['school'], ['id'])
    op.drop_column('curricula', 'standardcurriculum_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('curricula', sa.Column('standardcurriculum_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'curricula', type_='foreignkey')
    op.drop_constraint(None, 'curricula', type_='foreignkey')
    op.create_foreign_key(u'curricula_standardcurriculum_id_fkey', 'curricula', 'standardCurricula', ['standardcurriculum_id'], ['id'])
    op.drop_column('curricula', 'standardcurriculum')
    op.drop_column('curricula', 'school')
    op.drop_column('curricula', 'customization_table')
    op.create_table('curricula_schools',
    sa.Column('curriculum_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('school_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['curriculum_id'], [u'curricula.id'], name=u'curricula_schools_curriculum_id_fkey'),
    sa.ForeignKeyConstraint(['school_id'], [u'schools.id'], name=u'curricula_schools_school_id_fkey'),
    sa.PrimaryKeyConstraint('curriculum_id', 'school_id', name=u'curricula_schools_pkey')
    )
    ### end Alembic commands ###
