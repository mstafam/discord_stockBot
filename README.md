# Discord stockBot
This Discord bot allows users to receive information on any stock. This information includes the current price, open price, price change since opening(in percent), analyst recommendation(not financial advice), on whether to buy or sell the given stock, and news relating to the stock. The stock information is pulled from Yahoo finance, using the yfinance python library.

You can add this bot to your server using this [link.](https://discord.com/api/oauth2/authorize?client_id=1029134922012700834&permissions=8&scope=bot)

In case you want to run this program on your computer, you need to fulfill the following requirements:
1. You must have a valid discord bot token, toggle on the required intents, and allow it permissions.
2. You must have the following required libraries installed on your machine; you can install them using the commands: 
'''
pip install discord.py
pip install yfinance
'''

**License:**
MIT License

Copyright (c) 2022 Mustafa

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
