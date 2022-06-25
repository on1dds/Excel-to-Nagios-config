# Excel-to-Nagios-config
Nagios core configurations quickly become huge. It is impossible to keep an overview of every configuration. 
Using `xls2nag.py` you can keep your entire configuration in a single excel file.

The only object type you can't convert to excel is the `timeperiod` object since the directives are not consistent enought to convert to excel 

## xls2nag.py
`xls2nag.py` opens the excel and generates a new config file per sheet, using the name of the sheet as the name of the config file

every row in the excel defines an entire object as described in the [nagios definition pages](https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/objectdefinitions.html)

An example of how commands are configured in excel. This sheet is called `commands` in excel looks like this:
![alt text][excel-cmd]

`xls2nag.py` will generate the config file `commands.cfg` from this sheet and will look like this:
![alt text][nagios-cmd-cfg]

[excel-cmd]: https://github.com/on1dds/Excel-to-Nagios-config/raw/main/screenshots/excel-cmd.png "excel cmd"

[nagios-cmd-cfg]: https://github.com/on1dds/Excel-to-Nagios-config/raw/main/screenshots/nagios-cmd-cfg.png "nagios command configuration"
