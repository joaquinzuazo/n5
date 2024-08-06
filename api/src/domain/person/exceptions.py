class PersonEmailNotFound(Exception):

    message = "Person with email not found."

    def __str__(self):
        return self.message


class PersonExists(Exception):

    message = "Person email already exists."

    def __str__(self):
        return self.message


class PersonIDNotFound(Exception):

    message = "Person with ID not found."

    def __str__(self):
        return self.message
