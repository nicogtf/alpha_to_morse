import unicodedata

# myfoo = input()
myfoo = 'òòàè'

# ‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’.

output = unicodedata.normalize('NFD', myfoo).encode('ascii', 'ignore')
output2 = unicodedata.normalize('NFD', myfoo).encode('ascii', 'ignore').decode('utf-8')



print(myfoo)
print(output)
print(type(output))
print(output2)
