from World import World
from LevelEditorFiles import LevelEditor as LE
import thorpy


def startGame():
    World(20, 20)


def startLevelEditor():
    LE.LevelEditor(20,20)


if __name__ == "__main__":
    application = thorpy.Application(size=(500, 500), caption='Gut game')
    thorpy.set_theme("human")
    e_play = thorpy.make_button("Play", startGame)
    e_edit = thorpy.make_button("Level Editor", startLevelEditor)
    e_quit = thorpy.make_button("Quit", thorpy.functions.quit_menu_func)
    elements = [e_play, e_quit, e_edit]
    e_back = thorpy.Background.make(elements=elements)
    thorpy.store(e_back)
    m_main = thorpy.Menu(e_back)
    m_main.play()
    application.quit()
