class Invoice():

    def __init__(self, unique_id, customer_unique_id, vehicle_unique_id, rate, total_days, _total_price="", invoice_type="Debit", state="ACTIVE", ):
        self.unique_id = unique_id
        self.vehicle_unique_id = vehicle_unique_id
        self.customer_unique_id = customer_unique_id
        self.rate = rate
        self.total_days = total_days
        self._total_price = self.calculate_price()
        self.invoice_type = invoice_type #Can be Debit or Credit
        self.state = state #Is ACTIVE but if deleted becomes "DELETED"

    def calculate_price(self):
        total_price = int(self.rate) * int(self.total_days)
        return total_price