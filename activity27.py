#adding dictionary
empty_dictionary = {}
def print_anime():
    for x,y in empty_dictionary.items():
        print(f"CODE -- {x} ANIME -- {y}")
def search(key):
    print(f"Result shows {empty_dictionary[key]} on the List")

print("Save your anime List")
while True:
    keys = input("Keys for this anime(EX. OP for One Piece):\t")
    value = input("Anime Title:\t")
    empty_dictionary[keys] = value

    x = input("Continue?(yes/no/print/search):\t").lower()

    if x == "yes":
        continue
    elif x == "no":
        print("Program Cancelled")
        break
    elif x == "print":
        print_anime()
    elif x == "search":
        key = input("Type the code of the anime:")
        search(key)
    else:
        print("Select within the choices")
