'''Training Zones'''

# Athlete information function to determine Name, Max HR, LT HR,and FTP
# depending on age.


# Compute power zones and heart ratios zones.
def Zones():    
    name_1 = raw_input('Please enter your name:  ')
    age = input("How old are you?  ")
    max_hr = 220 - age
    lthr = input("What is your Lactate threshold HR?  ")
    ftp = input("What is your FTP?  ")

    zones = []
    HR = []

    hr_multipliers = (.68, .69, .83, .84, .94, .95, 1.05, 1.06)

    for i in (hr_multipliers):
        HR.append(lthr*i)
        
    multipliers = (.55,.56,.75,.76,.85,.86,.95,.96, 1.05, 1.06, 1.20, 1.21, 1.50,1.51)

    for i in (multipliers):
       zones.append(ftp*i)

    format_ar = ('{0:40} {1:6}  {2:.0f} {3}  {4:.0f}')
    format_hr = ('{0:40} {1:.0f}   -  {2:3.0f} {3:7.0f}   - {4:4.0f} ')
    format_no_hr = ('{0:40} {1:.0f}   - {2:4.0f}')
    format_vo = ('{0:40} {1:.0f}   - {2:4.0f} {3}    {4:.0f}')
    format_np = ('{0:40} {1:6} {2:.0f}')
    
    header_format = '{0:40} {1:17} {2:7}'

    print "\n"
    print "Here are your results {}:".format(name_1)
    print '=' * 70
    print
    print "Your maximum heart rate is {} BPM".format(max_hr)
    print

    print "Your Training Zones are:"
    print '=' * 70
    print header_format.format('Zone', 'Power', 'Heart Rate')
    print '-' * 70
    print format_ar.format('Active Recovery', 'Below >', zones[0], '    Below >', HR[0])
    print format_hr.format('Endurance', zones[1], zones[2], HR[1], HR[2])
    print format_hr.format('Tempo', zones[3], zones[4], HR[3], HR[4])
    print format_no_hr.format('Sweet Spot', zones[5], zones[6],)
    print format_hr.format('Threshhold', zones[7], zones[8], HR[5], HR[6])
    print format_vo.format('VO2', zones[9], zones[10], '    Above', HR[7])
    print format_no_hr.format('Anaerobic', zones[11], zones[12])
    print format_np.format('Neuromuscular', 'Above > ', zones[13])
    print '=' * 70

    print '='* 70
    another()


def another():
    another1 = raw_input("Would you like to enter another set of Values? ")
    if another1 == "y" or another1 == "n":
        if another1 == "y":
            Zones()
        if another1 == "n":
            import converter
            converter.menu()
    else:
        print """Enter 'y' to enter another athlete or 
        'n' to return to Main Menu"""
        another()

#Zones()
