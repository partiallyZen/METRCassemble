# METRCassemble
This repository creates CSV files for upload to METRC.

### Wut?!
This repository currently handles input through an A&D scale, Zebra Scanner, and keyboard to create a METRC-compliant CSV to upload weighed items

### Why?
I need it to help streamline operations in a cannabis grow operation. 

## Installation

## Installation

### Pre-Requisites
- [Python 3.10+](https://www.python.org/downloads/ "Python 3.10+")
- Python Modules: time, serial, datetime, textwrap, tabulate, os, numpy, [See imports.py]
- RS-232C Port for Input from Scale
- Scanner for METRC Tag Input (HID Mode)

### Install
- Plug in RS-232C Cord and USB to PC/Mac/Potato
- Plug USB scanner into same Potato
- Run main.py
_It is just a script so it does not really have a installation. Run "main.py" with computer connected to scale and scanner._
Follow the prompts. 
CSV will populate in folder run. You can change the name of the create file main.py line 16.

### Warning
Currently new rows will be appended to the same document during the same day. 
As METRC only requires the day/date, double check csv before submitting to the State.
_Consider yourself warned..._
