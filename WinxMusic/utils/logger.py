#
# Copyright (C) 2021-2022 by gabrielmaialva33 < https://github.com/gabrielmaialva33 >.
#
# This file is part of < https://github.com/gabrielmaialva33/winx-music-bot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/gabrielmaialva33/winx-music-bot/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from WinxMusic import app
from WinxMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
**سجل التشغيل**

**المحادثه:** {message.chat.title} [`{message.chat.id}`]
**المستخدم:** {message.from_user.mention}
**يوزره:** @{message.from_user.username}
**ايديه:** `{message.from_user.id}`
**يوزر المحادثه:** {chatusername}

**Query:** {message.text}

**😶😶😶😶:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
