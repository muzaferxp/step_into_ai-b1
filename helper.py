print('Welcome')

def build_pyramid(r): 
    for x in range(r):
        print( '_' * r  + '*' * x + '*' * x + '_' * r )
        r -= 1
    helper()

build_pyramid(5)   
box_office = { 'Avengers' : 10 ,
               'Harry Porter' : 10
            }

status = 'Assigned AND Executed'

print(status)
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

helper()

        
