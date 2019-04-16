#Open file for writing
filenameR = "authors.txt"
filenameW = "authors_processed.csv"
fhR = open(filenameR, "r")
fhW = open(filenameW, "w")


#Skip 1st line which had column names
fhR.readline()

fhW.write("Name,TotalCited,ID,Title,Area1,Area2,Area3,Area4,Area5\n")

#Lierature through author list
count = 0
for line in fhR:
		tmp = line.split("\t")
		areas = tmp[4].split(";")
		title = tmp[5].replace("\n","").split(",")
		print(tmp)
		print(areas)
		print(title)
		fhW.write(tmp[1] + "," + tmp[2] + "," + tmp[3] + "," + title[0])
		count = 0
		for a in areas:
			fhW.write("," + a)
			count += 1
		for i in range(0, 5 - count):
			fhW.write(",")
		if count > 5:
			print("More than 5 Areas")
			break
		fhW.write("\n")
		#break

#Close file
fhR.close()
fhW.close()