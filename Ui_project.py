# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Han Shaochen\Desktop\sjtu\byy_prj\byy_code\ui\project.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# modi
import sys
from PyQt5.QtCore import QCoreApplication
import main


class Ui_MainWindow(object):
    inputFilepath = None  # 输入路径
    outputFilepath = None  # 输出路径
    doc_result = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(881, 447)
        MainWindow.setMinimumSize(QtCore.QSize(881, 447))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.chooseFile = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseFile.sizePolicy().hasHeightForWidth())
        self.chooseFile.setSizePolicy(sizePolicy)
        self.chooseFile.setObjectName("chooseFile")
        self.gridLayout.addWidget(self.chooseFile, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.startCheck = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startCheck.sizePolicy().hasHeightForWidth())
        self.startCheck.setSizePolicy(sizePolicy)
        self.startCheck.setObjectName("startCheck")
        self.gridLayout.addWidget(self.startCheck, 4, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 3, 11, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 2)
        self.startOut = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startOut.sizePolicy().hasHeightForWidth())
        self.startOut.setSizePolicy(sizePolicy)
        self.startOut.setObjectName("startOut")
        self.gridLayout.addWidget(self.startOut, 8, 1, 1, 1)
        self.chooseFile_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseFile_2.sizePolicy().hasHeightForWidth())
        self.chooseFile_2.setSizePolicy(sizePolicy)
        self.chooseFile_2.setObjectName("chooseFile_2")
        self.gridLayout.addWidget(self.chooseFile_2, 7, 0, 1, 1)
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quit.sizePolicy().hasHeightForWidth())
        self.quit.setSizePolicy(sizePolicy)
        self.quit.setObjectName("quit")
        self.gridLayout.addWidget(self.quit, 10, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.chooseType = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseType.sizePolicy().hasHeightForWidth())
        self.chooseType.setSizePolicy(sizePolicy)
        self.chooseType.setObjectName("chooseType")
        self.chooseType.addItem("")
        self.chooseType.addItem("")
        self.chooseType.addItem("")
        self.gridLayout.addWidget(self.chooseType, 3, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 9, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # modi
        self.chooseFile.clicked.connect(self.chooseFile_reactor)
        self.chooseFile_2.clicked.connect(self.chooseFile_2_reactor)
        self.startCheck.clicked.connect(self.startCheck_reactor)
        self.startOut.clicked.connect(self.startOut_reactor)
        self.quit.clicked.connect(QCoreApplication.quit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文档审查"))
        self.chooseFile.setText(_translate("MainWindow", "选择文件..."))
        self.label_3.setText(_translate("MainWindow", "导出论证报告："))
        self.label_2.setText(_translate("MainWindow", "待审查文档类型："))
        self.startCheck.setText(_translate("MainWindow", "审查"))
        self.startOut.setText(_translate("MainWindow", "导出"))
        self.chooseFile_2.setText(_translate("MainWindow", "选择路径..."))
        self.quit.setText(_translate("MainWindow", "退出"))
        self.label.setText(_translate("MainWindow", "待审查文档："))
        self.chooseType.setItemText(0, _translate("MainWindow", "选择..."))
        self.chooseType.setItemText(1, _translate("MainWindow", "跨越施工类"))
        self.chooseType.setItemText(2, _translate("MainWindow", "其他"))

    # modi
    def chooseFile_reactor(self, Filepath):
        directory, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                                                             "选择待审查文件输入路径", "./",
                                                             "Doc文件 (*.doc;*.docx);;所有文件 (*)")
        self.inputFilepath = directory
        if len(directory) > 20:
            directory = "..." + directory[len(directory) - 17:len(directory)]
        self.chooseFile.setText(directory)

    def startCheck_reactor(self):
        # todo: 添加运行
        if self.inputFilepath is not None:
            self.textBrowser.append("开始审查文件" + self.inputFilepath + ", 审查类型为" + self.chooseType.currentText())
            nok, nouk, self.doc_result = main.check(self.inputFilepath)
            self.textBrowser.append(nok)
            self.textBrowser.append(nouk)
            if len(self.doc_result) > 0:
                for each in self.doc_result:
                    self.textBrowser.append(each)
            else:
                self.textBrowser.append("No unfound keys!")
        else:
            self.textBrowser.append("待审查文件路径未找到！")

    def chooseFile_2_reactor(self, Filepath):
        directory, _ = QtWidgets.QFileDialog.getOpenFileName(None,
                                                             "选择已审查文件输出路径", "./",
                                                             "所有文件 (*)")
        self.outputFilepath = directory
        if len(directory) > 20:
            directory = "..." + directory[len(directory) - 17:len(directory)]
        self.chooseFile_2.setText(directory)

    def startOut_reactor(self):
        if self.outputFilepath is not None:
            if self.doc_result is not None:
                self.textBrowser.append("审查文件输出到: " + self.outputFilepath)
                print(self.outputFilepath)
                main.write_paragraph(self.outputFilepath, self.doc_result)
            else:
                self.textBrowser.append("请先进行文件审查！")
        else:
            self.textBrowser.append("输出路径未找到！")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(mainWindow)

    mainWindow.show()

    sys.exit(app.exec_())
