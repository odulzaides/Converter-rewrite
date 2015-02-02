# from zonesClass import *

ftp = 230
zones = []


def zone(n): 
	return   ftp * n

multipliers = (.55,.56,.75,.76,.85,.86,.95,.96, 1.05, 1.06, 1.20, 1.21, 1.50,1.51)

for i in (multipliers):
   zones.append(zone(i))

format = ('%-*s      %*.2f')
format_2 = ('%-*s %-*.2f - %*.2f')
header_format = '%-*s%*s'
print '=' * 70
print header_format % (45, 'Zone', 6, 'Range')
print '-' * 70
print format % (45,'Active Recovery                               Below ==>> ',1, zones[0])
print format_2 % (45,'Endurance',10, zones[1], 10, zones[2])
print format_2 % (45,'Tempo',10, zones[3], 10, zones[4])
print format_2 % (45,'Sweet Spot',10, zones[5], 10, zones[6])
print format_2 % (45,'Threshhold',10, zones[7], 10, zones[8])
print format_2 % (45,'VO2',10, zones[9], 10, zones[10])
print format_2 % (45,'Anaerobic',10, zones[11], 10, zones[12])
print format % (45,'Neuromuscular                                 Above ==>>',7, zones[13])
print '=' * 70
