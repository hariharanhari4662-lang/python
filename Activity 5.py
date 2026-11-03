num=271
rev=0
count=0
while num>0:
        rem=num%10
        rev =(rev*10)+rem
        num = num//10
        count = count+1
print (rev)
print ("No of Digits:",count)

num=1192
rev=0
count=0
while num>0:
        rem=num%10
        rev =(rev*10)+rem
        num = num//10
        count = count+1
print (rev)
print ("No of Digits:",count)

num=29
rev=0
count=0
while num>0:
        rem=num%10
        rev =(rev*10)+rem
        num = num//10
        count = count+1
print (rev)
print ("No of Digits:",count)


correct_pin = "1234"
pin=""

while pin !=correct_pin:
    pin = input("Enter your ATM PIN:")

print("LOgin Successful!")

