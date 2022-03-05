from tokenize import String
import tkPDFViewer as pdf
from tkinter import*
from tkinter import filedialog as fd
root = Tk()
root.geometry("720x480")
root.title("Pdf Viewer in Python LIke Adobe Page reader")
zoomDPI=72

var1 = pdf.ShowPdf()

def zoomIn():
    global zoomDPI,var2
    zoomDPI=int(zoomDPI*1.5)
    if var2: # if old instance exists, destroy it first
        var2.destroy()
        # creating object of ShowPdf from tkPDFViewer. 
    var1 = pdf.ShowPdf() 
        # clear the image list # this corrects the bug inside tkPDFViewer module
    var1.img_object_li.clear()
        # Adding pdf location and width and height. 
    var2=var1.pdf_view(root,pdf_location = f"xyz.pdf",zoomDPI=zoomDPI) # default value for zoomDPI=72. Set higher dpi for zoom in, lower dpi for zoom out
        # Placing Pdf inside gui
    var2.pack()
def zoomOut():
    global zoomDPI,var2
    zoomDPI=int(zoomDPI/1.5)
    if var2: # if old instance exists, destroy it first
        var2.destroy()
        # creating object of ShowPdf from tkPDFViewer. 
    var1 = pdf.ShowPdf() 
        # clear the image list # this corrects the bug inside tkPDFViewer module
    var1.img_object_li.clear()
        # Adding pdf location and width and height. 
    var2=var1.pdf_view(root,pdf_location = f"xyz.pdf",zoomDPI=zoomDPI) # default value for zoomDPI=72. Set higher dpi for zoom in, lower dpi for zoom out
        # Placing Pdf inside gui
    var2.pack()

Button(root,text="Zoom In",command=zoomIn).pack()
Button(root,text="Zoom out",command=zoomOut).pack()


var2=var1.pdf_view(root,pdf_location=f"xyz.pdf",bar=True,load="after",zoomDPI=72)
var2.pack()
root.mainloop()