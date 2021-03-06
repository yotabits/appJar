import sys
sys.path.append("../")
from appJar import gui

def checkDone():
    return True

def launch(win):
    if win == "modal": app.showSubWindow("modal")
    elif win == "full": app.showSubWindow("full")
    elif win == "trans": app.showSubWindow("trans")
    elif win == "pos": app.showSubWindow("pos")
    elif win == "in": app.showSubWindow("inner")

with gui() as app:
    app.setLocation(100,100)
    app.setLogLevel("debug")

    app.addButtons(["modal", "full", "trans", "pos"], launch)

    with app.subWindow("modal", modal=True):
        app.setBg("orange")
        app.setGeometry("400x400")
        app.setStopFunction(checkDone)
        app.addLabel("l1", "In sub window - MODAL")

    with app.subWindow("full"):
        app.setGeometry("fullscreen")
        app.addLabel("l2", "Sub Window two - FULLSCREEN")

    with app.subWindow("trans"):
        app.setTransparency(50)
        app.addLabel("l3", "Sub Window three - TRANSPARENCY")

    with app.subWindow("pos"):
        app.setLocation(700,700)
        app.addLabel("l4", "Sub Window four - LOCATION")
