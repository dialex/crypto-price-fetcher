require 'httparty'
require 'json'
require 'jsonpath'
require_relative 'logging.rb'

def get_data (coin_ticker)
  log "Fetching data for #{coin_ticker}"

  headers = {"X-CMC_PRO_API_KEY": "SECRET_GOES_HERE"}
  url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?slug=#{coin_ticker}&convert=EUR"

  response = HTTParty.get(url, :headers => headers, format: :plain)
  return JSON.parse(response)
end

def extract_price (json)
  price = JsonPath.new("$..EUR.price").first(json)
  log " #{price.to_s} EUR"
  return price
end

def read_config (filepath)
  file = File.read(filepath)
  data = JSON.parse(file)
  return data
end
