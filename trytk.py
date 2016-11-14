import tkinter as tk
import random

g_MapSizeX=20
g_MapSizeY=20
g_CellSize=20

stone=0
empty=1
treasures=["gold"]
treasure=random.choice(treasures)
weapons=["sword"]
weapon=random.choice(weapons)
monsters=["orc"]
monster=random.choice(monsters)

g_CellTypes=[stone,empty,treasure,weapon,monster]

class Application(tk.Frame):
    Map=[[stone for x in range(g_MapSizeX+1)] for y in range(g_MapSizeY+1)]
    CharacterX=0
    CharacterY=0
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.initMap()
        self.drawMap()

    def printMap(self):
        for i in range(1,g_MapSizeX):
            print(self.Map[i])
 
    def initMap(self):
#        self.printMap()
#        for i in range(1,g_MapSizeX):
#            for j in range(1,g_MapSizeY):
#                self.Map[i][j]=stone
        i=random.randint(1,10)
        j=random.randint(1,10)
        self.Map[i][j]=empty
        for k in range(random.randint(4,200)):
            direction=random.choice(["north","south","west","east"])
#            print(k," ",i," ",j," ",direction)
            if direction == "north":
                if i > 1: i=i-1
            if direction == "south":
                if i < g_MapSizeY: i=i+1
            if direction == "west":
                if j > 1: j=j-1
            if direction == "east":
                if j < g_MapSizeX: j=j+1
            if self.Map[i][j] == stone:
                self.Map[i][j]=empty
            if random.randint(1,10) == 1:
                self.Map[i][j]=random.choice(treasures)
#            print("** ",self.Map[i][j])
#            self.printMap()
        self.CharacterX=i
        self.CharacterY=j

    def drawMap(self):
        self.canvas = tk.Canvas(root, width=800, height=500)
        self.canvas.pack()
        for i in range(1,g_MapSizeX):
            for j in range(1,g_MapSizeY):
                if self.Map[i][j] == stone:
                    self.canvas.create_rectangle(i*g_CellSize,j*g_CellSize,(i+1)*g_CellSize,(j+1)*g_CellSize,fill="black")
                if self.Map[i][j] == empty:
                    self.canvas.create_rectangle(i*g_CellSize,j*g_CellSize,(i+1)*g_CellSize,(j+1)*g_CellSize,fill="grey")
                if self.Map[i][j] == "gold":
                    self.canvas.create_rectangle(i*g_CellSize,j*g_CellSize,(i+1)*g_CellSize,(j+1)*g_CellSize,fill="yellow")
                if i == self.CharacterX and j == self.CharacterY:
                    self.canvas.create_text(i*g_CellSize+(g_CellSize/3),j*g_CellSize+1,anchor=tk.NW,width=g_CellSize,text=":-)")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

