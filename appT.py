from tkinter import *
from tkinter import ttk
import random
from Algorithms import bubbleSort, insertionSort, selectionSort, quickSort, heapSort

pady = 8
padx = 8

root = Tk()
root.title("My sorting programm")
root.maxsize(1200, 700)
root.config(bg="dark red")

selectedAlg = StringVar()
arr = []
maxElem = 0


def drawArr(arr, colors):
    canvas.delete("all")
    c_height = 480
    c_width = 800
    x_width = c_width / (len(arr)+1)
    offset = 20
    spacing = 10
    for i, height in enumerate(arr):
        x0 = (i * x_width) + offset + spacing
        y0 = c_height - (c_height - 50)*(height/maxElem)
        x1 = x0 + x_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colors[i])
        canvas.create_text(x0 + x_width/2, y0 - 15, text=str(arr[i]))

    root.update_idletasks()


def generateArr():
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 10
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal = 150
    try:
        size = int(sizeEntry.get())
    except:
        size = 25

    if minVal < 0 or minVal > 300:
        maxVal = 10
    if maxVal < 50 or maxVal > 600:
        maxVal = 150
    if size < 0 or size > 30:
        size = 25
    global arr
    global maxElem
    for _ in range(size):
        arr.append(random.randrange(minVal, maxVal + 1))
    for elem in arr:
        if elem > maxElem:
            maxElem = elem
    drawArr(arr, ["dark red" for _ in range(len(arr))])
    return arr, maxElem


def startSort():
    global arr
    global selectedAlg
    selectedAlg = algMenu.get()
    if selectedAlg == "Bubble Sort":
        bubbleSort(arr, drawArr)
    if selectedAlg == "Insertion Sort":
        insertionSort(arr, drawArr)
    if selectedAlg == "Selection Sort":
        selectionSort(arr, drawArr)
    if selectedAlg == "Quick Sort":
        quickSort(arr, drawArr)
    if selectedAlg == "Heap Sort":
        heapSort(arr, drawArr)


UI_frame = Frame(root, width=800, height=200, bg="pink")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=800, height=480, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)


# row0
Label(UI_frame, text="Choose algorithm: ", bg="pink").grid(
    row=0, column=0, padx=padx, pady=pady, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selectedAlg, values=[
                       "Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort", "Heap Sort"])
algMenu.grid(row=0, column=1, padx=padx, pady=pady)
algMenu.current(0)

Button(UI_frame, text="Generate array", command=generateArr,
       bg="dark red").grid(row=0, column=2, padx=padx, pady=pady)
Button(UI_frame, text="Start", command=startSort, bg="dark red").grid(
    row=0, column=3, padx=padx, pady=pady)
# row1
Label(UI_frame, text="Array size ", bg="pink").grid(
    row=1, column=0, padx=padx, pady=pady, sticky=W)
sizeEntry = Entry(UI_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Minimum value ", bg="pink").grid(
    row=1, column=2, padx=padx, pady=pady, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Maximim value ", bg="pink").grid(
    row=1, column=4, padx=padx, pady=pady, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=padx, pady=pady, sticky=W)
root.mainloop()

# add stop button, heap sort, merge sort
