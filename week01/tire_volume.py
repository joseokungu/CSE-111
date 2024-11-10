"""
Where:
    v is the volume in liters,
    π is the constant PI, which is the ratio of the circumference of a 
        circle divided by its diameter (use math.pi),
    w is the width of the tire in millimeters,
    a is the aspect ratio of the tire, and
    d is the diameter of the wheel in inches.

"""
import math
from datetime import datetime

# Get user inputs
# Input validation to handle non-numeric values
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the tire volume
total = (((math.pi * (w**2) * a)) * ((w * a) + (2540 * d)) / 10000000000)

# Output result to the user
print(f"\nThe approximante volume is: {total: .2f} liters")

# Get current date
total = round(total, 2)
today = datetime.now()
today = f"{today: %Y-%m-%d}"

# Append data to log file
with open('volumes.txt', "a") as volume_file:
    volume_file.write(f"\nCurrent date: {str(today)}"
                      f"\nWidth = {str(w)}"
                      f"\nAspect ratio of the tire is = {str(a)}"
                      f"\nDiameter of the wheel is = {str(d)}"
                      f"\nVolume of the tire is = {str(total)}")
    
 # Confirm to the user
    print("\nTire information successfully logged.")