from chuong1_ham.baitap21.ui.MainWindow21 import Ui_MainWindow


class MainWindow21Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()

