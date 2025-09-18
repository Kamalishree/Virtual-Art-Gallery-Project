class Artwork:
    def __init__(self, artwork_id=None, title=None, description=None, creation_date=None, medium=None, image_url=None, artist_id=None):
        self._artwork_id = artwork_id
        self._title = title
        self._description = description
        self._creation_date = creation_date
        self._medium = medium
        self._image_url = image_url
        self._artist_id = artist_id

    def get_artwork_id(self):
        return self._artwork_id

    def set_artwork_id(self, artwork_id):
        self._artwork_id = artwork_id

    # Repeat for title, description, etc.
