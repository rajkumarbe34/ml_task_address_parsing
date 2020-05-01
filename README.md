# Requirement

Given the recent outbreak of bush fires across the country the Queensland Fire and Emergency Services (QFES) 
have noted deficiencies in their current systems. After evaluating various platforms, the QFES has decided to adopt a 
Service Oriented Architecture (SOA) for its future IT infrastructure. However, they would like to gain a deeper 
understanding of the technologies and have asked for a demonstration of these technologies along with a brief 
explanation of the concepts and principles of how it works. To demonstrate your code, you have been provided with 
three data sources compiled with data from QFES. 

#### These are: 
● “Fire_Stations.csv” contains the information about 
the fire stations, 
● “Station_Locations.xml” contains the location coordinates for each fire station
● “Station_Regions.csv” 
contains a list of regions Important Note:​ 
For ease of demonstration, your code must be self-contained. In addition to using 
Standards-based HTML and Python, PETL, and Parser are the only additional frameworks you should need. If you use others they 
must be provided and must not require installation. Problem statement: 

1. The Fire_Stations.csv file contains non-printable 
Unicode characters, in order to perform other cleaning tasks and merging of data you’ll first need to clean these characters 
from the data. 
2. Anemailaddressforeachstationneedstobeconstructedfromitsname:e.g.for Acacia Ridge Fire Station will be 
enquiry@acaciaridge.qfes.gov.au 
3. You are to merge data from the three sources into “Fire_Station_Locations.csv” with 
fields as shown in Table 1 - Field Mapping. 
4. Ensure your field names match the fields as shown in Table 1 - Field Mapping. 
5. Ensure the order of fields matches the order in Table 1 - Field Mapping. 
6. Data must be sorted firstly on “RegionID” and then on “Station Number” 
7. By using the Machine learning model you have to separate the data in the Address field into “Street Address”, “Suburb” &amp; “Post Code” fields. You should get infer the model by displaying the classification report of the model. 

| Field Name | Mapping |
| ------ | ------ |
| RegionID | Station_Regions.RegionID | |
| Station Number | Fire_Stations.Stn Number  |
| Station Name | Fire_Stations.Fire Station | 
| Station Type | Fire_Stations.Stn Type |
| Street Address | Fire_Stations. Address | 
| Phone Number | Fire_Stations.Phone Number | 
| Fax Number | Fire_Stations.Fax Number | 
| E-Mail New | Calculated Field | 
| Lat | Station_Locations.Lat | 
| Lon | Station_Locations.Long | 

Table 1 - Field Mapping

### Steps to execute:

`docker build -t ml_task .`
`docker run --rm ml_task`

