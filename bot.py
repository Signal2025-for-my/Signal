import requests
import datetime

TOKEN = "8413097456:AAEZqtGlQevA6MJfMqZvP6O6bttJIe4XaDU"  # токен твоего бота
CHANNEL_ID = "-1002995636754"  # id твоего канала

def get_price(pair):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={pair}"
    response = requests.get(url).json()
    return float(response["price"])

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=payload)

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    eth_price = get_price("ETHUSDT")
    btc_price = get_price("BTCUSDT")

    message = (
        f"📊 <b>Сигнал {now}</b>\n\n"
        f"ETH/USDT: {eth_price:.2f}\n"
        f"BTC/USDT: {btc_price:.2f}\n\n"
        f"✅ Прогноз: анализируется автоматически"
    )
    send_message(message)

if _name_ == "_main_":
    main()
