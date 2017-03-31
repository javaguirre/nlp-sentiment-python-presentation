# El Bot autodidacta

## Installation

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You need a Telegram API bot key and an API key to use it, then export the
tokens as env variables and run the `app.py` file.

```bash
export FLASK_BASE_URL='https://hash.ngrok.io'
export TELEGRAM_AUTH_TOKEN='my_token'
export APIAI_ACCESS_TOKEN='my_apiai_token'
export FLASK_DEBUG=1
source .venv/bin/activate
python app.py
```

You can use [ngrok]() to create a tunnel connection to your localhost so
Telegram webhook can connect, something like.

```bash
./ngrok http 5000
```

You're done! :-)
