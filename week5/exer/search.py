from museum.artist import get_artists


def main():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")

main()
