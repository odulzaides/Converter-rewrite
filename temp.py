# Module to convert temperature


def celsius_to_fahrenheit(c_temp):
    return 9.0 / 5.0 * c_temp + 32


def fahrenheit_to_celsius(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0


def temp():
    print """
    \t1. Convert Celsius to Farenheit.
    \t2. Convert Farenheit to Celcius.
    \t3. Return to main menu.
    """

    choice = input("Enter Choice: ")

    if choice == 1:
        celcius = input("Enter temperatue Celcius to convert: ")
        celsius_to_fahrenheit(celcius)
        print """\n\n\t{0} degrees Celcius is {1:.1f} degrees Farenheit.
        """.format(celcius, celsius_to_fahrenheit(celcius))
        temp()
    if choice == 2:
        farenheit = input("Enter temperatue Farenheit to convert: ")
        print """\n\n\n\t{0} degrees Farenheit is {1:.1f} degrees Celcius.
        """.format(farenheit, fahrenheit_to_celsius(farenheit))
        temp()
    if choice == 3:
        import converter
        menu()
