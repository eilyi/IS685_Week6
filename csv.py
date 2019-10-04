#csv opener

import csv

with open("deniro.csv") as infile:
	rdr = csv.reader(infile)
	for row in csv
	
#csv writer

data = [
	["Name", "Address", "Age"],
	["Jane Smith", "123 Fake St.", 23],
	["Slim Dusty", "564 Cunnamulla Fella St", 44]
	]
	
with open("people_CSV.csv", "w") as outfile:
	writer= csv.writer(outfile, delimiter = ",")
	
	writer.writerow(data[0])