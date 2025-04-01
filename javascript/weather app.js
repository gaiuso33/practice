async function getWeather() {
    let city = document.getElementById("city").value;
    let apiKey = "YOUR_API_KEY"; // Replace with your OpenWeather API Key
    let url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        let response = await fetch(url);
        let data = await response.json();

        if (data.cod === 200) {
            document.getElementById("weather-info").innerHTML = `
                <h3>${data.name}, ${data.sys.country}</h3>
                <p>Temperature: ${data.main.temp}°C</p>
                <p>Humidity: ${data.main.humidity}%</p>
                <p>Condition: ${data.weather[0].description}</p>
            `;
        } else {
            document.getElementById("weather-info").innerHTML = `<p>City not found</p>`;
        }
    } catch (error) {
        console.error("Error fetching weather data", error);
    }
}
