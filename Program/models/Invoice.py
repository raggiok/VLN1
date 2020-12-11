class Invoice():

    def __init__(self,unique_id,contract_unique_id, customer_unique_id, vehicle_unique_id, rate, total_days, total_price, late_fee, invoice_type="Debit", state="Active"):
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

    def calculate_price(self):
        total_price = int(self.rate) * int(self.total_days)
        return total_price