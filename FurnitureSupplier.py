from Entities.Supplier import Supplier
class FurnitureSupplier(Supplier):
    def __init__(self, supplier_id, name, address, contact_details, furniture_type, rental_options):
        super().__init__(supplier_id, name, address, contact_details)
        self.furniture_type = furniture_type
        self.rental_options = rental_options
   