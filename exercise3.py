#START

time= int(input("how long the restaurant took to bring the meal? (in minutes)"))
price=int(input("what is the price of the meal? (in shekels)"))

is_quick_service = time < 15
is_expensive = price > 100

recommended = is_quick_service and not is_expensive

print("recommeded" if recommended else "not recommeded")

#STOP