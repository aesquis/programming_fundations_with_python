import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    #Exemple amb dues hores
    # time.sleep(10*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=gxEPV4kolz0&ab_channel=billyjoelVEVO")
    break_count = break_count + 1
print ("this program ends on "+time.ctime())
