import os
import shutil
import tkinter as tk
from tkinter import *
import subprocess
from tkinter import ttk


root = Tk()


frame = Frame(root)


frame.pack(fill = BOTH)


buttonFrame = Frame(frame)
buttonFrame.pack(side=LEFT, fill=Y)

def modProfiler():
    os.startfile("application\\ModProfilesMC.exe")

def seedmap():
    os.startfile("application\\cubiomes.exe")

def bedrockfinder():
    os.startfile("application\\bedrockfindercpp.exe")

def  terrainfinder():
    os.startfile("application\\terrainfinder\\TerrainFinderApp.exe")


modProfilerb = Button(buttonFrame, text="Mod Profiles", command=modProfiler)
modProfilerb.pack()

seedmapb = Button(buttonFrame, text="seed map", command=seedmap)
seedmapb.pack()

bedrockfinder = Button(buttonFrame, text="bedrock finder", command=bedrockfinder)
bedrockfinder.pack()

terrainfinderb = Button(buttonFrame, text="terrain finder", command=terrainfinder)
terrainfinderb.pack()
my_label = Label(buttonFrame, text=' ')
my_label.pack(pady=5)

root.title('MC ToolBox')
root.mainloop()