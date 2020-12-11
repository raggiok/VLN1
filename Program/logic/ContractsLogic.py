from models.Vehicle import Vehicle
from data.dataAPI import dataAPI
from models.contracts import Contract
from models.Invoice import Invoice
import logic.logicAPI
import datetime

LATECHARGE = 1.2

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
    
    def create_contract(self, a_list):                                          #Athugar hvort að bíllinn sé bókaður á þessum tíma, hvort að kúninn sé með réttindi o.s.frv.
        new_contract = Contract("", *a_list)
        if not self.check_availability(new_contract):
            return "\n*** Vehicle unavailable at that time ***\n"
        #elif not self.check_license(new_contract):
        #    return "*****Inadequate license type.*****"
        elif not self.check_country(new_contract):
            return "\n*** Vehicle position and contract destination differ ***\n"
        else:
            new_contract.end_date = self.change_to_string(new_contract.end_date)
            new_contract.start_date = self.change_to_string(new_contract.start_date)
            self.data.create_contract(new_contract)
            return "\n*** Contract successfully created ***\n"

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

    def update_contract(self, contract_instance):
            '''Edits a vehicle in the database'''
            return self.data.update_contract(contract_instance)


    ###def check_license(self, new_contract):      LAGA SÍÐAR
        #if logic.logicAPI.LogicAPI.search_vehicle_by_ID(logic.logicAPI.LogicAPI(),new_contract.vehicle_unique_id)[0].license_type not in logic.logicAPI.LogicAPI.customer_by_name(logic.logicAPI.LogicAPI(),new_contract.customer)[0].license:
        #    return False
        #else:
        #    return True

    def check_country(self, new_contract):
        vehicle = self.search_vehicle_by_ID(new_contract.vehicle_unique_id)
        if vehicle:
            if new_contract.country.lower() != vehicle[0].location.lower():
                return False
            else:
                return True
        
        

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
            if contract.unique_id == string:
                match.append(contract)
        return self.no_match_found(match)

    def no_match_found(self, result_list):
        if result_list:
            return result_list
        else:
            result_list.append("\n*** No match found ***\n")
            return result_list

    def delete_contract(self, contract_id):
        result = self.search_contracts_by_id(contract_id)
        if result[0] != "\n*** No match found ***\n":
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
        return retList

    def customer_by_ssn(self,ssn):
        custs = self.data.get_customers()
        retList = []
        for cust in custs:
            if cust.ssn == ssn:
                retList.append(cust)
        return retList
    
### Föll til að reikna leiguverð ### - á eftir að bæta inn í logicAPA

    def create_invoice(self, contract_nr):
        try:
            contract = self.search_contracts_by_id(contract_nr)[0]
            vehicle = self.search_vehicle_by_ID(contract.vehicle_unique_id)[0]
            customer = self.customer_by_ssn(contract.customer_ssn)[0]
        except (IndexError, AttributeError):
            return 'Customer, contract or vehicle not found.'
        late_hours = self.change_to_datetime(contract.checkin_date) - self.change_to_datetime(contract.end_date)
        hours_total = self.change_to_datetime(contract.end_date) - self.change_to_datetime(contract.start_date) 
        total = 0
        late_fee = 0
        rates = self.data.get_rates()
        rate_invoice = ""
        for rate in rates:
            if rate.name.lower() == vehicle.rate.lower():
                rate_invoice = rate
        if late_hours.days > 0:
            late_fee += late_hours.days * int(rate_invoice.cost_per_day) * LATECHARGE
        total += hours_total.days * int(rate_invoice.cost_per_day)
        total += late_fee
        invoice = Invoice("", contract.unique_id, customer.ssn, vehicle.unique_id, rate_invoice.cost_per_day, (hours_total.days + late_hours.days), int(total), int(late_fee))
        print(invoice)
        contract.total_price = total
        contract.state = 'INVOICED'
        self.data.update_contract(contract)
        return self.create_invoic(invoice)
        

    def create_invoic(self, new_invoice):
        for invoice in self.data.get_invoices():
            if invoice.contract_unique_id == new_invoice.contract_unique_id:
                return "*** Invoice already sent. ***"
        self.data.create_invoice(new_invoice)
        return 'Invoice successfully sent.'
    def get_invoices(self):
        return self.data.get_invoices()

    def vehicle_check_out(self, contract_id):
        contract = self.search_contracts_by_id(contract_id)
        if contract[0] != "\n*** No match found ***\n":
            contract[0].checkout_date = datetime.date.today().strftime("%d.%m.%y")
            self.data.update_contract(contract[0])
            return "Vehicle successfully checked out."
        else:
            return contract[0]

    def vehicle_check_in(self,contract_id):
        contract = self.search_contracts_by_id(contract_id)
        if contract[0] != "\n*** No match found ***\n":
            contract[0].checkin_date = datetime.date.today().strftime("%d.%m.%y")
            self.data.update_contract(contract[0])
            return "Vehicle successfully checked in."
        else:
            return contract[0]

    def search_invoices(self, invoice_id):
        match = []
        for invoice in self.data.get_invoices():
            if invoice.unique_id == invoice_id:
                match.append(invoice)
        return self.no_match_found(match)
    
    def get_all_invoices(self):
        a_list = self.data.get_invoices()
        return self.no_match_found(a_list)

    def set_invoice_to_payed(self, invoice_id):
        listi = self.search_invoices(invoice_id)
        if listi[0] != "\n*** No match found ***\n":
            listi[0].state = 'PAYED'
            self.data.update_invoice(listi[0])
            return 'State successfully changed.'
        else:
            return listi[0]
