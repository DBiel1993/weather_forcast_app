# I CHOSE TO USE THE CLI FOR USER INPUTS AS I SEE THIS APPLICATION AS A FEATURE FOR A MUCH LARGER APPLICATION.

import requests  # Imports the requests library to make HTTP requests

def get_grid_points(latitude, longitude):
    """
    This function takes latitude and longitude as inputs and returns the office,
    gridX, and gridY values by querying the NOAA API.
    """
    # Construct the URL using the provided latitude and longitude
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    # Make a GET request to the NOAA API
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the office, gridX, and gridY values
        office = data['properties']['gridId']
        gridX = data['properties']['gridX']
        gridY = data['properties']['gridY']
        # Return the extracted values
        return office, gridX, gridY
    else:
        # Raise an exception if the request failed
        raise Exception("Failed to get grid points. Please check the latitude and longitude.")

def get_forecast(office, gridX, gridY):
    """
    This function takes office, gridX, and gridY as inputs and returns the weather
    forecast by querying the NOAA API.
    """
    # Construct the URL using the provided office, gridX, and gridY
    url = f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast"
    # Make a GET request to the NOAA API
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        forecast_data = response.json()
        # Return the forecast periods
        return forecast_data['properties']['periods']
    else:
        # Raise an exception if the request failed
        raise Exception("Failed to get forecast data.")

def display_forecast(forecast):
    """
    This function takes the forecast data as input and displays it in a readable format.
    """
    print("\nWeather Forecast:")
    # Iterate through each period in the forecast and print the details
    for period in forecast:
        print(f"{period['name']}: {period['detailedForecast']}")

def main():
    """
    The main function that orchestrates the user input and API calls.
    """
    print("Welcome to the Weather Forecast App")
    # Prompt the user to enter the latitude
    latitude = input("Enter the latitude: ")
    # Prompt the user to enter the longitude
    longitude = input("Enter the longitude: ")

    try:
        # Get the office, gridX, and gridY values using the provided latitude and longitude
        office, gridX, gridY = get_grid_points(latitude, longitude)
        # Get the weather forecast using the obtained office, gridX, and gridY values
        forecast = get_forecast(office, gridX, gridY)
        # Display the weather forecast
        display_forecast(forecast)
    except Exception as e:
        # Print any exceptions that occur
        print(e)

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()