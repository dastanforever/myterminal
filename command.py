


import os


class Commands:
    """docstring for Commands"""


    def run_command(self, comm):
        if comm == 'ls':
            res = os.listdir(os.getcwd())
            st = ""
            for ob in res:
                st = st + str(ob) + "\n"
            return st

        if comm[0:2] == 'cd':
            try:
                os.chdir(comm[3:])
                return "Directory Changed to : " + os.getcwd()
            except:
                return 'No such file or Directory : ' + os.getcwd() + "/" + comm[3:]


        return "No command found!!"
