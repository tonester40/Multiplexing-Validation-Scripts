import pandas as pd
import datetime
from natsort import natsort_keygen
import os

# assign dataset
#csvData = pd.read_csv('X:\R_n_D\Multiplex Validation\COVIDSampleTransfer_DS36207_20220315191518.csv')
csvData = pd.read_csv('X:/COVID19/COVIDSourcePlates/DS36194/COVIDSampleTransfer_DS36194_20220315150128.csv')
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
newFolder="X:\R_n_D\Multiplex Validation\\"+time
newPath="X:\R_n_D\Multiplex Validation\\"+time + "\\" +time + ".csv"
print(newPath)
os.mkdir(newFolder)
csvData.to_csv(newPath)