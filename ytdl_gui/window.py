import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from ytdl_gui import host, port


def show():
    qtapp = QApplication(sys.argv)

    web = QWebEngineView()
    web.load(QUrl(f"http://{host}:{port}"))
    web.setWindowTitle("YouTube Downloader")
    web.show()

    sys.exit(qtapp.exec_())
