## Measurement converter module ###


def mtof(meters):
    """Converts meters to feet"""
    rawFeet = meters * 3.280839895
    inches = (rawFeet * 12) % 12
    feet = (rawFeet * 12 - inches) / 12
    # return (rawFeet * 12 - inches) / 12, (rawFeet * 12) % 12
    # print rawFeet, inches, feet
    print """
    \n\n\n\t{0} meters equals {1:.0f} feet {2:.0f} inches
    """.format(meters, feet, inches)
    measure()


def ftom(feet, inches):
    """ Converts feet to meters"""
    # print inches, feet
    totalFeet = ((feet * 12) + inches) / 12.0
    return totalFeet / 3.280839895


def ctoi(centimeters):
    """ Converts Centimeters to inches. """
    return centimeters * 0.39


def itoc(inches):
    """ Converts Inches to Centimeters"""
    return inches * 2.54


def measure():
    print """
    What would you like to convert?
    \t1. Meters to Feet.
    \t2. Feet to Meters.
    \t3. Centimeters to Inches.
    \t4. Inches to Centimeters.
    \t5. Return to main Menu.
    """
    choice = input("Enter choice: ")
    if choice == 1:
        meters = input("Enter meters to convert: ")
        mtof(meters)

    if choice == 2:
        print "Enter feet and inches."
        feet = input("Enter feet: ")
        inches = input("Enter inches: ")
        print """
        \n\n\n\t{0} feet {1:.0f} inches is equal to {2:.2f} meters
        """.format(feet, inches, ftom(feet, inches))
        measure()
    if choice == 3:
        centimeters = input("Enter centimeters to convert: ")
        print """
        \n\n\n\t{0} centimeters is equal to {1:.2f} inches
        """.format(centimeters, ctoi(centimeters))
        measure()
    if choice == 4:
        inches = input("Enter inches to convert: ")
        print """
        \n\n\n\t{0} inches is equal to {1:.2f} centimeters.
        """.format(inches, itoc(inches))
        measure()
    if choice == 5:
        from converter import *
        menu()
