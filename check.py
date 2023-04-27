import sys
import requests
from bs4 import BeautifulSoup
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

# Current Versions
szip_current = '22.01'
lav_current = '0.77.2'
edge_current = '111.0.1661.43'
dopdf_current = '11.7.374'

# 7-Zip
szip_url = "https://7-zip.org/"
szip_latest_paragraph = BeautifulSoup(requests.get(szip_url).text, "html.parser").find(class_='NewsTitle')
szip_v = szip_latest_paragraph.text.split()[-1]

if szip_v > szip_current:
    szip_color = 'color: red;'
    download_enabled = True
else:
    szip_color = 'color: green;'
    download_enabled = False

# LAV Filters
lav_url = "https://www.videohelp.com/software/LAV-Filters"
lav_latest_paragraph = BeautifulSoup(requests.get(lav_url).text, "html.parser").find('title')
lav_v = lav_latest_paragraph.text.split(' ')[2]

if lav_v > lav_current:
    lav_color = 'color: red;'
else:
    lav_color = 'color: green;'

# doPDF
dopdf_url = "https://www.dopdf.com/"
dopdf_latest_paragraph = BeautifulSoup(requests.get(dopdf_url).text, "html.parser").find(class_='d-none d-md-block')
dopdf_v = dopdf_latest_paragraph.text.strip().split(' ')[1]

if dopdf_v > dopdf_current:
    dopdf_color = 'color: red;'
else:
    dopdf_color = 'color: green;'

#! Window
class FirstPage(QWidget):
    def __init__(self):
        super().__init__()

        # BAAS
        self.szip = QLabel(self)
        self.szip.setText(f'7-Zip - {szip_v}')
        self.szip.setStyleSheet(szip_color)

        self.lav = QLabel(self)
        self.lav.setText(f'LAV Filters - {lav_v}')
        self.lav.setStyleSheet(lav_color)

        self.dopdf = QLabel(self)
        self.dopdf.setText(f'doPDF - {dopdf_v}')
        self.dopdf.setStyleSheet(dopdf_color)
        #

        self.putty = QLabel(self)

        title = QLabel(self)
        title.setText('Version Checker')
        title.setStyleSheet('font-size: 20px; margin-bottom: 20px;')

        baas = QLabel(self)
        baas.setText('Baastarkvara')
        baas.setStyleSheet('font-size: 18px;')

        layout = QVBoxLayout()
        layout.insertWidget(0, title)

        layout.insertWidget(1, baas)
        layout.addWidget(self.szip)
        layout.addWidget(self.lav)
        layout.addWidget(self.dopdf)

        self.setLayout(layout)

class SecondPage(QWidget):
    def __init__(self):
        super().__init__()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.first_page = FirstPage()
        self.second_page = SecondPage()
        self.stacked_widget.addWidget(self.first_page)
        self.stacked_widget.addWidget(self.second_page)

        button = QPushButton('Switch to Other Page')
        button.clicked.connect(self.switch_page)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        layout.addWidget(button)
        self.setLayout(layout)

    def switch_page(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index == 0:
            self.stacked_widget.setCurrentIndex(1)
        else:
            self.stacked_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())