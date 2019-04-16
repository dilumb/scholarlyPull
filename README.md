# scholarlyPull
Pull author details and papers from Google Scholar

This tool is build ontop of scholarly. Go through scholarly-README.rst for details on how to use scholarly for your need.

getStaffList.py - Pull list of authors registered under a given instituition. You just need to change line that include scholarly.search_author() function. Results will be written to authors.txt.

pullPapers.py - Pull list of papers under authors registered under a given instituition. You just need to change line that include scholarly.search_author() function. Results will be written to authors.txt and papers.txt. Tool purpospuly wait some random time before calling the next request as trying to pull too fast leads to blocking by Google. Even with it, you may need to prove that you are a human from time to time. In case, if script breaks, better to rerun from where it breaks in the author list.

processStaff.py - Generates a CSV file based on collected text files.
