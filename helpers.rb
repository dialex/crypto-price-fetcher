require 'rest-client'
require 'json'
require_relative 'logging.rb'

def get_data (coin_ticker)
  log "Fetching data for #{coin_ticker}"

  url = "https://api.coinmarketcap.com/v1/ticker/#{coin_ticker}/?convert=EUR"
  response = RestClient.get(url)
  JSON.parse(response)
end

def extract_price (json)
  json[0]['price_eur'].to_s
end
