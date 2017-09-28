def main():
    #This is a small program made to do dimensional analysis.
    #Units like Miles per hour are written like Mi/H, not MPH.
    type = input("What measurement type are you using? Area, temperature, volume, length, mass, pressure, or speed? ")
    type = type.lower()
    origUnit = input("What unit do you want to convert from? ")
    origUnit = origUnit.lower()
    newUnit = input("What unit do you want to convert to? ")
    newUnit = newUnit.lower()
    amount = float(input("What is the number of units? "))
    #Kilometer per hour to miles per hour.
    if type == "area":
        #Square feet to square miles
        if (origUnit == "sqft" or origUnit == "square feet" or origUnit == "square foot") and (newUnit == "sqmi" or newUnit == "square mile"):
            amount = amount * 0.0000000358701
            print("You have this many", newUnit, ':', amount)
        else:
            print("Invalid input. Please read the help manual.")
    elif type == "temperature":
            #Fahrenheit to Celsius
        if (origUnit == "f" or origUnit == "fahrenheit") and (newUnit == "c" or newUnit == "celsius"):
            amount = amount - 32 / (5/9)
            print("You have this many", newUnit, ':', amount)
        #Celsius to Fahrenheit
        elif (origUnit == "c" or origUnit == "celsius") and (newUnit == "f" or newUnit == "fahrenheit"):
            amount = amount * (9/5) + 32
            print("You have this many", newUnit, ':', amount)
        #Celsius to Kelvin
        elif (origUnit == "c" or origUnit == "celsius") and (newUnit == "k" or newUnit == "kelvin"):
            amount = amount + 273.15
            print("You have this many", newUnit, ':', amount)
        #Kelvin to Celsius
        elif (origUnit == "k" or origUnit == "kelvin") and (newUnit == "c" or newUnit == "celsius"):
            amount = amount - 273.15
            print("You have this many", newUnit, ':', amount)
        else:
            print("Invalid input. Please read the help manual.")
    elif type == "speed":
        #Kilometers per hour to miles per hour
        if (origUnit == "km/h" or origUnit == "kilometers per hour") and (newUnit == "mi/h" or newUnit == "miles per hour"):
            amount = amount * 0.621371
            print("You have this many", newUnit, ':', amount)
        #Miles per Hour to Kilometers per hour.
        elif (origUnit == "mi/h" or origUnit == "miles per hour") and (newUnit == "km/h" or newUnit == "kilometers per hour"):
            amount = amount * 1.60934
            print("You have this many", newUnit, ':', amount)
        #Meters per second to feet per second. 
        elif (origUnit == "m/s" or origUnit == "meters per second") and (newUnit == "ft/s" or newUnit == "feet per second"):
            amount = amount * 3.28084
            print("You have this many", newUnit, ':', amount)
        #Feet per second to meters per second.
        elif (origUnit == "ft/s" or origUnit == "feet per second") and (newUnit == "m/s" or newUnit == "meters per second"):
            amount = amount * 0.3048
            print("You have this many", newUnit, ':', amount)
        #Feet per second to miles per hour.
        elif (origUnit == "ft/s" or origUnit == "feet per second") and (newUnit == "mi/h" or newUnit == "miles per hour"):
            amount = amount * 0.681818
            print("You have this many", newUnit, ':', amount)
        #Miles per hour to feet per second.
        elif (origUnit == "mi/h" or origUnit == "miles per hour") and (newUnit == "ft/s" or newUnit == "feet per second"):
            amount = amount * 1.46667
            print("You have this many", newUnit, ':', amount)
        #Kilometers per hour to meters per second.
        elif (origUnit == "km/h" or origUnit == "kilometers per hour") and (newUnit == "m/s" or newUnit == "meters per second"):
            amount = amount * 0.277778
            print("You have this many", newUnit, ':', amount)
        #Meters per second to kilometers per hour.
        elif (origUnit == "m/s" or origUnit == "meters per second") and (newUnit == "km/h" or newUnit == "kilometers per hour"):
            amount = amount * 3.6
            print("You have this many", newUnit, ':', amount)
        else:
            print("Invalid input. Please read the help manual.")
    elif type == "length":
        #Feet to meters.
        if (origUnit == "ft" or origUnit == "foot" or newUnit == "feet") and (newUnit == "m" or newUnit == "meter"):
            amount = amount * 0.3048
            print("You have this many", newUnit, ':', amount)
        elif (origUnit == "yd" or origUnit == "yard") and (newUnit == "ft" or newUnit == "foot" or newUnit == "feet"):
            amount = amount * 3
            print("You have this many", newUnit, ':', amount)
        else:
            print("Invalid input. Please read the help manual.")
    elif type == "volume":
        #
        if (origUnit == "" or origUnit == "") and (newUnit == "m" or newUnit == "meter"):
            amount = amount
            print
        elif (origUnit == "" or origUnit == "") and (newUnit == "" or newUnit == ""):
        elif (origUnit == "" or origUnit == "") and (newUnit == "" or newUnit == ""):
        elif (origUnit == "" or origUnit == "") and (newUnit == "" or newUnit == ""):
        elif (origUnit == "" or origUnit == "") and (newUnit == "" or newUnit == ""):
    else:
        print("Invalid input. Please read the help manual.")
main()

#
#Template
#if (origUnit == "" or origUnit == "") and (newUnit == "" or newUnit == ""):
#   amount = amount *
#   print("You have this many", newUnit, ':', amount)
