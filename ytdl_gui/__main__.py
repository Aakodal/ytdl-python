from ytdl_gui import host, port, window
from threading import Thread
from bottle import run


server = Thread(target=run, kwargs={"host": host, "port": port, "debug": True}, daemon=True)

server.start()
window.show()
