import csv
from models.contracts import Contract
from models.Customers import Customer
from models.Destinations import Destination
from models.Employee import Employee
from models.Vehicle import Vehicle
from models.Invoice import Invoice
from models.rates import Rate

INSTANCE_TYPES = ["contract", "customer","destination", "employee", "vehicle", "invoice", "rate"]

ALL_FIELDNAMES = {
    "contract": ['unique_id', 'customer', 'vehicle_unique_id', 'start_date', 'end_date', 'country', 'employee', 'total_price', 'contract_creation_date', 'state'],
    "customer": ['unique_id', 'name', 'ssn', 'address', 'zip_code', 'city', 'country', 'phone', 'email', 'state'],
    "destination": ['unique_id', 'country', 'city', 'airport', 'phone_number', 'opening_time', 'closing_time', 'main_contact', 'state'],
    "employee": ['unique_id', 'name', 'ssn', 'role', 'address', 'zip_code', 'city', 'country', 'home_phone', 'mobile_phone', 'email', 'state'],
    "vehicle": ['unique_id', 'manufacturer', 'model', 'vehicle_type', 'status', 'man_year', 'color', 'license_type', 'location','state'],
    "invoice": ['unique_id', 'customer_unique_id', 'vehicle_unique_id', 'rate', 'total_days', '_total_price', 'invoice_type', 'state'],
    "rate": ['unique_id','name', 'cost_per_day']
    }

CSV_FOLDER_NAMES = {
    "contract": "data/csv_files/contracts.csv", 
    "customer": "data/csv_files/customers.csv", 
    "destination": "data/csv_files/destinations.csv", 
    "employee": "data/csv_files/employees.csv",
    "vehicle": "data/csv_files/vehicles.csv",
    "invoice": "data/csv_files/invoices.csv",
    "rate": "data/csv_files/rates.csv"
    }

ID_FOLDER_NAMES = {
    "contract": "data/unique_id/contract_unique_id.csv" , 
    "customer": "data/unique_id/customer_unique_id.csv", 
    "destination": "data/unique_id/destination_unique_id.csv", 
    "employee": "data/unique_id/employee_unique_id.csv" ,
    "vehicle": "data/unique_id/vehicle_unique_id.csv",
    "invoice": "data/unique_id/invoice_unique_id.csv",
    "rate": "data/unique_id/rate_unique_id.csv"
    }

