from krita import *

app = Krita.instance()
d = app.activeDocument()

selection = d.selection()

app.action('fill_selection_foreground_color').trigger()
if selection:
    app.action('fill_selection_foreground_color').trigger()
    selection.shrink(1,1, False)
    app.action('clear').trigger()
    d.waitForDone()
    d.refreshProjection()
