#!/usr/bin/ python
# imports
from psychopy import visual, core

#create the window with 400X400
win = visual.Window([400,400])
#crete the message on the screen Hello from:
message = visual.TextStim(win, text='Hello from :')
#draw
message.setAutoDraw(True)
#window will flip
win.flip()
#wait for 2 seconds
core.wait(2.0)
message.setText('incf in psychopy')
win.flip()
core.wait(4.0)
message.setText('known as:')
win.flip()
core.wait(2.0)
message.setText('The International Neuroinformatics Coordinating Facility (INCF)')
win.flip()
core.wait(7.0)
message.setText('there website')
win.flip()
core.wait(2.0)
message.setText('http://incf.org/')
win.flip()
core.wait(9.0)
