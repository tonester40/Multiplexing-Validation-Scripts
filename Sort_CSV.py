import pandas as pd
import datetime
from natsort import natsort_keygen
import os

# assign dataset
def sort_csv(filePath):
    csvData = pd.read_csv(filePath)
    new_row={"Sample Barcode":'Empty','Storage Plate Position':'G11'}
    csvData=csvData.append(new_row,ignore_index=True)
    #displaying unsorted data frame
    print("\nBefore sorting:")
    print(csvData)
    # sort data frame
    csvData.sort_values(["Storage Plate Position"],
                    axis=0,
                    ascending=[True],
                    inplace=True,
                    key = natsort_keygen()
                    )
    # displaying sorted data frame
    print("\nAfter sorting:")
    print(csvData)
    time=str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')
    newFolder = "X:\R_n_D\Multiplex Validation\Sorted Files\\" + time
    newPath = "X:\R_n_D\Multiplex Validation\Sorted Files\\" + time + "\\" + time + ".csv"
    print(newPath)
    os.mkdir(newFolder)
    csvData.to_csv(newPath)
    return(newPath)