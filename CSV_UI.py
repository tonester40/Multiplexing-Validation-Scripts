# source: https://www.daniweb.com/programming/software-development/code/452624/get-multiple-file-names-pyqt-pyside

# imports
from PyQt5.QtWidgets import QApplication, QFileDialog
def ui():
    app = QApplication([])
    # ----- start your widget test code ----
    caption = 'Open file'
    # use current/working directory
    directory = 'X:/COVID19/COVIDSourcePlates/'
    filter_mask = "CSV files (*.csv)"
    filenames = QFileDialog.getOpenFileNames(None,
    caption, directory, filter_mask)[0]
    print(filenames)  # test
    app.processEvents()
    return filenames
