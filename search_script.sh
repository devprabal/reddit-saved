#!/bin/bash

## this is just an example to show how one can easily search through the saved reddit posts
## more sophisticated scripts can be written
sort -k 1,2 -n oneliner.txt | cut -f 2,4 | fzf -e