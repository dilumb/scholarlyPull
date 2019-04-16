import scholarly

#Get all authors from university of moratuwa
search_query = scholarly.search_author('University of Moratuwa')

#Open file for writing
filename = "authors.txt"
fh = open(filename, "w")

fh.write("#\tName\t#Cite\tID\tInterest\tAffli\n")

#Lierature through author list
count = 0
for tmp in search_query:
#tmp = next(search_query)
	count += 1
	if hasattr(tmp, 'citedby'):
		fh.write(str(count) + "\t" + tmp.name + "\t" + str(tmp.citedby) + "\t" + tmp.id + "\t" + ';'.join(tmp.interests) + "\t" + tmp.affiliation + "\n")
	else:
		fh.write(str(count) + "\t" + tmp.name + "\t-1" + "\t" + tmp.id + "\t" + ';'.join(tmp.interests) + "\t" + tmp.affiliation + "\n")
	print(count)

#Close file
fh.close()