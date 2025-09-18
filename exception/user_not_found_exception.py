class UserNotFoundException(Exception):
    def __init__(self, message="User not found with the given ID."):
        self.message = message
        super().__init__(self.message)
