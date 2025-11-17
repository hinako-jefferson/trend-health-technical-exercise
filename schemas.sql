-- create tables 

-- Source: CTA - Ridership - Bus Routes - Daily Totals by Route
CREATE TABLE IF NOT EXISTS daily_ridership_bus_routes(
route text not null,
date date not null,
daytype text,
rides number,
primary key (route, date)
);

-- Source: CTA - Ridership - 'L' Stations - Daily Totals by Station
CREATE TABLE IF NOT EXISTS daily_ridership_l_stations(
station_id number not null,
stationname text,
date date not null,
daytype text,
rides number,
primary key (station_id, date)
);

-- Source: CTA - Ridership - Annual Boarding Totals
CREATE TABLE IF NOT EXISTS annual_boarding_totals(
year number primary key not null,
bus number,
paratransit number,
rail number,
total number
);

-- Create indexes for performance enhancement (even though this dataset is small)
-- Skipping index creation for annual_boarding_totals as this dataset's raw size is only 1.8 KB; The table will only contain 31 rows.
CREATE INDEX IF NOT EXISTS idx_drbr_route ON daily_ridership_bus_routes(route);
CREATE INDEX IF NOT EXISTS idx_drbr_date ON daily_ridership_bus_routes(date);

CREATE INDEX IF NOT EXISTS idx_drls_station_id ON daily_ridership_l_stations(station_id);
CREATE INDEX IF NOT EXISTS idx_drls_date ON daily_ridership_l_stations(date);