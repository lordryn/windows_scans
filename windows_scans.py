import subprocess
from tkinter import *

cmd_output = "stringy"
root = Tk()
ip_addr = Entry(root, width=50)
ip_addr.grid(row=0,
             column=1)


def run_terminal(self, *args):
    arg2, arg3 = args
    if arg3 == "":
        arg3 = None
    if arg3 is not None:
        process = subprocess.Popen([self, arg2, arg3],
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)
    else:
        process = subprocess.Popen([self, arg2],
                                   stdout=subprocess.PIPE,
                                   universal_newlines=True)
    while True:

        output = process.stdout.readline()
        print(output.strip())

        if output.strip() != "":
            print('Please wait...')
            for output in process.stdout.readlines():
                print(output.strip())
            break


myLabel = Label(root,
                text=cmd_output)


def get_public_ip():
    run_terminal('nslookup', 'myip.opendns.com.', 'resolver1.opendns.com')


publicIPButton = Button(root,
                        text="public ip",
                        padx=50,
                        pady=50,
                        command=get_public_ip)


def ip_config():
    tag = "/all"
    run_terminal('ipconfig', tag, None)


ipButton = Button(root,
                  text="ip",
                  padx=50,
                  pady=50,
                  command=ip_config)


def trace():
    target = ip_addr.get()
    flag = ""
    run_terminal('tracert', target, flag)


traceButton = Button(root,
                     text="trace",
                     padx=50,
                     pady=50,
                     command=trace)


def ping():
    ip = ip_addr.get()
    flag = ""
    run_terminal('ping', ip, flag)


pingButton = Button(root,
                    text="ping",
                    padx=50,
                    pady=50,
                    command=ping)

pingButton.grid(row=1,
                column=0)
publicIPButton.grid(row=2,
                    column=1)
ipButton.grid(row=1,
              column=1)
traceButton.grid(row=1,
                 column=2)
root.mainloop()
