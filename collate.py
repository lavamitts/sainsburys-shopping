from classes.menu_collection import MenuCollection


menu_collection = MenuCollection()
menu_collection.get_weekly_menus()
menu_collection.analyse_menu()
menu_collection.extract_and_sort_recipes()
menu_collection.write_to_excel()
