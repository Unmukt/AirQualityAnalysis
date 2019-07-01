import numpy as np # linear algebra

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import warnings
warnings.filterwarnings('ignore')
pd.options.display.max_rows = 10

# google bigquery library for quering data
from google.cloud import bigquery

import bq_helper

# BigQueryHelper for converting query result direct to dataframe
from bq_helper import BigQueryHelper

#-------------------------------------------------------------------------

# create a helper object for this dataset
bigData = bq_helper.BigQueryHelper(active_project="bigquery-public-data",
                                   dataset_name="epa_historical_air_quality")


# print all the tables in this dataset
bigData.list_tables()

# THE FOLOOWING ANALYSIS WILL BE CARRIED OUT IN FOR ALL THE DISTINCT COUNTIES IN THE US BASED ON CATEGORIES FOR EACH OF THE POLLUTANT

# create schema of all the relevant tables avaliable in the dataset
CO = bigData.table_schema('co_daily_summary')
SO2 = bigData.table_schema('so2_daily_summary')
O3 = bigData.table_schema('o3_daily_summary')
NO2 = bigData.table_schema('no2_daily_summary')
PM10 = bigData.table_schema('pm10_daily_summary')
PM25 = bigData.table_schema('pm25_frm_daily_summary')
PM25n = bigData.table_schema('pm25_nonfrm_daily_summary')


# Category : OVER THE YEARS

# Subcategory : AQI
# ~query~
co_aqiQ = """
        SELECT state_name, county_name, city_name, date_local, aqi, 
arithmetic_mean
        FROM `bigquery-public-data.epa_historical_air_quality.co_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

co_aqi = bigData.co_daily_summary.query_to_pandas_safe(co_aqiQ)

# ~query~
so2_aqiQ = """
        SELECT state_name, county_name, city_name, date_local, aqi, 
arithmetic_mean
        FROM `bigquery-public-data.epa_historical_air_quality.so2_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

so2_aqi = bigData.so2_daily_summaryquery_to_pandas_safe(so2_aqiQ)

# ~query~
o3_aqiQ = """
        SELECT state_name, county_name, city_name, date_local, aqi, 
arithmetic_mean
        FROM `bigquery-public-data.epa_historical_air_quality.o3_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

o3_aqi = bigData.o3_daily_summaryquery_to_pandas_safe(o3_aqiQ)

# ~query~
no2_aqiQ = """
        SELECT state_name, county_name, city_name, date_local, aqi, 
arithmetic_mean
        FROM `bigquery-public-data.epa_historical_air_quality.no2_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

no2_aqi = bigData.no2_daily_summaryquery_to_pandas_safe(no2_aqiQ)

# ~query~
pm10_aqiQ = """
        SELECT state_name, county_name, city_name, date_local, aqi, 
arithmetic_mean
        FROM `bigquery-public-data.epa_historical_air_quality.pm10_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

pm10_aqi = bigData.pm10_daily_summaryquery_to_pandas_safe(pm10_aqiQ)

# ~query~
pm25_aqiQ = """
        SELECT state_name, county_name, city_name, date_local, aqi, 
arithmetic_mean
        FROM `bigquery-public-data.epa_historical_air_quality.pm25_frm_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

pm25_aqi = bigData.pm10_frm_daily_summaryquery_to_pandas_safe(pm25_aqiQ)

# ~query~
pm25n_aqiQ = """
        SELECT state_name, county_name, city_name, date_local, aqi, 
arithmetic_mean
        FROM `bigquery-public-data.epa_historical_air_quality.pm25_nonfrm_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

pm25n_aqi = bigData.pm10_nonfrm_daily_summaryquery_to_pandas_safe(pm25n_aqiQ)

# Subcategory : MEAN OBSERVATION
# ~query~
co_obsQ = """
        SELECT state_name, county_name, city_name, date_local, arithmetic_mean
        FROM `bigquery-public-data.epa_historical_air_quality.co_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

co_obs = bigData.co_daily_summary.query_to_pandas_safe(co_obsQ)

# ~query~
so2_obsQ = """
        SELECT state_name, county_name, city_name, date_local, observation_percent, observation_count
        FROM `bigquery-public-data.epa_historical_air_quality.so2_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

so2_obs = bigData.so2_daily_summary.query_to_pandas_safe(so2_obsQ)

# ~query~
o3_obsQ = """
        SELECT state_name, county_name, city_name, date_local, observation_percent, observation_count
        FROM `bigquery-public-data.epa_historical_air_quality.o3_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

o3_obs = bigData.o3_daily_summary.query_to_pandas_safe(o3_obsQ)

# ~query~
no2_obsQ = """
        SELECT state_name, county_name, city_name, date_local, observation_percent, observation_count
        FROM `bigquery-public-data.epa_historical_air_quality.no2_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

no2_obs = bigData.no2_daily_summary.query_to_pandas_safe(no2_obsQ)

# ~query~
pm10_obsQ = """
        SELECT state_name, county_name, city_name, date_local, observation_percent, observation_count
        FROM `bigquery-public-data.epa_historical_air_quality.pm10_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

pm10_obs = bigData.pm10_daily_summary.query_to_pandas_safe(pm10_obsQ)

# ~query~
pm25_obsQ = """
        SELECT state_name, county_name, city_name, date_local, observation_percent, observation_count
        FROM `bigquery-public-data.epa_historical_air_quality.pm25_frm_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

pm25_obs = bigData.pm10_frm_daily_summary.query_to_pandas_safe(pm25_obsQ)

# ~query~
pm25n_obsQ = """
        SELECT state_name, county_name, city_name, date_local, aqi, 
arithmetic_mean
        FROM `bigquery-public-data.epa_historical_air_quality.pm25_nonfrm_daily_summary'
        WHERE completeness_indicator = 'Y'
        GROUPBY Year, longitude, latitude
        ORDERBY 'Year' DESC
        """

pm25n_obs = bigData.pm10_nonfrm_daily_summary.query_to_pandas_safe(pm25n_obsQ)
