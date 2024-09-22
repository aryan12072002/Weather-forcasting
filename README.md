
# Weather Forecasting Application 🌦️

A simple Django-based weather forecasting web application that fetches current weather data for a given city using the OpenWeatherMap API.

## Features
- Enter a city name and get the current weather forecast, including temperature and weather conditions.
- Error handling for invalid city names or API issues.
- Responsive and user-friendly interface with modern styling.

## Requirements

Before you begin, ensure you have the following installed:

- Python 3.12.5
- Django 5.1.1
- Requests library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/weather-forecasting-app.git
   cd weather-forecasting-app
   ```

2. **Create and activate a virtual environment**:

   On Windows:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**:

   - Sign up for an API key from [OpenWeatherMap](https://openweathermap.org/api).
   - Create a `.env` file in the root of the project and add your API key like this:

     ```
     OPENWEATHER_API_KEY=your_api_key_here
     ```

5. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to use the application.

## Usage

- Enter the name of any city in the input field and press "Get Weather" to see the current weather conditions for that city.
- Default city is London if no city is provided.
- Error messages will be displayed for invalid cities or API failures.

## Project Structure

```
weather-forecasting-app/
│
├── weatherapp/
│   ├── templates/
│   │   └── weather/
│   │       └── weather.html    # The main HTML template
│   ├── static/
│   │   └── weather/
│   │       └── styles.css      # CSS for styling the application
│   └── views.py                # The logic to fetch weather data
├── manage.py                   # Django project manager
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## API Usage

This app uses the [OpenWeatherMap API](https://openweathermap.org/api) to fetch weather data.

You need to sign up for an API key and add it to your `.env` file as shown in the installation steps.

## Technologies Used

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS (custom styles)
- **API**: OpenWeatherMap API for real-time weather data

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch for your feature (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

---

### Example of how to customize:

- You can adjust the default city by modifying the `weather_view` function in `views.py`.
- Customize the front-end by editing the HTML and CSS files in the `templates/weather/` and `static/weather/` directories.

### Contact

For any inquiries, please reach out at tayadearyan98@gmail.com

