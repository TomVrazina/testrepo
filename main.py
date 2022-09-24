
import sys
from PySide2.QtCore import QDateTime, QTimer, SIGNAL, QTime
from PySide2.QtGui import QGuiApplication
from PySide2.QtWidgets import QApplication, QWidget, QLCDNumber, QDesktopWidget




class myTimer(QWidget):
    # Our main window class for Timer
    def __init__(self, parent = None):
        super(myTimer, self).__init__(parent)
        self.initGUI()
        
    def initGUI(self):
        self.setWindowTitle("My digital clock")
        timer = QTimer(self) 
        
        self.connect(timer, SIGNAL("timeout()"), self.updtTime) # Prvni je objekt QTimer(self) druhý je SIGNAL (byte), a treti je objekt

        
        self.myTimeDisplay = QLCDNumber(self) # digitalni nastaveni
        self.myTimeDisplay.setSegmentStyle(QLCDNumber.Filled) # Barva čísel
        self.myTimeDisplay.setDigitCount(8) # počet čísel, které jsou zobrazeny default 5
        self.myTimeDisplay.resize(500, 150) # změna počáteční velikosti okna
        

        self.updtTime() # To display Current Time
        self.center()
        timer.start(1000)
        

        #self.show()

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QGuiApplication.primaryScreen().availableGeometry().center() #screens()[0] - pro jeden monitor
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def updtTime(self):
        #Function to update Time
        currentTime = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.myTimeDisplay.display(currentTime)

    # Main Function


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        myWindow = myTimer()
        myWindow.show()
        app.exec_()
        sys.exit(0)
        
    except NameError:
        print("Name Error:", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])

