from telethon import events
from ub import bot as javes
import asyncio
#BY Sh1vam Dont try to kang
from ub.utils import admin_cmd

@javes.on(admin_cmd("holi"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(0,9)
    await event.edit('π»πΆππππ»πππΎ')
    animation_chars = [
        '[Happy Holy Once Again To All](https://telegra.ph/file/ee2a7df3bc0a3334194b0.jpg)',
        '[Β­](https://telegra.ph/file/2e4ca1bc7f747858fe98d.jpg)',
        '[γ€Β­](https://telegra.ph/file/7f842a8f3aba51b8d5ac7.jpg)',
        '[Β­γ€](https://telegra.ph/file/f24efadcd212d996bb937.jpg)',
        '[γ€](https://telegra.ph/file/97b713907cd99f6831932.jpg)',
        '[π¨](https://telegra.ph/file/0b604517d37fc519f16b6.jpg)',
        '[β£οΈ](https://telegra.ph/file/aaadc0e87f78be44cfdaa.jpg)',
        '[β£οΈπ¨γ€Β­](https://telegra.ph/file/d7d62ebbff4b5b092d4e0.jpg)',
        ]
    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8],link_preview=True)

        
            
