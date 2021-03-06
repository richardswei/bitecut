"""latest

Revision ID: 438311de307e
Revises: a871cc1c6296
Create Date: 2019-11-10 00:24:10.653814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '438311de307e'
down_revision = 'a871cc1c6296'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hospital',
    sa.Column('unique_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('unique_id')
    )
    op.create_table('insurance',
    sa.Column('insurance_id', sa.Integer(), nullable=False),
    sa.Column('insurance_name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('insurance_id')
    )
    op.create_table('facility',
    sa.Column('hospital_id', sa.Integer(), nullable=False),
    sa.Column('facility_num', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.unique_id'], ),
    sa.PrimaryKeyConstraint('hospital_id', 'facility_num')
    )
    op.create_index(op.f('ix_facility_facility_num'), 'facility', ['facility_num'], unique=False)
    op.create_index(op.f('ix_facility_hospital_id'), 'facility', ['hospital_id'], unique=False)
    op.create_table('nurse',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('hospital_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.unique_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('patient',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date_of_birth', sa.DateTime(), nullable=False),
    sa.Column('SSN', sa.String(length=128), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('hospital_id', sa.Integer(), nullable=True),
    sa.Column('insurance_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.unique_id'], ),
    sa.ForeignKeyConstraint(['insurance_id'], ['insurance.insurance_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('physician',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('hospital_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hospital_id'], ['hospital.unique_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('physician_schedule',
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('physician_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('event_type', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['physician_id'], ['physician.user_id'], ),
    sa.PrimaryKeyConstraint('event_id')
    )
    op.create_table('prescription',
    sa.Column('prescription_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('physician_id', sa.Integer(), nullable=False),
    sa.Column('date_prescribed', sa.Date(), nullable=False),
    sa.Column('expir_date', sa.Date(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.user_id'], ),
    sa.ForeignKeyConstraint(['physician_id'], ['physician.user_id'], ),
    sa.PrimaryKeyConstraint('prescription_id')
    )
    op.create_table('appointment',
    sa.Column('appointment_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('hospital_id', sa.Integer(), nullable=False),
    sa.Column('facility_num', sa.String(length=64), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('purpose', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['physician_schedule.event_id'], ),
    sa.ForeignKeyConstraint(['facility_num'], ['facility.facility_num'], ),
    sa.ForeignKeyConstraint(['hospital_id'], ['facility.hospital_id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.user_id'], ),
    sa.PrimaryKeyConstraint('appointment_id')
    )
    op.drop_table('flight')
    op.drop_table('Appointment')
    op.drop_table('airplane')
    op.drop_table('Prescription')
    op.drop_table('Physician')
    op.drop_table('airport')
    op.drop_table('booking_agent')
    op.drop_table('airline_staff')
    op.drop_table('phone_number')
    op.drop_table('airline')
    op.drop_table('airline_stock')
    op.drop_table('Patient')
    op.drop_table('customer')
    op.drop_table('ticket')
    op.drop_table('Hospital')
    op.drop_table('Room')
    op.drop_table('address')
    op.add_column('user', sa.Column('creation_date', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('first_name', sa.String(length=64), nullable=False))
    op.add_column('user', sa.Column('hospital_id', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=64), nullable=False))
    op.create_unique_constraint(None, 'user', ['email'])
    op.create_foreign_key(None, 'user', 'hospital', ['hospital_id'], ['unique_id'])
    op.drop_column('user', 'member_since')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('member_since', sa.DATETIME(), nullable=True))
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'hospital_id')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'email')
    op.drop_column('user', 'creation_date')
    op.create_table('address',
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('building_num', sa.VARCHAR(length=64), nullable=False),
    sa.Column('street', sa.VARCHAR(length=64), nullable=False),
    sa.Column('city', sa.VARCHAR(length=64), nullable=False),
    sa.Column('state', sa.VARCHAR(length=64), nullable=False),
    sa.Column('zip_code', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['email'], ['customer.email'], ),
    sa.PrimaryKeyConstraint('email', 'building_num', 'street', 'city', 'state', 'zip_code')
    )
    op.create_table('Room',
    sa.Column('room_number', sa.INTEGER(), nullable=False),
    sa.Column('building', sa.VARCHAR(length=64), nullable=False),
    sa.Column('hospital', sa.VARCHAR(length=64), nullable=True),
    sa.ForeignKeyConstraint(['hospital'], ['Hospital.name'], ),
    sa.PrimaryKeyConstraint('room_number')
    )
    op.create_table('Hospital',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('country', sa.VARCHAR(length=64), nullable=False),
    sa.Column('state', sa.VARCHAR(length=64), nullable=False),
    sa.Column('city', sa.VARCHAR(length=64), nullable=False),
    sa.Column('zipcode', sa.VARCHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ticket',
    sa.Column('ticket_id', sa.VARCHAR(length=64), nullable=False),
    sa.Column('customer_email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('airline_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('flight_num', sa.VARCHAR(length=64), nullable=False),
    sa.Column('booking_agent_ID', sa.VARCHAR(length=64), nullable=True),
    sa.ForeignKeyConstraint(['airline_name'], ['airline.name'], ),
    sa.ForeignKeyConstraint(['booking_agent_ID'], ['booking_agent.booking_agent_id'], ),
    sa.ForeignKeyConstraint(['customer_email'], ['customer.email'], ),
    sa.ForeignKeyConstraint(['flight_num'], ['flight.flight_num'], ),
    sa.PrimaryKeyConstraint('ticket_id')
    )
    op.create_table('customer',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('middle_name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('passport_num', sa.VARCHAR(length=64), nullable=False),
    sa.Column('passport_expir', sa.DATE(), nullable=False),
    sa.Column('passport_country', sa.VARCHAR(length=64), nullable=False),
    sa.Column('date_of_birth', sa.DATE(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_table('Patient',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('password', sa.VARCHAR(length=64), nullable=False),
    sa.Column('ssn', sa.INTEGER(), nullable=False),
    sa.Column('dob', sa.DATETIME(), nullable=True),
    sa.Column('physician_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['physician_id'], ['Physician.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('ssn')
    )
    op.create_table('airline_stock',
    sa.Column('airline_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('model', sa.VARCHAR(length=3), nullable=False),
    sa.Column('unique_id', sa.VARCHAR(length=64), nullable=False),
    sa.ForeignKeyConstraint(['airline_name'], ['airline.name'], ),
    sa.ForeignKeyConstraint(['model'], ['airplane.id_num'], ),
    sa.PrimaryKeyConstraint('airline_name', 'model', 'unique_id')
    )
    op.create_table('airline',
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('phone_number',
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('number', sa.VARCHAR(length=64), nullable=False),
    sa.ForeignKeyConstraint(['email'], ['customer.email'], ),
    sa.PrimaryKeyConstraint('email', 'number')
    )
    op.create_table('airline_staff',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('date_of_birth', sa.DATETIME(), nullable=False),
    sa.Column('airline', sa.VARCHAR(length=64), nullable=False),
    sa.ForeignKeyConstraint(['airline'], ['airline.name'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('booking_agent',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('booking_agent_id', sa.VARCHAR(length=64), nullable=False),
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('password', sa.VARCHAR(length=64), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('booking_agent_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('airport',
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('code', sa.VARCHAR(length=3), nullable=True),
    sa.Column('city', sa.VARCHAR(length=64), nullable=True),
    sa.Column('country', sa.VARCHAR(length=64), nullable=True),
    sa.Column('latitude', sa.FLOAT(), nullable=True),
    sa.Column('longitude', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('name'),
    sa.UniqueConstraint('code')
    )
    op.create_table('Physician',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('email', sa.VARCHAR(length=64), nullable=False),
    sa.Column('password', sa.VARCHAR(length=64), nullable=False),
    sa.Column('hospital', sa.VARCHAR(length=64), nullable=True),
    sa.ForeignKeyConstraint(['hospital'], ['Hospital.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Prescription',
    sa.Column('medication', sa.VARCHAR(length=64), nullable=False),
    sa.Column('date_prescribed', sa.DATETIME(), nullable=False),
    sa.Column('date_expired', sa.DATETIME(), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=False),
    sa.Column('patient_id', sa.INTEGER(), nullable=False),
    sa.Column('physician_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['patient_id'], ['Patient.id'], ),
    sa.ForeignKeyConstraint(['physician_id'], ['Physician.id'], ),
    sa.PrimaryKeyConstraint('medication', 'date_prescribed', 'patient_id', 'physician_id')
    )
    op.create_table('airplane',
    sa.Column('id_num', sa.VARCHAR(length=3), nullable=False),
    sa.Column('aircraft_name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('seat_capacity', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id_num'),
    sa.UniqueConstraint('aircraft_name')
    )
    op.create_table('Appointment',
    sa.Column('appointment_id', sa.INTEGER(), nullable=False),
    sa.Column('start_time', sa.DATETIME(), nullable=False),
    sa.Column('end_time', sa.DATETIME(), nullable=False),
    sa.Column('physician_id', sa.INTEGER(), nullable=True),
    sa.Column('patient_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['Patient.id'], ),
    sa.ForeignKeyConstraint(['physician_id'], ['Physician.id'], ),
    sa.PrimaryKeyConstraint('appointment_id')
    )
    op.create_table('flight',
    sa.Column('flight_num', sa.VARCHAR(length=64), nullable=False),
    sa.Column('price', sa.FLOAT(), nullable=False),
    sa.Column('airline_name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('airplane_model', sa.VARCHAR(length=64), nullable=False),
    sa.Column('airplane_id', sa.VARCHAR(length=64), nullable=False),
    sa.Column('arrival', sa.VARCHAR(length=64), nullable=False),
    sa.Column('departure', sa.VARCHAR(length=64), nullable=False),
    sa.Column('arrival_date', sa.DATETIME(), nullable=False),
    sa.Column('departure_date', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['airline_name'], ['airline_stock.airline_name'], ),
    sa.ForeignKeyConstraint(['airplane_id'], ['airline_stock.unique_id'], ),
    sa.ForeignKeyConstraint(['airplane_model'], ['airline_stock.model'], ),
    sa.ForeignKeyConstraint(['arrival'], ['airport.name'], ),
    sa.ForeignKeyConstraint(['departure'], ['airport.name'], ),
    sa.PrimaryKeyConstraint('flight_num', 'airline_name')
    )
    op.drop_table('appointment')
    op.drop_table('prescription')
    op.drop_table('physician_schedule')
    op.drop_table('physician')
    op.drop_table('patient')
    op.drop_table('nurse')
    op.drop_index(op.f('ix_facility_hospital_id'), table_name='facility')
    op.drop_index(op.f('ix_facility_facility_num'), table_name='facility')
    op.drop_table('facility')
    op.drop_table('insurance')
    op.drop_table('hospital')
    # ### end Alembic commands ###
