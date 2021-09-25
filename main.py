import requests
import os

from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACc9bb6b4b49200b7966a72d0182e5db9f'
auth_token = os.environ.get("AUTH_TOKEN")
my_pone_number = os.environ.get("MY_PHONE_NUMBER")

parameters = {
    'lat': -25.586090,
    'lon': -49.405849,
    'exclude': 'current,minutely,daily',
    'appid': os.environ.get("OWM_APPID"),
}

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
next_12_hours_data = weather_data['hourly'][:12]
print(next_12_hours_data)

will_rain = False

for hour in next_12_hours_data:
    condition_code = hour['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True
        # break

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to rain today, remember to bring a ☂",
            from_='+15183124705',
            to=my_pone_number
        )

    print(message.status)
