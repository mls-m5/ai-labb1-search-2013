


from Tkinter import *


class apGui(Canvas):
	scale = .5
	def drawLine(self, x1,y1,x2,y2, width):
		scale = self.scale
		self.create_line(x1 * scale, y1 * scale, x2 * scale, y2 * scale, fill="black", width=width)
		
	def drawText(self, x,y, text):
		scale = self.scale
		self.create_text(x*scale,y*scale,text=text)
	def clear(self):
		self.delete("all")
		
	def __init__(self):
		Canvas.__init__(self, Tk(), bg="white", width=1000, height=800)
		self.pack()
		
	def start(self):
		mainloop()
	
if __name__ == "__main__":
	ap = apGui()
	ap.drawLine(0,0,100,100,4)
	mainloop()
	
apGui.apwindow = apGui()
