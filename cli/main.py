import sys
import os
from cli.menus import main_menu


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    main_menu()