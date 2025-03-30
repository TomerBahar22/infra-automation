#!/bin/bash


echo "Does your Package already installed? Y/N"
read answer

if [[ "$answer" == "Y" || "$answer" == "YES" || "$answer" == "y" || "$answer" == "yes" ]]; then
    echo "Package already installed."
elif [[ "$answer" == "N" || "$answer" == "NO" || "$answer" == "n" || "$answer" == "no" ]]; then
    echo "Installing Nginx....."
    echo "Installation complete."
else
    echo "There was an error getting the input."
fi