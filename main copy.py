#Assigning field variable values
field_1 = 234
field_2 = 324
field_3 = 311
field_4 = 155
field_5 = 322

#Using arithmetic operators
#Calculate total and average
total_har
print(f"Average harvest = {Average_harvest} kg")vest = field_1 + field_2 + field_3 + field_4 + field_5
Average_harvest = total_harvest/5
print(f"Total harvest =  {total_harvest} kg")

#Calculating the earnings from the harvest
price_per_kg = 300
earnings = total_harvest * price_per_kg
print(f"Total earnings from the harvest = {earnings} INR")

#Pack into 25 kg bags
bags = total_harvest // 25
leftover = total_harvest % 25
print("no of bags =" , bags)
print("leftover grains =" , leftover , "kgs")

#comparison prev year data
prevyrharvst = 2000
print("better than last year? " ,total_harvest > prevyrharvst)
print("same as last year? " ,total_harvest == prevyrharvst)
print("atleast as good as prev year " ,total_harvest >= prevyrharvst)

#adding bonus harvest 
total_harvest += 40
print("after adding bonus harvest =" ,total_harvest ,"kgs")

#remove some for next season
total_harvest -= 30
print("after reserve for next year = " ,total_harvest ,"kgs")

#final count
bags = total_harvest // 25 
print("bags packed =" ,bags )