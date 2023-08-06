# CSV to XML Converter
The CSV to XML Converter is a Python script that provides a user-friendly GUI (Graphical User Interface) to convert CSV (Comma Separated Values) files into XML (eXtensible Markup Language) format. This script allows users to select the input CSV file and choose an export directory for the generated XML file.

## Features
Easy-to-use graphical interface for selecting files and directories.
Converts CSV data into XML format following a simple structure.
Outputs the resulting XML file in a human-readable and indented format.
Requirements
`Python 3.x`
`pandas library`
`tkinter library`

## Installation
Ensure you have Python 3.x installed on your system.
Install the required libraries by running the following command in your terminal or command prompt:
````
pip install pandas
````

## How to Use
Run the script by executing the Python file `csv_to_xml_converter.py`.
The GUI window will open, providing two options for selecting files and directories.
Click the `Browse` button next to `Select CSV File` and navigate to the desired `CSV` file you want to convert.
Click the `Browse` button next to `Select Export Directory` and choose the directory where you want to save the resulting `XML` file.
Once both the `CSV` file and export directory are selected, click the `Convert to XML` button.
The script will read the `CSV` file, convert its data into `XML` format, and save it as `data.xml` in the chosen export directory.
The result will be displayed in the GUI, indicating the successful conversion and the path to the generated `XML` file.
Example
Suppose you have a CSV file named `data.csv` with the following content:

```CSV
Name,Age,Location
John,30,New York
Alice,25,Los Angeles
Bob,35,Chicago
```
After running the CSV to XML Converter script and selecting `data.csv` as the input file and `C:\Export` as the export directory, the script will generate an `XML` file named `data.xml` in the `C:\Export` directory with the following content:

```xml
<data>
   <record>
      <Name>John</Name>
      <Age>30</Age>
      <Location>New York</Location>
   </record>
   <record>
      <Name>Alice</Name>
      <Age>25</Age>
      <Location>Los Angeles</Location>
   </record>
   <record>
      <Name>Bob</Name>
      <Age>35</Age>
      <Location>Chicago</Location>
   </record>
</data>
```
## License
This project is licensed under the MIT License. Feel free to modify and use it as per your requirements.

## Authors
Rpbcry

## Contributions
Contributions are welcome! If you find any issues or want to add new features, please submit a pull request.

## Feedback and Support
If you have any feedback, suggestions, or need support, please feel free to create an issue in this repository.
