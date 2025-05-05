# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "65d84a03-6953-462d-9453-a13f442b540f",
# META       "default_lakehouse_name": "earthquake_lakehouse",
# META       "default_lakehouse_workspace_id": "4768aa00-9af1-42bc-a028-33b1a764f9c8",
# META       "known_lakehouses": [
# META         {
# META           "id": "65d84a03-6953-462d-9453-a13f442b540f"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
import requests
import json
#from datetime import date, timedelta

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Remove this before running Data Factory Pipeline
# start_date = date.today() - timedelta(7) # 7 days
# end_date = date.today() -timedelta(1)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Construct the API URL with start and end dates provided by Data Factory, formatted for geoson output.
url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_date}&endtime={end_date}"

try:
    # Make the GET request to fetch DeprecationWarning
    response = requests.get(url)

    # Check if the request was successful
    response.raise_for_status() # Raise HTTPError for bad responses(4xx or 5xx)
    data = response.json().get('features', [])

    if not data:
        print("No data returned forspecified date range.")
    else:
        # Specify the filename (and path if needed)
        file_path =f'/lakehouse/default/Files/{start_date}_earthquake_data.json'

        # Save the JSON data
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data successfuly saved to {file_path}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
