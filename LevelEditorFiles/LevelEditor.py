from LevelEditorFiles import LEdisplay as LED


class LevelEditor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        LED.LEdisplay()
