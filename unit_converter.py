
###################################Function Definitions#############################################
def temp_calculator():
    fc_cf = int(input("1. Fahrenheit ==> Celsius\n2. Celsius ==> Fahrenheit\nWhich one ? "))
    if fc_cf == 1:
        temperature_f = float(input("Enter the temperature in Fahrenheit : "))
        fc_calculated = round((temperature_f - 32) * (5 / 9),3)
        print(str(temperature_f) + " °F" + " = " + str(fc_calculated) + " °C")
    elif fc_cf == 2:
        temperature_c = float(input("Enter the temperature in Celsius : "))
        cf_calculated= round((temperature_c*9/5)+32,3)
        print(str(temperature_c)+ " °C"+ " = " + str(cf_calculated) + " °F")
    else:
        print("please enter 1 or 2")

####################################################################################################
def length_calculator():
    choose_length_input_unit = int(input("1. Meter\n2. kilometer\n3. Mile\n4. Foot\nWhich unit of measurement do you choose as the conversion source? "))
    if choose_length_input_unit == 1:
        length_meter=float(input("Enter the length in Meters: "))
        meter_to_kilometer = round(length_meter/1000,3)
        meter_to_mile = round(length_meter/1609344,3)
        meter_to_foot = round(length_meter*3.281,3)
        print(str(length_meter) + " Meter" + " = " + str(meter_to_kilometer) + " Kilometer" + " = " + str(meter_to_mile) + " Mile" + " = " + str(meter_to_foot) + " Foot")
    elif choose_length_input_unit == 2 :
        length_kilometer=float(input("Enter the length in Kilometers: "))
        kilometer_to_meter = round(length_kilometer*1000,3)
        kilometer_to_mile = round(length_kilometer/1.609344,3)
        kilometer_to_foot = round(length_kilometer*3281,3)
        print(str(length_kilometer) + " kilometer" + " = " + str(kilometer_to_meter) + " Meter" + " = " + str(kilometer_to_mile) + " Mile" + " = " + str(kilometer_to_foot) + " Foot")
    elif choose_length_input_unit == 3 :
        length_mile=float(input("Enter the length in Miles: "))
        miles_to_meter = round(length_mile*1609.344,3)
        miles_to_kilometer = round(length_mile*1.609344,3)
        miles_to_foot = round(length_mile*5280,3)
        print(str(length_mile) + " Mile" + " = " + str(miles_to_meter) + " Meter" + " = " + str(miles_to_kilometer) + " Kilometer" + " = " + str(miles_to_foot) + " Foot")
    elif choose_length_input_unit == 4 :
        length_foot= float(input("Enter the length in Foots: "))
        foot_to_meter = round(length_foot*0.3048,3)
        foot_to_kilometer = round(foot_to_meter/1000,3)
        foot_to_mile = round(length_foot/5280,3)
        print(str(length_foot) + " Foot" + " = " + str(foot_to_meter) + " Meter" + " = " + str(foot_to_kilometer) + " Kilometer" + " = " + str(foot_to_mile) + " Mile")

#######################################################################################################
def weight_calculator():
    choose_weight_input_unit = int(input("1. Kilogram\n2. Gram\n3. pound\n4. Ounce\nWhich unit of measurement do you choose as the conversion source? "))
    if choose_weight_input_unit == 1:
        weight_kilogram=float(input("Enter the weight in Kilograms: "))
        kilogram_to_gram = round(weight_kilogram*1000,3)
        kilogram_to_pound = round(weight_kilogram/0.4536,3)
        kilogram_to_ounce = round(weight_kilogram*35.274,3)
        print(str(weight_kilogram) + " Kilogram" + " = " + str(kilogram_to_gram) + " Gram" + " = " + str(kilogram_to_pound) + " Pound" + " = " + str(kilogram_to_ounce) + " Ounce")
    elif choose_weight_input_unit == 2 :
        weight_gram=float(input("Enter the weight in Grams: "))
        gram_to_kilogram = round(weight_gram/1000,3)
        gram_to_pound = round(gram_to_kilogram/0.4536,3)
        gram_to_ounce = round(gram_to_kilogram*35.274,3)
        print(str(weight_gram) + " Gram" + " = " + str(gram_to_kilogram) + " Kilogram" + " = " + str(gram_to_pound) + " Pound" + " = " + str(gram_to_ounce) + " Ounce")
    elif choose_weight_input_unit == 3:
        weight_pound = float(input("Enter the weight in Pounds: "))
        pound_to_kilogram = round(weight_pound / 2.205, 3)
        pound_to_gram = round(pound_to_kilogram * 1000, 3)
        pound_to_ounce = round(weight_pound * 16, 3)
        print(str(weight_pound) + " Pound" + " = " + str(pound_to_kilogram) + " Kilogram" + " = " + str(pound_to_gram) + " Gram" + " = " + str(pound_to_ounce) + " Ounce")
    elif choose_weight_input_unit == 4:
        weight_ounce = float(input("Enter the weight in ounce: "))
        ounce_to_kilogram = round(weight_ounce / 35.274, 3)
        ounce_to_gram = round(ounce_to_kilogram * 1000, 3)
        ounce_to_pound = round(weight_ounce /16, 3)
        print(str(weight_ounce) + " Ounce" + " = " + str(ounce_to_kilogram) + " Kilogram" + " = " + str(ounce_to_gram) + " Gram" + " = " + str(ounce_to_pound) + " Pound")

#################################### Main Program ####################################################
print("Welcome to the Unit Converter!\nList of inputs : \n1. Temperature Conversion\n2. Length Conversion\n3. Weight Conversion\n4. Exit")

while True:
    try:
        print("Welcome to the Unit Converter!\nList of inputs : \n1. Temperature Conversion\n2. Length Conversion\n3. Weight Conversion\n4. Exit")
        user_want_action = int(input("Please choose the type of conversion you would like to perform : "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if user_want_action == 1:
        temp_calculator()
    elif user_want_action == 2:
        length_calculator()
    elif user_want_action == 3:
        weight_calculator()
    elif user_want_action == 4:
        print("Thank you for using the Unit Converter. Goodbye!")
        break
    else:
        print("Please enter a number between 1 and 4!")

    again = input("Would you like to perform another conversion? (y/n): ")
    if again.lower() != "y":
        print("Thank you for using the Unit Converter. Goodbye!")
        break

