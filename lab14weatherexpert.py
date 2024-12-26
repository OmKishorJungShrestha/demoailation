#lab14weather expert system:
class WeatherExpertSystem:
    def init(self, temperature, humidity, is_cloudy, is_sunny):
        self.temperature = temperature
        self.humidity = humidity
        self.is_cloudy = is_cloudy
        self.is_sunny = is_sunny

    def predict_weather(self):
        if self.temperature > 30 and self.humidity < 40:
            return "Prediction: Hot and dry."
        elif self.temperature < 10:
            return "Prediction: Cold weather."
        elif self.is_cloudy and self.humidity > 60:
            return "Prediction: Rain likely."
        elif 20 <= self.temperature <= 30 and self.humidity < 50:
            return "Prediction: Pleasant weather."
        elif self.is_sunny:
            return "Prediction: Sunny weather."
        else:
            return "Prediction: Uncertain conditions."

# Input section
temperature = float(input("Enter the temperature: "))
humidity = float(input("Enter the humidity: "))
is_cloudy = input("Is it cloudy? (yes/no): ").lower() == "yes"
is_sunny = input("Is it sunny? (yes/no): ").lower() == "yes"

# Prediction
weather = WeatherExpertSystem(temperature, humidity, is_cloudy,is_sunny)
prediction = weather.predict_weather()
print(prediction)

