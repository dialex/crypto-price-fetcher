#!/bin/bash

function get_price {
  if [[ $# -ne 1 ]]
  then
    echo "${FUNCNAME[0]} requires 1 parameter: [COIN_TICKER]"
    return 1
  fi

  local param_coin=$1

  curl -X GET \
    "https://api.coinmarketcap.com/v1/ticker/$param_coin/?convert=EUR" \
    -H 'cache-control: no-cache'
}

function extract_price {
  local param_json=$1
  
}