class Data:
    def __init__(self):
        pass
    
    #Get all the fieldnames for the specific instance type
    def get_fieldnames(self, instance_type):
        instance_type = instance_type.lower()
        if instance_type in INSTANCE_TYPES:
            return ALL_FIELDNAMES[instance_type]

    #Get the path to save instance of data based on type of data
    def get_csv_folder(self, instance_type):
        instance_type = instance_type.lower()
        if instance_type in INSTANCE_TYPES:
            return CSV_FOLDER_NAMES[instance_type]

    #Get the path for folder to save unique_id values
    def get_id_folder(self, instance_type):
        instance_type = instance_type.lower()
        if instance_type in INSTANCE_TYPES:
            return ID_FOLDER_NAMES[instance_type]

    def new_id(self, instance_type):
        '''Returns a new ID for a the data and stores it in a .csv file'''
        unique_id_folder = self.get_id_folder(instance_type)
        unique_id_title_str = f"{instance_type}_unique_id"
        temp_list = []
        #Read current ID's in file
        with open(f'{unique_id_folder}', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temp_list.append(row)
            counter = len(temp_list) + 1 #add's one
            #Write's a new file and add's the next ID
            with open(f'{unique_id_folder}', 'w', newline='', encoding="utf-8") as newfile:
                fieldnames = [unique_id_title_str]
                writer = csv.DictWriter(newfile, fieldnames=fieldnames,)
                writer.writeheader()
                for row in temp_list:
                    writer.writerow(row)
                writer.writerow({unique_id_title_str: counter})
        return counter

    def write_data(self, instance, instance_type):
        '''Registers the new vehicle in the database'''
        instance_fieldnames = self.get_fieldnames(instance_type) #get correct fieldnames for intance
        csv_folder = self.get_csv_folder(instance_type) #get csv folder path to save instance
        
        #Create the row we will save to csv
        row = {}
        instance_values = []
        for item in instance.__dict__.values(): #unpack instance values
            instance_values.append(item)

        for i in range(0, len(instance_fieldnames)): #add values to correct dict key
            if i == 0:
                row[instance_fieldnames[i]] = self.new_id(instance_type)
            else:
                row[instance_fieldnames[i]] = instance_values[i]
        
        #write the instance created to csv
        with open(f'{csv_folder}', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = instance_fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,)
            writer.writerow(row)
        # # #we need to return True if all elements of vehicle were stored accurately in database else false
        #Add a function that goes through each parameter and checks if it's the same as what was delivered
        
    def edit_data(self, updated_instance, instance_type):
        '''Register's changes of a specific vehicle'''
        instance_fieldnames = self.get_fieldnames(instance_type) #get correct fieldnames for intance
        csv_folder = self.get_csv_folder(instance_type) #get csv folder path to save instance

        #Create the row we will save to csv
        updated_row = {}
        instance_values = []
        for item in updated_instance.__dict__.values(): #unpack instance values
            instance_values.append(item)

        for i in range(0, len(instance_fieldnames)): #add values to correct dict key
            updated_row[instance_fieldnames[i]] = instance_values[i]

        #read file and add content to temp file
        instance_list = []
        confirmation = False
        with open(f'{csv_folder}', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                instance_list.append(row)

            #write new file with same content and add new row if it has same ID
            with open(f'{csv_folder}', 'w', newline='', encoding="utf-8") as newfile:
                fieldnames = instance_fieldnames
                writer = csv.DictWriter(newfile, fieldnames=fieldnames,)
                writer.writeheader()
                for row in instance_list:
                    if updated_instance.unique_id == row["unique_id"]:
                        row = updated_row
                        confirmation = True
                    writer.writerow(row)
        return confirmation

    #Delete Vehicle from data
    def delete_data(self, instance, instance_type): #Data layer receives an instance of Vehicle
        instance_fieldnames = self.get_fieldnames(instance_type) #get correct fieldnames for intance
        csv_folder = self.get_csv_folder(instance_type) #get csv folder path to save instance

        #Create the row we will save to csv
        delete_row = {}
        instance_values = []
        for item in instance.__dict__.values(): #unpack instance values
            if item == "Active":
                item = "Inactive"
            instance_values.append(item)

        for i in range(0, len(instance_fieldnames)): #add values to correct dict key
            delete_row[instance_fieldnames[i]] = instance_values[i]

        instance_list = []
        confirmation = False
        with open(f'{csv_folder}', 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                instance_list.append(row)
            with open(f'{csv_folder}', 'w', newline='', encoding="utf-8") as writecvsfile:
                fieldnames = instance_fieldnames
                writer = csv.DictWriter(writecvsfile, delimiter=',', fieldnames=fieldnames)
                writer.writeheader()
                for row in instance_list:
                    if row['unique_id'] == instance.unique_id:
                        row = delete_row
                        confirmation = True
                    writer.writerow(row)
        return confirmation #Returns True if successfully deleted, otherwise False

    def get_data(self, instance_type):
        '''Returns a list of all vehicles in database'''
        csv_folder = self.get_csv_folder(instance_type) #get csv folder path to save instance

        instance_list = []
        with open(f'{csv_folder}', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                instance_attribute_list = []
                for value in row:
                    instance_attribute_list.append(row[f"{value}"])
                if instance_type == "contract":
                    contract = Contract(*instance_attribute_list)
                    instance_list.append(contract)
                elif instance_type == "customer":
                    customer = Customer(*instance_attribute_list)
                    instance_list.append(customer)
                elif instance_type == "destination":
                    destination = Destination(*instance_attribute_list)
                    instance_list.append(destination)
                elif instance_type == "employee":
                    employee = Employee(*instance_attribute_list)
                    instance_list.append(employee)
                elif instance_type == "vehicle":
                    vehicle = Vehicle(*instance_attribute_list)
                    instance_list.append(vehicle)

                instance_attribute_list.clear()

        return instance_list