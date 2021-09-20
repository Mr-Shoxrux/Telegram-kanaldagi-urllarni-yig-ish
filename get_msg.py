from telethon import TelegramClient
import re
import requests,os
from bs4 import BeautifulSoup

ip_id=0000000 # my.telegram.org dagi ip_id
ip_hash=''     # my.telegram.org dagi ip_hash
client = TelegramClient('session_name', ip_id, ip_hash).start()



async def main():
    try:
        async for msg in client.iter_messages('https://t.me/Daryo', 100):
            asosiy_xabarlar = []
            match = re.search("(?P<url>https?://[^\s]+)",  msg.message)
            if match is not None:
                url = match.group("url")
                res = requests.get(url)
                html_page = res.content
                soup = BeautifulSoup(html_page, 'html.parser')
                text = soup.get_text()
                with open('readme.txt', 'w', encoding='utf-8') as f:
                    f.write(text)
                    f.close()
                with open('readme.txt', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    f.close()
                os.remove("readme.txt")
                index = 0
                lenght = 0
                for i in range(len(lines)):
                    if len(lines[i]) > lenght:
                        lenght = len(lines[i])
                        index = i
                asosiy_xabarlar.append(lines[index])
    except Exception as ex:
        print(ex)
with client:
    client.loop.run_until_complete(main())
