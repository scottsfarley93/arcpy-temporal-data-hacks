# Tools for putting together a temporal analysis in ArcGIS
I am working on a project to map the number of mentions of each country in various news sources.
I have done much work to do the data mining of the news sources, which has resulted in a large number of comma-delimited python outputs.
I will be using ArcGIS as my GIS platform, and, while they do have tools to do temporal analysis (or at least show temporal data), the formats required by these tools are difficult to put together.
The key step that is lacking the the temporal workflow is the capability to do a one-to-many join on a shapefile.  These tools hack together one solution that allows the formation of a shapefile that can be ingested by ArcGIS's temporal tools.



