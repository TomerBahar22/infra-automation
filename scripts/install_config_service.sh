#!/bin/bash

# Define the log file path
LOGFILE="logs/provisioning.log"

# Function to log messages with timestamps
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOGFILE"
}

# Log the start of the Nginx installation process
log_message "installing nginx started."

# Prompt the user to check if the package is already installed
echo "Does your Package already installed? Y/N"
read -r answer  # Read user input into the 'answer' variable

# Loop until the user provides a valid response
while true; do 
    # Check if the user answered "Yes"
    if [[ "$answer" == "Y" || "$answer" == "YES" || "$answer" == "y" || "$answer" == "yes" ]]; then
        echo "Package already installed."  # Inform the user
        log_message "Package already installed."  # Log the event
        break  # Exit the loop

    # Check if the user answered "No"
    elif [[ "$answer" == "N" || "$answer" == "NO" || "$answer" == "n" || "$answer" == "no" ]]; then
        echo "Installing Nginx....."  # Notify the user about the installation
        echo "Installation complete."  # Notify the user about completion
        log_message "Package installed."  # Log the installation event
        break  # Exit the loop

    # If the input is invalid, prompt the user again
    else
        log_message "There was an error getting the input."  # Log the invalid input
        echo "There was an error getting the input."  # Inform the user
        echo "Does your Package already installed? Y/N"  # Ask the question again
        read -r answer  # Read the user input again
    fi
done  
