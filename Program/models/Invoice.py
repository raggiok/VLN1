class Invoice():

    def __init__(self,unique_id,contract_unique_id, customer_unique_id, vehicle_unique_id, rate, total_days, total_price, late_fee, invoice_type="Debit", state='ACTIVE'):
        self.unique_id = unique_id
        self.contract_unique_id = contract_unique_id
        self.customer_unique_id = customer_unique_id
        self.vehicle_unique_id = vehicle_unique_id
        self.rate = rate
        self.total_days = total_days
        self.total_price = total_price
        self.late_fee = late_fee
        self.invoice_type = invoice_type #Can be Debit or Credit
        self.state = state #Is ACTIVE but if deleted becomes "DELETED"

    def __str__(self):
        return f'{self.unique_id:<20}{self.contract_unique_id:<20}{self.vehicle_unique_id:<20}{self.customer_unique_id:<20}{self.rate:<20}{self.total_days:<20}{self.total_price:<20}{self.late_fee:<20}{self.state:<20}'
