# Smart Recommendation System
# Rule-Based Recommendation using Python

print("=" * 50)
print("🎬 Welcome to Smart Recommendation System")
print("=" * 50)

while True:

    print("\nChoose a Category")
    print("1. Movies")
    print("2. Books")
    print("3. Music")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    # ---------------- MOVIES ----------------
    if choice == "1":

        print("\nMovie Genres")
        print("Action")
        print("Comedy")
        print("Romance")
        print("Horror")
        print("Sci-Fi")

        genre = input("\nEnter your favorite genre: ").lower()

        if "action" in genre:
            print("\nRecommended Movies")
            print("• John Wick")
            print("• Extraction")
            print("• Mad Max: Fury Road")

        elif "comedy" in genre:
            print("\nRecommended Movies")
            print("• 3 Idiots")
            print("• Bhool Bhulaiyaa")
            print("• Welcome")

        elif "romance" in genre:
            print("\nRecommended Movies")
            print("• Jab We Met")
            print("• The Notebook")
            print("• Titanic")

        elif "horror" in genre:
            print("\nRecommended Movies")
            print("• The Conjuring")
            print("• Annabelle")
            print("• It")

        elif "sci" in genre:
            print("\nRecommended Movies")
            print("• Interstellar")
            print("• Inception")
            print("• The Martian")

        else:
            print("Sorry! No recommendations found.")

    # ---------------- BOOKS ----------------
    elif choice == "2":

        print("\nBook Categories")
        print("Fiction")
        print("Mystery")
        print("Self Help")
        print("Fantasy")

        book = input("\nEnter your favorite category: ").lower()

        if "fiction" in book:
            print("\nRecommended Books")
            print("• The Alchemist")
            print("• To Kill a Mockingbird")

        elif "mystery" in book:
            print("\nRecommended Books")
            print("• Sherlock Holmes")
            print("• Gone Girl")

        elif "self" in book:
            print("\nRecommended Books")
            print("• Atomic Habits")
            print("• The Power of Now")

        elif "fantasy" in book:
            print("\nRecommended Books")
            print("• Harry Potter")
            print("• The Hobbit")

        else:
            print("No recommendations available.")

    # ---------------- MUSIC ----------------
    elif choice == "3":

        print("\nMusic Types")
        print("Pop")
        print("Rock")
        print("Lofi")
        print("Classical")

        music = input("\nEnter your favorite music type: ").lower()

        if "pop" in music:
            print("\nRecommended Artists")
            print("• Taylor Swift")
            print("• Dua Lipa")

        elif "rock" in music:
            print("\nRecommended Artists")
            print("• Imagine Dragons")
            print("• Linkin Park")

        elif "lofi" in music:
            print("\nRecommended Channels")
            print("• Lofi Girl")
            print("• Chillhop Music")

        elif "classical" in music:
            print("\nRecommended Composers")
            print("• Mozart")
            print("• Beethoven")

        else:
            print("No recommendations available.")

    # ---------------- EXIT ----------------
    elif choice == "4":
        print("\nThank you for using Smart Recommendation System!")
        break

    else:
        print("\nInvalid Choice! Please try again.")
