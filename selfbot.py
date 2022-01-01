import requests, sys, os
from colorama import Fore

def BeepBoop_BoopBeep():
    message = input(f" {Fore.RESET}[{Fore.BLUE}>{Fore.RESET}]{Fore.RESET} Message to Mass DM: ")
    tokens = input(f" {Fore.RESET}[{Fore.BLUE}>{Fore.RESET}]{Fore.RESET} Token: ")
    with open(f'users.txt', 'r') as Tokens:
        tkens = []
        for line in Tokens:
            tkens.append(line.strip())
        for tid in tkens:
            try:
                print(f" {Fore.RESET}[{Fore.BLUE}>{Fore.RESET}]{Fore.RESET} Dmed")
                for tok in tokens:
                    r = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', headers = {'Authorization': tokens}, json = {'recipient_id': tid}).json()
                    r2 = requests.post(f"https://discordapp.com/api/v9/channels/{r['id']}/messages", headers = {'Authorization': tokens}, json = {'content': message,'nonce':'','tts':False})
            except Exception as e:
                pass

BeepBoop_BoopBeep()