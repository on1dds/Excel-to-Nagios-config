# Excel-to-Nagios-config
Nagios core configurations quickly become huge. It is impossible to keep an overview of every configuration. 
Using `xls2nag.py` you can keep your entire configuration in a single excel file.

The only object type you can't convert to excel is the `timeperiod` object since the directives are not consistent enought to convert to excel 

## xls2nag.py
`xls2nag.py` opens the excel and generates a new config file per sheet, using the name of the sheet as the name of the config file

every row in the excel defines an entire object as described in the [nagios definition pages](https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/objectdefinitions.html)

