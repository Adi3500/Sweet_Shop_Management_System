class SweetShop:
    def __init__(self):
        # Initialize an empty list to store sweet data
        self.sweets = []

    def add_sweet(self, id, name, category, price, quantity):
        
        #Add a new sweet to the shop. All fields are required.
        if not id or not name or not category or price is None or quantity is None:
            raise ValueError("Missing required sweet fields.")

        self.sweets.append({
            "id": id,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        })
    def view_sweets(self):

        # Return a list of all available sweets.
        return self.sweets