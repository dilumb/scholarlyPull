import scholarly
from time import sleep
from random import randint
import io

#Get all authors from university of moratuwa
search_query = scholarly.search_author('University of Moratuwa')

#Open file for writing
filenameR = "authors.txt"
filenameW = "papers.txt"
fhR = open(filenameR, "r")
#fhW = open(filenameW, "w")
fhW = io.open(filenameW, "w", encoding="utf-8")


#Skip 1st line which had column names
fhR.readline()

fhW.write("#\tName\tNo Cited\tTitle\tYear\tAuthors\tJournal\tPublisher\tAbstract\n")

#Lierature through author list
count = 0
for line in fhR:
	items = line.split("\t")
	print(items[0] + "\t" + items[1])
	
	author_query = scholarly.search_author(items[1])
	author = next(author_query).fill()
	for pub in author.publications:
		count += 1
		title = ""
		year = ""
		authors = ""
		journal = ""
		publisher = ""
		abstract = ""
		citedby = 0
		
		myrnd = randint(1, 10)
		print("Waiting inner <<<<<<<<<<<<<<  " + str(myrnd))
		sleep(myrnd)
	
		details = pub.fill()
		#print(details)
		if 'title' in details.bib:
			title = details.bib["title"]
		print(title)
		if 'year' in details.bib:
			year = details.bib["year"]
		print(year)
		if 'author' in details.bib:
			authors = details.bib["author"]
		print(authors)
		if 'journal' in details.bib:
			journal = details.bib["journal"]
		print(journal)
		if 'publisher' in details.bib:
			publisher = details.bib["publisher"]
		print(publisher)
		if 'abstract' in details.bib:
			abstract = details.bib["abstract"]
		print(abstract)
		if hasattr(details, 'citedby'):
			citedby = details.citedby
		print(citedby)
		print("Paper no: " + str(count))
		print("-------------------------------------")
		fhW.write(items[0] + "\t" + items[1] + "\t" + str(citedby) + "\t" + title + "\t" + str(year) + "\t" + str(authors) + "\t" + str(journal) + "\t" + str(publisher) + "\t" + str(abstract) + "\n")
	count = 0
	myrnd = randint(1, 30)
	print("Waiting outer >>>>>>>>>>>>  " + str(myrnd))
	sleep(myrnd)
	

#Close file
fhR.close()
fhW.close()