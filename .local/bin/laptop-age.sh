#!/bin/bash

#read -p "Enter your birth year.  Example: 1900 : " year
#read -p "Enter your birht month. Example: 06 " month
year=2017
month=01

yearnow=$(date '+%Y')
monthnow=$(date '+%m')

agey=$(($yearnow-$year))
agem=$(($monthnow-$month))

if [ $agem -lt 0 ] ; then
   agem=$(($monthnow-$month+12))
else
   agem=$(($monthnow-$month))
fi

echo "$agey""Y" "$agem""M"

