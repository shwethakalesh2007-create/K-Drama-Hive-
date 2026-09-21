import pandas as pd

df = pd.read_csv("KDrama.csv")
import pandas as pd

df = pd.read_csv("KDrama.csv")

print("===================================")
print("          🎬 K-DRAMA HIVE")
print("===================================")

print("\n1. Search by Genre")
print("2. Search by Title")
print("3. Search by Trope")
print("4. Find Something Like This Drama")

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
