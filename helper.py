from PyQt4 import QtGui, uic, QtCore, Qt
import PyQt4
import pandas
import sys
import os

viewBase, viewForm = uic.loadUiType(os.path.join(os.path.dirname(os.path.realpath(__file__)),"view.ui"))


class Helper(viewBase, viewForm):

    def __init__(self, parent = None):
        super(viewBase,self).__init__(parent)
        self.setupUi(self)

    def __version__(self):
        print("0.0.1")

    def View(self, df):
        """
        This is to view a data frame
        :param df: pandas.Dataframe
        :return: Qt object to view the data
        """

        #df = pandas.DataFrame()
        #self.table = QtGui.QTableWidget()
        self.table.setColumnCount(len(df.columns))
        self.table.setRowCount(len(df.index))
        self.sortOrder = {}
        for p in df.columns:
            self.sortOrder[p] = ""
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.table.setItem(i,j, QtGui.QTableWidgetItem(str(df.iloc[i][j])))

        for i in range(len(df.columns)):
            self.table.setHorizontalHeaderItem(i,QtGui.QTableWidgetItem(str(df.columns[i])))
        for i in range(len(df.index)):
            self.table.setVerticalHeaderItem(i,QtGui.QTableWidgetItem(str(df.index[i])))

        # for i in range(len(df.columns)):
        #     self.table.horizontalHeaderItem(i).setText(str(df.columns[i]))


        self.horizHeader = self.table.horizontalHeader()
        self.horizHeader.setSortIndicatorShown(True)
        QtCore.QObject.connect(self.horizHeader, QtCore.SIGNAL("sectionClicked(int)"), self.sortByColumn)

        self.show()

    def sortByColumn(self,p):
        print(self.sortOrder[p])
        if self.sortOrder[p]=="":
            self.horizHeader.setSortIndicator(p, Qt.Qt.DescendingOrder)
            self.table.sortByColumn(p, Qt.Qt.DescendingOrder)
            self.sortOrder[p]="D"
        elif self.sortOrder[p]=="A":
            self.horizHeader.setSortIndicator(p, Qt.Qt.DescendingOrder)
            self.table.sortByColumn(p, Qt.Qt.DescendingOrder)
            self.sortOrder[p]="D"
        elif self.sortOrder[p]=="D":
            self.horizHeader.setSortIndicator(p, Qt.Qt.AscendingOrder)
            self.table.sortByColumn(p, Qt.Qt.AscendingOrder)
            self.sortOrder[p]="A"






def View(df):
    app = QtGui.QApplication(sys.argv)
    app.setStyle("plastique")
    h = Helper()
    h.View(df)
    h.show()
    app.exec_()

