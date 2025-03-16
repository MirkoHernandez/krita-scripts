import os

# Requires: swaymsg, ydotool

# List of event codes:
# /usr/include/linux/input-event-codes.h

cmd=\
'swaymsg "fullscreen disable; focus left;" \
&& swaymsg border pixel 1 && sleep .1 && swaymsg border pixel 0 \
&& ydotool key 57:1 57:0 42:1 35:1 35:0 42:0\
&& swaymsg "fullscreen disable; focus left;"'
os.system(cmd)
