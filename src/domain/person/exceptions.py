class PersonNotFound(Exception):

    message = "Person with email not found."

    def __str__(self):
        return self.message
