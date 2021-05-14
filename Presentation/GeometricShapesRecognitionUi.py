from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from Helpers.ImageHelper import resize_image
from Logic.ShapesRecognition import shapes_recognition


class GeometricShapesRecognitionUi:
    __shapesLabel__ = []
    __filesPaths__ = []

    def __init__(self, master):

        # Set Window Title.
        master.title('Geometric Shapes Recognition - Project AI 2021')

        # Set Window icon.
        img = PhotoImage(file='../assets/imgs/icon.png')
        master.tk.call('wm', 'iconphoto', master._w, img)

        # Set Window size.
        master.geometry("1000x500")

        cTableContainer = Canvas(master)
        content = Frame(cTableContainer)
        sbVerticalScrollBar = Scrollbar(master)

        self.create_footer(master, cTableContainer, content)
        self.create_scrollable_container(cTableContainer, sbVerticalScrollBar, content)

    def create_footer(self, master, cTableContainer, content):
        footer = Frame(master, height=30)
        open_button = Button(footer, text='Choose your images',
                             command=lambda: self.on_click_open_button(cTableContainer, content))
        open_button.grid(row=1, column=0)

        recognize_button = Button(footer, text='Recognize', command=self.recognize_images)
        recognize_button.grid(row=1, column=1)

        exit_button = Button(footer, text='Exit', command=master.quit)
        exit_button.grid(row=1, column=2)

        footer.pack(fill='both', side='bottom')

    def recognize_images(self):
        for x, y in zip(self.__filesPaths__, self.__shapesLabel__):
            w = Label(y, text=shapes_recognition(x))
            w.pack()

    def update_scroll_region(self, cTableContainer, content):
        cTableContainer.update_idletasks()
        cTableContainer.config(scrollregion=content.bbox())

    # Sets up the Canvas, Frame, and scrollbars for scrolling
    def create_scrollable_container(self, cTableContainer, sbVerticalScrollBar, content):
        cTableContainer.config(yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
        sbVerticalScrollBar.config(orient=VERTICAL, command=cTableContainer.yview)

        sbVerticalScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
        cTableContainer.pack(fill=BOTH, expand=TRUE)
        cTableContainer.create_window(0, 0, window=content, anchor=NW)

    # Function to open file browser it allows the selection of multiple files and return their full path.
    def open_file_browse(self):
        # Tuple FileTypes only allowing images
        filetypes = (("Image File", '.png'), ("Image File", '.jpg'), ("Image File", '.jpeg'))
        # Opening File browser
        filenames = fd.askopenfilenames(title='Choose your images', initialdir='/home/sergezoghbi/',
                                        filetypes=filetypes)
        # This will return a list of files paths
        return filenames

    def on_click_open_button(self, cTableContainer, content):
        files = self.open_file_browse()

        i = 0
        j = 0
        count = 0
        for file in files:
            frame = LabelFrame(content, text="Shape {0}".format(count), padx=50, pady=50)
            im = Image.open(file)
            image = ImageTk.PhotoImage(resize_image(im))
            image_label = Label(frame, image=image)
            image_label.image = image
            image_label.pack()

            if j == 3:
                i = i + 1
                j = 0

            frame.grid(row=i, column=j, rowspan=1, columnspan=1)

            # Add the Frame to the list
            self.__shapesLabel__.append(frame)
            self.__filesPaths__.append(file)

            # Also, just as an FYI, j = j + 2 can be better written like this
            j = j + 1
            count = count + 1
        self.update_scroll_region(cTableContainer, content)
