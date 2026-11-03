total_seats = 5

while total_seats > 0:
    print("Seat Booked Successfully")
    print("Remaining Seats:", total_seats - 1)
    total_seats -= 1

print("All Seats Are Filled")


total_candy=5

while total_candy>0:
    print("candy sold successfully")
    print("remaining candy:",total_candy-1)
    total_candy-=1


print ("All Candy Are sold")


print("Available Seat Numbers:")

for seat in range(10,0,-1):
    print("Seat Number:", seat)

n= int (input("Enter the Number:"))
sum=0
for i in range (1,n+1):
    sum =sum + i
    print (sum)



    
n= int (input("Enter the Number:"))
f=1
for i in range (1,n+1):
    f =f*i
    #print (f)

    

total_seats = 5

for booking in range(1, 10):

    if booking > total_seats:
        print("No Seats Available")
        break

    if booking == 3:
        print("Checking Special Reservation")
        continue

    pass

    print("Seat", booking, "Booked Successfully")
