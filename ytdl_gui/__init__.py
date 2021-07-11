import bottle

root = __import__("pathlib").Path(__file__).resolve().parent
bottle.TEMPLATE_PATH = [str(root / "views")]
app = bottle.default_app()

host = "127.0.0.1"
port = "65534"

from . import controller
from . import download_video
