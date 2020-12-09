from data.dataAPI import dataAPI
from models.contracts import Contract
import logic.logicAPI
import datetime


class ContractLogic:

    def __init__(self):
        self.data = dataAPI()

    def all_contracts(self):
        return self.data.get_contracts()

    def change_to_datetime(self, date_text):
        try:
            date_text = datetime.datetime.strptime(date_text, '%d.%m.%y')
            return date_text
        except ValueError:
            pass
    
    def change_to_string(self, date_time):
        date_string = datetime.datetime.strftime(date_time, '%d.%m.%y')
        return date_string
    
    def create_contract(self, a_list):
        new_contract = Contract(self.data.new_contract_id() , *a_list)
        if not self.check_availability(new_contract):
            return "Vehicle unavailable at that time."
        #elif not self.check_license(new_contract):
        #    return "Inadequate license type."
        elif not self.check_country(new_contract):
            return "Vehicle position and contract destination differ."
        else:
            new_contract.end_date = self.change_to_string(new_contract.end_date)
            new_contract.start_date = self.change_to_string(new_contract.start_date)
            self.data.create_contract(new_contract)
            return "Contract successfully created."

    def check_availability(self, new_contract):     #Athugar tímaskorður
        new_contract.end_date = self.change_to_datetime(new_contract.end_date)
        new_contract.start_date = self.change_to_datetime(new_contract.start_date)
        for contract in self.all_contracts():
            contract.start_date = self.change_to_datetime(contract.start_date)
            contract.end_date = self.change_to_datetime(contract.end_date)
            if contract.vehicle_unique_id == new_contract.vehicle_unique_id:
                if (contract.start_date < new_contract.start_date) & (contract.end_date >= new_contract.start_date):
                    return False
                elif (contract.end_date >= new_contract.end_date) & (new_contract.end_date >= contract.start_date):
                    return False
                elif (contract.start_date >= new_contract.start_date) & (contract.start_date <= new_contract.end_date):
                    return False
        return True


    ###def check_license(self, new_contract):      LAGA SÍÐAR
        #if logic.logicAPI.LogicAPI.search_vehicle_by_ID(logic.logicAPI.LogicAPI(),new_contract.vehicle_unique_id)[0].license_type not in logic.logicAPI.LogicAPI.customer_by_name(logic.logicAPI.LogicAPI(),new_contract.customer)[0].license:
        #    return False
        #else:
        #    return True

    def check_country(self, new_contract):
        vehicle = self.search_vehicle_by_ID(new_contract.vehicle_unique_id)
        if vehicle:
            if new_contract.country.lower() != vehicle[0].location.lower():
                return True
            else:
                return False
        
        

    def search_contracts_by_customer(self, string):
        result_list = []
        for contract in self.all_contracts():
            if contract.get_customer().lower() == string.lower():
                result_list.append(contract)
        return self.no_match_found(result_list)
        
    def search_contracts_by_vin(self, string):
        result_list = []
        for contract in self.all_contracts():
            if contract.get_vin().lower() == string.lower():
                result_list.append(contract)
        return self.no_match_found(result_list)

    def search_contracts_by_id(self, string):
        match = []
        for contract in self.all_contracts():
            if contract.get_unique_id() == string:
                match.append(contract)
        return self.no_match_found(match)

    def no_match_found(self, result_list):
        if result_list:
            return result_list
        else:
            result_list.append("\n*** No match found ***n")
            return result_list

    def delete_contract(self, contract_id):
        result = self.search_contracts_by_id(contract_id)
        if result[0] != "\n*** No match found ***n":
            self.data.delete_contract(result[0])
            return "\n*** Contract successfully deleted ***\n"
        else:
            return result



### föll fyrir virkni ###

    def search_vehicle_by_ID(self, ID):
        retList = []
        search_list = self.data.get_vehicles()
        for vehicle in search_list:
            if vehicle.unique_id == ID:
                retList.append(vehicle)
        return self.no_match_found(retList)

    def customer_by_name(self,name):
        custs = self.data.get_customers()
        retList = []
        for cust in custs:
            if cust.name.lower() == name.lower():
                retList.append(cust)
        return self.no_match_found(retList)