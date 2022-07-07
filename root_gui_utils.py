from tkinter import *

# class for root gui configs
class RootGui:
    def __init__(self):
        self.root = Tk()
        self.root.title('serial communication')
        self.root.geometry("360x120")
        self.root.config(bg="white")

# class for COM gui configs
class ComGui:
    def __init__(self, root):
        self.root  = root
        #create frame to be stored in root gui
        self.frame = LabelFrame(root, text = "Com Manager", padx = 5, 
                                pady = 5, bg="white")
        #create label for the frame, this will have root as the frame.
        self.label_com = Label(self.frame, text="Available port(s): ", bg="white",
                                width=15, anchor="w")
        #publish the frame
        self.publish()

    def publish(self):
        self.frame.grid(row=0, column=0, rowspan=3, 
                        columnspan=3, padx=5, pady=5)
        self.label_com.grid(column=1, row=2)




if __name__ == '__main__':
    RootGui()
    ComGui()
