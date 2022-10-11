import discord
import yfinance as yf
import os

my_secret = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)

def get_news(wanted_stock):
  stock = yf.Ticker(wanted_stock)
  news = ""
  counter = 0
  while counter < 5:
    news = news + "Title: **" + stock.news[counter][
      "title"] + "**\n" + "Link: <" + stock.news[counter]["link"] + ">\n\n"
    counter += 1
  return news

currencies = {"USD": "$", "CAD": "$", "EUR": "€", "GBP": "£", "AUD": "$"}

def get_stock(wanted_stock):
  try:
    stock = yf.Ticker(wanted_stock)
    stock_currency = stock.info["currency"].upper()
    stock_price = stock.info["currentPrice"]
    stock_open = stock.info["open"]
    stock_change_since_open = str(
      round((((stock_price - stock_open) / stock_open) * 100), 2)) + "%"
    stock_recommendation = stock.info["recommendationKey"].capitalize()
    news = get_news(wanted_stock)
    to_print = f"Stock: **{wanted_stock}**\nCurrent Price: {currencies[stock_currency]}{stock_price} {stock_currency}\nOpen Price: {currencies[stock_currency]}{stock_open} {stock_currency}\nPercent change since open: {stock_change_since_open}\nRecommendation(**NFA**): {stock_recommendation}\n**News:**\n{news}"
    return to_print
  except:
    return "Invalid Stock!"

stockBotInfo = "To recieve stock information use the command **'/stockBot [TICKER]'**. For example, '/stockBot MSFT' will return the stock information for Microsoft.\
    \nThe Information returned includes the current price, open price, percent change since open, analyst recommendation(NFA), and news relating to the stock."

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(
    type=discord.ActivityType.watching, name="/stockBot info"))
  print('Python bot is now online!')

@client.event
async def on_guild_join(guild):
  channel = guild.text_channels[0]
  await channel.send(
    "StockBot has joined the server! Use the command '/stockBot info' for information on how to use the bot."
  )

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/stockBot'):
    content = message.content.split(" ")
    if (len(content) == 2 and content[1] != "info"):
      wanted_stock = str(content[1])
      await message.channel.send(get_stock(wanted_stock))
    elif (len(content) == 2 and content[1] == "info"):
      await message.channel.send(stockBotInfo)
    else:
      await message.channel.send('Please input a valid statement.')

client.run(my_secret)