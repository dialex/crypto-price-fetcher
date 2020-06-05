#!/bin/bash

cd $(dirname $0)
rake clean_run fetch
open prices.txt
