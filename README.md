# EnsemblRESTEndpoint
Ensembl REST Endpoint (in Django)

# Development

Models were automatically generated by importing the Database Schema into Django by using inspectdb after configuring the DATABASE in settings.py:
"python manage.py inspectdb > models.py  "

Django REST Framework was used for generating the REST endpoints

XML and JSON renderers were included for the results.

All queries are capitalized in this code in order to match the "brc" example.  

Searching was done by the "starts with" field lookup in Django.  

Case-insensitive searching could be done by replacing this field lookup by "istarts with" in a production environment, depending on design choices.  

The "gene_suggestenv" was used during development but is not needed for testing this application.

# Requirements:

Python 3.6.X

# Installation:

1. Download the Zip file or clone this Github directory (19,4 MB)

2. Run:

"pip3 install -r requirements.txt"

For installing other requirements.

# Usage:
Please start the Django server using:

"python3 manage.py runserver"

The REST endpoint can be queried by using the following URL and GET parameters:

URL: http://127.0.0.1:8000/geneautocomplete/

GET parameters:

* query - the partial query typed by the user, e.g. `brc` (REQUIRED)
* species - the name of the target species, e.g. `homo_sapiens`(OPTIONAL)
* limit - the maximum number of suggestions to return (OPTIONAL)

Examples:

* Querying for "brc":  
http://127.0.0.1:8000/geneautocomplete/?query=brc

* Querying for "bcr" and for Homo sapiens as a species:  
http://127.0.0.1:8000/geneautocomplete/?query=brc&species=homo_sapiens

* Querying for "bcr" and for Homo sapiens as a species. 10 results limit:  
http://127.0.0.1:8000/geneautocomplete/?query=brc&species=homo_sapiens&limit=10
