# dynamic-viz
The objective of this project is to develop a dynamic dashboard in Tableau which can update the data source. The dataset for this visualization includes wheat consumption (domestic, fsi, feed dom., etc) in Canada over 20 years timeline.

• XAMPP is used to host the data in a local server. <br>
• The data is fetched from the local server into Tableau. <br>
• The Tableau dashboard presents a crosstab and a line chart of the time series data. <br>
• A REST API is developed using Django which can perform PUT, POST, GET and DELETE request. <br>
• Any data on the dashbord can be updated dynamically (underneath it uses the REST API). <br>

<img src="dynamicViz.gif" width="100%">

# How to run:
> 1. Download XAMP from the following link:
https://www.apachefriends.org/download.html

> 2. Create a database into the server and insert data from data.csv.

> 3. Download the MYSQL driver from the following link.
https://www.tableau.com/support/drivers?_ga=2.248449924.208892635.1591984007-131215343.1584834650&_fsi=9MP9fyGg
and connect the database with Tableu.
