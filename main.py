import requests

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'


parameters = {
    'lat': "Your latitude",
    'lon': "Your longitude",
    'exclude': 'current,minutely,daily',
    'appid': 'b8d63b0cbdf006a7deb108e2b29d09f2',
}

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
next_12_hours_data = weather_data['hourly'][:12]
# print(next_12_hours_data)


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
        from_='Your twillo generated number',
        to='Your number'
    )

else:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="No rain today =D",
        from_='Your twillo generated number',
        to='Your phone number'
    )

# print(message.status)
