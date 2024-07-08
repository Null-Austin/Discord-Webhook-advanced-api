from discord_webhook import DiscordWebhook
import time
file = open('Webhooks.txt','r')
file_txt = file.read().splitlines()
file.close()
spam = input("what would you like to send?: ")

while(True):
    urls = input("Make sure all your discord webhooks are in the file, \"Webhooks.txt\" in seperate lines.\n(y/n)?: ")
    if urls == "y":
        break
def openfile():
    file = open('Webhooks.txt','r')
    file_txt = file.read().splitlines()
    file.close()
    return(file_txt)

file_txt = openfile()
num = 1
def send_webhooks(urls, content, num):
    results = []
    for url in urls:
        webhook = DiscordWebhook(url=url, content=(content + num), rate_limit_retry=True)
        response = webhook.execute()
        results.append((response.status_code, url))
    return results

while(True):
    send_webhooks(file_txt, spam, str(num))
    num += 1
    time.sleep(.3)