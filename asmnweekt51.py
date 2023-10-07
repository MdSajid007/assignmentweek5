while True:
    given_input = input("Please enter two words: ")
    
    if given_input == "done":
        print("Bye!")
        break

    if ' ' not in given_input:
        continue

    words = given_input.split()

    word1, word2 = words
    if word1 > word2:
        result = word2
    else:
        result = word1

    print(f"{result} comes first.")
