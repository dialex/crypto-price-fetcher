#!/bin/bash
#set -x #debug

source helpers.sh

echo 'starting'

local coin_data=get_price bitcoin
local coin_price=extract_price $coin_data

echo $coin_price

#TODO
#read config
#loop and get price
#export
