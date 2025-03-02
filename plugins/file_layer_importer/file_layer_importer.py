from krita import *
import os

def import_file_layer():
    app = Krita.instance()
    d = app.activeDocument()
    filelayer = os.popen("rg -L --files -i -g '*.kra' ~/data/i | rofi -show -dmenu -fuzzy").read().rstrip()
    if filelayer:
        n = d.createFileLayer("File Layer", filelayer, "None",  "Bicubic")
        r = d.rootNode();
        c = r.childNodes();
        r.addChildNode(n, c[0])
        d.refreshProjection()

class ImportFL(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    # Krita.instance() exists, so do any setup work
    def setup(self):
        pass
    # called after setup(self)
    def createActions(self, window):
        action = window.createAction("importfilelayer", "File Layer Importer")
        action.triggered.connect(import_file_layer)
        pass
