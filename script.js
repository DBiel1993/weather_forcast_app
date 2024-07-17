// Function to fetch and display the weather forecast
async function fetchForecast() {
    const latitude = 39.1178;
    const longitude = -106.4454;

    try {
        // Get the grid points for the given latitude and longitude
        const gridPointsResponse = await fetch(`https://api.weather.gov/points/${latitude},${longitude}`);
        if (!gridPointsResponse.ok) throw new Error("Failed to get grid points");

        const gridPointsData = await gridPointsResponse.json();
        const office = gridPointsData.properties.gridId;
        const gridX = gridPointsData.properties.gridX;
        const gridY = gridPointsData.properties.gridY;

        // Get the weather forecast using the grid points
        const forecastResponse = await fetch(`https://api.weather.gov/gridpoints/${office}/${gridX},${gridY}/forecast`);
        if (!forecastResponse.ok) throw new Error("Failed to get forecast data");

        const forecastData = await forecastResponse.json();
        const forecastPeriods = forecastData.properties.periods.slice(0, 6); // Get forecast for the next 3 days (6 periods)

        // Combine day and night forecasts
        const combinedForecasts = [];
        for (let i = 0; i < forecastPeriods.length; i += 2) {
            const day = forecastPeriods[i];
            const night = forecastPeriods[i + 1];
            combinedForecasts.push({ day, night });
        }

        // Display the forecast
        const forecastList = document.getElementById("forecast-list");
        forecastList.innerHTML = ""; // Clear any existing content

        combinedForecasts.forEach(({ day, night }) => {
            const listItem = document.createElement("div");
            listItem.className = "forecast-item";
            listItem.innerHTML = `
                <div class="day">${day.name}</div>
                <div class="temperature">${day.temperature} ${day.temperatureUnit} / ${night.temperature} ${night.temperatureUnit}</div>
            `;
            forecastList.appendChild(listItem);
        });

    } catch (error) {
        console.error(error);
    }
}

// Call the function to fetch and display the weather forecast
fetchForecast();