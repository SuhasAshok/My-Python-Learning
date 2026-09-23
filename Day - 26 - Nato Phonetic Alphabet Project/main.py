import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_list = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
output = [nato_list[letter] for letter in word]
print(output)