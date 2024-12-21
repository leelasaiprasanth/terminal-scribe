from scribes.terminalScribe import TerminalScribe
from scribes.robotScribe import RobotScribe
from canvases.canvasAxis import CanvasAxis
from canvases.canvas import Canvas 

scribe = TerminalScribe(color='green')
scribe.forward(20)
robotScribe = RobotScribe(color='yellow')
robotScribe.drawSquare(20)

canvas = Canvas(20, 20, scribes=[scribe, robotScribe])
canvas.toFile('solution_file')

newCanvas = Canvas.fromFile('solution_file', globals())
newCanvas.go()
