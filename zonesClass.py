
zones = []
multipliers = (.55,.56,.75,.76,.85,.86,.95,.96, 1.05, 1.06, 1.20, 1.21, 1.50,1.51)
class Athlete(object):
	"""This class contains all the info for an athlete's profile."""
	def __init__(self, name):
		super(Athlete, self).__init__()
		self.name = name
	def ftp(ftp):
		ftp = ftp
	def lthr(lthr):
		lthr = lthr
	def zone_calc():
		# Will calculate zones
            for i in (multipliers):
                zones.append(zone(i))
	def print_zones():
		print format % (45,'Active Recovery               Below ==>> ',10, zones[:1])
		print format % (45,'Endurance',10, zones[1:3])
		print format % (45,'Tempo',10, zones[3:5])
		print format % (45,'Sweet Spot',10, zones[5:7])
		print format % (45,'Threshhold',10, zones[7:9])
		print format % (45,'VO2',10, zones[9:11])
		print format % (45,'Anaerobic',10, zones[11:13])
		print format % (45,'Neuromuscular                 Above ==>>',5, zones[12])
		print '=' * 65
