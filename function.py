#!/usr/bin/env python3

from imports import *
from variablestore import *
from pyserial import scaleweight



def kevcount():
    kevnum =+ 1
    print("You have currently added " + str(kevnum) + " rows this session.")
    return (kevnum)


#def tabledisp():
 #   print(tabulate(display, disphead, tablefmt="grid")
  #  return


def kevdate():
    today = date.today().strftime('%Y-%m-%d')
    screen_clear()
    print("\nToday is " + today + ". Adding this to the METRC Table...\n")
    sleep(3)
    screen_clear()
    return (today)


def rfidscan():
    RFIDTAG = input("Please scan METRC RFID TAG now...")
    RFIDTAGs = str(RFIDTAG)
    print("You have scanned Tag #: " + RFIDTAGs)
    sleep(5)
    screen_clear()
    return (RFIDTAGs)  #add choice to rescan, or add to <metrcrow>


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
    # print out some text


def harvestloc():
    print(tabulate(table, headers = ["Numeral", "Room Name"], tablefmt="grid"))
    #printform = pformat(rooms)
    #print(printform)
    harvestloc0 = rooms[1]

    print("Select Harvest Location by Numeral [1-4] | Currently: " + harvestloc0)
    while True:
        try:
            value=int(input())
        except ValueError:
            print("Please Select a Number 1-4...")
            continue
        else:
            harvestloc0 = rooms[value]
            screen_clear()
            print("You selected: " + harvestloc0)
            sleep(3)                              #Need to add input validation, will throw errors with non int
            screen_clear()
            return (harvestloc0)


def harvestnom():
    harvestnom0 = input("Type your Harvest Name here: ")
    print("You have entered: " + harvestnom0)
    print("Adding harvest date...")
    sleep(5)
    screen_clear()
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

    harvestrow0 = (rfidscan(), scaleweight(), "grams", harvestloc(),
                   harvestnom(), '', kevdate())
    print("Printing the following row(s) to METRC Template")
    display.append(harvestrow0)
    x = str(len(display))
    print("You have added " + x + " rows.")
    screen_clear()
    return (harvestrow0)

