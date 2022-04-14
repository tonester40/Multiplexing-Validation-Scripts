from CSV_UI import ui
from Sort_CSV import sort_csv
from FileCreater384 import fileCreater
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   file1=ui()
   file2=ui()
   file3 =ui()
   file4 =ui()

   screeningSubString = "COVIDSourcePlates"
   boolScreening1=0
   boolScreening2 = 0
   boolScreening3 = 0
   boolScreening4 = 0


   if screeningSubString in file1[0]:
      boolScreening1=1
   if screeningSubString in file2[0]:
      boolScreening2=1
   if screeningSubString in file3[0]:
      boolScreening3=1
   if screeningSubString in file4[0]:
      boolScreening4=1

   newFile1=sort_csv(file1[0])
   newFile2=sort_csv(file2[0])
   newFile3 = sort_csv(file3[0])
   newFile4 = sort_csv(file4[0])

   fileCreater(newFile1,newFile2,newFile3,newFile4,boolScreening1,boolScreening2,boolScreening3,boolScreening4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
