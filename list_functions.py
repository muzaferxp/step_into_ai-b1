#List Functions

Tech_list = ['Python','JavaScript','Html','CSS','Bootstrap']
Int_list = [10,9,5,4,3]
Int_list2 = [10,9,11,12]
print(Tech_list)

#Getting length
print('Length : ' , len(Tech_list))

#Sort 
Int_list.sort()
print(Int_list)

#type
print(type(Tech_list))

#append
Tech_list.append('Flask')
print(Tech_list)


#index
print(Tech_list.index('Flask'))


#min
print(min(Tech_list))
print(min(Int_list))

#max
print(max(Tech_list))
print(max(Int_list))


#implementation

data = []
f = open('C:/Users/R computer/Downloads/students2.csv', 'r')

for line in f:
    data.append(line)

print(data[:10])

data_base  = []

def insert_data(user):
    data_base.append(user)

def sign_up():
    username = input('Username: ')
    password = input('Password: ')

    obj = {}

    obj['username'] = username
    obj['password'] = password

    print(obj)

    insert_data(obj)

sign_up()

print(data_base)

    
    
    

    





