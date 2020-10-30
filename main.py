# Carlos Perez
# Student ID: 000819792

from UI import *
import os

class Main():

    # Interface where delivery begins. Package can be viewed at certain times based on user input. After running
    # a delivery simulation, package progress can be viewed based on input time. For example, user can input times 8:35
    # and 9:25 and view package status between those two. Or, after time selection, the user can input [0] to complete
    # delivery. User will not see the address change on package 9 until time >= 10:20

    # 0(1)
    def user_interface(self):
        print('---------------MAIN MENU---------------')
        print('IT IS 8:00am.')
        menu = input('Press [1] and "Enter" to begin delivery ')


        if menu == '1':
            time = input('Enter time in "24-Hour" format, ex. "13:00" for 1:00 ')
            if time == '':
                raise Exception('Please enter a time')
            elif not (len(time) >= 4):
                raise Exception('Please enter a valid time')

            ui.run(time)

            ui.package_statuses(time)

            choice = input('Enter [0] to view complete delivery\n'
                        'Enter [1] to run again\n'
                        'Enter [2] to search package\n'
                        'Enter [3] to exit')

            if choice == '0':
                ui.lookup_all()

            elif choice == '1':
                os.execl(sys.executable, sys.executable, *sys.argv)
                self.user_interface()

            elif choice == '2':
                print('Searching package at', time)
                option = input('Choose one of the following:\n'
                               'Address [1]\n'
                               'City [2]\n'
                               'Zipcode [3]\n'
                               'State [4]\n'
                               'Deadline [5]\n'
                               'Weight [6]\n'
                               'Status [7]\n')
                id = input('Enter ID')

                ui.lookup_package(option, id, time)

            else:
                SystemExit






main = Main()

main.user_interface()