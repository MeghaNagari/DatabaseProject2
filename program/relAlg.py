import os
from pathlib import Path, PurePath

supplierString = "Suppliers"
productString = "Products"
supplyString = "Supply"
path = ""

def select(rel):
    print("hello")
    if rel == supplierString:
        path = os.getcwd()
        mypath = os.path.dirname(path)
        data_folder = Path(mypath+"/data/Suppliers")
        file_to_open = data_folder / "pageLink"
        fileNames = file_to_open.read_text().splitlines()
        for i in fileNames:
            readContent()

    else:
        print("not found")

select(supplierString)