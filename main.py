with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    letters = file_contents.lower()
    #dictionary to store length of each character found
    letter_count = {}
    for letter in letters:
        #regex to not include special characters
        if letter.isalpha() == False:
            continue
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    #sort the dictionary by frequency
    letter_count = dict(sorted(letter_count.items(), key=lambda item: item[1], reverse=True))
    for key in letter_count:
        print(f"The '{key}' character was found {letter_count[key]} times")
    