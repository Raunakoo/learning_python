def convert_days_to_seconds(days):
	hours=days*24
	minutes=hours*60
	seconds=minutes*60
	print(seconds)

	return seconds

total_seconds=convert_days_to_seconds(7)
milliseconds=total_seconds*1000
print(milliseconds)
