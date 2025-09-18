class User:
    def __init__(self, user_id=None, username=None, password=None, email=None,
                 first_name=None, last_name=None, date_of_birth=None, profile_pic=None):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._profile_pic = profile_pic

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, user_id):
        self._user_id = user_id

    # Repeat for other fields
