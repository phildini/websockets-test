# Hello, Caller

```shell
% ./setup.sh
% ./start.sh
```

## To be able to test making and receiving calls:
1. Have your server running (`./start.sh`)
2. Have ngrok running, and pointing at your server. It will be easier if you've authed with ngrok so you can customize the subdomain, ie `ngrok http 8000 --subdomain={subdomain}`
3. Have a [TwiML App created in the dashboard](https://www.twilio.com/console/voice/twiml/apps).
4. Have that TwiML app's Voice url is pointing at `https://{your ngrok url}/calls/call`.
6. Copy the TwiML app's SID into your `.env` file, `TWIML_APPLICATION_SID='{your app SID}'`
5. Have a [Twilio Phone number in the dashboard](https://www.twilio.com/console/phone-numbers/incoming).
7. That phone number's Voice section should be pointing at your TwiML app.
8. Copy the phone number into your `.env` file, `TWILIO_NUMBER='{your number, including the + at the front }'`
9. Copy the ACCOUNT SID from [the dashboard](https://www.twilio.com/console). Paste it into your `.env` as `TWILIO_ACCOUNT_SID='{account sid}'`
10. Copy the AUTH TOKEN from [the dashboard](https://www.twilio.com/console). Paste it into your `.env` as `TWILIO_AUTH_TOKEN='{auth token}'`
