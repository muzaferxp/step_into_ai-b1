#GLOBAL variables 
Login_status = False

box_office = { 'Avengers' : 10 ,
               'Harry Porter' : 10
            }


#dictionary database example
dict_data = {
    'name0' : 'Pass0',
    'name2' : 'Pass2'
    }


def build_pyramid(r):
    for x in range(r):
        print( '_' * r  + '*' * x + '*' * x + '_' * r )
        r -= 1
    helper()

def book_seats(movie):
    status = 'UPDATED!!!'
    print(status)
    if box_office[movie] > 0:
        print('Seats Availability : ' ,  (box_office[movie]))
        seats = input('How Many Seats you need? ')
        box_office[movie] = box_office[movie] - int(seats)

        print('Booking Done Successfully!')

        print(box_office)

        helper()
    else:
        print('Seats Not Available')
        helper()

    
def helper():
    #verify user login    
    print('What can i do for you? ')
    print('Select 1 for booking seats ')
    print('Select 2 for Building a Pyramid')

    ans = int(input())
    
    if ans == 2:
        #Can Ask Width of Pyramid
        build_pyramid(9)
    if ans == 1:
        #Can Ask Movie name
        book_seats('Avengers')



def authenticate(user,passw):
    for x in dict_data:
        if x == user:
            if dict_data[x] == passw:
                print('Logged in for dictionary!')
                Login_status = True
                return True
            else:
                print("Password doesn't match")
                return False
        else:
            print('User not found!')

    return False


if Login_status:
    print('Logged IN')

    
#Login_user() Take username and password from user input
#calling authenticate(user,passw)
#if true -> helper()
#else -> login_user()
        
