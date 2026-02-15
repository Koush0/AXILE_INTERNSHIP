dictionary = {
    "python": "Programming language",
    "list": "Collection of items",
    "tuple": "Immutable collection"
}

word = input("Enter word to search: ").lower()

if word in dictionary:
    print("Meaning:", dictionary[word])
else:
    print("Word not found.")
