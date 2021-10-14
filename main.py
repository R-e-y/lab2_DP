while True:

    action = input("Choose the action: 1 2 3 4 5 | ")
    if action.lower() == "q":
        break

    action = int(action)
    if action == 1:
        s = input("Please input some string with spaces: ")
        s = s.split()
        longest = 0  # index of longest word

        for i in range(1, len(s)):
            if len(s[longest]) < len(s[i]):
                longest = i
            # print(len(s[longest]), len(s[i]), s[longest], s[i])

        print("The longest word is", s[longest].upper())

    elif action == 2:
        s = input("Please input some string with semicolon: ")
        s = s.split("; ")
        longest = 0  # index of longest word

        for i in range(1, len(s)):
            if len(s[longest]) < len(s[i]):
                longest = i
            # print(len(s[longest]), len(s[i]), s[longest], s[i])

        print("The longest word is", s[longest].upper())

    elif action == 3:
        s = input("Please input some string: ")
        punctuation_mark = input("Please input the punctuation mark: ")
        s = s.split(punctuation_mark)
        shortest = 0  # index of shortest word

        for i in range(1, len(s)):
            if len(s[shortest]) > len(s[i]):
                shortest = i
            # print(len(s[longest]), len(s[i]), s[longest], s[i])

        print("The shortest word is", s[shortest].upper())

    elif action == 4:
        s = input("Please input some string: ")
        word = input("Please input the word which you want to find: ")
        s = s.split()

        try:
            num = s.index(word)
            print('The location of inputted word is', num + 1)
        except ValueError:
            print("There is no such word")

    elif action == 5:
        s = input("Please input some string: ")
        s = s.split()
        print("The count of words is", len(s))

    else:
        print("Input error!\n")

    print("Click q to exit\n")