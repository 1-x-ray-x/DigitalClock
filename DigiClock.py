import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# timer
from PyQt5.QtCore import QTimer, QTime, Qt

# to work with specific font
from PyQt5.QtGui import QFont, QFontDatabase

# inheriting from QWidget instead of QMainWindow
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        
        #label that displays time
        self.time_label = QLabel(self)
        
        # adding timer to clock
        self.timer = QTimer(self)
        
        #initializes UI
        self.initUI()
        
    def initUI(self):
        # design clock
        # window title
        self.setWindowTitle("Digital Clock")
        
        # geometry
        self.setGeometry(600, 400, 300, 100)
        
        # layout manager (layouts widget vertically)
        vbox = QVBoxLayout()
        
        # adds time label to vbox
        vbox.addWidget(self.time_label)
        
        # set layout as vbox
        self.setLayout(vbox)
        
        # centre align
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # font
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(111, 100%, 50%)")
        
        self.setStyleSheet("background-color: black;")
        
        # custom font (adds to database)
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        # adds the font_id as a font family in this file
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        # set the font
        myfont = QFont(font_family, 150)
        self.time_label.setFont(myfont)
        
        # update time every second, times out for every 1000ms
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # update time
        self.update_time()
        
    def update_time(self):
        # current time from class qtime, AP means AM/PM
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        
        # to set the text as the current time variable
        self.time_label.setText(current_time)

if __name__ == '__main__':
    # main
    # argv = arguments
    app = QApplication(sys.argv)
    # clock object
    clock = DigitalClock()
    #show the clock
    clock.show()
    # show until exit (executes the app until exit)
    sys.exit(app.exec_())