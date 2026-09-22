import pandas as pd
import random

df = pd.read_csv("KDrama.csv")

print("===================================")
print("          🎬 K-DRAMA HIVE")
print("===================================")

print("\n1. Search by Genre")
print("2. Search by Title")
print("3. Search by Trope")
print("4. Find Something Like This Drama")
print("5. 🎲 Pick a Random K-Drama")
print("6. 📺 Search by Platform")

choice = input("\nChoose an option: ")


# ---------------- GENRE SEARCH ----------------

if choice == "1":

    genre = input("\nEnter a genre: ").lower()

    print("\nDo you want a specific lead?")
    print("1. Female Lead")
    print("2. Male Lead")
    print("3. No Preference")

    lead_choice = input("\nChoose an option: ")

    if lead_choice == "1":

        lead_type = input(
            "\nWhat type of female lead do you want? "
        ).lower()

        result = df[
            (
                df["Genre_1"].str.lower().str.contains(genre) |
                df["Genre_2"].str.lower().str.contains(genre) |
                df["Genre_3"].str.lower().str.contains(genre)
            )
            &
            df["Female_Lead_Type"].str.lower().str.contains(lead_type)
        ]

        if len(result) > 0:

            print("\n🎬 K-Dramas found:")

            print(
                result[
                    ["Title", "Female_Lead_Type"]
                ].to_string(index=False)
            )

        else:
            print("\nNo K-Dramas found.")


    elif lead_choice == "2":

        lead_type = input(
            "\nWhat type of male lead do you want? "
        ).lower()

        result = df[
            (
                df["Genre_1"].str.lower().str.contains(genre) |
                df["Genre_2"].str.lower().str.contains(genre) |
                df["Genre_3"].str.lower().str.contains(genre)
            )
            &
            df["Male_Lead_Type"].str.lower().str.contains(lead_type)
        ]

        if len(result) > 0:

            print("\n🎬 K-Dramas found:")

            print(
                result[
                    ["Title", "Male_Lead_Type"]
                ].to_string(index=False)
            )

        else:
            print("\nNo K-Dramas found.")


    elif lead_choice == "3":

        result = df[
            df["Genre_1"].str.lower().str.contains(genre) |
            df["Genre_2"].str.lower().str.contains(genre) |
            df["Genre_3"].str.lower().str.contains(genre)
        ]

        if len(result) > 0:

            print("\n🎬 K-Dramas found:")

            print(
                result[
                    ["Title", "Genre_1", "Genre_2", "Genre_3"]
                ].to_string(index=False)
            )

        else:
            print("\nNo K-Dramas found.")


    else:
        print("\nInvalid option.")


# ---------------- TITLE SEARCH ----------------

elif choice == "2":

    title = input("\nEnter a Kdrama title: ").lower()

    result = df[
        df["Title"].str.lower().str.contains(title)
    ]

    if len(result) > 0:

        print("\n🎬 K-Drama Found:")

        print(result.to_string(index=False))

        similar = input(
            "\nDo you want to find something similar to this drama? (yes/no): "
        ).lower()

        if similar == "yes":

            print("\nSimilar dramas:")

            print(
                result[
                    ["Similar_To_1", "Similar_To_2"]
                ].to_string(index=False)
            )

    else:
        print("\nNo K-Drama found.")


# ---------------- TROPE SEARCH ----------------

elif choice == "3":

    trope = input("\nEnter a trope: ").lower()

    result = df[
        df["Trope_1"].str.lower().str.contains(trope) |
        df["Trope_2"].str.lower().str.contains(trope) |
        df["Trope_3"].str.lower().str.contains(trope) |
        df["Trope_4"].str.lower().str.contains(trope)
    ]

    if len(result) > 0:

        print("\n🎬 K-Dramas with this trope:")

        print(
            result[
                ["Title", "Trope_1", "Trope_2",
                 "Trope_3", "Trope_4"]
            ].to_string(index=False)
        )

        compare = input(
            "\nDo you have a drama with a similar trope that you want to compare? (yes/no): "
        ).lower()

        if compare == "yes":

            drama = input("\nEnter the drama title: ").lower()

            drama_result = df[
                df["Title"].str.lower().str.contains(drama)
            ]

            if len(drama_result) > 0:

                print("\n🎬 Comparison:")

                print("\nSelected Drama:")

                print(
                    drama_result[
                        ["Title", "Trope_1", "Trope_2",
                         "Trope_3", "Trope_4"]
                    ].to_string(index=False)
                )

                print("\nDramas matching your trope:")

                print(
                    result[
                        ["Title", "Trope_1", "Trope_2",
                         "Trope_3", "Trope_4"]
                    ].to_string(index=False)
                )

            else:
                print("\nDrama not found.")

    else:
        print("\nNo K-Dramas found with this trope.")


# ---------------- SIMILAR DRAMA ----------------

elif choice == "4":

    title = input("\nEnter a Kdrama title: ").lower()

    result = df[
        df["Title"].str.lower().str.contains(title)
    ]

    if len(result) > 0:

        print("\n🎬 Drama Found:")

        print(result.to_string(index=False))

        print("\nSimilar dramas:")

        print(
            result[
                ["Similar_To_1", "Similar_To_2"]
            ].to_string(index=False)
        )

    else:
        print("\nNo K-Drama found.")


# ---------------- RANDOM K-DRAMA ----------------

elif choice == "5":

    print("\n1. Random from All K-Dramas")
    print("2. Random by Genre")

    random_choice = input("\nChoose an option: ")

    if random_choice == "1":

        again = "yes"

        while again == "yes":

            random_drama = random.choice(
                df["Title"].tolist()
            )

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


# ---------------- PLATFORM SEARCH ----------------

elif choice == "6":

    platform = input("\nEnter a platform: ").lower()

    result = df[
        df["Platform_1"].str.lower().str.contains(platform) |
        df["Platform_2"].str.lower().str.contains(platform)
    ]

    if len(result) > 0:

        print("\n📺 K-Dramas on this platform:")

        print(
            result["Title"].to_string(index=False)
        )

    else:
        print("\nNo K-Dramas found on this platform.")


# ---------------- INVALID OPTION ----------------

else:

    print("\nInvalid option.")
