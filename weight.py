# Module to convert weight measurements


def ktop(kilograms):
    """Converts kilos to pounds"""
    return kilograms * 2.2046


def ptok(pounds):
    """ Converts pounds to kilos"""
    return pounds / 2.2046


def gtoo(grams):
    """ Converts grams to ounces """
    return grams / 28.0


def otog(ounces):
    """ Converts ounces to grams """
    return ounces * 28


def mltoo(milliliters):
    """ Converts milliliters to ounces """
    return milliliters / 29.57


def otoml(ounces):
    """ Converts ounces to milliliters """
    return ounces * 29.57


def weight():
    """ Weight conversion menu """
    print """What would you like to convert?
    \t1. Kilograms to Pounds.
    \t2. Pounds to Kilograms.
    \t3. Grams to Ounces
    \t4  Ounces to grams
    \t5. Milliliters to Ounces.
    \t6. Ounces to Milliliters.
    \t7. Return to Main Menu.
    """
    choice = input("Enter choice: ")
    if choice == 1:
        kilograms = input("Enter kilograms to convert: ")
        print """\n\n\t{} kilograms is equal to {} pounds
        """.format(kilograms, ktop(kilograms))
        weight()
    if choice == 2:
        pounds = input("Enter pounds to convert: ")
        print """
        \n\n\n\t{0} pounds is equal to {1:.2f} kilograms
        """.format(pounds, ptok(pounds))
        weight()
    if choice == 3:
        grams = input("Enter grams to convert: ")
        print """
        \n\n{0} grams is equalt to {1:.2f} ounces
        """.format(grams, gtoo(grams))
        weight()
    if choice == 4:
        ounces = input("Enter ounces to convert: ")
        print """
        \n\n\t{0} ounces is equal to {1:.2f} grams.
        """.format(ounces, otog(ounces))
        weight()
    if choice == 5:
        milliliters = input("Enter milliltiers to convert: ")
        print """\n\n{0} milliliters is equal to {1:.2f} ounces.
        """.format(milliliters, mltoo(milliliters))
        weight()
    if choice == 6:
        ounces = input("Enter ounces to convert: ")
        print """\n\n{0} ounces is equal to {1:.2f} milliliters.
        """.format(ounces, otoml(ounces))
        weight()
    if choice == 7:
        from converter import *
        menu()
