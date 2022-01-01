import requests, sys, os
from colorama import Fore

def BeepBoop_BoopBeep():
    message = input(f" {Fore.RESET}[{Fore.BLUE}>{Fore.RESET}]{Fore.RESET} Message to Mass DM: ")
    tokens = open('tokens.txt','r').read().splitlines()
    with open(f'users.txt', 'r') as Tokens:
        tkens = []
        for line in Tokens:
            tkens.append(line.strip())
        for tid in tkens:
            try:
                print(f" {Fore.RESET}[{Fore.BLUE}>{Fore.RESET}]{Fore.RESET} Dm")
                for tok in tokens:
                    r = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', headers = {'Authorization': f"Bot {tok}"}, json = {'recipient_id': tid}).json()
                    r2 = requests.post(f"https://discordapp.com/api/v9/channels/{r['id']}/messages", headers = {'Authorization': f"Bot {tok}"}, json = {'content': message,'nonce':'','tts':False})
            except Exception as e:
                pass

BeepBoop_BoopBeep()
