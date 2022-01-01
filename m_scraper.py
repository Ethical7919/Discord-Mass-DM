#Based on https://github.com/Merubokkusu/Discord-S.C.U.M/blob/master/examples/gettingGuildMembers.py

import discum
from colorama import Fore

T0k3n = input(f" {Fore.RESET}[{Fore.BLUE}>{Fore.RESET}]{Fore.RESET} Token: ")
guild_id = input(f" {Fore.RESET}[{Fore.BLUE}>{Fore.RESET}]{Fore.RESET} Guild ID: ")
channel_id = input(f" {Fore.RESET}[{Fore.BLUE}>{Fore.RESET}]{Fore.RESET} Channel ID: ")

bot = discum.Client(token=T0k3n)

def close_after_fetching(resp, guild_id):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched) + ' members fetched')
        bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.close()

def get_members(guild_id, channel_id):
    bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
    bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
    bot.gateway.run()
    bot.gateway.resetSession()
    return bot.gateway.session.guild(guild_id).members

members = get_members(guild_id, channel_id)
memberslist = []

for memberID in members:
    memberslist.append(memberID)
    print(memberID)

f = open('users.txt', "a")
for element in memberslist:
    f.write(element + '\n')
f.close()