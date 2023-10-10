# **Project 3** -- Yelp API
## Yelp, for Travel Help!
When planning your next trip, it's easy to know where you want to go next. The hardest part is knowing that all your necessities are covered when you get there. We made a travel guide with data from Yelp to assist in your decisions on your hotels and restaurants. The map and graph visualizations are customizable and easy for users of any skill level to use.
- The maps and graphs show the top rated hotels and restaurants for the areas you plan to visit
- You can easily filter down to the category and city you're looking for
- See the locations of each marker on the maps so you know exactly where you'll be!

### Running the code
1. Open app.py and run the code, if you would like to view the raw data, you can open it locally on browser by selecting the provided url
2. With the flask app running, migrate to index.html, right click within the code, and select Open With Live Server
3. Once opened in your browser, you will be presented with a dropdown menu, a map, and a graph
4. To change the city or category displayed, select the choice from the dropdown menu

### Workflow
1. To start, we set up the Yelp API and all made a personal API key, and stored locally on our computers. We made our own config.py file and entered the API key in there, and made sure to add the files to our .gitignore so the keys are kept private
2. We evenly(ish) divided the top 10 populated cities in the US: NYC, LA, Chicago, Houston, Phoenix, Philly, San Antonio, San Diego, Dallas, Austin
3. Then we pulled the data from the Yelp API for our assigned cities, for all businesses under the category of "food" and "hotels", and saved them all in separate JSON files
4. Created the flask app with dummy data first to make sure it ran, then altered the code to pull in the JSON data pulled from the Yelp API
5. We then created the html, css, and javascript files
6. Added in the map and dropdown menu so that different cities and categories could be selected
7. Finally, parsed in the data from the flask app to create the markers and popups on the map
### Resources
- API: https://docs.developer.yelp.com/docs/fusion-intro
- Used to retrieve top 10 populated cities in the US: https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population
- JavaScript Library Used: https://www.chartjs.org/docs/latest/getting-started/
- https://stackoverflow.com/questions/10314800/flask-url-for-urls-in-javascript
- https://flask.palletsprojects.com/en/3.0.x/patterns/javascript/
- https://stackoverflow.com/questions/32201678/how-to-get-json-data-from-a-url-using-flask-in-python

#### Modules Used
- JavaScript
- Python
- JSON
- HTML
- CSS
- Flask
- D3
- Jsonify