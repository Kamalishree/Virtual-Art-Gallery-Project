class Artist:
    def __init__(self, artist_id=None, name=None, biography=None, birth_date=None, nationality=None, website=None, contact_info=None):
        self._artist_id = artist_id
        self._name = name
        self._biography = biography
        self._birth_date = birth_date
        self._nationality = nationality
        self._website = website
        self._contact_info = contact_info

    def get_artist_id(self):
        return self._artist_id

    def set_artist_id(self, artist_id):
        self._artist_id = artist_id

    # Repeat for other fields
