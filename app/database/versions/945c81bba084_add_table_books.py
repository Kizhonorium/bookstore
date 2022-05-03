"""add table books

Revision ID: 945c81bba084
Revises: dd26cb581761
Create Date: 2022-05-03 16:51:16.819546

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '945c81bba084'
down_revision = 'dd26cb581761'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', mysql.BIGINT(unsigned=True), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('price', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('currency', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_name'), 'books', ['name'], unique=True)
    op.create_index(op.f('ix_books_price'), 'books', ['price'], unique=False)
    op.create_index(op.f('ix_books_updated_at'), 'books', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_books_updated_at'), table_name='books')
    op.drop_index(op.f('ix_books_price'), table_name='books')
    op.drop_index(op.f('ix_books_name'), table_name='books')
    op.drop_table('books')
    # ### end Alembic commands ###