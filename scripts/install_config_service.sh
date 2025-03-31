#!/bin/bash
echo "Does your Package already installed? Y/N"
read -r answer
while true; do 
    if [[ "$answer" == "Y" || "$answer" == "YES" || "$answer" == "y" || "$answer" == "yes" ]]; then
        echo "Package already installed."
        break
    elif [[ "$answer" == "N" || "$answer" == "NO" || "$answer" == "n" || "$answer" == "no" ]]; then
        echo "Installing Nginx....."
        echo "Installation complete."
        break
    else
        echo "There was an error getting the input."
        echo "Does your Package already installed? Y/N"
        read -r answer
    fi
done
