import sys

from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout
from PyQt5.QtWidgets import QLineEdit, QSpinBox, QPlainTextEdit, QListWidget, QListView
from PyQt5.QtWidgets import QPushButton, QLabel, QMessageBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5 import QtCore
from PersonalAss import Run
import tweepy
from PersonalAss import TwitterApp

__version__ = '0.1'
__author__ = 'GM'


class botTalking(QThread):
    updateWords = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self._isRunning = True

    def __del__(self):
        self.wait()

    def stop(self):
        self._isRunning = False

    @pyqtSlot()
    def assistantBot(self):
        Run.Assistant.wishMe()
        while True:
            Run.Assistant.query = Run.Assistant.takeCommand().lower()  # Converting user query into lower case
            # Logic for executing tasks based on query
            botWords = Run.choose_function(Run.Assistant.query)

            self.updateWords.emit(
                str(botWords))  # izpolzvame PyQt Signals, za da updatevame v GUI-to dumite, kazani ot asistenta

    def run(self):
        self.assistantBot()


class PerAssistUI(QMainWindow):

    def __init__(self):
        super().__init__()
        # Nastroivame Title na prozoreca, razmer i background cvqt
        self.setWindowTitle('Personal Assistant')
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: white;")
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        # Syzdavame layout-a za programata
        self.generalLayout = QVBoxLayout()
        self._centralWidget.setLayout(self.generalLayout)

        self.frame = QFrame()
        self.frame2 = QFrame()
        self.generalLayout.addWidget(self.frame)
        self.generalLayout.addWidget(self.frame2)
        self._basicUI()
        self._settingUI()

        # Starting bot
        self.get_thread = botTalking()
        self.get_thread.updateWords.connect(self.updateBotWords)
        self.get_thread.start()

    def _startGif(self):
        # syzdavame label, za da mojem da dobavim GIF na robot
        self.label = QLabel()
        self.label.setGeometry(QtCore.QRect(25, 25, 200, 200))
        self.label.setMinimumSize(QtCore.QSize(128, 200))
        self.label.setMaximumSize(QtCore.QSize(128, 200))
        self.label.setObjectName("label")

        self.movie = QMovie("robot.gif")

        self.label.setMovie(self.movie)
        self.movie.start()

    def _basicUI(self):
        # Syzdavame UI-to na bota
        self.layout2 = QVBoxLayout()

        self._startGif()
        self.layout2.addWidget(self.label, alignment=Qt.AlignCenter)

        self.botwords = QLabel("Hello")
        self.layout2.addWidget(self.botwords, alignment=Qt.AlignCenter)

        self.goToSettingsBtn = QPushButton('Settings')

        self.goToSettingsBtn.clicked.connect(self.goToSettings)

        self.layout2.addWidget(self.goToSettingsBtn)

        self.frame.setLayout(self.layout2)

    def _settingUI(self):
        # Syzdavame UI-to na Settings page-a
        self.layout3 = QVBoxLayout()

        # Email Settings
        self.emailAdd = QLineEdit()
        self.emailPass = QLineEdit()
        self.emailPass.setEchoMode(QLineEdit.Password)
        layout = QFormLayout()
        layout.addRow('Email:', self.emailAdd)
        layout.addRow('Password:', self.emailPass)
        # Twitter Settings
        self.twitterConKey = QLineEdit()
        self.twitterConKey.setEchoMode(QLineEdit.Password)
        layout.addRow('Twitter Consumer Key:', self.twitterConKey)

        self.twitterConSec = QLineEdit()
        self.twitterConSec.setEchoMode(QLineEdit.Password)
        layout.addRow('Twitter Consumer Secret:', self.twitterConSec)

        self.twitterAccToken = QLineEdit()
        self.twitterAccToken.setEchoMode(QLineEdit.Password)
        layout.addRow('Twitter Access Token:', self.twitterAccToken)

        self.twitterAccSec = QLineEdit()
        self.twitterAccSec.setEchoMode(QLineEdit.Password)
        layout.addRow('Twitter Access Token Secret:', self.twitterAccSec)

        self.authTwitter = QPushButton('Authorize Twitter')
        layout.addRow(self.authTwitter)

        self.authTwitter.clicked.connect(self.getTwitterAuth)

        self.layout3.addLayout(layout)

        self.goBack = QPushButton('Go Back')

        self.goBack.clicked.connect(self.goBackFunc)

        self.layout3.addWidget(self.goBack)
        self.frame2.setLayout(self.layout3)
        self.frame2.hide()

    def goToSettings(self):
        # Za da otidem pri nastroikite skrivame BasicUI
        self.frame.setLayout(self.layout3)
        self.frame.hide()
        self.frame2.show()

    def goBackFunc(self):
        # Za da se vyrnem ot nastroikite skrivame settingsUI
        self.frame.setLayout(self.layout2)
        self.frame2.hide()
        self.frame.show()

    def updateBotWords(self, text):
        # funkciq za update na dumite na asistenta
        self.botwords.setText(text)

    def getTwitterAuth(self):
        print(self.twitterConKey.text())

        TwitterApp.authenticateTwitter(self.twitterConKey.text(),self.twitterConSec.text(),
                                       self.twitterAccToken.text(),self.twitterAccSec.text())



# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    redditapp = QApplication(sys.argv)
    # Show the GUI
    view = PerAssistUI()
    view.show()
    # Execute the main loop
    sys.exit(redditapp.exec_())


if __name__ == '__main__':
    main()
