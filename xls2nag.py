#!/usr/bin/env python
#################################################################
## Author: Joachim Elen
## Date: 2022-06-25
## 
## Purpose: Convert Excel file to Nagios Core config files
## License: GNU GPLv2
#################################################################
import sys
import xlrd
import time

def align24(line):
    count=0
    line+='\t'
    for c in line:
        count+=1
        if c=='\t':
            count+=3
    while count<=23:
        line+='\t'
        count+=4
    return line

fname = sys.argv[1:][0]

with xlrd.open_workbook(fname) as wb:
    sheet_names = wb.sheet_names()
    for sheet_name in sheet_names:
        with open(sheet_name + ".cfg","w") as f:
            f.write ("#######################################################\n")
            f.write ("#  Nagios configuration file\n")
            f.write ("#  Generated from: " + fname + ", tab " + sheet_name + "\n")
            f.write (time.strftime("#  by xls2nag.py on %Y-%m-%d %H:%M")+ "\n")
            f.write ("#######################################################\n\n")

            sheet = wb.sheet_by_name(sheet_name)
            header = sheet.row(0)
            for row_index in range(1, sheet.nrows):
                col  = sheet.row(row_index)
                if col.count > 1:
                    if len((str(col[0].value))) > 0 and (str(col[0].value))[:1] != "#":
                        f.write ("# " + str(col[0].value) + " " + str(col[1].value) + "\n")
                        #if str(col[0].value) == "service":
                        #    f.write ("\t")
                        f.write ("define " + str(col[0].value) + " {\n")
                        for i in range(1,len(header)):
                            s = header[i].value
                            if len(str(col[i].value)) > 0:
                                #if str(col[0].value) == "service":
                                #    s = "\t" + s
                                f.write("\t" + align24(s) + str(col[i].value) + "\n")
                        #if str(col[0].value) == "service":
                        #    f.write("\t")
                        f.write("}\n\n")
                    else:
                        if str(col[0].value)[:1] == "#" and len(str(col[1].value)) < 1:
                            f.write ("# ----------------------------\n")
                            f.write (str(col[0].value)+ '\n')
                            f.write ("# ----------------------------\n")
                            f.write ("\n")
            f.close()

