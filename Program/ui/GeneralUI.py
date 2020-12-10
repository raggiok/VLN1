class GeneralUI():

    def __init__(self):
        pass


        #Menu header
    def ui_menu_header(self, menu_name):
        # print(" _   _       _   _            _      _ _                  ")
        # print("| \ | |     | \ | |     /\   (_)    | (_)                 ")
        # print("|  \| | __ _|  \| |    /  \   _ _ __| |_ _ __   ___  ___  ")
        # print("| . ` |/ _` | . ` |   / /\ \ | | '__| | | '_ \ / _ \/ __| ")
        # print("| |\  | (_| | |\  |  / ____ \| | |  | | | | | |  __/\__ \ ")
        # print("|_| \_|\__,_|_| \_| /_/    \_\_|_|  |_|_|_| |_|\___||___/ ")
        print("-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("-"*50)