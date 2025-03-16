import subprocess
from krita import *

# Requires: grim, slurp, wl-copy

cmd=\
"slurp | grim -g - - | wl-copy"

result = subprocess.call([cmd], shell=True)

print(result)
if result == 0:
    app = Krita.instance()
    app.action('KritaShape/KisToolBrush').trigger()
    app.action('edit_paste').trigger()

    
   

