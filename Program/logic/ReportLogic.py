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


    ### UTILIZATION REPORT ###

    def destinations_to_dict(self):
        #report {"Destination": [vehicle_type, days, days_out_of_year]}
        report = {}
        destinations = self.fetch_all_destinations()
        for destination in destinations:
            dest = destination.get_destination()
            if dest in report:
                continue
            else:
                report[dest] = 0
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
        #sum_list = [(vehicle_id, days_rented),(vehicle_id, days_rented)...]
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
            vehicle_type_list.append([vehicle_id, vehicle_type])
        return vehicle_type_list

    def add_vehicle_type(self):
        #combo_vehicle_list = [(vehicle_id,vehicle_type,days_rented),(vehicle_id,vehicle_type,days_rented)]
        result = {}
        vehicle_list = self.contracts_to_list()
        days_list = self.calcuate_days_per_vehicle(vehicle_list)
        vehicle_types = self.vehicle_id_and_types()
        print(days_list)
        
        for vehicle in vehicle_types:
            vehicle_id = vehicle[0]
            vehicle_type = vehicle[1]
            if vehicle_type in result:


            if vehicle_id not in result:
                for a_vehicle in days_list:
                    unique_id = a_vehicle[0]
                    days_rented = a_vehicle[1]
                    if vehicle_id == unique_id:
                        result[vehicle_type] = [days_rented, vehicle_id])
                    else:
                        result.append([vehicle_id, vehicle_type, "0"])
            else:
                continue
        print(result)



                

    


        



    def merge_report(self):
        pass
        # report = self.destinations_to_dict()


        
        
        
        





    #Contracts --> Rental days
    #Vehicle --> types