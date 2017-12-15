require 'rest-client'
require 'json'
require_relative 'logging.rb'

def get_data (coin_ticker)
  log "Fetching data for #{coin_ticker}"

  url = "https://api.coinmarketcap.com/v1/ticker/#{coin_ticker}/?convert=EUR"
  response = RestClient.get(url)
  return JSON.parse(response)
end

def extract_price (json)
  price = json[0]['price_eur'].to_s
  log " #{price.to_s} EUR"
  return price
end

def read_config (filepath)
  file = File.read(filepath)
  data = JSON.parse(file)
  return data
end

def list_tickers
  url = "https://api.coinmarketcap.com/v1/ticker/?limit=0"
  response = RestClient.get(url)
  json_response = JSON.parse(response)

  list = []
  json_response.each { |element|
    list << element['id'].gsub('"','')
  }
  return list.sort
end
