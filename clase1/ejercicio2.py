words = ['cat', 'window', 'defenestrate']
print('Con for')
string = ""
for w in words:
    string = string + w + ";"
    print(w)
print('Total for: ' + string)


print('Con while')
i = 0
string = ""
while (i < len(words)):
    string = string + words[i] +";"
    print(words[i])
    i = i + 1
print('Total while: ' + string)