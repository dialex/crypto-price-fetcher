#!/bin/bash

cd $(dirname $0)
pipenv run invoke app
open prices.txt
