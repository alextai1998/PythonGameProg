import sys
from PyQt5.QtWidgets import QApplication, QDialog
# --- Import the converted UI
from findReplace import Ui_Form as dlg

# --- Create a QT application
app = QApplication(sys.argv)
# --- Create a Dialog window
window = QDialog()
# --- Create a findReplace dialog (object)
ui = dlg()
# --- Add the findReplace dialog to the main window
ui.setupUi(window)

window.show()
sys.exit(app.exec_())


