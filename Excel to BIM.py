#! /usr/bin/python
''' This script was written by David Wigley for Atkins.  It opens a spreadsheet
which has its first sheet as the input titled 'MASTER RAW DATA' and the
subsequent sheets to copy from. There are a number of lists to populate
cell list = the input cells and outputlist = the rows in the master raw data
Also you need to change the lists of lists section to relect the number of
cells in the cell list

This version works with Foxit and Acrobat output which are not as consistant
as Bluebeam's output.
'''

import openpyxl
import os

# Paste directory in the next line parentheses
os.chdir(r"C:\\Users\\wigl2744\\OneDrive Corp\\OneDrive - Atkins Ltd\\Desktop")

# load workbook
wb = openpyxl.load_workbook("Scans.xlsx")

# List of cells to copy (!!!!!!!List not correct!!!!!)
celllist = [
            'A2',
            'A3',
            'D3',
            'G2',
            'G3',
            'A4',
            'D5',
            'G5',
            'A7',
            'A9',
            'A10',
            'A12',
            'B12',
            'D12',
            'A14',
            'A16',
            'A18',
            'A20',
            'A21',
            'A22',
            'A24',
            'A27',
            'A28',
            'A29',
            'D27',
            'D28',
            'D29',
            'G27',
            'J27',
            'G28',
            'G29',
            'J29',
            'M27',
            'M28',
            'M29',
            'O27',
            'O28',
            'O29',
            'R29',
            'T28',
            'R24',
            'T21',
            'T20',
            'M20',
            'G20',
            'J21',
            'J2',
            'L2',
            'M2',
            'O2',
            'Q2',
            'R2',
            'T2',
            'V2',
            'T7',
            'T9',
            'R9',
            'M9',
            'O9',
            'M9',
            'M7',
            'M3',
            'J5',
            'J3',
            'J7',
            'L7',
            'L9',
            'G9',
            'G10',
            'L10',
            'A25',
            'R27',
            'M18',
            'M21',
            'O12',
            'U14',
            'M16'
            ]

# List of columns to send to
outputlist = [
            'E',
            'M',
            'N',
            'G',
            'O',
            'CV',
            'CW',
            'CX',
            'V',
            'AA',
            'AD',
            'AM',
            'AN',
            'AO',
            'AV',
            'CU',
            'AL',
            'BL',
            'BM',
            'BT',
            'BU',
            'BZ',
            'CA',
            'CF',
            'CB',
            'CC',
            'CG',
            'CD',
            'CE',
            'CJ',
            'CH',
            'CI',
            'CM',
            'CQ',
            'CS',
            'CO',
            'CR',
            'CT',
            'CL',
            'CP',
            'BX',
            'BS',
            'BQ',
            'BP',
            'BN',
            'BO',
            'H',
            'CZ',
            'J',
            'I',
            'DA',
            'F',
            'B',
            'A',
            'BK',
            'AK',
            'AI',
            'AJ',
            'AH',
            'AG',
            'BH',
            'P',
            'CY',
            'DB',
            'Z',
            'Q',
            'AF',
            'AB',
            'AE',
            'AC',
            'BY',
            'CN',
            'DD',
            'BR',
            'AU',
            'BG',
            'DC'
            ]

# Input row to start input at
row = input("Input next blank row number? ")

# Get sheet names store number of sheets
sheet_names = wb.sheetnames

# Temporary list for output
content = []
# Iterate through sheets
for sheet in sheet_names:
    print(sheet)
    WS = wb[sheet]
    if "MASTER RAW DATA" in sheet:
        pass

    else:
        # Append the values of the cells
        for cell in celllist:
            print(cell)
            try:
                content.append(WS[cell].value.split('\n')[1])
            except (IndexError, AttributeError):
                content.append('')


# Change to output sheet
WS = wb['MASTER RAW DATA']

# This makes a list of lists in the data vairable
# change last number in second term to match No. of output cells
data = [content[i:i + 77]
        for i in range(0, len(content), 77)]

for data_row in data:
    # Make cell addresses
    adress = []
    for column in outputlist:
        adress.append(column + str(row))

    # Iterate data and adress save to spreadsheet
    for save_cell, save_data in zip(adress, data_row):
        WS[save_cell] = save_data
    row = int(row)
    row += 1

# Save excel workbook
wb.save('Output.xlsx')
print("Finished")
