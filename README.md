# Weather Forecast App

This is a simple Weather Forecast App that takes user input for latitude and longitude, retrieves the corresponding weather forecast using the NOAA API, and displays it.

## Setup Instructions

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
   ```sh
   pip install -r requirements.txt
   ```

How the App Works:

    1.	User Input:

    •	The app starts by prompting the user to enter latitude and longitude coordinates. These coordinates represent the geographical location for which the user wants to obtain the weather forecast.

    2.	Fetch Grid Points:

    •	The app uses the entered latitude and longitude to make a request to the NOAA API endpoint: https://api.weather.gov/points/{latitude},{longitude}.
    •	This endpoint returns a response containing the office identifier (gridId), and the grid coordinates (gridX and gridY), which are necessary for querying the forecast.

    3.	Fetch Weather Forecast:

    •	Using the obtained office, gridX, and gridY values, the app makes another request to the NOAA API endpoint: https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast.
    •	This endpoint returns detailed weather forecast data for the specified grid location.

    4.	Display Forecast:

    •	The app processes the forecast data and displays it in a user-friendly format. The forecast includes detailed information for different periods (e.g., day, night) within the requested location.

    5.	Error Handling:

    •	If there is an issue with fetching data (e.g., incorrect latitude/longitude, network issues), the app handles the errors gracefully and informs the user.

Workflow Summary:

    1.	Prompt user for latitude and longitude.
    2.	Query NOAA API to get grid location (office, gridX, gridY).
    3.	Query NOAA API to get the weather forecast using the grid location.
    4.	Display the weather forecast to the user in a readable format.
    5.	Handle any errors that may occur during the process.

Benefits:

    •	Localized Forecasts: Provides specific weather forecasts for precise locations.
    •	User-Friendly: Simple input and clear output make it accessible for users.
    •	Reliable Data: Uses data from the NOAA National Weather Service, a trusted source for weather information.
