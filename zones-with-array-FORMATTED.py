ftp = 230
zones = []

def zone(n): return   ftp * n

multipliers = (.55,.56,.75,.76,.85,.86,.95,.96, 1.05, 1.06, 1.20, 1.21, 1.50,1.51)

for i in (multipliers):
   zones.append(zone(i))

format = ('%-*s%*s')
header_format = '%-*s%*s'
# print "Active Recovery  Below >>   {}".format(zones[:1])
# print "Endurance  {}".format(zones[1:3])
# print "Tempo  {}".format(zones[3:5])
# print "Sweet Spot  {}".format(zones[5:7])
# print "Threshhold  {}".format(zones[7:9])
# print "Anaerobic  {}".format(zones[9:11])
# print "Neuromuscular  Above >>  {}".format(zones[11:])

print '=' * 65
print header_format % (45, 'Zone', 10, 'Range')
print '-' * 65

print format % (45,'Active Recovery               Below ==>> ',10, zones[:1])
print format % (45,'Endurance',10, zones[1:3])
print format % (45,'Tempo',10, zones[3:5])
print format % (45,'Sweet Spot',10, zones[5:7])
print format % (45,'Threshhold',10, zones[7:9])
print format % (45,'VO2',10, zones[9:11])
print format % (45,'Anaerobic',10, zones[11:13])
print format % (45,'Neuromuscular                 Above ==>>',10, zones[12])
print '=' * 65

