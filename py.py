#1
import sqlite3

shopping_cart = [["pear",1], ["orange", 1], ["apple",2], ["tomatoes",2], ["yoghurt",3]]

def reverse_cart(cart):
    reversed=[]
    for i in range(len(cart)-1,-1,-1):
        reversed.append(cart[i])
    
    return reversed

conn=sqlite3.connect("cart")
cursor=conn.cursor()

cursor.execute("CREATE TABLE SHOPPINGCART (PRODUCT TEXT, QUANTITY INTEGER)")
new_cart=reverse_cart(shopping_cart)
for item in new_cart:
    product,quantity=item
    cursor.execute("INSERT INTO SHOPPINGCART (PRODUCT, QUANTITY) VALUES (?,?)", (product,quantity))

conn.commit()
conn.close()

#2
menu = {"cola": 1.99, "fries": 2.99, "burger": 3.99, "shake": 3.5, "soda": 2.4, "chicken strips": 3.9}

def get_order(sia):
    print("Menu: ")
    for items in sia.keys():
        print(items)
    order=[]
    while True:
        food=input("What can i get for you? ").strip().lower()
        if food not in sia.keys():
            print("We don't serve that. ")
        else:
            quantity=int(input("How many " + food + "s would you like? ").strip())
            order.append([food,quantity])
            next=input("Anything else? yes/no ").strip().lower()
            if next not in ["yes","no"]:
                print("Please input yes or no")
            elif next=="no":
                return order

print(get_order(menu))

#3
import numpy as np

#1var

# arr1 = np.random.randint(1, 101, 50)
# arr2 = np.random.randint(1, 101, 50)

# sum = arr1+arr2
# prod = arr1*arr2
# div = arr1/arr2
# diff = arr1-arr2

# comb = np.concatenate((arr1,arr2))
# reshaped = comb.reshape(5,20)
# print(reshaped)

#2var

array1 = np.random.randint(1,101,50)
array2 = np.random.randint(1,101,50)

combined = np.concat((array1,array2))

divbytwo = combined[combined % 2 == 0]
divbyfive = combined[combined % 5 == 0]
 

print(divbytwo,divbyfive)

#4

from pymongo import MongoClient
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

client = MongoClient("mongodb://localhost:27017")
database = client["menu"]
collection = database["menu_items"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 509)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.product_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.product_label.setGeometry(QtCore.QRect(30, 40, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.product_label.setFont(font)
        self.product_label.setObjectName("product_label")
        self.price_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.price_label.setGeometry(QtCore.QRect(30, 80, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_label.setFont(font)
        self.price_label.setObjectName("price_label")
        self.increase_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.increase_button.setGeometry(QtCore.QRect(80, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.increase_button.setFont(font)
        self.increase_button.setObjectName("increase_button")
        self.change_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.change_button.setGeometry(QtCore.QRect(290, 190, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.change_button.setFont(font)
        self.change_button.setObjectName("change_button")
        self.display_widget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.display_widget.setGeometry(QtCore.QRect(65, 270, 391, 192))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.display_widget.setFont(font)
        self.display_widget.setObjectName("display_widget")
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(150, 40, 256, 81))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.product_input = QtWidgets.QTextEdit(parent=self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.product_input.setFont(font)
        self.product_input.setObjectName("product_input")
        self.product_input_2 = QtWidgets.QTextEdit(parent=self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.product_input_2.setFont(font)
        self.product_input_2.setObjectName("product_input_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.initialize_database()
        self.display()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.increase_button.clicked.connect(self.increase)
        self.change_button.clicked.connect(self.change_price)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.product_label.setText(_translate("MainWindow", "Product:"))
        self.price_label.setText(_translate("MainWindow", "Price:"))
        self.increase_button.setText(_translate("MainWindow", "Increase"))
        self.change_button.setText(_translate("MainWindow", "Change"))

    def initialize_database(self):
        if collection.count_documents({}) == 0:
            menu = {"soda": 5.2, "wine": 5.6, "burger": 1.99, "tea": 2.5, "milk": 2.4, "chicken": 4.1}
            for product, price in menu.items():
                collection.insert_one({"product": product, "price": price})
    
    def increase(self):
       prod = self.product_input.toPlainText().lower()
       item = collection.find_one({"product": prod})
       if item:
           new_price = item['price'] + 1
           collection.update_one({"product": prod}, {"$set": {"price": new_price}})
           self.display()
           QMessageBox.information(self.centralwidget,"Success", f"Price of {prod} increased to {new_price:.2f}")
       else:
            QMessageBox.warning(self.centralwidget,"Error", "Product not found. Please enter a valid product")

    def change_price(self):
       prod = self.product_input.toPlainText().lower()
       price_text = self.product_input_2.toPlainText()

       if not prod:
        QMessageBox.warning(self.centralwidget,"Error", "Please enter a product name")
        return

       if not price_text:
        QMessageBox.warning(self.centralwidget,"Error", "Please enter a price")
        return

       try:
           new_price = float(price_text)
           if new_price < 0:
               raise ValueError
        
           item = collection.find_one({"product": prod})
           if item:
               collection.update_one({"product": prod}, {"$set": {"price": new_price}})
               message = f"Price of {prod} changed to {new_price:.2f}"
           else:
               collection.insert_one({"product": prod, "price": new_price})
               message = f"New product {prod} added with price {new_price:.2f}"
        
           self.display()
           QMessageBox.information(self.centralwidget,"Success", message)
       except ValueError as e:
           QMessageBox.warning(self.centralwidget,"Error", e)

    def display(self):
        self.display_widget.clear()
        for item in collection.find():
            self.display_widget.addItem(f"{item['product']}: ${item['price']:.2f}")
  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())