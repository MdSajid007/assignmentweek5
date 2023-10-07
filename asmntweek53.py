while True:
    str1 = input("Enter a string: ")

    if str1 == 'done':
        print("Bye!")
        break
    num= 0
    upper = 0
    lower = 0
    other = 0

    
    for word in str1:
        if word.isupper():
            upper += 1
        elif word.islower():
            lower += 1
        elif word.isdigit():
            num += 1
        else:
            other += 1
        
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)
    print("Numbers:", num)
    print("Other characters:", other)
    



