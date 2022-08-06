#!/usr/bin/env python3
import imports
from function import *
import variablestore


kevdate()
x = kevdate()

f = open(str(x) + "beta.csv", 'w')
f.close

while True:
  newrow = harvestrow()
  print(tabulate(display, headers=["|METRC RFID Tag #|", "Weight", "Unit", "Location Name", "Harvest Name", 'blank', "Today's Date"], tablefmt="grid"))
  f = open(str(x) + "beta.csv", 'a') #finalize the measurement
  writer = csv.writer(f) # open writer
  writer.writerow(newrow) # write row or write all     rows...havent decided
  f.close #closer 'er up
  truthcheck = input("Are you finished? [Y or N]: ")
  if truthcheck.upper() == "Y":
    print("Your METRC compatible CSV file is complete")
    print("Thanks for using the METRC assembler!")
    break

# harvestrow = (rfidscan(), scalewght(), "grams", harvestloc(), harvestnom(), '', kevdate())

#f = open(str(x) + "beta.csv", 'a') #finalize the measurement
#writer = csv.writer(f) # open writer
#writer.writerow(harvestrow) # write row or write all rows...havent decided
#f.close #closer 'er up
