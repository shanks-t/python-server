class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, breed, treatment, location_id, customer_id):
        self.id = id
        self.name = name
        self.breed = breed
        self.treatment = treatment
        self.locationId = location_id
        self.customerId = customer_id
        self.location = None
