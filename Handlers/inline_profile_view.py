from aiogram import Router, F
from aiogram import types
from Handlers.database import gun
import hashlib

router = Router()


@router.inline_query()
async def inline_m_profile(query: types.InlineQuery):
    id = query.from_user.id
    pstats = gun(id)
    profile = f'''<b>---YOUR PROFILE---
Name: {query.from_user.username}
Wins: {pstats[0][0]}
Looses: {pstats[0][1]}
Draws: {pstats[0][2]}

Lb place:
</b>'''
    result_id = hashlib.md5(str(query.from_user.username).encode()).hexdigest()
    result = types.InlineQueryResultArticle(
        id=result_id, title='profile',
        input_message_content=types.InputTextMessageContent(message_text=profile, parse_mode='HTML'),
        description='@aparfins_bot'
    )
    await query.answer([result], cache_time=1)