dictionary = {'p': 1}


dictionary['p'] += 1

print(dictionary)

try:
    dictionary['a'] += 1
except:
   dictionary['a'] = 1 

print(dictionary)