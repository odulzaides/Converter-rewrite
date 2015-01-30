ftp = 230
zones = []

def zone(n): return   ftp * n

multipliers = (.55,.56,.75,.76,.85,.86,.95,.96, 1.05, 1.21, 1.50,1.51)

for i in (multipliers):
   zones.append(zone(i))

header_format = ('25-s, ')

print "Active Recovery  Below >>   {}".format(zones[:1])
print "Endurance  {}".format(zones[1:3])
print "Tempo  {}".format(zones[3:5])
print "Sweet Spot  {}".format(zones[5:7])
print "Threshhold  {}".format(zones[7:9])
print "Anaerobic  {}".format(zones[9:11])
print "Neuromuscular  Above >>  {}".format(zones[11:])

