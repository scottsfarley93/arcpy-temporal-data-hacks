# Tools for putting together a temporal analysis in ArcGIS
###### Scott Farley
###### Nov. 2015
I am working on a project to map the number of mentions of each country in various news sources.
I have done much work to do the data mining of the news sources, which has resulted in a large number of comma-delimited python outputs.
I will be using ArcGIS as my GIS platform, and, while they do have tools to do temporal analysis (or at least show temporal data), the formats required by these tools are difficult to put together.
The key step that is lacking the the temporal workflow is the capability to do a one-to-many join on a shapefile.  These tools hack together one solution that allows the formation of a shapefile that can be ingested by ArcGIS's temporal tools.

### temporalize_csv.py
If you have a csv data file that has headers of some data and rows representing dates, you will need to modify this file so that there are records for each country at each date.  

For example, you have a csv with ten fields (country names) and ten rows (dates), each daet record has a date, and then ten data values, one for each country name field.  This script will output a new csv file where each date now has ten records, and each record is composed of a single datum for a single field.  

### CopyAndAppendShapefile.py
If you want to add your csv data to an existing arcgis geometry, you probably have already considered a join.  However, for me, the joining the data that was transformed as above, would only join one record to each feature in a shapefile.  In other words, it was doing a one-to-one join, rather than doing a one-to-many join.  While it would have been easier to have my dates as columns and then join one-to-one to the features (rather than having multiple records for each feature, one for each date), there were two problems with this: 1.  arcGIS did not recognize having dates as field names, and 2. it would not have been supported by the time slider toolbar.  In short, I needed a one-to-many join, which is not so easy to do.  

This script will take an existing shapefile that has the geometry you want to join your data with, and add N-copies of each feature to it.  For example, if I want to add a week long temporal dataset with 1 day resolution to a US states shapefile, the resulting shapefile will have seven copies of California, seven copies of New York, etc.  This is totally inefficient on its own, because to this point, these new records have no attributes.  So proceed to the next section...

### TemporalJoin.py
So now you have a shapefile with N-copies of each feature.  You have a csv file with each unit having N-records, one for each date.  You can now join the two, using this script.  This script will add two fields to your shapefile (Date, Value), and will then search through your shapefile and populate these new fields with values from your CSV based on a common field.  The script should be able to handle having multiple geometries representing a single entity (ie Alaska can will be populated with the same values as the US even if they started as separate records in the original shapefile). 

###### Conclusion
If everything worked, you should be left with a shapefile that has two new columns (Date and Value) that show the value from your csv for that record at that date.  You can then enable temporal display by clicking on the Time tab of the layer properties and 'enabling time on this layer.'  The time slider can then be used to curse through the data temporally. 



