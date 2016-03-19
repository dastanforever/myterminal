


import os, shutil


class Commands:
    """docstring for Commands"""


    def run_command(self, comm):
        if comm == 'ls':
            res = os.listdir(os.getcwd())
            st = ""
            for ob in res:
                st = st + str(ob) + "\n"
            return st

        if comm[0:3] == 'cd ':
            try:
                os.chdir(comm[3:])
                return "Directory Changed to : " + os.getcwd()
            except:
                return 'No such file or Directory : ' + os.getcwd() + "/" + comm[3:]

        if comm[0:6] == 'mkdir ':
            try:
                os.mkdir(comm[6:])
                return "Directory created : " + comm[6:]
            except Exception as e:
                return str(e)

        if comm[0:3] == "rm ":
            try:
                shutil.rmtree(comm[3:], ignore_errors = True)
                return "Removed Directory : " + comm[3:]
            except Exception as e:
                return str(e)

        return "No command found!!"
