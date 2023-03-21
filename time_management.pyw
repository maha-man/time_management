# -*- coding: utf-8 -*-

# Welcome to time management free software.
# time management comes with ABSOLUTELY NO WARRANTY.
# 18.03.2023 - Michael Tschoepe - mich.tscho@gmail.com


from datetime import datetime
from datetime import date
from file_read_backwards import FileReadBackwards
import PySimpleGUI as sg
import sys, os


sg.theme('SandyBeach')
#sg.theme('TealMono')
#sg.theme('Light Blue 3')

#  Go to script folder.

scriptPath = os.path.abspath(os.path.dirname(sys.argv[0])) 

os.chdir(scriptPath)


# Create config und result textfile.

tFile = "time_management.txt"

if not os.path.exists(tFile):
    f = open(tFile, "w")
    f.write("\n")
    f.write("time management\n")
    f.write("Welcome to time management free software.\n")
    f.write("time management comes with ABSOLUTELY NO WARRANTY.\n")
    f.write("18.03.2023 - Michael Tschoepe - mich.tscho@gmail.com\n")
    f.write("\n")
    f.close()


# Functions

def ins_log_schreiben(line):
    text_file = open(tFile, "a")
    text_file.write(line + "\n")
    text_file.close()


# if file is empty make two empty lines.

with FileReadBackwards(tFile, encoding="utf-8") as log:

    count = 0
    for line in log:
        count += 1 
   
    if count < 2:
        ins_log_schreiben("\n")
       


# Create the window.


layout = [[sg.Button("start", size=(7,1)), sg.Button("stop", size=(7,1)), sg.Button("calculate", size=(7,1))]]

window = sg.Window("time mgmt.", layout)


# Create an event loop.

while True:
    event, values = window.read()

    if event == "start" or event == sg.WIN_CLOSED:
        today = datetime.today()
        startTime = datetime.now()

        with FileReadBackwards(tFile, encoding="utf-8") as log:
           for line in log:
                try:
                    logline = (line.strip())
                    action = logline.split()[0]
                    date = logline.split()[1]
                    time = logline.split()[2]
                    secArb = logline.split()[3]
                except:
                    ins_log_schreiben("\n")
                    ins_log_schreiben("start " + str(startTime) + " n")
                    break

                if str(action) == "calculate":
                    ins_log_schreiben("\n")
                    ins_log_schreiben("start " + str(startTime) + " n")
                    break

                elif str(action) == "stop":

                    dateTimee = (date + str(" ") + time)

                    datetimeObjDateTime = datetime.strptime(dateTimee, '%Y-%m-%d %H:%M:%S.%f')

                    diff = startTime - datetimeObjDateTime

                    diff = diff.total_seconds()
                    diff = int(diff)
                    secArb = int(secArb)

                    ins_log_schreiben("start " + str(startTime) + str(" ") + str(secArb))

                    break

                elif str(action) == "start" and secArb != "n":

                    dateTimee = (date + str(" ") + time)

                    datetimeObjDateTime = datetime.strptime(dateTimee, '%Y-%m-%d %H:%M:%S.%f')

                    diff = startTime - datetimeObjDateTime

                    diff = diff.total_seconds()
                    diff = int(diff)
                    secArb = int(secArb)

                    ins_log_schreiben("start " + str(startTime) + str(" ") + str(secArb))

                    break

    if event == "stop" or event == sg.WIN_CLOSED:
        stopTime = datetime.now()
        with FileReadBackwards(tFile, encoding="utf-8") as log:
            for line in log:
                logline = (line.strip())
                action = logline.split()[0]
                date = logline.split()[1]
                time = logline.split()[2]
                secArb = logline.split()[3]

                if secArb == "n":
                    dateTime = (date + str(" ") + time)

                    datetimeObjLogin = datetime.strptime(dateTime, '%Y-%m-%d %H:%M:%S.%f')
                    diff = stopTime - datetimeObjLogin
                    diff = diff.total_seconds()
                    diff = int(diff)
                    ins_log_schreiben("stop " + str(stopTime) + str(" ") + str(diff))
                    break

                elif secArb != "n":

                    dateTimee = (date + str(" ") + time)

                    datetimeObjDateTime = datetime.strptime(dateTimee, '%Y-%m-%d %H:%M:%S.%f')

                    diff = stopTime - datetimeObjDateTime
                    diff = diff.total_seconds()
                    diff = int(diff)
                    secArb = int(secArb)

                    sum = diff + secArb
                    ins_log_schreiben("stop " + str(stopTime) + str(" ") + str(sum))

                    break

    if event == "calculate" or event == sg.WIN_CLOSED:

        from datetime import date

        #today = date.today()
        today = datetime.today()
        exitTime = datetime.now()
        with FileReadBackwards(tFile, encoding="utf-8") as log:
  
            for line in log:
                logline = (line.strip())
                action = logline.split()[0]
                date = logline.split()[1]
                time = logline.split()[2]
                secArb = logline.split()[3]

                dateTimee = (date + str(" ") + time)

                datetimeObjDateTime = datetime.strptime(dateTimee, '%Y-%m-%d %H:%M:%S.%f')

                try:
                    secArb = int(secArb)
                except:
                    dateTime = (date + str(" ") + time)
                    datetimeObjLogin = datetime.strptime(dateTime, '%Y-%m-%d %H:%M:%S.%f')
                    diff = exitTime - datetimeObjLogin
                    diff = diff.total_seconds()
                    secArb = int(diff)

                hoursDez = secArb / 60 / 60

                hoursDez = round(hoursDez, 5)

                hoursDez = hoursDez -8


                hours = int(secArb / 60 / 60)

                mins_ = int(secArb / 60)

                mins = mins_ - int(hours) * 60

             

                for lineBack in FileReadBackwards(tFile, encoding="utf-8"):

                    if lineBack.startswith("calculate"):

                        first, *middle, last = lineBack.split()

                        last = float(last)

                        break

                    else:
                        last = 0

                uberGesa = last + hoursDez

                ins_log_schreiben("calculate " + str(exitTime) + str(" ") + str(secArb) + " | hours: " + str(hours) + " | minutes: " + str(mins) + " | calculation day: " + str(hoursDez) + " | total calculation: " + str(uberGesa))

                


                break

        break

window.close()
