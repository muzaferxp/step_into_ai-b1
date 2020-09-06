#String
#int
#list
#tuple
#dictionary

tech_list = ['Python', 'Javascript', 'Flask']

#print(tech_list)

#print(tech_list[0])

#for x in tech_list:
    #print(x)


#for x in tech_list:
    #if x == 'Flask':
        #print('Element Found')


#if 'Flask' in tech_list:
    #print('Element Found')

#print(tech_list.index('Python'))

#print(len(tech_list))



#database model
#ID,USERNAME,PASSWORD,BATCH

#tuple database example
database = ([1,'name1','Pass1','batch 1'],
            [2,'name2','Pass2','batch 1'],
            [3,'name3','Pass3','batch 1'],
            [4,'name4','Pass4','batch 1'])

#dictionary database example
dict_data = {
    'name0' : 'Pass0',
    'name2' : 'Pass2'
    }




#sample credentials
user = 'name1'
passw = 'Pass1'


#Authentication for Lists and Tuples
for x in database:
    if x[1] == user:
        if x[2] == passw:
            print('Logged in!')
            break #return home page
        else:
            print("Password doesn't match") #return login page
            break
    else:
        print('User not found!')


#Authentication for dictionary or Json
for x in dict_data:
    if x == user:
        if dict_data[x] == passw:
            print('Logged in for dictionary!')
            break
        else:
            print("Password doesn't match")
            break
    else:
        print('User not found!')


        

        
