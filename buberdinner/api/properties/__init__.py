import configparser
import pathlib

root = pathlib.Path(__file__).absolute().parent

config = configparser.ConfigParser()
config.read(root / "appsettings.dev.ini")
