"""
生成以max-number为上限的随机正数
"""

import secrets

from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.rule import to_me

random_number = on_command(
    "随机数",
    rule=to_me(),
    aliases={"random"},
    priority=10,
    block=True,
)


@random_number.handle()
async def random_handle(args: Message = CommandArg()):
    # 提取参数纯文本作为最大值，并判断是否有效
    if max_text := args.extract_plain_text():
        max_num = int(max_text)
        value = secrets.randbelow(max_num)
        await random_number.finish(f"随机数是{value}")
    else:
        await random_number.finish("请输入随机数最大值")
