import pandas as pd

def fileCreater():

    rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
    columns = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12","13","14","15","16","17","18","19","20","21","22","23","24"]
    positions384=[]

    i=0
    while (i<16):
        j=0
        while (j<24):
            position=rows[i]+columns[j]
            positions384.append(position)
            j = j + 1
        i = i + 1
    print(*positions384)

    i = 0
    index384 = []
    while (i < 384):
        index384.append(i)
        i = i + 1

        i = 1
        index384 = []
        while (i < 385):
            index384.append(i)
            i = i + 1
        barcodes = []
        i = 0
        while (i < 96):
            j = 0
            while (j < 4):
                if (j == 0):
                    tempBarcode = df1.iloc[i:i + 1, 0:1]
                if (j == 1):
                    tempBarcode = df2.iloc[i:i + 1, 0:1]
                if (j == 2):
                    tempBarcode = df3.iloc[i:i + 1, 0:1]
                if (j == 3):
                    tempBarcode = df4.iloc[i:i + 1, 0:1]
                barcodes.append(tempBarcode.iat[0, 0])
                j = j + 1
            i = i + 1

        print(barcodes)
        data = {"Well": index384, "Well Position": positions384, "Sample Name": barcodes}
        dfFinal = pd.DataFrame(data)
        print(dfFinal)
        dfFinal.to_csv("X:\R_n_D\Multiplex Validation\Quant Ready Files\Test.csv", index=False)

    data = {"Well": index384, "Well Position": positions384}
    dfFinal = pd.DataFrame(data)
    print(dfFinal)


if __name__ == '__main__':
    fileCreater()