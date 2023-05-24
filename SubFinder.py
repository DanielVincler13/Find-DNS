import requests
import colorama 
from colorama import Fore, Back, Style 

print('''      _______. __    __  .______   
     /       ||  |  |  | |   _  \  
    |   (----`|  |  |  | |  |_)  | 
     \   \    |  |  |  | |   _  <  
 .----)   |   |  `--'  | |  |_)  | 
 |_______/     \______/  |______/  
                                   
  _______  __  .__   __.  _______   _______ .______      
 |   ____||  | |  \ |  | |       \ |   ____||   _  \     
 |  |__   |  | |   \|  | |  .--.  ||  |__   |  |_)  |    
 |   __|  |  | |  . `  | |  |  |  ||   __|  |      /     
 |  |     |  | |  |\   | |  '--'  ||  |____ |  |\  \----.
 |__|     |__| |__| \__| |_______/ |_______|| _| `._____|
                                                         
''')

url = input("Coloque a URL ex(test.com): ")

with open("wordlist.txt", "r") as dir:
    find = dir.readlines()

    for word in find:
        word = word.strip()  # Remove espaços em branco no início e no final da palavra
        full_url = f"https://{word}.{url}"  # Adiciona o esquema "https://" à URL
        
        try:
            a = req.head(full_url)
            code = a.status_code
            
            if code == 200:
                print(Fore.GREEN, "[ + ] FIND SUB DOMAIN ->", full_url)
            if code == 301:
                ru = a.headers.get('Location')
                print(Fore.BLUE, full_url, ">> {}".format(ru))
            if code == 404:
                pass
            
        except req.exceptions.ConnectionError:
            pass
         
