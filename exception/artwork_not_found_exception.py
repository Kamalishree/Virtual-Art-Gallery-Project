class ArtworkNotFoundException(Exception):
    def __init__(self, message="Artwork not found with the given ID."):
        self.message = message
        super().__init__(self.message)
