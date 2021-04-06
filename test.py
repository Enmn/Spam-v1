import os
import time


yellow = "\033[1;93m"
red = "\033[1;31;40m"
white = "\033[1;37;40m"

try:
    import pyautogui
    from pynput.keyboard import Key, Controller
except ImportError:
    print(red + 'Error! : There appears to be a package that has not been installed ):')
    print(red + 'You must ensure that you have installed the packages correctly using the \'requirements.txt\'')
    exit()
    

keyboard = Controller()


print(yellow + '''


   ████████                                               ██
  ██░░░░░░  ██████                                       ███
 ░██       ░██░░░██  ██████   ██████████        ██    ██░░██
 ░█████████░██  ░██ ░░░░░░██ ░░██░░██░░██ █████░██   ░██ ░██
 ░░░░░░░░██░██████   ███████  ░██ ░██ ░██░░░░░ ░░██ ░██  ░██
        ░██░██░░░   ██░░░░██  ░██ ░██ ░██       ░░████   ░██
  ████████ ░██     ░░████████ ███ ░██ ░██        ░░██    ████
 ░░░░░░░░  ░░       ░░░░░░░░ ░░░  ░░  ░░          ░░    ░░░░

 --------------------------------------------------------------
 developers - Osama
 TikTok - @l.7a
 --------------------------------------------------------------
''')
o = input(f'''
[ 1 ] {white+ 'Spam - Message Enter'}
{yellow+ '[ 2 ]'} {white+ 'Spam - Send using files .txt'}
{yellow + '[ 3 ]'} {white+ 'Exit the tool'}
{yellow+ '->'} ''')

if o =="1":
    word = input("[+] Messages you want to send: ")
    count = int(input('[+] Count Messages: '))
    time.sleep(3)
    for x in range(count):
         pyautogui.typewrite(word)
         keyboard.press(Key.enter)


if o =="2":
    file = input('[+] Enter file name or file path: ')
    password = open(file).read().splitlines()
    time.sleep(3)
    for uu in password:
        pyautogui.typewrite(uu)
        keyboard.press(Key.enter)


if o =="3":
    os.system('exit')
    




    

    
        
        
