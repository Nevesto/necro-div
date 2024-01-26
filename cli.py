from colorama import Fore
from utils import twitter, youtube

print(Fore.RED + '''
 ███▄    █ ▓█████  ▄████▄   ██▀███   ▒█████     ▓█████▄  ██▓ ██▒   █▓
 ██ ▀█   █ ▓█   ▀ ▒██▀ ▀█  ▓██ ▒ ██▒▒██▒  ██▒   ▒██▀ ██▌▓██▒▓██░   █▒
▓██  ▀█ ██▒▒███   ▒▓█    ▄ ▓██ ░▄█ ▒▒██░  ██▒   ░██   █▌▒██▒ ▓██  █▒░
▓██▒  ▐▌██▒▒▓█  ▄ ▒▓▓▄ ▄██▒▒██▀▀█▄  ▒██   ██░   ░▓█▄   ▌░██░  ▒██ █░░
▒██░   ▓██░░▒████▒▒ ▓███▀ ░░██▓ ▒██▒░ ████▓▒░   ░▒████▓ ░██░   ▒▀█░  
░ ▒░   ▒ ▒ ░░ ▒░ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░     ▒▒▓  ▒ ░▓     ░ ▐░  
░ ░░   ░ ▒░ ░ ░  ░  ░  ▒     ░▒ ░ ▒░  ░ ▒ ▒░     ░ ▒  ▒  ▒ ░   ░ ░░  
   ░   ░ ░    ░   ░          ░░   ░ ░ ░ ░ ▒      ░ ░  ░  ▒ ░     ░░  
         ░    ░  ░░ ░         ░         ░ ░        ░     ░        ░  
                  ░                              ░               ░   
''')

print(Fore.RESET)

print("Digite 1 para divulgar dentro do twitter.")
print("Digite 2 para divulgar dentro do youtube.")

response = input("-> ")

if response == '1':
      twitter()
elif response == '2':
      youtube()
else:
      print("Digite o número 1 ou 2. para poder usar a ferramenta")