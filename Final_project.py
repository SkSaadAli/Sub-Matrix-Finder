#All important imports for the program to be fully functional
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox,QVBoxLayout,QLabel,QDialog,QFrame
from PyQt5.QtCore import QRect

import random

# global varialbes number and tardimension stores the target dimension and number of sub matrices equal to the target Sum given

global number
tar_dimension=[]

#com_sub stores the submatrices in string then return to get printed in qtmain window

def com_sub(index,mat):
    sub_final='<html><head/><body><p align=\"center\" style=font-size:15px;>'

    for i in index:
        sub_final+=print_sub(i[0], i[1], mat)
        sub_final+='<br>'

    sub_final += '</span></p></body></html>'

    return sub_final

#print_sub get called by com_sub to constantly provides next rows of the sub matrices

def print_sub(i,j,mat):
    all_sub='['
    for c in range(tar_dimension[0]):

        for r in range(tar_dimension[1]):
            if all_sub[len(all_sub)-1]=='>':
                all_sub+='['
            if r<tar_dimension[1]-1:
                all_sub+= f'{mat[i + c][j + r]},'
            else:
                all_sub += f'{mat[i + c][j + r]}]<br>'
    all_sub+='\n'
    return all_sub

#printer function returns the base matrix stored in string

def printer(mat):
    final='<html><head/><body><p align=\"center\" style=font-size:15px;>'
    for i in mat:
        final += f'{i}<br>'

    final+='</span></p></body></html>'
    return final

#sub is the main function that counts how many submatrices are there with target sum count is stored in global variable
#number that reset after each print
#along with the indexes of the start point of the sub matrices

def sub(string_sub,sum_sub,mat):
    try:
        num = 0
        indexes = []
        clear=int(sum_sub)
        string_sub.replace(" ", "")
        n = (string_sub.split("x"))
        global tar_dimension
        tar_dimension = [int(x) for x in n]

        for i in range(len(mat) - tar_dimension[0] + 1):

            for j in range(len(mat[0]) - tar_dimension[1] + 1):
                sub = 0

                for r in range(tar_dimension[1]):

                    for c in range(tar_dimension[0]):
                        sub += mat[i + c][j + r]
                # print(sub)
                if sub == clear:
                    indexes.append([i, j])

                    num += 1
        global number
        number=num
        return indexes
    except:
        return None

#base takes the input from application user to determine the dimension of the random base matrix

def base(string):
    try:
        string.replace(" ", "")
        b = (string.split("x"))
        m = [int(x) for x in b]

        mat = []
        for i in range(m[0]):
            temp = []
            for j in range(m[1]):
                temp.append(random.randint(0, 9))
            mat.append(temp)
        return mat
    except:
        return None

#class ui_mainwindow does all the gui work and placement in it

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("Minor Project: ")
        MainWindow.resize(847, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(640, 160, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 100, 261, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(575, 220, 311, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(640, 270, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(630, 330, 301, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(640, 390, 131, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 211, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 200,200 ))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 90, 331, 51))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 530, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(550, 500, 301, 20))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(405, 210, 200, 400))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 10, 651, 81))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(70, 530, 261, 101))
        self.label_10.setObjectName("label_7")
        self.label_10.setStyleSheet("border:0.5px solid black;")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(140, 610, 71, 41))
        self.label_11.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.lock=0
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# click function is really important at it holds the flow control of the whole program
#avoiding the errors to make gui fully functional

    def click(self):
        global number
        if self.lineEdit.text()!='':
            if self.lock==0:

                self.mat=base(self.lineEdit.text())
                if self.mat==None:
                    dlg = CustomDialogWrongdimbase()
                    dlg.exec_()
                else:
                    self.lock = 1
                    self.label_5.setText(printer(self.mat))

                    if self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '':
                        self.sub_index = sub(self.lineEdit_2.text(), self.lineEdit_3.text(), self.mat)
                        if self.sub_index!=None:
                            if self.sub_index != []:
                                self.submat = com_sub(self.sub_index, self.mat)
                                self.label_7.setText(self.submat)


                                self.label_11.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">{number}</span></p></body></html>')
                                number=0
                                # print(self.submat)
                                self.update()
                            else:
                                dlg=CustomDialogNotFound()
                                dlg.exec_()
                        else:
                            dlg=CustomDialogWrongdimsub()
                            dlg.exec_()
                    else:
                        dlg = CustomDialogNoSub()
                        dlg.exec_()
                        self.label_7.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N/A</span></p></body></html>')
                        self.label_11.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N/A</span></p></body></html>')

                        number=0
                        self.update()
            else:
                self.lock = 1
                self.label_5.setText(printer(self.mat))
                if self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '':
                    self.sub_index = sub(self.lineEdit_2.text(), self.lineEdit_3.text(), self.mat)
                    if self.sub_index != None:
                        if self.sub_index != []:
                            self.submat = com_sub(self.sub_index, self.mat)
                            self.label_7.setText(self.submat)


                            self.label_11.setText(f'<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">{number}</span></p></body></html>')
                            number = 0
                            self.update()
                        else:
                            dlg = CustomDialogNotFound()
                            dlg.exec_()
                            self.label_7.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N/A</span></p></body></html>')
                            self.label_11.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N/A</span></p></body></html>')

                            number = 0
                            self.update()
                    else:
                        dlg = CustomDialogWrongdimsub()
                        dlg.exec_()
                else:
                    dlg = CustomDialogNoSub()
                    dlg.exec_()
                    self.label_7.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N/A</span></p></body></html>')
                    self.label_11.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N/A</span></p></body></html>')

                    number = 0
                    self.update()
        else:
            dlg=CustomDialog()
            dlg.exec_()
        self.update()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Minor Project : "))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Enter the dimension of the base matrix:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Enter the dimension of the Sub-Matrix:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Enter the Target Sum:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Main Base Matrix With given dimension:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">All sub matrices with the total</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\"> sum equal to the target sum:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N/A</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Click it"))
        self.label_10.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">No.of Submatrices with </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">the total sum equal to </span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">target Sum:</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_11.setText(_translate("MainWindow","<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">N/A</span></p></body></html>"))
        self.pushButton.clicked.connect(self.click)
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Click below when all arguments are inputted:</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#000000;\">Application to get Subset Matrices with Target Sum:</span></p></body></html>"))
        self.update()
    def update(self):
        self.label.adjustSize()
        self.label_2.adjustSize()
        self.label_3.adjustSize()
        self.label_4.adjustSize()
        self.label_5.adjustSize()
        self.label_6.adjustSize()
        self.label_7.adjustSize()
        self.label_8.adjustSize()
        self.label_9.adjustSize()
        self.label_10.adjustSize()
        self.label_11.adjustSize()

# below are some cutom dialog boxes that get triggered with something wrong happens

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Error!!!")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("No Base Matrix!")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class CustomDialogWrongdimbase(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Error!!!")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Wrong dimension inputted format for base: (row x coloumn)!")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class CustomDialogWrongdimsub(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Error!!!")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Wrong dimension inputted format for submatrix: (row x coloumn)!")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class CustomDialogNoSub(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Error!!!")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Please Enter both target sum and dimension!")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class CustomDialogNotFound(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("search complete:")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("No sub matrix is found with given sum and dimension")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

#this is the main function the executes the main window ui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
