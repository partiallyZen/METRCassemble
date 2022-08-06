#!/usr/bin/env python3

from imports import *
from variablestore import *

def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')     # I love when menus clear and re-open...
    else:
        # for windows platfrom
        _ = os.system('cls')
    # print out some text

def kevdate():
    today = date.today().strftime('%Y-%m-%d')
    print("Today is " + today + ".")
    print("Adding this information to METRC Table...") #kevdate with some flair
    screen_clear()
    return (today)

def kevcount():
    kevnum = len(display)
    print("You have currently added " + str(kevnum) + " rows this session.")  #Prog'd for the testing, stays because I like it 
    return (kevnum)

def rfidscan():
  while True:
    RFIDTAG = input("Please scan METRC RFID TAG now...")
    RFIDTAGs = str(RFIDTAG)
    if int(len(RFIDTAGs)) != 24:                                      #RFID Scan and Length verification. [Will need to update with **args]
      screen_clear()
      print("ENTRY INVALID INTIALIZING RESCAN")
    else:
      print("You scanned valid METRC Tag: " + RFIDTAGs)
      print("Adding this information to the table...")
      time.sleep(2)
      screen_clear()
      return (RFIDTAGs)  #add choice to rescan, or add to <metrcrow> 
      break

def scalewght():
    WGHT = input("Please press the ENTER key on scale | ")
    # x=ser.readline()
    # d=x.decode()    #prints out the number only                   uncomment these lines for serial input
    # WGHT=d[5:10]
    print("The scale returned " + WGHT + " grams")
    return (WGHT)
    # Needs input validations and testing

def harvestloc():
    print(tabulate(table, headers = ["Numeral", "Room Name"], tablefmt="grid"))
    #printform = pformat(rooms)
    #print(printform)
    harvestloc0 = rooms[1]

    print("Select Harvest Location by Numeral | Currently: " + harvestloc0)
    x = input()
    n = int(x)
    harvestloc0 = rooms[n]
    screen_clear()
    print("You selected: " + harvestloc0)
    return (harvestloc0)


def harvestnom():
    harvestnom0 = input("Type your Harvest Name here: ")
    return (harvestnom0 + kevdate())


def harvestrow():
    harvestrow0 = (
    )  # EXAMPLE [ABCDEF012345670000010011,100.23,Grams,Harvest Location,2015-12-15-Harvest Location-H,X00001,2015-12-15]
    #    Plant Label {<labelscan>}
    #    Harvested Weight {<WGHT>}
    #    Unit of Weight {"grams"}
    #    Drying Location Name {<HARVESTLOCATION>}
    #    Harvest Name {<HARVESTNAME>} Is it one of these: LIST or ADD NEW
    #    Patient License Number {=USER?=}
    #    Actual Date {<today>}

    harvestrow0 = (rfidscan(), scalewght(), "grams", harvestloc(),
                   harvestnom(), '', kevdate())
    print("Printing the following row(s) to METRC Template")
    display.append(harvestrow0)
    print(display)
    return (harvestrow0)
