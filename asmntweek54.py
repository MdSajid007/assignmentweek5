while True:
    str1 = input("Enter a string: ")
    if str1 == "done":
        print("Bye!")
        break

    result = ""
    special_char = set(":,.;!")

    for word in str1:
        if word not in special_char:
            result += word.upper()            
    print("Your string is: ", result)

