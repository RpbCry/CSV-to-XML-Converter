import tkinter as tk
from tkinter import filedialog
import pandas as pd
import xml.etree.ElementTree as ET
from xml.dom import minidom

def browse_csv_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    csv_file_entry.delete(0, tk.END)
    csv_file_entry.insert(0, file_path)

def browse_export_dir():
    export_dir = filedialog.askdirectory()
    export_dir_entry.delete(0, tk.END)
    export_dir_entry.insert(0, export_dir)

def convert_csv_to_xml():
    input_csv_file = csv_file_entry.get()
    export_directory = export_dir_entry.get()

    if not input_csv_file or not export_directory:
        result_label.config(text="Please select both CSV file and export directory.")
        return

    try:
        df = pd.read_csv(input_csv_file)
        xml_data = df.to_dict(orient='records')
        root = ET.Element("data")
        for item in xml_data:
            record = ET.SubElement(root, "record")
            for key, value in item.items():
                ET.SubElement(record, key).text = str(value)

        xml_string = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
        xml_file_path = f"{export_directory}/data.xml"
        with open(xml_file_path, "w") as xml_file:
            xml_file.write(xml_string)

        result_label.config(text=f"CSV file converted and saved as XML: {xml_file_path}")
    except Exception as e:
        result_label.config(text=f"Error occurred: {str(e)}")

# Create the main GUI window
root = tk.Tk()
root.title("CSV to XML Converter")

# CSV file selection widgets
csv_file_label = tk.Label(root, text="Select CSV File:")
csv_file_label.grid(row=0, column=0, padx=10, pady=5)
csv_file_entry = tk.Entry(root, width=50)
csv_file_entry.grid(row=0, column=1, padx=10, pady=5)
csv_browse_button = tk.Button(root, text="Browse", command=browse_csv_file)
csv_browse_button.grid(row=0, column=2, padx=10, pady=5)

# Export directory selection widgets
export_dir_label = tk.Label(root, text="Select Export Directory:")
export_dir_label.grid(row=1, column=0, padx=10, pady=5)
export_dir_entry = tk.Entry(root, width=50)
export_dir_entry.grid(row=1, column=1, padx=10, pady=5)
export_dir_browse_button = tk.Button(root, text="Browse", command=browse_export_dir)
export_dir_browse_button.grid(row=1, column=2, padx=10, pady=5)

# Conversion button
convert_button = tk.Button(root, text="Convert to XML", command=convert_csv_to_xml)
convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Start the main loop
root.mainloop()
