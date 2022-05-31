import ctypes
import string
import os
import time
from pystyle import *


flower = '''
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ 
█       █       █   ▄  █ █   █      ██       █    █       █  █▄█  █       █
█  ▄▄▄▄▄█▄     ▄█  █ █ █ █   █  ▄    █    ▄▄▄█    █    ▄▄▄█       █    ▄▄▄█
█ █▄▄▄▄▄  █   █ █   █▄▄█▄█   █ █ █   █   █▄▄▄     █   █▄▄▄█       █   █▄▄▄ 
█▄▄▄▄▄  █ █   █ █    ▄▄  █   █ █▄█   █    ▄▄▄█▄▄▄ █    ▄▄▄██     ██    ▄▄▄█
 ▄▄▄▄▄█ █ █   █ █   █  █ █   █       █   █▄▄▄█   ██   █▄▄▄█   ▄   █   █▄▄▄ 
█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄█  █▄█▄▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄▄██▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█
                       appuie sur entrer
                                                                                
'''[1:]




System.Size(140, 40)
System.Title("STIDE>EXE")
System.Clear()
Anime.Fade(Center.Center(flower), Colors.red_to_blue, Colorate.Vertical, interval=0.025, enter=True)

banner1 = r'''

 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ 
█       █       █   ▄  █ █   █      ██       █    █       █  █▄█  █       █
█  ▄▄▄▄▄█▄     ▄█  █ █ █ █   █  ▄    █    ▄▄▄█    █    ▄▄▄█       █    ▄▄▄█
█ █▄▄▄▄▄  █   █ █   █▄▄█▄█   █ █ █   █   █▄▄▄     █   █▄▄▄█       █   █▄▄▄ 
█▄▄▄▄▄  █ █   █ █    ▄▄  █   █ █▄█   █    ▄▄▄█▄▄▄ █    ▄▄▄██     ██    ▄▄▄█
 ▄▄▄▄▄█ █ █   █ █   █  █ █   █       █   █▄▄▄█   ██   █▄▄▄█   ▄   █   █▄▄▄ 
█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄█  █▄█▄▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄▄██▄▄▄▄▄▄▄█▄▄█ █▄▄█▄▄▄▄▄▄▄█
                        
                        discord.gg/stride.exe
                                                          
                                                                                                                                   
'''

banner2 = r"""

"""         


banner = Add.Add(banner1, banner2, center=True)

url = "http://billythegoat356.github.io/api/apollyon/files/"


def stage(text: str) -> str:
    return print(f"""{Col.Symbol('...', Col.orange, Col.red)} {Col.orange}{text}{Col.reset}""")


print(Colorate.Diagonal(Colors.red_to_blue, Center.XCenter(banner + '\n\n')))

USE_WEBHOOK = True


time.sleep(1)

try:  
    from discord_webhook import DiscordWebhook  
except ImportError: 
    
    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\nPress enter to continue.")
    USE_WEBHOOK = False
try:  
    import requests  
except ImportError:  
    
    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit()  
try:  
    import numpy  
except ImportError:  
    
    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nPress enter to exit")
    exit()  

#
url = "https://github.com"
try:
    response = requests.get(url)  
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    # Tell the user
    input("You are not connected to internet, check your connection and try again.\nPress enter to exit")
    exit()  


class NitroGen:  
    def __init__(self):  
        self.fileName = "Nitro Codes.txt"  

    def main(self):  
        os.system('cls' if os.name == 'nt' else 'clear')  
        if os.name == "nt":  
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Générateur et checker de Nitro - Crée par ! deathgonytb#5527")  
        else:  
            print(f'\33]0;Nitro Generator and Checker - Crée par ! deathgonytb#5527\a',
                  end='', flush=True)  


        
        self.slowType("Crée par ! deathgonytb#5527", .02)
        time.sleep(1)  
        
        self.slowType(
            "\nEcrit combien de codes veux tu générer et vérifier : ", .02, newLine=False)

        try:
            num = int(input(''))  
        except ValueError:
            input("Ceci n'est pas un nombre\nAppuie sur entrer pour quitter")
            exit()  

        if USE_WEBHOOK:
            
            self.slowType(
                "Appuie sur entrer", .02, newLine=False)
            url = input('')  
            
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(  
                        url=url,
                        content=f"``Je commence à vérifier les nitros\nJe vais envoyer les codes valides ici```"
                    ).execute()

        

        valid = []  
        invalid = 0  
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        
        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:  
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}" 

                result = self.quickChecker(url, webhook)  

                if result:  
                    
                    valid.append(url)
                else:  
                    invalid += 1  
            except KeyboardInterrupt:
                
                print("\nInterrupted by user")
                break  

            except Exception as e:  
                print(f" Error | {url} ")  

            if os.name == "nt":  
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Crée par ! deathgonytb#5527")  
                print("")
            else:  
                
                print(
                    f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Crée par ! deathgonytb#5527\a', end='', flush=True)

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid)}""")  

        # Tell the user the program finished
        input("\nFinis ! Appuie sur entrer 5 fois pour fermer le programme")
        [input(i) for i in range(4, 0, -1)]  

    
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  
            
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine:  
            print()  

    def quickChecker(self, nitro:str, notify=None):  
        
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  

        if response.status_code == 200:  
            
            print(f" Valid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:  
                
                file.write(nitro)

            if notify is not None:  
                DiscordWebhook(  
                    url=url,
                    content=f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True  

        
        else:
            
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  


if __name__ == '__main__':
    Gen = NitroGen()  
    Gen.main()  