from dao.virtual_art_gallery_impl import VirtualArtGalleryImpl
from entity.artwork import Artwork
from exception.artwork_not_found_exception import ArtworkNotFoundException
from exception.user_not_found_exception import UserNotFoundException


def main():
    service = VirtualArtGalleryImpl()

    while True:
        print("\n===== Virtual Art Gallery Menu =====")
        print("1. Add Artwork")
        print("2. Update Artwork")
        print("3. Remove Artwork")
        print("4. View Artwork by ID")
        print("5. Search Artworks")
        print("6. Add Artwork to Favorites")
        print("7. Remove Artwork from Favorites")
        print("8. Get User Favorite Artworks")
        print("0. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                title = input("Title: ")
                desc = input("Description: ")
                date = input("Creation Date (YYYY-MM-DD): ")
                medium = input("Medium: ")
                url = input("Image URL: ")
                artist_id = int(input("Artist ID: "))
                art = Artwork(None, title, desc, date, medium, url, artist_id)
                if service.add_artwork(art):
                    print("Artwork added successfully.")
                else:
                    print("Failed to add artwork.")

            elif choice == '2':
                aid = int(input("Artwork ID: "))
                title = input("Title: ")
                desc = input("Description: ")
                date = input("Creation Date (YYYY-MM-DD): ")
                medium = input("Medium: ")
                url = input("Image URL: ")
                artist_id = int(input("Artist ID: "))
                art = Artwork(aid, title, desc, date, medium, url, artist_id)
                if service.update_artwork(art):
                    print("Artwork updated.")
                else:
                    print("Failed to update artwork.")

            elif choice == '3':
                aid = int(input("Enter Artwork ID to remove: "))
                if service.remove_artwork(aid):
                    print("Artwork removed.")
                else:
                    print("Artwork not found or deletion failed.")

            elif choice == '4':
                aid = int(input("Enter Artwork ID: "))
                art = service.get_artwork_by_id(aid)
                if art:
                    print(f"Artwork: {art._title}, {art._description}, {art._medium}")
                else:
                    print("Artwork not found.")

            elif choice == '5':
                keyword = input("Enter keyword to search: ")
                results = service.search_artworks(keyword)
                if results:
                    for a in results:
                        print(f"{a._artwork_id}: {a._title} - {a._medium}")
                else:
                    print("No artworks found.")

            elif choice == '6':
                uid = int(input("Enter User ID: "))
                aid = int(input("Enter Artwork ID: "))
                if service.add_artwork_to_favorite(uid, aid):
                    print("Added to favorites.")
                else:
                    print("Failed to add.")

            elif choice == '7':
                uid = int(input("Enter User ID: "))
                aid = int(input("Enter Artwork ID: "))
                if service.remove_artwork_from_favorite(uid, aid):
                    print("Removed from favorites.")
                else:
                    print("Failed to remove.")

            elif choice == '8':
                uid = int(input("Enter User ID: "))
                favs = service.get_user_favorite_artworks(uid)
                if favs:
                    for a in favs:
                        print(f"{a._artwork_id}: {a._title}")
                else:
                    print("No favorites found.")

            elif choice == '0':
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Try again.")

        except ArtworkNotFoundException as e:
            print("Artwork Error:", e)
        except UserNotFoundException as e:
            print("User Error:", e)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == '__main__':
    main()
