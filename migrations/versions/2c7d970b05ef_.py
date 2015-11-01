"""empty message

Revision ID: 2c7d970b05ef
Revises: 5336e67b210c
Create Date: 2015-10-31 18:15:02.418415

"""

# revision identifiers, used by Alembic.
revision = '2c7d970b05ef'
down_revision = '5336e67b210c'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('curricula',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('standardcurriculum', sa.Integer(), nullable=True),
    sa.Column('ordered_subtopics', postgresql.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['standardcurriculum'], ['standardCurricula.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('curricula_schools',
    sa.Column('curriculum_id', sa.Integer(), nullable=False),
    sa.Column('school_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['curriculum_id'], ['curricula.id'], ),
    sa.ForeignKeyConstraint(['school_id'], ['schools.id'], ),
    sa.PrimaryKeyConstraint('curriculum_id', 'school_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('curricula_schools')
    op.drop_table('curricula')
    ### end Alembic commands ###
