class Invoices():

    def __init__(self, unique_id, customer_unique_id, vehicle_unique_id, rate, total_days, invoice_type="Debit", state="Active"):
        self.unique_id = unique_id
        self.vehicle_unique_id = vehicle_unique_id
        self.customer_unique_id = customer_unique_id
        self.rate = rate
        self.total_days = total_days
        self.total_price = self.calculate_price()
        self.invoice_type = invoice_type #Can be Debit or Credit
        self.state = state #Is active but if deleted becomes "Inactive"

    def calculate_price(self):
        total_price = int(self.rate) * int(self.total_days)
        return total_price