-- CREATE TABLE table_name (
--             vendor_id TEXT NOT NULL,
--             pickup_datetime DATETIME NOT NULL,
--             dropoff_datetime DATETIME NOT NULL,
--             passenger_count INTEGER NULL,
--             trip_distance INTEGER NOT NULL,
--             rate_code TEXT NOT NULL,
--             store_and_fwd_flag TEXT NOT NULL,
--             payment_type TEXT NOT NULL,
--             fare_amount NUMERIC NOT NULL,
--             extra NUMERIC NOT NULL,
--             mta_tax NUMERIC NOT NULL,
--             tip_amount NUMERIC NOT NULL,
--             tolls_amount NUMERIC NOT NULL,
--             imp_surcharge NUMERIC NOT NULL,
--             total_amount NUMERIC NOT NULL,
--             pickup_location_id TEXT NOT NULL,
--             dropoff_location_id TEXT NOT NULL
-- );

LOAD DATA INFILE 'raccon.csv'
INTO TABLE table_name
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;