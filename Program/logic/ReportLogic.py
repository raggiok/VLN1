from data.dataAPI import dataAPI
import datetime

class ReportLogic():
    def __init__(self):
        self.data = dataAPI()

    def fetch_all_contracts(self):
        return self.data.get_contracts()

    def fetch_all_vehicles(self):
        return self.data.get_vehicles()

    def fetch_all_destinations(self):
        return self.data.get_destinations()

    def fetch_all_invoices(self):
        return self.data.get_invoices()

    ### UTILIZATION REPORT ###
    #This is the report we are going to create {"Destination": [vehicle_type, days, days_out_of_year]}

    def destinations_to_dict(self):
        #report = {"Destination": ""}
        report = {}
        destinations = self.fetch_all_destinations()
        for destination in destinations:
            dest = destination.get_destination()
            if dest in report:
                continue
            else:
                report[dest] = ""
        return report
    
    def contracts_to_list(self):
        #vehicle_list = [vehicle_id, checkout_date, checkin_date]
        vehicle_list = []
        contracts = self.fetch_all_contracts()
        for contract in contracts:
            vehicle_id = contract.get_vin()
            start_date = contract.get_start_date()
            end_date = contract.get_end_date()
            temp_vehicle = [vehicle_id, start_date, end_date]
            vehicle_list.append(temp_vehicle.copy())
            temp_vehicle.clear()
        return vehicle_list

    def calcuate_days_per_vehicle(self, vehicle_list):
        '''Takes a list of vehicles in this format: vehicle_id, checkout_date, checkin_date'''
        #sum_list = [[vehicle_id, days_rented],[vehicle_id, days_rented]...]
        sum_list = []
        for vehicle in vehicle_list:
            vehicle_id = vehicle[0]
            start_date = datetime.datetime.strptime(vehicle[1],'%d.%m.%y')
            end_date = datetime.datetime.strptime(vehicle[2],'%d.%m.%y')
            days_rented = end_date - start_date
            sum_list.append([vehicle_id, days_rented.days])
        return sum_list
        
    def vehicle_id_and_types(self):
        #vehicle_type_list = [(vehicle_id,vehicle_type),(vehicle_id,vehicle_type)]
        vehicle_type_list = []
        vehicles = self.fetch_all_vehicles()
        for vehicle in vehicles:
            vehicle_id = vehicle.get_id()
            vehicle_type = vehicle.type_of_vehicle()
            vehicle_location = vehicle.get_location()
            vehicle_type_list.append([vehicle_id, vehicle_type, vehicle_location])
        return vehicle_type_list

    def merge_report(self):
        #Returns a Dictonary Report in the following format.
        #combo_vehicle_list = {"vehicle_id": [vehicle_type,days_rented],"vehicle_id": [vehicle_type,days_rented],....}
        result_dict = {}
        vehicle_list = self.contracts_to_list()
        days_list = self.calcuate_days_per_vehicle(vehicle_list)
        vehicle_types = self.vehicle_id_and_types()
        for vehicle in vehicle_types:
            unique_id = vehicle[0]
            vehicle_type = vehicle[1]
            destination = vehicle[2]
            if unique_id in result_dict:
                if not isinstance(result_dict[unique_id], list):
                    result_dict[unique_id] = [result_dict[unique_id]]
                result_dict[unique_id].append(destination)
                result_dict[unique_id].append(vehicle_type)
            else:
                result_dict[unique_id] = [destination, vehicle_type]
        for key, value in result_dict.items():
            for a_vehicle in days_list:
                a_unique_id = a_vehicle[0]
                days_rented = a_vehicle[1]
                if a_unique_id == key:
                    value.append(days_rented)
        return result_dict

    def utilization_report(self):
        result_list = []
        current_dict = self.merge_report()
        for key, val in current_dict.items():
            destination = val[0]
            vehicle_type = val[1]
            days_rented = 0
            for i in range(2,len(val)):
                if len(val) > 2:
                    days_rented =+ int(val[i])
                else:
                    continue
            result_list.append([destination, vehicle_type, days_rented])
        return result_list


    def result_list(self):
        final_dict = {}
        final_final_dict = {}
        result_list = self.utilization_report()
        for row in result_list:
            location = row[0]
            vehicle_type = row[1]
            days = row[2]
            if location not in final_dict:
                final_dict[location] = []
                final_dict[location].append([vehicle_type, days])
            else:
                final_dict[location].append([vehicle_type, days])
        for key, val in sorted(final_dict.items()):
            vehicle_type_dict = {}
            days = 0
            total_days = 0
            for row in val:
                vehicle_type = row[0]
                days += row[1]
                total_days += 365
                average = days/total_days
                if vehicle_type not in vehicle_type_dict:
                    vehicle_type_dict[vehicle_type] = average
                else:
                    vehicle_type_dict[vehicle_type] = average
            final_final_dict[key] = vehicle_type_dict
        return final_final_dict





    #Contracts --> Rental days
    #Vehicle --> types
    def change_to_datetime(self, date_text):
        try:
            date_text = datetime.datetime.strptime(date_text, '%d.%m.%y')
            return date_text
        except ValueError:
            pass
    
    def change_to_string(self, date_time):
        date_string = datetime.datetime.strftime(date_time, '%d.%m.%y')
        return date_string

    def get_paid_invoices(self):
        paid = []
        for invoice in self.fetch_all_invoices():
            if invoice.state.lower() == 'paid':
                paid.append(invoice)
        return paid

    def get_paid_invoices_and_contracts(self):
        paid_invoices = self.get_paid_invoices()
        invoice_contracts = []
        list_of_lists = []
        for invoice in paid_invoices:
            for contract in self.fetch_all_contracts:
                if invoice.contract_unique_id == contract.unique_id:
                    invoice_contracts.append(contract)
        list_of_lists.append(paid_invoices)
        list_of_lists.append(invoice_contracts)
        return list_of_lists

    def revenue_by_date(self, date_from, date_to):
        list_of_lists = self.get_paid_invoices_and_contracts()
        result_list = []
        begin = self.change_to_datetime(date_from)
        end = self.change_to_datetime(date_to)
        for contract in list_of_lists[1]:
            if (self.change_to_datetime(contract.checkin_date) >= begin) & (self.change_to_datetime(contract.checkin_date) <= end):
                result_list.append(contract)
        if result_list:
            return result_list
        else:
            return 'No revenue to show during that time period.'

