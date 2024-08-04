class VehicleNotFound(Exception):

    message = "Vehicle with license plate not found."

    def __str__(self):
        return self.message
