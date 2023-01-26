import random
phonebook = {}

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

"""

print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))
print(len(phonebook))

mydictionary = dict(m=1, n=2)
print(mydictionary)
print(phonebook['Chris'])
print(phonebook['chris'])





print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = "Chris"
if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")





print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()
print(phonebook)
phonebook ["Chris"] = "555-0123"
phonebook ["Joe"]= "555-444"
print(phonebook)


print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

del phonebook["Chris"]
print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()


for k in phonebook:
    print(k)
    print(phonebook[k])

for v in phonebook.values():
    print(v)

mydict = {'mylist':[1,2,3,4]}

for v in mydict.values():
    for element in v:
        print(element)

print()
print('*****  end section 5 ********')
print()



for key, value in phonebook.items():
    print(f"Name:{key} and their phone number:{value}")

for ph_tuple in phonebook.items():
    print(ph_tuple)

print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get("Chris", "key not found")
print(phone)

phone = phonebook.get("Chris", "555-5555")
print(phone)

phone.clear


print()
print('*****  end section 6 ********')
print()


print()
print('*****  start section 7 - using pop method ********')
print()


remove = phonebook.pop('Chris', 'key not found')
print(remove)
print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

#popitem method gives you both item and value, it picks a random key value from your lib and gives you
#apparently it pops out the last element and doesn't work with random
a = phonebook.popitem()
print(a)
print(phonebook)


print()
print('*****  end section 8 ********')
print()


"""

print()
print('*****  start section 9 - using random and converting to list ********')
print()

#random doesnt work with dictionaries 
#one way to work
#list_of_keys = list(phonebook)
#print(list_of_keys)
#random_key = random.choice(list_of_keys)
#print(phonebook[random_key])
#efficient way to work
print(phonebook[random.choice(list(phonebook))])

print()
print('*****  end section 9 ********')
print()








