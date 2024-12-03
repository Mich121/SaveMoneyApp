import style, addrevenue, addspending
import subprocess   #restart func
import sqlite3, sys
import matplotlib.pyplot as plt     #generate figure
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

con = sqlite3.connect("money.db") 
cur = con.cursor()

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.homespending = 0.0
        self.busspending = 0.0
        self.clothesspending = 0.0
        self.eatspending = 0.0
        self.phonespending = 0.0
        self.carspending = 0.0
        self.economy = 0.0
        self.salary = 0.0
        self.spend = 0.0
        self.setGeometry(250,150,900,700)
        self.setWindowTitle(' Saving Money App')
        self.setWindowIcon(QIcon('icons/coin.png'))
        self.setFixedSize(self.size())  #block extending of window
        self.UI()
        self.show()

    def UI(self):
        self.toolBar()
        self.tabWidget()
        self.widgets()
        self.layouts()
        self.tabChanged()


    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setStyleSheet("font: 11pt Arial; color: #C26D3C; background-color: #FFFFFF;")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        ######################################################################toolbar buttons
        ###################################generate figure
        self.generateFigure = QAction(QIcon('icons/generatefigure.png'), "GENERATE FIGURE", self)
        self.generateFigure.triggered.connect(self.funcGenerateFigure)
        self.tb.addAction(self.generateFigure)
        self.tb.addSeparator()
        ###################################delete datas (new month)
        self.deleteDatas = QAction(QIcon('icons/trashbin.png'), "NEW MONTH", self)
        self.deleteDatas.triggered.connect(self.funcDeleteDatas)
        self.tb.addAction(self.deleteDatas)
        self.tb.addSeparator()


    def tabWidget(self):
        self.tabs = QTabWidget()
        self.tabs.blockSignals(True)    #first thing to refresh window automatically
        self.tabs.currentChanged.connect(self.tabChanged)   #third thing to refresh window automatically
        self.setCentralWidget(self.tabs)    #thanks that we can see tables
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "Main")
        self.tabs.addTab(self.tab2, "Revenue")
        self.tabs.addTab(self.tab3, "Spendings")
        self.tabs.setFont(QFont("Times", 12))
        self.tabs.setStyleSheet("color: #1F8F36; background-color: #FFFFFF;")

    def widgets(self):
        ############################################tab1 widgets
        #left
        self.homeImg = QLabel()
        homepixmap = QPixmap('icons/home.png')
        self.homeImg.setPixmap(homepixmap)
        self.homeImg.setStyleSheet("background-color:#F28416")
        self.homeSpending = QLabel(f"{self.homespending} PLN")
        self.homeSpending.setFont(QFont("Times", 20))
        self.homeSpending.setStyleSheet("background-color:#F28416; color: white;")

        self.busImg = QLabel()
        buspixmap = QPixmap('icons/bus.png')
        self.busImg.setPixmap(buspixmap)
        self.busImg.setStyleSheet("background-color:#FF0D0D;")
        self.busSpending = QLabel(f"{self.busspending} PLN")
        self.busSpending.setFont(QFont("Times", 20))
        self.busSpending.setStyleSheet("background-color:#FF0D0D; color: white;")

        self.clothesImg = QLabel()
        clothespixmap = QPixmap('icons/clothes.png')
        self.clothesImg.setPixmap(clothespixmap)
        self.clothesImg.setStyleSheet("background-color:#FF00E6")
        self.clothesSpending = QLabel(f"{self.clothesspending} PLN")
        self.clothesSpending.setFont(QFont("Times", 20))
        self.clothesSpending.setStyleSheet("background-color:#FF00E6; color: white;")

        self.eatImg = QLabel()
        eatpixmap = QPixmap('icons/eat.png')
        self.eatImg.setPixmap(eatpixmap)
        self.eatImg.setStyleSheet("background-color:#3BFF5B")
        self.eatSpending = QLabel(f"{self.eatspending} PLN")
        self.eatSpending.setFont(QFont("Times", 20))
        self.eatSpending.setStyleSheet("background-color:#3BFF5B; color: white;")
        
        self.phoneImg = QLabel()
        phonepixmap = QPixmap('icons/phone.png')
        self.phoneImg.setPixmap(phonepixmap)
        self.phoneImg.setStyleSheet("background-color:#412BFF")
        self.phoneSpending = QLabel(f"{self.phonespending} PLN")
        self.phoneSpending.setFont(QFont("Times", 20))
        self.phoneSpending.setStyleSheet("background-color:#412BFF; color: white;")

        self.carImg = QLabel()
        carpixmap = QPixmap('icons/car.png')
        self.carImg.setPixmap(carpixmap)
        self.carImg.setStyleSheet("background-color:#B17DFF")
        self.carSpending = QLabel(f"{self.carspending} PLN")
        self.carSpending.setFont(QFont("Times", 20))
        self.carSpending.setStyleSheet("background-color:#B17DFF; color: white;")

        self.economyImg = QLabel()
        economypixmap = QPixmap('icons/economy.png')
        self.economyImg.setPixmap(economypixmap)
        self.economyImg.setStyleSheet("background-color:#3EE807")
        self.economySpending = QLabel(f"{self.economy} PLN")
        self.economySpending.setFont(QFont("Times", 20))
        self.economySpending.setStyleSheet("background-color:#3EE807; color: white;")
        #right
        self.addRevenue = QPushButton("     Add Revenue")
        self.addRevenue.setIcon(QIcon('icons/good.png'))
        self.addRevenue.setStyleSheet(style.addRevenueButton())
        self.addRevenue.clicked.connect(self.funcAddRevenue)

        self.addSpending = QPushButton("    Add Spending")
        self.addSpending.setIcon(QIcon('icons/wrong.png'))
        self.addSpending.setStyleSheet(style.addSpendingButton())
        self.addSpending.clicked.connect(self.funcAddSpending)

        self.Salary = QLabel(f"Salary: {round(self.salary, 2)} PLN")
        self.Salary.setContentsMargins(50,50,50,50)
        self.Salary.setStyleSheet("font-size: 20pt; border: 2px solid green; background-color: green; color:white;")
        self.Spend = QLabel(f"Spend: {round(self.spend, 2)} PLN")
        self.Spend.setContentsMargins(50,50,50,50)
        self.Spend.setStyleSheet("font-size: 20pt; color: red; border: 2px solid red; background-color: red; color:white;")
        self.Saldo = QLabel(f"Saldo: {round(self.salary - self.spend - self.economy, 2)} PLN")
        self.Saldo.setContentsMargins(50,50,50,50)
        self.Saldo.setStyleSheet("font-size: 20pt; border: 2px solid green; background-color: green; color:white;")
        self.SaldoButton = QPushButton("        Salary figure")
        self.SaldoButton.setIcon(QIcon('icons/currency.png'))
        self.SaldoButton.clicked.connect(self.funcSaldoFigure)
        self.SaldoButton.setStyleSheet(style.GenerateFigureSaldoButton())

        ############################################tab2 widgets
        self.revenueTable = QTableWidget()
        self.revenueTable.setColumnCount(2)
        self.revenueTable.setHorizontalHeaderItem(0, QTableWidgetItem("Revenue amount"))
        self.revenueTable.setHorizontalHeaderItem(1, QTableWidgetItem("Revenue name"))
        self.revenueTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.revenueTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        ############################################tab3 widgets
        ###table
        self.spendingTable = QTableWidget()
        self.spendingTable.setColumnCount(3)
        self.spendingTable.setHorizontalHeaderItem(0, QTableWidgetItem("Spend amount"))
        self.spendingTable.setHorizontalHeaderItem(1, QTableWidgetItem("Spend name"))
        self.spendingTable.setHorizontalHeaderItem(2, QTableWidgetItem("Spend category"))
        self.spendingTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.spendingTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.spendingTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        ###buttons to look for
        self.searchSpendEntry = QLineEdit()
        self.searchSpendEntry.setPlaceholderText("Look for spend...")
        self.lookforSpendBtn = QPushButton("Search")
        self.lookforSpendBtn.setStyleSheet(style.LookForSpendBtn())
        self.lookforSpendBtn.clicked.connect(self.funcLookforSpend)
        

    def layouts(self):
        ############################################tab1
        self.mainLayout = QHBoxLayout()
        self.mainLeftLayout = QFormLayout()
        self.mainRightLayout = QVBoxLayout()

        #thanks group box we can make some stylesheet
        self.leftLayout1 = QHBoxLayout()
        self.leftGB1 = QGroupBox()
        self.leftGB1.setStyleSheet(style.leftGroup1())
        self.leftLayout2 = QHBoxLayout()
        self.leftGB2 = QGroupBox()
        self.leftGB2.setStyleSheet(style.leftGroup2())
        self.leftLayout3 = QHBoxLayout()
        self.leftGB3 = QGroupBox()
        self.leftGB3.setStyleSheet(style.leftGroup3())
        self.leftLayout4 = QHBoxLayout()
        self.leftGB4 = QGroupBox()
        self.leftGB4.setStyleSheet(style.leftGroup4())
        self.leftLayout5 = QHBoxLayout()
        self.leftGB5 = QGroupBox()
        self.leftGB5.setStyleSheet(style.leftGroup5())
        self.leftLayout6 = QHBoxLayout()
        self.leftGB6 = QGroupBox()
        self.leftGB6.setStyleSheet(style.leftGroup6())
        self.leftLayout7 = QHBoxLayout()
        self.leftGB7 = QGroupBox()
        self.leftGB7.setStyleSheet(style.leftGroup7())

        #adding widgets to layouts
        self.leftLayout1.addWidget(self.homeImg)
        self.leftLayout1.addWidget(self.homeSpending)   
        self.leftLayout2.addWidget(self.busImg)
        self.leftLayout2.addWidget(self.busSpending) 
        self.leftLayout3.addWidget(self.clothesImg)
        self.leftLayout3.addWidget(self.clothesSpending)
        self.leftLayout4.addWidget(self.eatImg)
        self.leftLayout4.addWidget(self.eatSpending)
        self.leftLayout5.addWidget(self.phoneImg)
        self.leftLayout5.addWidget(self.phoneSpending)
        self.leftLayout6.addWidget(self.carImg)
        self.leftLayout6.addWidget(self.carSpending)
        self.leftLayout7.addWidget(self.economyImg)
        self.leftLayout7.addWidget(self.economySpending)

        self.leftGB1.setLayout(self.leftLayout1)
        self.leftGB2.setLayout(self.leftLayout2)
        self.leftGB3.setLayout(self.leftLayout3)
        self.leftGB4.setLayout(self.leftLayout4)
        self.leftGB5.setLayout(self.leftLayout5)
        self.leftGB6.setLayout(self.leftLayout6)
        self.leftGB7.setLayout(self.leftLayout7)

        self.mainLeftLayout.addWidget(self.leftGB1)
        self.mainLeftLayout.addWidget(self.leftGB2)
        self.mainLeftLayout.addWidget(self.leftGB3)
        self.mainLeftLayout.addWidget(self.leftGB4)
        self.mainLeftLayout.addWidget(self.leftGB5)
        self.mainLeftLayout.addWidget(self.leftGB6)
        self.mainLeftLayout.addWidget(self.leftGB7)

        self.toprightLayout = QVBoxLayout()
        self.toprightLayout.addWidget(self.Salary)
        self.toprightLayout.addWidget(self.Spend)
        self.toprightLayout.addWidget(self.Saldo)

        self.bottomrightLayout = QVBoxLayout()
        self.bottomrightLayout.addWidget(self.addRevenue)
        self.bottomrightLayout.addWidget(self.addSpending)
        self.bottomrightLayout.addWidget(self.SaldoButton)
   
        self.mainRightLayout.addLayout(self.toprightLayout, 40)
        self.mainRightLayout.addLayout(self.bottomrightLayout, 60)

        self.mainLayout.addLayout(self.mainLeftLayout, 60)
        self.mainLayout.addLayout(self.mainRightLayout, 40)
        self.tab1.setLayout(self.mainLayout)

        ############################################tab2
        self.mainRevenueLayout = QVBoxLayout()
        self.mainRevenueLayout.addWidget(self.revenueTable)
        self.tab2.setLayout(self.mainRevenueLayout)
        ############################################tab3
        self.mainSpendingLayout = QVBoxLayout()
        self.mainSpendingLayout.addWidget(self.spendingTable)
        self.mainSpendingLayout.addWidget(self.searchSpendEntry)
        self.mainSpendingLayout.addWidget(self.lookforSpendBtn)
        self.tab3.setLayout(self.mainSpendingLayout)

        ###
        self.tabs.blockSignals(False)   #second thing to refresh window automatically

    def displayRevenues(self):
        self.revenueTable.setFont(QFont("Arial",11))
        for i in reversed(range(self.revenueTable.rowCount())):
            self.revenueTable.removeRow(i)

        query = cur.execute("SELECT revenueamount, revenuename FROM revenue")   #displaying only this field
        for row_data in query:
            row_number = self.revenueTable.rowCount()
            self.revenueTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.revenueTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.revenueTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    #cannot change value of elements in table

    def displaySpending(self):
        self.spendingTable.setFont(QFont("Arial",11))
        for i in reversed(range(self.spendingTable.rowCount())):
            self.spendingTable.removeRow(i)

        query = cur.execute("SELECT spendingamount, spendingname, spendingcategory FROM spending")  #displaying only this field
        for row_data in query:
            row_number = self.spendingTable.rowCount()
            self.spendingTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.spendingTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        self.spendingTable.setEditTriggers(QAbstractItemView.NoEditTriggers)    #cannot change value of elements in table

    def funcSaldoFigure(self):
        if self.salary != 0.0:
            slices = [self.salary - self.spend, self.spend - self.economy, self.economy]
            parts = ["cash", 'spending', 'economy']  #cash we have ("revenue" or "cash"), cash we spend, cash we save
            colours = ['#1F8F36','#E30000','#3EE807']
            plt.rcParams['font.size'] = 12
            plt.rcParams['figure.facecolor'] = 'gray'
            plt.rcParams['text.color'] = 'white'
            plt.pie(slices, labels = parts, startangle = 90, shadow = True, explode = (0.1, 0.1, 0.1), autopct = '%1.1f%%', colors = colours)
            plt.title("Salary Figure")
            plt.show()
        else:
            QMessageBox.information(self, "Warning!", "To create figure you must have something on account!")


    def funcDeleteDatas(self):
        mbox = QMessageBox.question(self,"Warning","Are you sure to delete data? This option recommend for new month!", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            try:
                query1 = cur.execute("DELETE FROM revenue")
                query2 = cur.execute("DELETE FROM spending")
                query3 = cur.execute("DELETE FROM spendingcategories")
                con.commit()
                QMessageBox.information(self,"Success","Data deleted! You can start with clean slate! I will restart aplication!")
                self.close()
                subprocess.call("python" + " main.py", shell=True)  #restart because after deleting data you cannot see revenues/spends tabels it will crash application
                con.close()
            except:
                QMessageBox.information(self,"Warning","Data have not been deleted!")

    def funcGenerateFigure(self):
        if self.spend > 0:   
            ###option with circle diagram
            #slices = [self.homespending, self.busspending, self.clothesspending, self.eatspending, self.phonespending, self.carspending]
            #parts = ["home", 'public transport', 'clothes', 'eat', 'gadgets', 'car'] 
            #colours = ['#7DFBFF', '#FF0D0D', '#FF00E6', '#3BFF5B', '#412BFF', '#B17DFF']
            #plt.rcParams['font.size'] = 12
            #plt.rcParams['figure.facecolor'] = 'gray'
            #plt.rcParams['text.color'] = 'white'
            #plt.pie(slices, labels = parts, startangle = 90, shadow = True, explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1), autopct = '%1.1f%%', colors = colours)
            #plt.title("Categories Figure")
            #plt.show()

            ###option with bar diagram
            parts = {'home': self.homespending, 'transport': self.busspending, 'fashion': self.clothesspending,'food': self.eatspending, 'gadgets': self.phonespending, 'car': self.carspending}
            colours = ['#7DFBFF', '#FF0D0D', '#FF00E6', '#3BFF5B', '#412BFF', '#B17DFF']
            courses = list(parts.keys())
            values = list(parts.values())
            plt.rcParams['figure.facecolor'] = 'white'
            plt.bar(courses, values, color=colours, width=0.6)
            plt.title("Spends category") 
            plt.show()
        else:
            QMessageBox.information(self,"Warning","You must spend something to create spending categories figure!")



    def getValues(self):
        allRevenues = cur.execute("SELECT SUM(revenueamount) FROM revenue").fetchall()
        if allRevenues[0][0] != None:
            self.salary = allRevenues[0][0]
        self.Salary.setText(f"Salary: {round(self.salary, 2)}")

        allSpending = cur.execute("SELECT SUM(spendingamount) FROM spending").fetchall()
        if allSpending[0][0] != None:
            self.spend = allSpending[0][0]
        self.Spend.setText(f"Spend: {round(self.spend, 2)}")

        self.Saldo.setText(f"Saldo: {round(self.salary - self.spend, 2)}")

        allHomeSpending = cur.execute("SELECT SUM(homespending) FROM spendingcategories").fetchall()
        if allHomeSpending[0][0] != None:
            self.homespending = allHomeSpending[0][0]
        self.homeSpending.setText(f"{round(self.homespending, 2)} PLN")
        allBusSpending = cur.execute("SELECT SUM(busspending) FROM spendingcategories").fetchall()
        if allBusSpending[0][0] != None:
            self.busspending = allBusSpending[0][0]
        self.busSpending.setText(f"{round(self.busspending, 2)} PLN")
        allClothesSpending = cur.execute("SELECT SUM(clothesspending) FROM spendingcategories").fetchall()
        if allClothesSpending[0][0] != None:
            self.clothesspending = allClothesSpending[0][0]
        self.clothesSpending.setText(f"{round(self.clothesspending, 2)} PLN")
        allFoodSpending = cur.execute("SELECT SUM(eatspending) FROM spendingcategories").fetchall()
        if allFoodSpending[0][0] != None:
            self.eatspending = allFoodSpending[0][0]
        self.eatSpending.setText(f"{round(self.eatspending, 2)} PLN")
        allPhoneSpending = cur.execute("SELECT SUM(phonespending) FROM spendingcategories").fetchall()
        if allPhoneSpending[0][0] != None:
            self.phonespending = allPhoneSpending[0][0]
        self.phoneSpending.setText(f"{round(self.phonespending, 2)} PLN")
        allCarSpending = cur.execute("SELECT SUM(carspending) FROM spendingcategories").fetchall()
        if allCarSpending[0][0] != None:
            self.carspending = allCarSpending[0][0]
        self.carSpending.setText(f"{round(self.carspending, 2)} PLN")
        allEconomy = cur.execute("SELECT SUM(economy) FROM spendingcategories").fetchall()
        if allEconomy[0][0] != None:
            self.economy = allEconomy[0][0]
        self.economySpending.setText(f"{round(self.economy, 2)} PLN")

    def funcLookforSpend(self): #looking spend in table 3
        value = self.searchSpendEntry.text()
        if value == "":
            QMessageBox.information(self,"Warning","Search entry is empty!")
        else:
            self.searchSpendEntry.setText("")
            query = ("SELECT spendingamount, spendingname, spendingcategory FROM spending WHERE spendingname LIKE ?")
            results = cur.execute(query, ('%'+value+'%',)).fetchall()

            if results == []:
                QMessageBox.information(self,"Warning","There is not such spend!")
            else:
                for i in reversed(range(self.spendingTable.rowCount())):
                    self.spendingTable.removeRow(i)

                for row_data in results:
                    row_number = self.spendingTable.rowCount()
                    self.spendingTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.spendingTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        

    def tabChanged(self):   #fourth thing to refresh window automatically
        self.getValues()
        self.displayRevenues()
        self.displaySpending()

    def funcAddRevenue(self):
        self.addrevenue = addrevenue.AddRevenue()

    def funcAddSpending(self):
        if (self.salary > 0.0 and self.salary > self.spend):  #we cant add spending without money
            self.addspending = addspending.AddSpending(self.salary, self.spend)
        else:
            QMessageBox.information(self, "Warning!", "You do not have money!")



def main():
    app = QApplication(sys.argv)
    window = Window()
    app.exec_()

if __name__ == '__main__':
    main()