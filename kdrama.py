import pandas as pd
import random

df = pd.read_csv("kdrama.csv")

print("===================================")
print("          🎬 K-DRAMA HIVE")
print("===================================")

print("\n1. Search by Title")
print("2. Search by Trope")
print("3. Find Something Like This Drama")
print("4. Find Kdramas with Similar L5ead Characters")
print("5. Pick a Random K-Drama")
choice = input("\nChoose an option: ")

# ---------------- TITLE SEARCH ----------------
if choice == "1":
    title = input("\nEnter a Kdrama title: ").lower()
    result = df[df["Title"].str.lower().str.contains(title)]

    if len(result) > 0:
        print("\n🎬 K-Drama Found:")
        print(result.to_string(index=False))

        similar = input("\nDo you want to find something similar to this drama? (yes/no): ").lower()
        if similar == "yes":
            print("\nComing next! 🔥")
    else:
        print("\nNo K-Drama found.")

# ---------------- TROPE SEARCH ----------------
elif choice == "2":
    trope = input("\nEnter a trope: ").lower()
    result = df[
        df["Trope_1"].str.lower().str.contains(trope) |
        df["Trope_2"].str.lower().str.contains(trope) |
        df["Trope_3"].str.lower().str.contains(trope) |
        df["Trope_4"].str.lower().str.contains(trope)
    ]

    if len(result) > 0:
        print("\n🎬 K-Dramas with this trope:")
        print(result[["Title", "Trope_1", "Trope_2", "Trope_3", "Trope_4"]].to_string(index=False))

        compare = input("\nDo you have a drama with a similar trope that you want to compare? (yes/no): ").lower()
        if compare == "yes":
            drama = input("\nEnter the drama title: ").lower()
            drama_result = df[df["Title"].str.lower().str.contains(drama)]

            if len(drama_result) > 0:
                print("\n🎬 Comparison:")
                print("\nSelected Drama:")
                print(drama_result[["Title", "Trope_1", "Trope_2", "Trope_3", "Trope_4"]].to_string(index=False))

                print("\nDramas matching your trope:")
                print(result[["Title", "Trope_1", "Trope_2", "Trope_3", "Trope_4"]].to_string(index=False))
            else:
                print("\nDrama not found.")
    else:
        print("\nNo K-Dramas found with this trope.")

# ---------------- SIMILAR DRAMA ----------------
elif choice == "3":
    title = input("\nEnter a Kdrama title: ").lower()
    result = df[df["Title"].str.lower().str.contains(title)]

    if len(result) > 0:
        print("\n🎬 Drama Found:")
        print(result.to_string(index=False))

        print("\nSimilar dramas:")
        print(result[["Similar_To_1", "Similar_To_2"]].to_string(index=False))
    else:
        print("\nNo K-Drama found.")

# ---------------- SIMILAR LEAD CHARACTERS ----------------
elif choice == "4":
    drama_name = input("\nEnter a K-drama: ").lower()
    sub_choice = input("Compare with female lead (f) or male lead (m)? ").lower()

    if sub_choice in ["f", "m"]:
        # Pick the right column
        column = "Female_Lead_Type" if sub_choice == "f" else "Male_Lead_Type"

        # Find the drama
        result = df[df["Title"].str.lower().str.contains(drama_name)]
        if len(result) == 0:
            print("\nDrama not found.")
        else:
            target_type = result.iloc[0][column].lower()
            matches = df[df[column].str.lower().str.contains(target_type) &
                         ~df["Title"].str.lower().str.contains(drama_name)]

            if len(matches) > 0:
                print(f"\n🎬 Dramas with {column.replace('_',' ').lower()} like {drama_name}:")
                print(matches[["Title", column]].to_string(index=False))
            else:
                print("\nNo similar leads found.")
    else:
        print("Invalid choice.")

# ---------------- RANDOM K-DRAMA ----------------

elif choice == "5":

    print("\n1. Random from All K-Dramas")
    print("2. Random by Genre")

    random_choice = input("\nChoose an option: ")

    if random_choice == "1":

        again = "yes"

        while again == "yes":

            random_drama = random.choice(df["Title"].tolist())

            print("\n🎲 Your random K-Drama is:")
            print(random_drama)

            again = input(
                "\nWant another one? (yes/no): "
            ).lower()


    elif random_choice == "2":

        genre = input("\nEnter a genre: ").lower()

        result = df[
            df["Genre_1"].str.lower().str.contains(genre) |
            df["Genre_2"].str.lower().str.contains(genre) |
            df["Genre_3"].str.lower().str.contains(genre)
        ]

        if len(result) > 0:

            again = "yes"

            while again == "yes":

                random_drama = random.choice(
                    result["Title"].tolist()
                )

                print("\n🎲 Your random K-Drama is:")
                print(random_drama)

                again = input(
                    "\nWant another one? (yes/no): "
                ).lower()

        else:
            print("\nNo K-Dramas found for this genre.")


    else:
        print("\nInvalid option.")



# ---------------- INVALID OPTION ----------------
else:
    print("\nInvalid option.")
