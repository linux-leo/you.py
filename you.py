# The main file of you.py!
import time, os
App = 1
while App != 2:
    print('Welcome to you.py, select an app from the list below')
    print('1 Countdown')
    print('2 exit')
    App = int(input())
    if App == 1:
        countdown = 1
        columns, rows = os.get_terminal_size(0)
        spacer = '{:^' + str(columns) + '}'
        countdownlength = input("Enter the Number to countdown from: ")
        displaymode = input("Do you want to use figlet for displaying the countdown? y/N ")
        unixtimestamp = int(time.time()) + int(countdownlength)
        while countdown != 0:
            countdown = unixtimestamp-int(time.time())
            if displaymode == "y":
                output = os.popen("figlet -f big -c -w " + str(columns) + " " + str(countdown)).read()
            else:
                output = spacer.format(countdown)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(output)
            print(spacer.format(str(round(countdown/60)) + " Minutes " + str(round(countdown/60/60)) + " Hours " + str(int(countdown/60/60/24)) + " Days"))
            time.sleep(1)
        print("App ended or couldn't be found, restarting...")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')