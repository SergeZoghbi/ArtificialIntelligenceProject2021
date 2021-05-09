from tkinter import *
from Presentation.GeometricShapesRecognitionUi import GeometricShapesRecognitionUi


class Main:

    def __init__(self):
        self.start_gui(self)


    def start_gui(self, environment):
        root = Tk()
        GeometricShapesRecognitionUi(root)
        root.mainloop()


if __name__ == "__main__":
    Main()
