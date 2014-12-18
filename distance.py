# Module for converting distances


def km_miles(kilometers):
    """Converts kilometers to miles"""
    return kilometers * 0.621371


def miles_km(miles):
    """Converts miles to kilometers"""
    return miles * 1.60934


def distance():
    print """
    What would you like to convert?
    \t1. Kilometers to miles.
    \t2. Miles to kilometers.
    \t3. Return to main menu
    """
    choice = input("Enter choice: ")

    if choice == 1:
        kilometers = input("Enter kilometers to be converted")
        print """\""n\n\t{0} kilometers is {1} miles
        """.format(kilometers, km_miles(kilometers))
        distance()
    if choice == 2:
        miles = input("Enter miles to be converted.")
        print """\n\n\t{0}miles is {1} kilometers
        """.format(miles, miles_km(miles))
        distance()
    if choice == 3:
        import converter
        converter.menu()
