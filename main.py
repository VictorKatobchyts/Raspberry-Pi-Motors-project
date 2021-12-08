import sys
import RPi.GPIO as GPIO
import time
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
try:
 class MainWindow(QMainWindow):
   
  def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("template1.ui", self)
        self.action.triggered.connect(self.exit_action)
        self.pushButton.setAutoRepeat(True)
        self.pushButton.setAutoRepeatInterval(100)
        self.pushButton.clicked.connect(lambda: self.was_clicked_forward())
        self.pushButton_2.setAutoRepeat(True)
        self.pushButton_2.setAutoRepeatInterval(100)
        self.pushButton_2.clicked.connect(lambda: self.was_clicked_backward())
        self.pushButton_3.setAutoRepeat(True)
        self.pushButton_3.setAutoRepeatInterval(100)
        self.pushButton_3.clicked.connect(lambda: self.was_clicked_left())
        self.pushButton_4.setAutoRepeat(True)
        self.pushButton_4.setAutoRepeatInterval(100)
        self.pushButton_4.clicked.connect(lambda: self.was_clicked_right())
    
  def was_clicked_forward(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(29, GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(35, GPIO.OUT, initial = GPIO.LOW)#Dir+
        GPIO.setup(32, GPIO.OUT, initial = GPIO.LOW)#Pull+
        GPIO.output(35, GPIO.HIGH)
        for j in range (1, 200):
         for i in range (1, 9):
          time.sleep(0.0000025)
          GPIO.output(32, GPIO.LOW)
          time.sleep(0.0000025)
          GPIO.output(32, GPIO.HIGH)
     
  def was_clicked_backward(self):
         GPIO.setmode(GPIO.BOARD)
         GPIO.setup(35, GPIO.OUT, initial = GPIO.LOW)#Dir+
         GPIO.setup(32, GPIO.OUT, initial = GPIO.LOW)#Pull+
         for j in range (1, 200):
          for i in range (1, 9):
           time.sleep(0.0000025)
           GPIO.output(32, GPIO.LOW)
           time.sleep(0.0000025)
           GPIO.output(32, GPIO.HIGH)
           
  def was_clicked_left(self):
         GPIO.setmode(GPIO.BOARD)
         GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW)#Dir+
         GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW)#Pull+
         for j in range(1, 200):
          for i in range (1, 9):
           time.sleep(0.0000025)
           GPIO.output(33, GPIO.LOW)
           time.sleep(0.0000025)
           GPIO.output(33, GPIO.HIGH)
         
           
  def was_clicked_right(self):
         GPIO.setmode(GPIO.BOARD)
         GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW)#Dir+
         GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW)#Pull+
         GPIO.output(31, GPIO.HIGH)
         for j in range (1, 200):
          for i in range (1, 9):
           time.sleep(0.0000025)
           GPIO.output(33, GPIO.LOW)
           time.sleep(0.0000025)
           GPIO.output(33, GPIO.HIGH)
         
          
  def exit_action(self):
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(35, GPIO.OUT, initial = GPIO.LOW)#Dir+
   GPIO.setup(32, GPIO.OUT, initial = GPIO.LOW)#Pull+
   
   GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW)#Dir+
   GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW)#Pull+
   self.close()
        
        
 if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    desktop = QtWidgets.QApplication.desktop()
    window.show()
    sys.exit(app.exec_())


# except KeyboardInterrupt:
#  GPIO.output(33, GPIO.LOW)
#  GPIO.output(29, GPIO.LOW)
#  GPIO.output(31, GPIO.LOW)
#  GPIO.output(35, GPIO.LOW)
#  GPIO.output(38, GPIO.LOW)
#  print("Interrupt")
# except:
#     print("Some error")
finally:
    GPIO.cleanup()


    

    #for j in range (1, 1600):
     #for i in range(1,9):
         #impulse()
#     time.sleep(0.0000025)
#     GPIO.output(32, GPIO.LOW)
#     time.sleep(0.0000025)
#     GPIO.output(32, GPIO.HIGH)
#     time.sleep(0.0000025)
#     GPIO.output(32, GPIO.LOW)
#     time.sleep(0.0000025)
#     GPIO.output(32, GPIO.HIGH)
#     time.sleep(0.0000025)
#     GPIO.output(32, GPIO.LOW)
#     time.sleep(0.0000025)
#     GPIO.output(32, GPIO.HIGH)
#     time.sleep(0.0000025)
#     GPIO.output(32, GPIO.LOW)
#     time.sleep(0.0000025)
#     GPIO.output(32, GPIO.HIGH)
    
# def was_clicked_backward():
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(38, GPIO.OUT)#Pull+
#    # GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW)
#     GPIO.setup(29, GPIO.OUT, initial = GPIO.HIGH)#Dir+
#     GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW)#Dir-
#     pwmOutput = GPIO.PWM(38, 200000)
#     pwmOutput.start(50)
#     time.sleep(0.5)
#     print("Clicked!!")
#     GPIO.cleanup()
# def was_clicked_Left():
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(32, GPIO.OUT)#Pull+
#     GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW)
#     GPIO.setup(35, GPIO.OUT, initial = GPIO.HIGH)#Dir+
#     #GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW)#Dir-
#     pwmOutput = GPIO.PWM(32, 200000)
#     pwmOutput.start(50)
#     time.sleep(0.5)
#     print("Clicked!!!")
#     GPIO.cleanup()
# def was_clicked_Right():
#     GPIO.setmode(GPIO.BOARD)
#     GPIO.setup(32, GPIO.OUT)#Pull+
#     GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW)
#     GPIO.setup(35, GPIO.OUT, initial = GPIO.LOW)#Dir+
#     #GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW)#Dir-
#     pwmOutput = GPIO.PWM(32, 200000)
#     pwmOutput.start(50)
#     time.sleep(0.5)
#     print("Clicked!!!!")
#     GPIO.cleanup()
# def impulse():
#     time.sleep(0.0000025)
#     GPIO.output(32, GPIO.LOW)
#     time.sleep(0.0000025)
#     GPIO.output(32, GPIO.HIGH)
#     
# 
# 
# form.pushButton.clicked.connect(was_clicked_forward)#move forward
# form.pushButton_2.clicked.connect(was_clicked_backward)#move backward
# form.pushButton_3.clicked.connect(was_clicked_Left)#move left
# form.pushButton_4.clicked.connect(was_clicked_Right)#move right
# form.action.triggered.connect(exit_action)
