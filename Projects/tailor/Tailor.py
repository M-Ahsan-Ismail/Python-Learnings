import pyttsx3
import keyboard

voice = pyttsx3.init()

class A():
    def __init__(self):
        self.Customers = {
            "Customer_1": {
                'name': '',
                'arm_size': '',
                'leg_size': '',
                'waist_size': '',
                'neck_size': ''
            },
            "Customer_2": {
                'name': '',
                'arm_size': '',
                'leg_size': '',
                'waist_size': '',
                'neck_size': ''
            },
            "Customer_3": {
                'name': '',
                'arm_size': '',
                'leg_size': '',
                'waist_size': '',
                'neck_size': ''
            }
        }

    def ReturnEmpty_Maps(self):
        EmptyMaps = []
        for empty_map, map_vals in self.Customers.items():
            if all(vals == '' for vals in map_vals.values()):
                EmptyMaps.append(empty_map)
        return EmptyMaps

    def InsertValues(self):
        obj = self.ReturnEmpty_Maps()
        if not obj:
            print('No Space Available')
        emp = obj[0]
        name = input('Enter Name: ')
        arm_size = input('Arm Size: ')
        leg_size =  input('Leg Size: ')
        waist_size =input('Waist Size: ')
        neck_size = input('Neck Size: ')

        self.Customers[emp] = {
            'name': name,
        'arm_size': arm_size,
        'leg_size': leg_size,
        'waist_size': waist_size,
        'neck_size': neck_size
        }

    def UpdateValues(self):
        what_customer_to_update = input('Enter Customer: ')
        if what_customer_to_update in self.Customers:
            print('1  : For Single Value Change')
            print('2  : For All Value Change')
            one_or_many = input(': ')
            if one_or_many == '1':
                which_to_change = input('Enter Value Name To Change: ')
                if which_to_change in self.Customers[what_customer_to_update]:
                    new_val = input('Enter New Value: ')
                    self.Customers[what_customer_to_update][which_to_change] = new_val
                    print('Updated:- ', self.Customers[what_customer_to_update][which_to_change])
                else:
                    print(f'{which_to_change} Not Exits!')

            elif one_or_many == '2':
                self.Customers[what_customer_to_update]['name'] = input('Enter New Name: ')
                print('Updated:- ', self.Customers[what_customer_to_update]['name'])
                self.Customers[what_customer_to_update]['arm_size'] = input('Enter Arm Size: ')
                print('Updated:- ', self.Customers[what_customer_to_update]['arm_size'])
                self.Customers[what_customer_to_update]['leg_size'] = input('Enter Leg Size: ')
                print('Updated:- ', self.Customers[what_customer_to_update]['leg_size'])
                self.Customers[what_customer_to_update]['waist_size'] = input('Enter Waist Size: ')
                print('Updated:- ', self.Customers[what_customer_to_update]['waist_size'])
                self.Customers[what_customer_to_update]['neck_size'] = input('Enter Neck Size: ')
                print('Updated:- ', self.Customers[what_customer_to_update]['neck_size'])

            else:
                print('Invalid Choice!')
        else:
             print(f'{what_customer_to_update} Not Exists!')
    def DeleteValues(self):
        for x in self.Customers:
            A = self.Customers[x]
            for x,y in A.items():
                if y!='':
                    Map_Want = input("Enter CustomerName: ")
                    if Map_Want in self.Customers:
                        Value_To_Delete = input("Enter Value TO Delete: ")
                        if Value_To_Delete in self.Customers[Map_Want]:
                            self.Customers[Map_Want][Value_To_Delete] = ''
                            print(f"{Value_To_Delete} in {Map_Want} has been cleared.")
                        else:
                            print(f"{Value_To_Delete} not found in {Map_Want}.")
                    else:
                        print(f"{Map_Want} Invalid")

                return 'All Maps Are Empty'




    def Print_All_CustomerInfo(self):
        for customer_name, customer_info in self.Customers.items():
            print(f"Customer: {customer_name}")
            for key, value in customer_info.items():
                print(f"  {key}: {value}")
            print()

    def main_menu(self):
        while True:
            print("\nSelect an option:")
            print("1: Insert Values")
            print("2: Update Values")
            print("3: Delete Values")
            print("4: Print All Customer Info")
            print("Press Esc to exit")
            voice.say("Welcome To Tailor Measurements Saver App")

            option = input("Enter option: ")

            if option == '1':
                self.InsertValues()
            elif option == '2':
                self.UpdateValues()
            elif option == '3':
                self.DeleteValues()
            elif option == '4':
                self.Print_All_CustomerInfo()
            elif keyboard.is_pressed('esc'):
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

# Create an instance of the class
Obj = A()
Obj.main_menu()
