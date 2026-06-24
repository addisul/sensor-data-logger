import serial
import csv
from datetime import datetime

# Ensure this matches Arduino settings
PORT = 'COM3'  # Change port if necessary
BAUD = 9600
FILENAME = 'data.csv'

# Open serial connection
arduino = serial.Serial(PORT, BAUD, timeout=1)
print(f"Connected to {PORT}...")

# Open CSV file for writing
with open(FILENAME, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write Header
    writer.writerow(["Date", "Time", "Timestamp"]) 
    print(f"Logging to {FILENAME} (Press Ctrl+C to stop)")

    try:
        while True:
            if arduino.in_waiting > 0:
                # Read line and decode
                data = arduino.readline().decode('utf-8').strip()
                if data:
                    # Split the CSV data received from Arduino
                    # Assuming Arduino sends: "23/6/2026,12:00:00,1750680000"
                    row = data.split(',') 
                    
                    # Write to file
                    writer.writerow(row)
                    print(f"Logged: {data}")
                    
    except KeyboardInterrupt:
        print("\nLogging stopped.")
        arduino.close()
