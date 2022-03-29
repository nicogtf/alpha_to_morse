import pandas as pd
import unicodedata

# url = "http://www.sckans.edu/~sireland/radio/code.html"
url = "morse_code.html"
tables = pd.read_html(url)
alpha = tables[0]
numbers_punct = tables[1]

alpha.drop(columns=['NATO','English', 'American', 'Italian', 'German', 'International'], inplace=True)
numbers = numbers_punct.iloc[:,0:2]
punct = numbers_punct.iloc[:,2:4]
punct.dropna(inplace=True)

old_values = punct['Punctuation'].tolist()
new_values = ['.', ',', ':', '?', "'", '-', '/', '()', '"']
punct['Punctuation'] = punct['Punctuation'].replace(old_values, new_values)


# df2 = df.rename({'a': 'X', 'b': 'Y'}, axis=1)

alpha = alpha.rename({'Letter': 'alpha', 'Morse': 'morse'}, axis=1)
numbers = numbers.rename({'Number': 'alpha', 'Code': 'morse'}, axis=1)
punct = punct.rename({'Punctuation': 'alpha', 'Code.1': 'morse'}, axis=1)

# print(type(alpha))
#
# print(alpha.columns)
# print(numbers)
# print(punct)



alpha_to_morse = pd.concat([alpha, numbers, punct], ignore_index=True)

for idx in alpha_to_morse.index:
    string_revised = " ".join(alpha_to_morse.iloc[idx,1])
    alpha_to_morse.iloc[idx, 1] = string_revised


# add one row for "space"
alpha_to_morse.loc[alpha_to_morse.shape[0]] = [' ', ' '*7]
# alpha_to_morse['alpha'].astype(str)
# print(alpha_to_morse.dtypes)

alpha_to_morse.set_index('alpha', inplace=True)

# print(type(alpha_to_morse.iloc[-1][0]))
# print(alpha_to_morse)

# print(morse)

string_to_convert = input('Please type what you want to convert to Morse Code:\n')

# for item in string_to_convert:
#     print(type(item))
string_to_convert_og = string_to_convert
string_to_convert = unicodedata.normalize('NFD', string_to_convert).encode('ascii', 'ignore').decode('utf-8')
string_to_convert = string_to_convert.upper()


morse_string = ''

for char in string_to_convert:
    if char.isdigit():
        char = int(char)
    morse_char = alpha_to_morse.loc[char]['morse']
    morse_string += morse_char + ' '*3




print(f"String to be coded:\t'{string_to_convert_og}'\nMorse Code:\t\t{morse_string}")






