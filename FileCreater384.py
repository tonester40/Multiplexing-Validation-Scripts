import pandas as pd
import datetime
import os

def fileCreater(file1,file2,file3,file4,bs1,bs2,bs3,bs4):
    cols_to_read = ['Sample Barcode', 'Storage Plate Position']
    df1 = pd.read_csv(file1, usecols=cols_to_read)
    df2 = pd.read_csv(file2, usecols=cols_to_read)
    df3 = pd.read_csv(file3, usecols=cols_to_read)
    df4 = pd.read_csv(file4, usecols=cols_to_read)

    checkCols=['s_ssid']
    confirmationCheckDf = pd.read_csv("X:\R_n_D\Multiplex Validation\Confirmation Check CSV\Confirmation Check.csv",usecols = checkCols)

    print(confirmationCheckDf)


    confirmationCheckDf.head()
    print(confirmationCheckDf)

    df1.head()
    df2.head()
    df3.head()
    df4.head()

    rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
    columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
               "20", "21", "22", "23", "24"]
    positions384 = []

    i = 0
    while (i < 16):
        j = 0
        while (j < 24):
            position = rows[i] + columns[j]
            positions384.append(position)
            j = j + 1
        i = i + 1
    #print(*positions384)

    i=1
    index384=[]
    while(i<385):
        index384.append(i)
        i=i+1

    barcodes=[]

    screeningSubString="COVIDSourcePlates"

    if bs1 == 1:
        for h, row in df1.iterrows():
            k=0
            for k, row in confirmationCheckDf.iterrows():
                if df1.iat[h,0] == confirmationCheckDf.iat[k,0]:
                    df1.iat[h,0] = df1.iat[h,0] + "(null)"

    k = 0
    h=0
    if bs2 == 1 :
        for h, row in df2.iterrows():
            k = 0
            for k, row in confirmationCheckDf.iterrows():
                if df2.iat[h,0] == confirmationCheckDf.iat[k,0]:
                    df2.iat[h,0] = df2.iat[h,0] + "(null)"

    k = 0
    h=0
    if bs3 == 1:
        for h, row in df3.iterrows():
            k = 0
            for k, row in confirmationCheckDf.iterrows():
                if df3.iat[h,0] == confirmationCheckDf.iat[k,0]:
                    df3.iat[h,0] = df3.iat[h,0] + "(null)"

    k = 0
    h=0
    if bs4 == 1:
        for h, row in df4.iterrows():
            k = 0
            for k, row in confirmationCheckDf.iterrows():
                if df4.iat[h,0] == confirmationCheckDf.iat[k,0]:
                    df4.iat[h,0] = df4.iat[h,0] + "(null)"

    i=0
    j=0
    rowSwitch=0
    for i in range(len(rows)):
        for j in range(len(columns)):
            if (rowSwitch == 0):
                if (j % 2 == 0):
                    tempBarcode = df1.iloc[int((i/2)*12 + j/2):int(((i/2)*12 + j/2) + 1), 0:1]
                    #rint("I=" + str(i))
                    #print("J=" + str(j))
                    #print('1st File')
                    #print(tempBarcode.iat[0, 0])
                else:
                    tempBarcode = df2.iloc[int((i/2)*12 + (j-1)/2):int(((i/2)*12 + (j-1)/2) + 1), 0:1]
                    #print("I=" + str(i))
                    #print("J=" + str(j))
                    #print('2nd File')
                    #print(tempBarcode.iat[0, 0])
            if (rowSwitch == 1):
                if (j % 2 == 0):
                    tempBarcode = df3.iloc[int(((i-1)/2)*12 + j/2):int(((i-1)/2)*12 + j/2) + 1, 0:1]
                    #print("I=" + str(i))
                    #print("J=" + str(j))
                    #print('3rd File')
                    #print(tempBarcode.iat[0, 0])
                else:
                    tempBarcode = df4.iloc[int(((i-1)/2)*12 + (j-1)/2):int(((i-1)/2)*12 + (j-1)/2) + 1, 0:1]
                    #print("I=" + str(i))
                    #print("J=" + str(j))
                    #print('4th File')
                    #print(tempBarcode.iat[0, 0])
            barcodes.append(tempBarcode.iat[0, 0])
        if (rowSwitch == 1):
            rowSwitch = 0
        else:
            rowSwitch = 1

    print(barcodes)
    data={"Well":index384,"Sample Name":barcodes}
    dfFinal=pd.DataFrame(data)
    print(dfFinal)
    time = str(datetime.datetime.now().date()) + '_' + str(datetime.datetime.now().time()).replace(':', '.')
    os.mkdir("X:\R_n_D\Multiplex Validation\Quant Ready Files\\" + time +"\\")
    dfFinal.to_csv("X:\R_n_D\Multiplex Validation\Quant Ready Files\\" + time +"\\" + time+ ".csv",index=False)


'''
    for r in range(len(rows)):
        i = r + 1
        for j in range(len(columns)):
            if (rowSwitch == 0):
                if (j % 2 == 0):
                    tempBarcode = df1.iloc[(i - 1) * 24 + j:((i - 1) * 24 + j) + 1, 0:1]
                    print("I=" + str(i))
                    print("J=" + str(j))
                    print(tempBarcode.iat[0, 0])
                else:
                    tempBarcode = df2.iloc[(i - 1) * 24 + j:((i - 1) * 24 + j) + 1, 0:1]
                    print("I=" + str(i))
                    print("J=" + str(j))
                    print(tempBarcode.iat[0, 0])
            if (rowSwitch == 1):
                if (j % 2 == 0):
                    tempBarcode = df3.iloc[(i - 1) * 24 + j:((i - 1) * 24 + j) + 1, 0:1]
                    print("I=" + str(i))
                    print("J=" + str(j))
                    print(tempBarcode.iat[0, 0])
                else:
                    tempBarcode = df4.iloc[(i - 1) * 24 + j:((i - 1) * 24 + j) + 1, 0:1]
                    print("I=" + str(i))
                    print("J=" + str(j))
                    print(tempBarcode.iat[0, 0])
            barcodes.append(tempBarcode.iat[0, 0])
        if (rowSwitch == 1):
            rowSwitch = 0
        else:
            rowSwitch = 1
        '''
'''
    while(i<16):
        i=i+1
        while(j<24):
           if (rowSwitch == 0):
               if (j % 2 == 0) :
                   tempBarcode = df1.iloc[(i-1)*24+j:((i-1)*24+j) + 1, 0:1]
                   print("I="+str(i))
                   print("J="+str(j))
                   print(tempBarcode.iat[0,0])
               else:
                   tempBarcode = df2.iloc[(i-1)*24+j:((i-1)*24+j) + 1, 0:1]
                   print("I=" + str(i))
                   print("J=" + str(j))
                   print(tempBarcode.iat[0,0])
           if (rowSwitch == 1):
               if (j % 2 == 0):
                   tempBarcode = df3.iloc[(i-1)*24+j:((i-1)*24+j) + 1, 0:1]
                   print("I=" + str(i))
                   print("J=" + str(j))
                   print(tempBarcode.iat[0,0])
               else:
                   tempBarcode = df4.iloc[(i-1)*24+j:((i-1)*24+j) + 1, 0:1]
                   print("I=" + str(i))
                   print("J=" + str(j))
                   print(tempBarcode.iat[0,0])
           barcodes.append(tempBarcode.iat[0, 0])
           j=j+1
        if(rowSwitch == 1):
           rowSwitch=0
        else:
           rowSwitch=1
'''