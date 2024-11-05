# Objective: Take the code from ex5 and modify it to include the following:

# Tasks:
    # Obtain and process 3 additional attributes in the weather data.
    # Graphically represent the additional attributes.
	# Update the HTML template to display the additional attributes.

# Submission Timeline:
    # Submit the code in 2 weeks.
from ex5 import*

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = None
    graph_filenames = {}
    if request.method == 'POST':
        city = request.form['city']
        
        # Geocoding to get latitude and longitude for the city using Open-Meteo's location API
        geocoding_response = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}')
        
        if geocoding_response.status_code == 200 and geocoding_response.json().get('results'):
            location = geocoding_response.json()['results'][0]
            latitude, longitude = location['latitude'], location['longitude']
            
            # Fetch hourly forecast data for temperature, humidity, windspeed, and precipitation
            weather_response = requests.get(
                f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,humidity_2m,windspeed_10m,precipitation&timezone=auto'
            )
            
            if weather_response.status_code == 200:
                weather_data = weather_response.json()
                graph_filenames = generate_weather_graphs(weather_data)
            else:
                weather_data = {'error': 'Unable to retrieve weather data.'}
        else:
            weather_data = {'error': 'City not found'}
            
    return render_template('dashboard.html', weather_data=weather_data, graph_filenames=graph_filenames)

def generate_weather_graphs(weather_data):
    # Parse hourly data for the next 24 hours
    times = weather_data['hourly']['time'][:24]
    time_labels = [datetime.datetime.fromisoformat(time).strftime('%H:%M') for time in times]
    
    # Get data for each attribute
    temperatures = weather_data['hourly']['temperature_2m'][:24]
    humidity = weather_data['hourly']['humidity_2m'][:24]
    windspeed = weather_data['hourly']['windspeed_10m'][:24]
    precipitation = weather_data['hourly']['precipitation'][:24]

    # Ensure the static directory exists
    if not os.path.exists('static'):
        os.mkdir('static')
        
    # Dictionary to store filenames
    graph_filenames = {}

    # Temperature Graph
    plt.figure(figsize=(10, 5))
    plt.plot(time_labels, temperatures, marker='o', linestyle='-', color='b')
    plt.xticks(rotation=45)
    plt.xlabel('Time (24 hours)')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Forecast for the Next 24 Hours')
    plt.tight_layout()
    graph_filenames['temperature'] = './static/temperature_plot.png'
    plt.savefig(graph_filenames['temperature'])
    plt.close()

    # Humidity Graph
    plt.figure(figsize=(10, 5))
    plt.plot(time_labels, humidity, marker='o', linestyle='-', color='g')
    plt.xticks(rotation=45)
    plt.xlabel('Time (24 hours)')
    plt.ylabel('Humidity (%)')
    plt.title('Humidity Forecast for the Next 24 Hours')
    plt.tight_layout()
    graph_filenames['humidity'] = './static/humidity_plot.png'
    plt.savefig(graph_filenames['humidity'])
    plt.close()

    # Windspeed Graph
    plt.figure(figsize=(10, 5))
    plt.plot(time_labels, windspeed, marker='o', linestyle='-', color='r')
    plt.xticks(rotation=45)
    plt.xlabel('Time (24 hours)')
    plt.ylabel('Wind Speed (m/s)')
    plt.title('Wind Speed Forecast for the Next 24 Hours')
    plt.tight_layout()
    graph_filenames['windspeed'] = './static/windspeed_plot.png'
    plt.savefig(graph_filenames['windspeed'])
    plt.close()

    # Precipitation Graph
    plt.figure(figsize=(10, 5))
    plt.plot(time_labels, precipitation, marker='o', linestyle='-', color='purple')
    plt.xticks(rotation=45)
    plt.xlabel('Time (24 hours)')
    plt.ylabel('Precipitation (mm)')
    plt.title('Precipitation Forecast for the Next 24 Hours')
    plt.tight_layout()
    graph_filenames['precipitation'] = './static/precipitation_plot.png'
    plt.savefig(graph_filenames['precipitation'])
    plt.close()

    return graph_filenames

