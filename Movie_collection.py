movies = [
    ("The Shawshank Redemption", "Drama", 1994),
    ("The Dark Knight", "Action", 2008),
    ("Inception", "Sci-Fi", 2010),
    ("Pulp Fiction", "Crime", 1994),
    ("The Godfather", "Crime", 1972),
    ("The Matrix", "Sci-Fi", 1999)
]

def categorize_by_genre(movies):
    
    genre_dict = {}
    for title, genre, year in movies:
        if genre not in genre_dict:
            genre_dict[genre] = set()
        genre_dict[genre].add((title, year))
    return genre_dict

def add_movie(movies, title, genre, year):
    
    movies.append((title, genre, year))
    print(f"Movie '{title}' added successfully!")

def remove_movie(movies, title):
    
    for movie in movies:
        if movie[0].lower() == title.lower():
            movies.remove(movie)
            print(f"Movie '{title}' removed successfully!")
            return
    print(f"Movie '{title}' not found in the collection.")

def search_movie(movies, title):
    
    for movie in movies:
        if movie[0].lower() == title.lower():
            print(f"Movie found: {movie[0]} - Genre: {movie[1]}, Year: {movie[2]}")
            return
    print(f"Movie '{title}' not found in the collection.")

def sort_movies_by_year(movies):
    
    sorted_movies = sorted(movies, key=lambda movie: movie[2])
    print("Movies sorted by year:")
    for movie in sorted_movies:
        print(f"{movie[0]} - Genre: {movie[1]}, Year: {movie[2]}")

def count_unique_genres(movies):
    
    genres = {genre for _, genre, _ in movies}
    print(f"Number of unique genres: {len(genres)}")
    print(f"Genres: {', '.join(genres)}")

def display_movies_by_genre(genre_dict):
    
    print("\nMovies categorized by genre:")
    for genre, movie_set in genre_dict.items():
        print(f"\n{genre}:")
        for title, year in movie_set:
            print(f" - {title} ({year})")

# if __name__ == "__main__":
while True:
        print("\nMovie Collection Organizer:")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. Search Movie")
        print("4. Sort Movies by Year")
        print("5. Display Movies by Genre")
        print("6. Count Unique Genres")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input("Enter the movie title: ")
            genre = input("Enter the movie genre: ")
            try:
                year = int(input("Enter the release year: "))
                add_movie(movies, title, genre, year)
            except ValueError:
                print("Please enter a valid year.")
        elif choice == '2':
            title = input("Enter the movie title to remove: ")
            remove_movie(movies, title)
        elif choice == '3':
            title = input("Enter the movie title to search for: ")
            search_movie(movies, title)
        elif choice == '4':
            sort_movies_by_year(movies)
        elif choice == '5':
            genre_dict = categorize_by_genre(movies)
            display_movies_by_genre(genre_dict)
        elif choice == '6':
            count_unique_genres(movies)
        elif choice == '7':
            print("Thank You, Have a nice day!!!")
            break
        else:
            print("Invalid choice! Please select a valid option.")
