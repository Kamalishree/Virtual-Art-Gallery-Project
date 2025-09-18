class Gallery:
    def __init__(self, gallery_id=None, name=None, description=None, location=None, curator_id=None, opening_hours=None):
        self._gallery_id = gallery_id
        self._name = name
        self._description = description
        self._location = location
        self._curator_id = curator_id
        self._opening_hours = opening_hours

    def get_gallery_id(self):
        return self._gallery_id

    def set_gallery_id(self, gallery_id):
        self._gallery_id = gallery_id

    # Repeat for other fields
