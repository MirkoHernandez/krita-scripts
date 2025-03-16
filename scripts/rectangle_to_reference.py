import subprocess
from krita import *

# Requires: grim, slurp, wl-copy

cmd=\
"slurp | grim -g - - | wl-copy"

result = subprocess.call([cmd], shell=True)

if result == 0:
    app = Krita.instance()
    app.action('paste_as_reference').trigger()
