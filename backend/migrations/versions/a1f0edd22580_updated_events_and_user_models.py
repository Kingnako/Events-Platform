"""Updated events and user models

Revision ID: a1f0edd22580
Revises: ed7710da19d9
Create Date: 2023-09-28 16:09:38.962635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1f0edd22580'
down_revision = 'ed7710da19d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_events', sa.Column('event_id', sa.String(length=255), nullable=False))
    op.create_foreign_key(None, 'user_events', 'events', ['event_id'], ['event_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_events', type_='foreignkey')
    op.drop_column('user_events', 'event_id')
    # ### end Alembic commands ###