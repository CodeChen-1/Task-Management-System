import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli.menus import main_menu

if __name__ == "__main__":
    main_menu()
