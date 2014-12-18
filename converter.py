from measureMenu import *
from weight import *
from distance import *
from temp import *
from Zones import *

def menu():
    print """
    Python converter program
        1. Convert Measurements
        2. Convert Weight
        3. Convert Temperatures
        4. Convert Distances
        5. Compute Training Zones
    """
    choice = input("Enter choice: ")
    if choice == 1:
        measure()
    if choice == 2:
        weight()
    if choice == 3:
        temp()
    if choice == 4:
        distance()
    if choice == 5:
        Zones()

menu()
