import unittest
from dao.virtual_art_gallery_impl import VirtualArtGalleryImpl
from entity.artwork import Artwork
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestArtwork(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = VirtualArtGalleryImpl()

    def test_add_artwork(self):
        artwork = Artwork(
            artwork_id=None,
            title="Test Art",
            description="Test Description",
            creation_date="2023-01-01",
            medium="Oil",
            image_url="http://test.url/art.jpg",
            artist_id=1  # Assume artist with ID 1 exists
        )
        result = self.service.add_artwork(artwork)
        self.assertTrue(result)

    def test_update_artwork(self):
        # Assume artwork ID 1 exists
        artwork = Artwork(
            artwork_id=1,
            title="Updated Title",
            description="Updated Description",
            creation_date="2023-02-01",
            medium="Acrylic",
            image_url="http://test.url/new.jpg",
            artist_id=1
        )
        result = self.service.update_artwork(artwork)
        self.assertTrue(result)

    def test_remove_artwork(self):
        # Add a new artwork to ensure we can remove it
        artwork = Artwork(None, "To Delete", "Desc", "2023-03-01", "Digital", "url", 1)
        self.service.add_artwork(artwork)

        # Get the last inserted artwork ID (manual workaround)
        all_artworks = self.service.search_artworks("To Delete")
        last_artwork = all_artworks[-1] if all_artworks else None
        if last_artwork:
            result = self.service.remove_artwork(last_artwork._artwork_id)
            self.assertTrue(result)
        else:
            self.fail("Test remove_artwork: could not find artwork to delete")

    def test_search_artworks(self):
        results = self.service.search_artworks("Test")
        self.assertIsInstance(results, list)

if __name__ == '__main__':
    unittest.main()
