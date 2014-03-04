import Tkinter,tkFileDialog

root = Tkinter.Tk()
root.withdraw()

file = tkFileDialog.askopenfile(parent=root,mode='rb',filetypes=[('JSON Files','*.json')],title='Choose a file')
if file != None:
    data = file.read()
    file.close()
    print "I got %d bytes from this file." % len(data)