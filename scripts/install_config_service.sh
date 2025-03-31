#!/bin/bash
LOGFILE="logs/provisioning.log"
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOGFILE"
}

log_message "installing nginx started."

echo "Does your Package already installed? Y/N"
read -r answer
while true; do 
    if [[ "$answer" == "Y" || "$answer" == "YES" || "$answer" == "y" || "$answer" == "yes" ]]; then
        echo "Package already installed."
        log_message "Package already installed."
        break
    elif [[ "$answer" == "N" || "$answer" == "NO" || "$answer" == "n" || "$answer" == "no" ]]; then
        echo "Installing Nginx....."
        echo "Installation complete."
        log_message "Package installed."
        break
    else
        log_message "There was an error getting the input."
        echo "There was an error getting the input."
        echo "Does your Package already installed? Y/N"
        read -r answer
    fi
done
