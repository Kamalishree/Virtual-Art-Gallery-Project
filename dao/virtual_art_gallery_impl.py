import pyodbc
from dao.ivirtual_art_gallery import IVirtualArtGallery
from util.db_connection_util import DBConnection
from entity.artwork import Artwork
from exception.artwork_not_found_exception import ArtworkNotFoundException
from exception.user_not_found_exception import UserNotFoundException

class VirtualArtGalleryImpl(IVirtualArtGallery):
    def __init__(self):
        self.conn = DBConnection.get_connection()

    def add_artwork(self, artwork: Artwork) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL, ArtistID)
                VALUES (?, ?, ?, ?, ?, ?)
            """, artwork._title, artwork._description, artwork._creation_date,
                 artwork._medium, artwork._image_url, artwork._artist_id)
            self.conn.commit()
            return True
        except Exception as e:
            print("Error in add_artwork:", e)
            return False

    # def update_artwork(self, artwork: Artwork) -> bool:
    #     try:
    #         cursor = self.conn.cursor()
    #         cursor.execute("""
    #             UPDATE Artwork
    #             SET Title = ?, Description = ?, CreationDate = ?, Medium = ?, ImageURL = ?, ArtistID = ?
    #             WHERE ArtworkID = ?
    #         """, artwork._title, artwork._description, artwork._creation_date,
    #              artwork._medium, artwork._image_url, artwork._artist_id, artwork._artwork_id)
    #         self.conn.commit()
    #         return cursor.rowcount > 0
    #     except Exception as e:
    #         print("Error in update_artwork:", e)
    #         return False
    def update_artwork(self, artwork: Artwork) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE Artwork
                SET Title = ?, Description = ?, CreationDate = ?, Medium = ?, ImageURL = ?, ArtistID = ?
                WHERE ArtworkID = ?
            """, (
                artwork._title,
                artwork._description,
                artwork._creation_date,
                artwork._medium,
                artwork._image_url,
                artwork._artist_id,
                artwork._artwork_id
            ))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error in update_artwork:", e)
            return False


    def remove_artwork(self, artwork_id: int) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Artwork WHERE ArtworkID = ?", artwork_id)
            self.conn.commit()
            if cursor.rowcount == 0:
                raise ArtworkNotFoundException(f"Artwork with ID {artwork_id} not found.")
            return True
        except Exception as e:
            print("Error in remove_artwork:", e)
            return False

    # def get_artwork_by_id(self, artwork_id: int) -> Artwork:
    #     try:
    #         cursor = self.conn.cursor()
    #         cursor.execute("SELECT * FROM Artwork WHERE ArtworkID = ?", artwork_id)
    #         row = cursor.fetchone()
    #         if not row:
    #             raise ArtworkNotFoundException()
    #         return Artwork(*row)
    #     except Exception as e:
    #         print("Error in get_artwork_by_id:", e)
    #         return None 
    def get_artwork_by_id(self, artwork_id: int):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Artwork WHERE ArtworkID = ?", (artwork_id,))
            row = cursor.fetchone()

            if row is None:
                raise ArtworkNotFoundException(f"No artwork found with ID: {artwork_id}")

            return Artwork(*row)

        except ArtworkNotFoundException as ae:
            ("Error in get_artwork_by_id:", ae)
            return None

        except Exception as e:
            print("Unexpected error in get_artwork_by_id:", e)
            return None



    def search_artworks(self, keyword: str) -> list[Artwork]:
        artworks = []
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT * FROM Artwork
                WHERE Title LIKE ? OR Description LIKE ?
            """, f"%{keyword}%", f"%{keyword}%")
            rows = cursor.fetchall()
            for row in rows:
                artworks.append(Artwork(*row))
            return artworks
        except Exception as e:
            print("Error in search_artworks:", e)
            return []

    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO User_Favorite_Artwork (UserID, ArtworkID)
                VALUES (?, ?)
            """, user_id, artwork_id)
            self.conn.commit()
            return True
        except Exception as e:
            print("Error in add_artwork_to_favorite:", e)
            return False

    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                DELETE FROM User_Favorite_Artwork
                WHERE UserID = ? AND ArtworkID = ?
            """, user_id, artwork_id)
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Error in remove_artwork_from_favorite:", e)
            return False

    def get_user_favorite_artworks(self, user_id: int) -> list[Artwork]:
        artworks = []
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT a.* FROM Artwork a
                JOIN User_Favorite_Artwork ufa ON a.ArtworkID = ufa.ArtworkID
                WHERE ufa.UserID = ?
            """, user_id)
            rows = cursor.fetchall()
            for row in rows:
                artworks.append(Artwork(*row))
            return artworks
        except Exception as e:
            print("Error in get_user_favorite_artworks:", e)
            return []
