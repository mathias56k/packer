import sys
import requests
from bs4 import BeautifulSoup
from PyQt6.QtCore import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

# 7-Zip
szip_current = '22.01'

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
lav_current = '0.77.2'

lav_url = "https://www.videohelp.com/software/LAV-Filters"
lav_latest_paragraph = BeautifulSoup(requests.get(lav_url).text, "html.parser").find('title')
lav_v = lav_latest_paragraph.text.split(' ')[2]

if lav_v > lav_current:
    lav_color = 'color: red;'
else:
    lav_color = 'color: green;'

# Microsoft Edge
edge_current = '111.0.1661.43'

edge_url = "https://www.microsoft.com/et-ee/edge/business-pages/download?form=MA13FJ"
edge_latest_paragraph = BeautifulSoup(requests.get(edge_url).text, "html.parser").find_all(class_='c-paragraph')[1]
edge_v = edge_latest_paragraph.text.strip().split('(')[-1].strip(')')

if edge_v > edge_current:
    edge_color = 'color: red;'
else:
    edge_color = 'color: green;'

# doPDF
dopdf_current = '11.7.374'

dopdf_url = "https://www.dopdf.com/"
dopdf_latest_paragraph = BeautifulSoup(requests.get(dopdf_url).text, "html.parser").find(class_='d-none d-md-block')
dopdf_v = dopdf_latest_paragraph.text.strip().split(' ')[1]

if dopdf_v > dopdf_current:
    dopdf_color = 'color: red;'
else:
    dopdf_color = 'color: green;'

"""
# FireFox
ffox_current = '91.8.0'

ffox_url = "https://www.frontmotion.com/"
ffox_latest_paragraph = BeautifulSoup(requests.get(ffox_url).text, "html.parser").find('a', {'class': 'title'})
ffox_v = ffox_latest_paragraph.text.strip().split(' ')[1]

print(ffox_latest_paragraph)
print(ffox_v)

if ffox_v > ffox_current:
    ffox_color = 'color: red;'
else:
    ffox_color = 'color: green;'
"""
# Putty
putty_url = "https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html"
putty_latest_paragraph = BeautifulSoup(requests.get(putty_url).text, "html.parser").find("h1")
putty_v = putty_latest_paragraph.text.split('(')[-1].strip(')')

#! Window
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # BAAS
        self.szip = QLabel(self)
        self.szip.setText(f'7-Zip - {szip_v}')
        self.szip.setStyleSheet(szip_color)

        self.lav = QLabel(self)
        self.lav.setText(f'LAV Filters - {lav_v}')
        self.lav.setStyleSheet(lav_color)

        self.edge = QLabel(self)
        self.edge.setText(f'Microsoft Edge - {edge_v}')
        self.edge.setStyleSheet(edge_color)

        self.dopdf = QLabel(self)
        self.dopdf.setText(f'doPDF - {dopdf_v}')
        self.dopdf.setStyleSheet(dopdf_color)
        #

        self.putty = QLabel(self)
        self.putty.setText(f'Putty - {putty_v}')

        title = QLabel(self)
        title.setText('Version Checker')
        title.setStyleSheet('font-size: 20px; margin-bottom: 20px;')

        baas = QLabel(self)
        baas.setText('Baastarkvara')
        baas.setStyleSheet('font-size: 18px;')

        eri = QLabel(self)
        eri.setText('Eritarkvara')
        eri.setStyleSheet('font-size: 18px;')

        layout = QVBoxLayout()
        layout.insertWidget(0, title)
        
        layout.insertWidget(1, baas)
        layout.addWidget(self.szip)
        layout.addWidget(self.lav)
        layout.addWidget(self.edge)
        layout.addWidget(self.dopdf)

        layout.insertWidget(6, eri)
        layout.addWidget(self.putty)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())