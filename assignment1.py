"""
Name: Jiaxiang Lin
Date started:22/10/2023
GitHub URL:https://github.com/Linye2000/starter_a1_songs.git
"""



import csv

def load_data():
    with open('songs.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for row in reader:
            data.append([row[0], row[1], int(row[2]), row[3]])
        return sorted(data, key=lambda x: (x[1], x[0]))

list_got = load_data()


def displaymenu():
    print("Menu:")
    print("D - Display songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")


def choice():
    selected_key = input(">>> ").strip().upper()
    return selected_key


def findall():
    list_get = sorted(list_got, key=lambda x: (x[1], x[0]))
    learned_count = 0
    to_learn_count = 0

    for i, album in enumerate(list_get, start=1):
        status = "*" if album[3] == "r" else " "
        print(f"{i}. {status} {album[0]} - {album[1]} ({album[2]})")

        if album[3] == "r":
            learned_count += 1
        else:
            to_learn_count += 1

    print(f"{learned_count} song{'s' if learned_count != 1 else ''} learned, {to_learn_count} song{'s' if to_learn_count != 1 else ''} still to learn.")
    print("=" * 30)



def addalbum():
    new_title = input("Title: ").strip()
    while new_title == "":
        print("Input can not be blank")
        new_title = input("Title: ").strip()

    new_artist = input("Artist: ").strip()
    while new_artist == "":
        print("Input can not be blank")
        new_artist = input("Artist: ").strip()

    while True:
        try:
            new_year = int(input("Year: "))
            if new_year <= 0:
                print("Number must be > 0")
            else:
                break
        except ValueError:
            print("Invalid input; enter a valid number")

    new_info = [new_title, new_artist, new_year, "c"]
    list_got.append(new_info)

    print(f"{new_title} by {new_artist} ({new_year}) added to song list.")


def countwrite():
    findall()
    while True:
        try:
            number = int(input("Enter the number of a song to mark as learned: "))
            if 1 <= number <= len(list_got):
                break
            else:
                print("Invalid song number")
        except ValueError:
            print("Invalid input; enter a valid number")

    album = list_got[number - 1]
    if album[3] == "c":
        print(f"You have already learned {album[0]}")
    else:
        album[3] = "r"
        print(f"{album[0]} by {album[1]} learned")


def quitmenu():
    with open('songs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for album in list_got:
            writer.writerow(album)

    print(f"{len(list_got)} songs saved to songs.csv")


def main():
    print("Album Tracker 1.0 - by <Jiaxiang Lin>")
    while True:
        displaymenu()
        key = choice()
        if key == "D":
            findall()
        elif key == "A":
            addalbum()
        elif key == "C":
            countwrite()
        elif key == "Q":
            quitmenu()
            break


main()


