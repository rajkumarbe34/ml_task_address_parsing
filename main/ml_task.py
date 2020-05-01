import petl as etl
import pandas as pd
from postal.expand import expand_address
from postal.parser import parse_address


# Read files
fire_station = (
                etl
                .fromcsv('Fire_Stations.csv')
                )
station_locations = etl.fromxml('Station_Locations.xml','STATION',
                                {
                                    'NAME': 'NAME',
                                    'LONG':'LONG',
                                    'LAT':'LAT'
                                })
station_regions = etl.fromcsv('Station_Regions.csv')

#1.Clean non-printable unicode characters
fire_station["Fire Station"]

fire_station_df = fire_station.todataframe()
fire_station_df['Fire Station'] = fire_station_df['Fire Station'].str.encode('ascii', 'ignore').str.decode('ascii')

#2.Construct email
fire_station_df['email'] = 'enquire@' + fire_station_df['Fire Station'].str.replace('Fire Station','').str.replace(' ','').str.lower() + '.qfes.gov.au'
#3a.Prepare datasets for joins
station_locations_df = station_locations.todataframe()
#print
station_locations_df.head()
station_regions_df = station_regions.todataframe()
fire_station_df['Region'] = fire_station_df['Region'].astype('str') 
fire_station_df['Name'] = fire_station_df['Fire Station'].str.replace(' Fire Station','').str.upper()

#3b.Join 3 datasets to prepare desired table
#Join fire station and station location data sets
join_df_1 = pd.merge(fire_station_df, station_locations_df, left_on='Name',right_on='NAME'
                     ,how='left',suffixes=('_left','_right'))

#Join fire station & station location with station regions data set.
join_df_2 = pd.merge(join_df_1, station_regions_df, left_on='Region',right_on='Region Code'
                     ,how='left',suffixes=('_left','_right'))


#4, 5 : Follow Field names like Table 1 - Field Mapping
columns = ['RegionID', 'Stn Number', 'Fire Station', 'Stn Type', 'Address', 'Phone Number', 'Fax Number', 'email','LAT','LONG' ]
final_df = join_df_2[columns]

#6: Sort data by “RegionID” and then on “Station Number”
final_df['RegionID'] = final_df['RegionID'].astype('int')
final_df['Stn Number'] = final_df['Stn Number'].astype('int') 
final_df.sort_values(['RegionID', 'Stn Number'], ascending='True')

final_df.to_csv('ml_result.csv')
#print(final_df)




