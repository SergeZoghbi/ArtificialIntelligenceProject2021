from tkinter import *
from tkinter import filedialog as fd
import PIL
from PIL import Image, ImageTk


def create_footer():
    footer = Frame(root, height=30)
    open_button = Button(footer, text='Choose your images', command=on_click_open_button)
    open_button.grid(row=1, column=0)

    exit_button = Button(footer, text='Exit', command=root.quit)
    exit_button.grid(row=1, column=1)

    footer.pack(fill='both', side='bottom')


def update_scroll_region():
    cTableContainer.update_idletasks()
    cTableContainer.config(scrollregion=content.bbox())


# Sets up the Canvas, Frame, and scrollbars for scrolling
def create_scrollable_container():
    cTableContainer.config(yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
    sbVerticalScrollBar.config(orient=VERTICAL, command=cTableContainer.yview)

    sbVerticalScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
    cTableContainer.pack(fill=BOTH, expand=TRUE)
    cTableContainer.create_window(0, 0, window=content, anchor=NW)


# Resize images for a better display
def resize_image(image):
    my_width = 350
    w_percent = (my_width / float(image.size[0]))
    h_size = int((float(image.size[1]) * float(w_percent)))
    image = image.resize((my_width, h_size), PIL.Image.ANTIALIAS)
    return image


# Function to open file browser it allows the selection of multiple files and return their full path.
def open_file_browse():
    # Tuple FileTypes only allowing images
    filetypes = (("Image File", '.png'), ("Image File", '.jpg'), ("Image File", '.jpeg'))
    # Opening File browser
    filenames = fd.askopenfilenames(title='Choose your images', initialdir='/home/sergezoghbi/Pictures',
                                    filetypes=filetypes)
    # This will return a list of files paths
    return filenames


def on_click_open_button():
    files = open_file_browse()

    frames = []
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
        # Add the Frame to the list
        frame.grid(row=i, column=j, rowspan=1, columnspan=1)

        frames.append(frame)

        # Also, just as an FYI, j = j + 2 can be better written like this
        j = j + 1
        count = count + 1
    update_scroll_region()


root = Tk()

# Set Window Title.
root.title('Geometric Shapes Recognition - Project AI 2021')

# Set Window icon.
img = PhotoImage(file='icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

# Set Window size.
root.geometry("1000x500")

cTableContainer = Canvas(root)
content = Frame(cTableContainer)
sbVerticalScrollBar = Scrollbar(root)

create_footer()
create_scrollable_container()

root.mainloop()
