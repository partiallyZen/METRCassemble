#!/usr/bin/env python3

from imports import *
from variablestore import *


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
    print("Today is " + today + ".")
    print("Adding this to the METRC Table...")
    return (today)


def rfidscan():
    RFIDTAG = input("Please scan METRC RFID TAG now...")
    RFIDTAGs = str(RFIDTAG)
    return (RFIDTAGs)  #add choice to rescan, or add to <metrcrow>


def scalewght():
    print("Please press the ENTER key on scale |")
    # x=ser.readline()
    # d=x.decode()    #prints out the number only
    # WGHT=d[5:10]
    WGHT = input()
    print(WGHT + " grams")
    return (WGHT)


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
    kevcount()
    return (harvestrow0)

