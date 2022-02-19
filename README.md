# surfs_up
Investing in Waves and Ice Cream!

## Objective 
After a lovely vacation in Hawaii, I came up with a business plan to open a Surf n' Shake shop in Oahu.  A potential investor wanted an analysis of the weather in the area.  
### Original Analysis: 
    - Retrieve the Precipitation Data
    - Find the Number of Stations
    - Determine the Most Active Stations
    - Find Low, High, and Average Temperatures
    - Build Flask Routes

After presenting my original analysis, the investor requested an analysis of the temperature data for June and December. The is to determine if the business will be sustainable year-round.
### Additonal Analysis:
    - Summary Statistics for June
    - Summary Statistics for December

## Resources
### Files: 
climate_analysis.ipynb, hawaii.sqlite

### Software/Dependecies: 
Python 3.9.7, Jupyter Notebook 6.4.5, Flask 1.1.2, Pandas 1.3.4, Numpy 1.20.3, 
Matplotlib 3.4.3, SQLAlchemy 1.4.22, Visual Studio Code 1.64.0

## Results

### Exploratory Climate Analysis
- Plot of Precipitaion Data by Date

![plot](https://user-images.githubusercontent.com/33010018/154778152-623bc864-5b82-4510-8563-4fdfab94b0bf.png)

- Summary Statistics For the Precipitation Data

![stats_prec](https://user-images.githubusercontent.com/33010018/154778174-055eb1d9-31d6-4aa6-8d94-40455e41c142.png)

- Most Active Stations

![most_active](https://user-images.githubusercontent.com/33010018/154778189-d96f00ae-f373-4d77-a8cf-8b04447c82c3.png)

- Histogram of the Temperature Observation Data for the Most Active Station

![histogram](https://user-images.githubusercontent.com/33010018/154778202-8ee7fde1-21ba-4e5f-b493-722672cd5f8c.png)

### June Analysis
- June Temperature Statistics

![june_temps](https://user-images.githubusercontent.com/33010018/154784769-5b6d160c-c3aa-4429-9cd9-4579f62ea8c2.png)

- June Precipitation Statistics

![j_prcp_stats](https://user-images.githubusercontent.com/33010018/154784843-9d892398-2840-4f5a-9105-010f925cfcc1.png)

### December Analysis    

- December Temperature Statistics

![dec_temps](https://user-images.githubusercontent.com/33010018/154784884-9c95c3ae-47a1-4e56-9ed0-84bc945950aa.png)

- December Precipitation Statistics

![d_prcp_stats](https://user-images.githubusercontent.com/33010018/154784937-e06252da-58d3-4041-b622-d2674a4ddcc0.png)

### June and December Weather Differences
- Per the Precipitation Statistics table, December had a significantly higher average precipitation than June. 
- Per the Temperatures Statistics table, June's minimum temperature was 8 degrees higher than December's.
- Based on the count for Temperatures Statistics, we were given alot more weather data for June than December.

## Summary
### Last 12 Months of Precipitation Data
Precipitation appears to be at its lowest in early Jan 2017.  Precipitation was at its peak between Sept 2016 and Oct 2016.

### June and December Additional Queries 

- June Precipitation Query

![j_prcp_query](https://user-images.githubusercontent.com/33010018/154784817-e088c06d-9758-4e47-bf56-0e9ab62a4998.png)

- December Precipitation Query

![d_prcp_query](https://user-images.githubusercontent.com/33010018/154784898-7eaa07d8-d9a0-4265-8f46-83de11bc0bba.png)

### June and December Data
With the exception of the minimum temperature, there wasn't a significant difference in temperature between June and December.  The weather seemed to stay consistent in both months.  However, there appears to be a significant difference in the amount of precipitation recorded in both months.
