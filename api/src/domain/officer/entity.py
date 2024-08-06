import bcrypt


class OfficerEntity:
    def __init__(
        self, id: int, name: str, badge_number: str, hashed_password: str, role: str
    ):
        self.id = id
        self.name = name
        self.badge_number = badge_number
        self.hashed_password = hashed_password
        self.role = role

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"), self.hashed_password.encode("utf-8")
        )
