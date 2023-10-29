from django.shortcuts import render
from .models import Crypto_Price
import httpx
import asyncio
from asgiref.sync import sync_to_async
import logging

@sync_to_async
def create_or_update_crypto_price(symbol, price):
    cryptocurrency, created = Crypto_Price.objects.get_or_create(symbol=symbol, defaults={"price": price})
    if not created:
        cryptocurrency.price = price
        cryptocurrency.save()

async def get_price():
    symbols = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "LTCUSDT", "BNBUSDT", "DOGEUSDT"]
    async with httpx.AsyncClient() as client:
        tasks = []
        for symbol in symbols:
            url = "https://api.binance.com/api/v3/ticker/price"
            params = {"symbol": symbol}
            task = client.get(url, params=params)
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        data = [response.json() for response in responses]
        
        for symbol, price_data in zip(symbols, data):
            price = price_data["price"]
            await create_or_update_crypto_price(symbol, price)

async def index(request):
    await get_price()
    cryptocurrencies = await sync_to_async(list)(Crypto_Price.objects.all())
    
    usd_to_eur = 0.85
    usd_to_rub = 73.0
    usd_to_cny = 6.5

    for cryptocurrency in cryptocurrencies:
        cryptocurrency.eur_price = float(cryptocurrency.price) * usd_to_eur
        cryptocurrency.rub_price = float(cryptocurrency.price) * usd_to_rub
        cryptocurrency.cny_price = float(cryptocurrency.price) * usd_to_cny
        
    logger = logging.getLogger(__name__)
    logger.info("Prices were retrieved successfully.")

    return render(request, "crypto_viewer/index.html", {'cryptocurrencies': cryptocurrencies})
