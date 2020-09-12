database = {
    'Techs' : ['Python','Html', 'CSS', 'JavaScript'],
    'Date' : '09-12-2020'
    }

print(database)

database_copy = database.copy()

#clear
database.clear()


print(database)

print(database_copy)


#formkeys (create a dictionary)
x = ('key1', 'key2', 'key3')
y = ('val', 'val2', 'val3')

thisdict = dict.fromkeys(x, y)

print(thisdict)


#retrive using values
Dt = database_copy.get('Date')
print(Dt)
database_copy['Date'] = '09-13-2020'
print(database_copy['Date'])

#assign values in a loop
rand = ['HTML' , 'CSS' , 'HTML','HTML' , 'CSS' , 'HTML']

obj = {}
for item in rand:
    if item in obj:
        obj[item] += 1
    else:
        obj[item] = 1

print(obj)

#key
k = database_copy.keys()

for x in k:
    print(database_copy[x])

#values
print(database_copy.values())

#pop
x = database_copy.pop('Date')

print(x)

if 'Date' in database_copy:
    database_copy.pop('Date')

try:
    database_copy.pop('Date')
except:
    pass


database_copy.update({'Time' : '09:13'})


print(database_copy)


#Create a data (Dictionary)
#Create a Function to add student name {'Student_name' : 0}
###can also use nested dictionary for each subject
eg = {'student' : {
    'DataScience' : 56,
    'Python' : 80
    }
      }

#Create a Function deleting students 
#create a Function for adding marks {'Student_name' : 95}

