import os
from PyQt5.Qt import *
from krita import *

# Requires: wl-color-picker, wl-paste

view = Krita.instance().activeWindow().activeView()

cmd=\
"wl-color-picker clipboard && wl-paste"

result = os.popen(cmd).read().rstrip()

if result:
    color =QColor(result)
    view.setForeGroundColor(ManagedColor.fromQColor(color, view.canvas()))

