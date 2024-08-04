class OfficerNotFound(Exception):

    message = "Badge not found or incorrect password"

    def __str__(self):
        return self.message
