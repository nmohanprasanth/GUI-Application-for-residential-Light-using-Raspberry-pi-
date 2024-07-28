Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... from PyQt5.QtCore import pyqtSlot
... from PyQt5.QtWidgets import QApplication, QDialog
... from PyQt5.uic import loadUi
... import RPi.GPIO as gpio
... 
... 
... load1 = 26
... load2 = 6
... load3 = 13
... load4 = 21
... 
... gpio.setmode(gpio.BCM)
... gpio.setwarnings(False)
... 
... gpio.setup(load1, gpio.OUT)
... gpio.setup(load2, gpio.OUT)
... gpio.setup(load3, gpio.OUT)
... gpio.setup(load4, gpio.OUT)
... 
... class New(QDialog):
...     def __init__(self):
...         super(New, self).__init__()
...         loadUi('desingn4.ui', self)  
...         self.setWindowTitle('New HMI System')
... 
...         if not hasattr(self, 'load_1'):
...             print("Error: 'load_1' button not found in the UI file")
...         if not hasattr(self, 'label'):
...             print("Error: 'label' not found in the UI file")
... 
...        
...         if hasattr(self, 'load_1'):
...             self.load_1.clicked.connect(self.load1)
...         if hasattr(self, 'load_2'):
...             self.load_2.clicked.connect(self.load2)
...         if hasattr(self, 'load_3'):
            self.load_3.clicked.connect(self.load3)
        if hasattr(self, 'load_4'):
            self.load_4.clicked.connect(self.load4)

    @pyqtSlot()
    def load1(self):
        if gpio.input(load1):
            gpio.output(load1, gpio.LOW)
            self.label.setText('Load1 OFF')
        else:
            gpio.output(load1, gpio.HIGH)
            self.label.setText('Load1 ON')

    @pyqtSlot()
    def load2(self):
        if gpio.input(load2):
            gpio.output(load2, gpio.LOW)
            self.label_2.setText('Load2 OFF')
        else:
            gpio.output(load2, gpio.HIGH)
            self.label_2.setText('Load2 ON')

    @pyqtSlot()
    def load3(self):
        if gpio.input(load3):
            gpio.output(load3, gpio.LOW)
            self.label_3.setText('Load3 OFF')
        else:
            gpio.output(load3, gpio.HIGH)
            self.label_3.setText('Load3 ON')

    @pyqtSlot()
    def load4(self):
        if gpio.input(load4):
            gpio.output(load4, gpio.LOW)
            self.label_4.setText('Load4 OFF')
        else:
            gpio.output(load4, gpio.HIGH)
            self.label_4.setText('Load4 ON')

    def closeEvent(self, event):
        gpio.cleanup()  
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = New()
    widget.show()
