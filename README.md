# Crypto Currencies Price Fetcher

## Why?

I have my own spreadsheet with how much I invested in each coin, how many I hold, and the current sell value. Once in a while I want to batch update the "sell value" column and let the sheet do its magic and give the total value of my portfolio.

I used to do this manually for each coin, but quickly the process became painful. ~~Almost as painful as realizing how much money I lost with cryptos...~~ **I needed a faster way to copy-paste to all rows the latest price of each coin.**

## What?

Before

- Go to [CoinMarketCap](https://coinmarketcap.com/#EUR) and search for my coin
- Copy the coin price
- Select the respective cell in the spreadsheet
- Paste the price (without formatting)
- Repeat this 27 times 😰

Today

- Call spotlight (`⌘+Space`), type **fetcher** and `Enter`
- Wait 5 secs, *while script reads a config file, calls an API x 27 times, and writes to a file*
- Copy all values (`⌘+A`, `⌘+C`, `⌘+Q`)
- Select all rows and paste (`⌘+V`) 😎 👍

## How?

- 💎  **Ruby** version
  - cd `ruby`
  - Execute `run-bigbang.sh` to install everything required to run the app.
  - Execute `run-fetcher.sh` or `rake` to fetch the prices.
- 🐍  **Python** version
  - cd `python`
  - Execute `run-bigbang.sh` to install everything required to run the app.
  - Execute `run-fetcher.sh` or `invoke app` to fetch the prices.
