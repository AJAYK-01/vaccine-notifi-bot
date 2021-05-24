# vaccine-notifi-bot

Code to send cowin vaccine slots availability notifications over telegram

Steps:

1. Configure your district:
   - to get state ID use:
     `curl -X GET "https://cdn-api.co-vin.in/api/v2/admin/location/states" -H "accept: application/json" -H "Accept-Language: hi_IN"`
   - use the state id to get district info.:
     `curl -X GET "https://cdn-api.co-vin.in/api/v2/admin/location/districts/16" -H "accept: application/json" -H "Accept-Language: hi_IN"`
   - use the district id in the heroku env variables that are asked when you press deploy to heroku
2. Press Deploy to Heroku to deploy bot
   - Get Bot token from Telegram BotFather
   - Get your chat id using [@chatIDrobot](https://t.me/chatIDrobot) in telegram
   - Add age limit and district id that you got from step 1

## Deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AJAYK-01/vaccine-notifi-bot)
