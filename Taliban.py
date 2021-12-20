import requests, discord, sys, os
from discord.ext import commands
from colorama import Fore

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="Scraper!", case_insensitive=False, intents=intents)

#The Scraper is not mine!

async def Taliban():
    guild = input(f" {Fore.RESET}[{Fore.BLUE}>{Fore.RESET}]{Fore.RESET} Guild ID: ")
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()

    members_ = 0
    os.remove('users.txt')
    f = open("users.txt", "a+")
    for member in members:
        f.write(f"{member.id}\n")
        members_ += 1
    print(f" {Fore.RESET}[{Fore.BLUE}>{Fore.RESET}]{Fore.RESET} Scraped {members_} Members!")

def BeepBoop_BoopBeep():
    message = open('message.txt', 'r').read()
    tokens = open('token.txt','r').read().splitlines()
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

@client.event
async def on_ready():
    await Taliban()

client.run("", bot=False) #Put your token here (Not bot token) so it can scrape
BeepBoop_BoopBeep()
os.system('cls; clear')