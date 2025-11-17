# trend-health-technical-exercise
## Chicago Transit Authority Ridership Analysis 🚌
## Overview 📊
This project demonstrates an end-to-end data pipeline to showcase abilities in data collection, data modeling, and data analytics. 

## Source Data
The data used in this project is public information provided by the Chicago Transit Authority (CTA). The following three data points have been ingested in this exercise:
- [CTA - Ridership - Annual Boarding Totals] (https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd/about_data)
- [CTA - Ridership - Bus Routes - Daily Totals by Route] (https://data.cityofchicago.org/Transportation/CTA-Ridership-Bus-Routes-Daily-Totals-by-Route/jyb9-n7fm/about_data)
- [CTA - Ridership - 'L' Station Entries - Daily Totals] (https://data.cityofchicago.org/Transportation/CTA-Ridership-L-Station-Entries-Daily-Totals/5neh-572f/about_data)

Information into each of the datasets are linked above.

One of the reasons I chose to leave Nashville and move to Chicago back in 2023 is because I was tired of having driving as my only option. After moving to the city, despite still owning my car, walking and CTA are my only modes of transportation. Regardless of whether I'm traveling from the North-East side to the South-West neighborhoods, I will choose to take public transportation over Uber or Taxi services. CTA impacts my daily life, so I thought investigating this data would be interesting. Selfishly, I hoped to use the data source to figure out what days of the week I should work from home based on the average of L riders on each day of the week. Unfortunately, the data provided lumped all weekdays together, so I'm out of luck this time. 

The original intention of the ingestion portion of this project was to read the data using [SODA API] (https://dev.socrata.com/). However, version 3 requires use of an Access Token, and the python script requires login information along with the access token to hit the City of Chicago data endpoint. Therefore, I defaulted to downloading the data and ingesting via file read. All of the source files are located under the "data" directory.

## Project Contents
This repository contains the following file structure:
└── 📁 data

    ├── annual_boarding_totals.csv

    ├── daily_ridership_bus_routes.csv

    ├── daily_ridership_l_stations.csv
    
├── README.md

├── analysis.ipynb

├── ingestion.py

├── requirements.txt

├── schemas.sql


## Commit History
Commits were made under the *feature/development* branch. This was done out of habit of not committing directly to main. Please [view full commit history here] (https://github.com/hinako-jefferson/trend-health-technical-exercise/pull/1). 

## Execution
### 1. Clone the repository
I recommend cloning the repository from Github by running the following command:
```git clone https://github.com/<your-github-user>/trend-health-technical-exercise.git```

If you have Github Desktop application installed, you can clone from the [trend-health-technical-exercise repository] (https://github.com/hinako-jefferson/trend-health-technical-exercise.git) as well. 

### 2. Install requirements
Please be sure to have Python 3.10 or higher installed. 

Additionally, install libraries required to execute this script by running the following command:
```pip install -r requirements.txt```

### 3. Execute ingestion.py
This script needs to be ran first in order to 
- Create SQLite database and tables
- Ingest CTA data
- Populate the data into the SQLite tables

### 4. Execute analysis.ipynb
Once the data is loaded, this script will conduct analysis on the collected data. The data points to be explored and the afterthoughts are documented on the analysis.ipynb script.