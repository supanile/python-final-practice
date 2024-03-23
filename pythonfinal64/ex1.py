def find_vowels(text):
    vowels = 'aeiou'
    found_vowels = []
    positions = []

    for i in range(len(text)):
        char = text[i]
        if char in vowels:
            found_vowels.append(char)
            positions.append(str(i))

    return ' '.join(found_vowels), ' '.join(positions)

text = input("name: ")
vowels, positions = find_vowels(text)
print(positions)
print(vowels)
