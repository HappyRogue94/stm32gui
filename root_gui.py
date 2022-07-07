from root_gui_utils import RootGui, ComGui

# create tk object
root_master = RootGui()
# create new frame object stemming for root gui and pass root object 
com_master  = ComGui(root_master.root)

# call the main loop function to initialie the root GUI
root_master.root.mainloop()


