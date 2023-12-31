# from cli import main
from sys import exit
from lib.db.database import session
from lib.db.models import Doctor, Patient, Appointment, Dict_Object
from lib.db.functions.add_functions import buffer



def print_table(table):
    query_result = session.query(table).all()
    print('----------------------------')
    for i, row in enumerate(query_result, 1):
        print(row)
        if i % 500 == 0:
            input('Press ENTER to view more records...')
    print('----------------------------')
    print(f'These are your {table.__name__} records')
    print('----------------------------')
    return [row for row in query_result]

def read_func_1():
    print()
    print('What records would you like to see?')
    print()
    choice = 0
    while choice != 5:
        print('1) Doctors')
        print('2) Patients')
        print('3) Appointments')
        print('4) Return to previous menu')
        print('5) Quit')
        print('    ...or type 999 to see a dictionary object')
        print()
        print('-' * 30)
        try:
            choice = int(input('Enter choice number: '))
            print()
            if choice == 1:
                print_table(Doctor)
            elif choice == 2:
                print_table(Patient)
            elif choice == 3:
                print_table(Appointment)
            elif choice == 4:
                print('Previous menu...')
                break
            elif choice == 5:
                print('Closing application...')
                exit()
            elif choice == 999:
                buffer(Dict_Object())
            elif not 1 <= choice <= 5:
                print('Please enter valid choice (integers 1 through 5)')
        except ValueError:
            print('Please enter a valid integer choice (1 through 5)')
