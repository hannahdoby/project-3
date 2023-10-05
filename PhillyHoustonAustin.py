
## This script is used to pull data from the Yelp API for the cities of Philadelphia, Houston, and Austin.
import requests
import json
import pprint

# Define the locations and interests to be used in the API call
locations = ["Philadelphia", "Houston", "Austin"]
interests = ["hotels", "food"]
filenames = []

# Loop through the locations and interests to pull the data from the Yelp API
for location in locations:
    i = 0
    j = 0
    while i < 2:
        term = interests[i]
        url = "https://api.yelp.com/v3/businesses/search?location="+location+"&term="+term+"&sort_by=best_match&limit=40"
        headers = { "accept": "application/json","Authorization": "Bearer kYCbl77E-qMIxVjuJLWY4p_8UFapl1_LehuxNfNpWBU68an-kZr6rrgr90Pj8Flmlsyx0IiUwaJStbmgDlZvUQ19hsaVoBcTbrYBaF30FnxtmgX69qwpXiqqgloTZXYx" }
        response = requests.get(url, headers=headers)
        locals()[location+'_'+term] = json.loads(response.text)
        filenames.append([location+'_'+term])
        i = i + 1
        
        
with open('file.json', 'w') as outfile:
    json.dump(filenames[0], outfile)       
"""
#Since categorie querys have a different structure, we need to loop through them seperately
for location in locations:
    category = "museums"
    url = 'https://api.yelp.com/v3/businesses/search?location='+location+'&categories='+category+'&sort_by=best_match&limit=40'
    headers = {"accept": "application/json","Authorization": "Bearer kYCbl77E-qMIxVjuJLWY4p_8UFapl1_LehuxNfNpWBU68an-kZr6rrgr90Pj8Flmlsyx0IiUwaJStbmgDlZvUQ19hsaVoBcTbrYBaF30FnxtmgX69qwpXiqqgloTZXYx" }
    response = requests.get(url, headers=headers)
    locals()[location+'_'+category] = json.loads(response.text)
"""

# Save the data to a json file
    

 