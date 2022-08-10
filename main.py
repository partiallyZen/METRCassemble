#!/usr/bin/env python3
from imports import *
from function import *
from variablestore import *
import serial

x = kevdate()

while True:
  newrow = harvestrow()
  print(tabulate(display, headers=["Tag#", "Weight", "Unit", "Location", "Harvest", 'blank', "Date"], tablefmt="grid"))
  truthcheck = input("Are you finished? [Y or N]: ")
  if truthcheck.upper() == "Y":
    print("Your METRC compatible CSV file is compiling...")
    np.savetxt(str(x)+"beta.csv", display, delimiter=", ", fmt="% s")
    for i in tqdm(range(2)):
      sleep(2)
    print("Your METRC compatible " + str(x) + "beta.csv is complete.")
    print("Thanks for using the METRC assembler!")
    break


# harvestrow = (rfidscan(), scalewght(), "grams", harvestloc(), harvestnom(), '', kevdate())

#f = open(str(x) + "beta.csv", 'a') #finalize the measurement
#writer = csv.writer(f) # open writer
#writer.writerow(harvestrow) # write row or write all rows...havent decided
#f.close #closer 'er up
