#Automatic Discord Message sending system v.1.1
import pyautogui as pag
import time
#opening message
print(' █████  ██████  ███    ███ ')
print('██   ██ ██   ██ ████  ████ ')
print('███████ ██   ██ ██ ████ ██ ')
print('██   ██ ██   ██ ██  ██  ██ ')
print('██   ██ ██████  ██      ██ ')


#Detemins the way that the user would like to open the file to input text
method = input('Would you like to provide a file path or text input? Options f/t')


if method == 'f':
    print('Please enter the message into the file on the desktop labled ADM_Input. This is a shortcut to another file')
    file = open('ADM_Input.txt')
    file.seek(0)
    fileinputtext = file.read()
    #Confirmation of message
    print(fileinputtext)
    time.sleep(0.5)
    confirmation = input('Is the message correct y/n')
    if confirmation == 'y':
        pag.getWindowsWithTitle("Discord")[0].maximize()
        pag.click(700, 980)
        pag.typewrite(fileinputtext)
        pag.press('enter')
    else:
        print('Invalid/Denied input, canceling')
        exit()
else:
    print('You have either inputted the text method or given an invalid input')
    inputmessage = input('Please give a message to send to last open user: ')
    print('Message to send:{}'.format(input))
    #Confirmation of message
    time.sleep(0.5)
    confirmation = input('Is the message correct y/n')
    if confirmation == 'y':
        pag.getWindowsWithTitle("Discord")[0].maximize()
        pag.click(700, 980)
        pag.typewrite(inputmessage)
        pag.press('enter')
    else:
        print('Invalid/Denied input, canceling')
        exit()