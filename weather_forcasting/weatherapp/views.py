from django.shortcuts import render
import requests


def weather_view(request):
    api_key = '8ad3d30df507ffa31ece13f0b1862881'
    city = request.GET.get('city', 'London')  
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(weather_url)
    weather_data = response.json()
    
    # Debugging: Print the API response to the console
    print(weather_data)
    
    # Check if 'main' exists in response
    if response.status_code == 200 and 'main' in weather_data:
        context = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
        }
    else:
        # Handle error cases or invalid responses
        context = {
            'error': weather_data.get('message', 'City not found or API error'),
        }
    
    return render(request, 'weather/weather.html', context)
