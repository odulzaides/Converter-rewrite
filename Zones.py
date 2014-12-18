'''Training Zones'''

# Athlete information function to determine Name, Max HR, LT HR,and FTP
# depending on age.


# Compute power zones and heart ratios zones.
def Zones():
    print '\n'
    name_1 = raw_input('Please enter your name:  ')
    print '\n'
    age = input("How old are you?  ")
    print '\n'
    max_hr = 220 - age
    print '\n'
    thresh_hr = input("What is your Lactate threshold HR?  ")
    print '\n'
    ftp_1 = input("What is your FTP?  ")
    ar_hr = thresh_hr * 0.68
    end1_hr = thresh_hr * 0.69
    end2_hr = thresh_hr * 0.83
    temp1_hr = thresh_hr * 0.84
    temp2_hr = thresh_hr * 0.94
    lt1_hr = thresh_hr * 0.95
    lt2_hr = thresh_hr * 1.05
    vo1_hr = thresh_hr * 1.06
    ar1_ftp = ftp_1 * 0.55
    end1_ftp = ftp_1 * 0.56
    end2_ftp = ftp_1 * 0.75
    tempo1_ftp = ftp_1 * 0.76
    tempo2_ftp = ftp_1 * 0.85
    ss1_ftp = ftp_1 * 0.86
    ss2_ftp = ftp_1 * 0.95
    thresh1_ftp = ftp_1 * 0.96
    thresh2_ftp = ftp_1 * 1.05
    vo1_ftp = ftp_1 * 1.06
    vo2_ftp = ftp_1 * 1.20
    ac_ftp1 = ftp_1 * 1.21
    print
    print "Here are your results %s:" % name_1
    print
    print "Your maximum heart rate is %d BPM" % max_hr
    print
    print "You're Training Zones are:"
    print
    print "=" * 70
    print ("        Training Zones         Power         Heart Rate")
    print "=" * 70
    print "1.   Active Recovery:==>     Below  %d     Below %d " % (ar1_ftp, ar_hr)
    print "2.   Endurance Power:==>     %d - %d      %d - %d" % (end1_ftp, end2_ftp, end1_hr, end2_hr)
    print "3.       Tempo Power:==>     %d - %d      %d - %d" % (tempo1_ftp, tempo2_ftp, temp1_hr, temp2_hr)
    print "4.        Sweet Spot:==>     %d - %d" % (ss1_ftp, ss2_ftp)
    print "5.         Threshold:==>     %d - %d      %d - %d" % (thresh1_ftp, thresh2_ftp, lt1_hr, lt2_hr)
    print "6.           VO2 Max:==>     %d - %d      Above %d" % (vo1_ftp, vo2_ftp, vo1_hr)
    print "7. Anaerobic Capacity==>     Above %d" % ac_ftp1
    print "=" * 70
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
