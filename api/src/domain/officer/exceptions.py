class OfficerLoginNotFound(Exception):

    message = "Badge not found or incorrect password"

    def __str__(self):
        return self.message


class OfficerNotFound(Exception):

    message = "Officer not found"

    def __str__(self):
        return self.message


class OfficerBadgeExists(Exception):

    message = "Badge already exists"

    def __str__(self):
        return self.message
