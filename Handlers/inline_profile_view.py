from aiogram import Router, F
from aiogram import types
from Handlers.database import gun
import hashlib

router = Router()


@router.inline_query()
async def inline_m_profile(query: types.InlineQuery):
    ui = query.from_user.username
    impc = gun(ui)
    profile = f'''<b>---YOUR PROFILE---
Name: {ui}
Wins: {impc[0][0]}
Looses: {impc[0][1]}
Draws: {impc[0][2]}

Lb place:
</b>'''
    result_id = hashlib.md5(str(ui).encode()).hexdigest()
    result = types.InlineQueryResultArticle(
        id=result_id, title='profile',
        input_message_content=types.InputTextMessageContent(message_text=profile, parse_mode='HTML'),
        description='@aparfins_bot'
    )
    await query.answer([result], cache_time=1)