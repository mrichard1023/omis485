#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    gallon_cost = float(input("Cost of gallon of gas   "))

    if miles_driven <= 0:  
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        total_cost = round((gallon_cost * gallons_used), 2)
        cost_per_mile = round((total_cost/miles_driven), 2)
        print("Miles Per Gallon:          ", mpg)
        print("Gas cost:        ", total_cost)
        print("Per Mile cost:     ", cost_per_mile)

    choice = input ("Continue?:  ")
    print()
print()
print("Bye")