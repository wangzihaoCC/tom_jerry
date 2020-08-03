from source import tools,setup
from source.states import main_menu, load_screen, level

def main():

    #state = main_menu.MainMenu()
    state_dict = {
        'main_menu':main_menu.MainMenu(),
        'load_screen':load_screen.LoadScreen(),
        'level':level.Level()
    }
    game = tools.Game(state_dict, 'main_menu')

    game.run()
    #game.run(setup.GRAPHICS)

if __name__ == '__main__':
    main()