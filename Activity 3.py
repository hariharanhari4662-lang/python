#Perform Ticket Fare Calculations
number_of_passengers = 3
ticket_price = 2450
total_fare = number_of_passengers * ticket_price
print("Total Fare :", total_fare)


#Store Ticket Price and Seat Number
train_name = "Rajdhani Express"
seat_number = "B2-45"
ticket_price = 2450
journey_date = "25-May-2026"
print("Train Name :", train_name)
print("Seat Number :", seat_number)
print("Ticket Price :", ticket_price)
print("Journey Date :", journey_date)



gst_percentage = 5
gst_amount = (total_fare * gst_percentage) / 100
print("GST Amount :", gst_amount)
final_amount = total_fare + gst_amount
print("Final Payable Amount :", final_amount)


print("----------- Indian Railways Ticket -----------")
print("Passenger Name\t\t  :", passenger_name)
print("Train Name 	:", train_name)
print("Seat Number	:", seat_number)
print("Journey Date   :", journey_date)
print("Passengers 	:", number_of_passengers)
print("Ticket Fare	:", total_fare)
print("GST Amount 	:", gst_amount)
print("Final Amount   :", final_amount)
print("----------------------------------------------")
