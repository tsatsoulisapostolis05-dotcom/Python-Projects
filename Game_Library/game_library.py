games = []

while True:
    print("\nGAME LIBRARY")
    print("1. Add a game")
    print("2. View all games")
    print("3. Exit")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        title = input("Enter the title of the game: ")
        genre = input("Enter the genre of the game: ")
        platform = input("Enter the platform of the game: ")

        try:
            rating = float(input("Enter the rating of the game: "))

        except ValueError:
            print("The rating must be a number.")
            continue

        if rating < 0 or rating > 10:
            print("The rating must be between 0 and 10.")
            continue

        elif rating <= 4:
            print("This game is not recommended.")

        elif rating <= 7:
            print("This game is recommended.")

        else:
            print("This game is highly recommended.")

        game = {
            "title": title,
            "genre": genre,
            "platform": platform,
            "rating": rating
        }

        games.append(game)
        print("Game added successfully!")

    elif choice == "2":
        if games:
            print("\nYour games are:")

            for game in games:
                print(f"\nTitle: {game['title']}")
                print(f"Genre: {game['genre']}")
                print(f"Platform: {game['platform']}")
                print(f"Rating: {game['rating']}/10")
                print("--------------------")

        else:
            print("Your game library is empty.")

    elif choice == "3":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")