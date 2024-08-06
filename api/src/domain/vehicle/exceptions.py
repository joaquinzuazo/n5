class VehicleNotFound(Exception):

    message = "Vehicle with license plate not found."

    def __str__(self):
        return self.message


class VehicleAlreadyExists(Exception):

    message = "Vehicle with license plate already exists."

    def __str__(self):
        return self.message


class OwnerIDNotFound(Exception):

    message = "Owner ID not found."

    def __str__(self):
        return self.message
