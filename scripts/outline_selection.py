from krita import *

app = Krita.instance()
d = app.activeDocument()

def grow_opaque_selection():
    def new_layer():
        layer = d.createNode("Outline", "paintLayer")
        r = d.rootNode();
        r.addChildNode(layer, None)
        d.waitForDone()
        currentDoc = app.activeDocument()
        currentDoc.setActiveNode(layer)
        d.refreshProjection()

    # Select contiguous then opaque.
    app.action('KisToolSelectContiguous').trigger()
    d.waitForDone()
    app.action('selectopaque').trigger()
    d.waitForDone()
    selection = d.selection()
    # Grow selection.
    if selection:
        d.waitForDone()
        selection.grow(1 , 1)
        d.waitForDone()
        d.refreshProjection()
        new_layer()
    else:
        print("NO Selection")

grow_opaque_selection()
d.waitForDone()


