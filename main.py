#!/usr/bin/env python3
import imports
from function import * # Yeah I am a weird guy who puts all his stuff in other files...
import variablestore

kevdate()
x = kevdate()

while True:
  newrow = harvestrow()
  kevcount()
  print(tabulate(display, headers=["RFID Tag #", "Weight", "Unit", "Location", "Harvest", 'blank', "Date"], tablefmt="grid")) # Format Pretty Table
  truthcheck = input("Are you finished? [Y or N]: ")
  if truthcheck.upper() == "Y": # Need a loop for multi-row input
    print("Your METRC compatible CSV file is compiling...") 
    np.savetxt(str(x)+"beta.csv", display, delimiter=", ", fmt="% s") # Numpy is superior to the csvwriter IMHO
    for i in tqdm(range(3)): # Classic wait so as not to confused anyone...
      sleep(2)
    print("Your METRC compatible " + str(x) + "beta.csv is complete.")
    print("Thanks for using the METRC assembler!")
    break
