import sys
import os
import datetime
from dateutil.relativedelta import relativedelta

INTERVAL = relativedelta(months=+1)
fname_format = "fp_NZ.%s.10.%s__%s__%s"
fp_path = 'waveformsKHZ/fingerprints/'
ts_path = 'waveformsKHZ/timestamps/'
station = 'KHZ'
channel = 'HHE'

def construct_filename(t):
	return fname_format % (station, channel, t.strftime('%Y%m%dT000000Z'), (t + INTERVAL).strftime('%Y%m%dT000000Z'))

if __name__ == '__main__':
	start_time = datetime.datetime.strptime(sys.argv[1], "%y-%m")
	end_time = datetime.datetime.strptime(sys.argv[2], "%y-%m")
	if len(sys.argv) > 3:
		station_channel = sys.argv[3]
	time = start_time
	nfp = 0
	if os.path.exists("NZ.%s.%s.fp" % (station, channel)):
		os.remove("NZ.%s.%s.fp" % (station, channel))
	while time <= end_time:
		fname = construct_filename(time)
		#print fname
		#os.system("cat " + fp_path + fname + (" >> NZ.%s.%s.fp" % (station, channel)))

		# Verify number of fingerprints
		num_lines = sum(1 for line in open(ts_path + 'ts_' + fname[3:]))
		nfp += num_lines
		fsize = os.path.getsize(fp_path + fname)
		if fsize / 512 != num_lines:
			print fname
			print fsize / 512, num_lines


		time += INTERVAL

	#fsize = os.path.getsize("NZ.%s.%s.fp" % (station, channel))
	#print "File size: %d bytes" % (fsize)
	#print "# fingerprints: %d, %d" %(nfp, fsize / 512)

