from nonebot import on_command, on_message
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.permission import GROUP  , PRIVATE
from nonebot.typing import T_State 
from nonebot.plugin import PluginMetadata
from .xj_calc24 import xj_calc24
class_calc24 = xj_calc24()

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-calc24",
    description="{插件介绍}",
    usage="加载插件后使用/calc24或/24点开始游戏，在游戏中可以使用‘退出’退出游戏。",
    type="application",
    homepage="https://github.com/ajdgg/nonebot-plugin-calc24",
    supported_adapters={"~onebot.v11", "~telegram"},
)
_calc24_session = {} 
_original_array = {}

# calc24 = on_command("calc24", rule=to_me(), aliases={"24点"}, priority=10, block=True)
calc24 = on_command("calc24", aliases={"24点"}, rule=to_me(), permission=GROUP | PRIVATE, priority=10, block=True)  
@calc24.handle()  
async def handle_first_receive(bot: Bot, event: Event, state: T_State):  
    a_data = class_calc24.a_main()
    _original_array['array'] = a_data
    await calc24.send(str(a_data))
    user_id = event.get_user_id()  
    _calc24_session[user_id] = "waiting_for_input"
    
calc24_input = on_message(rule=lambda event: isinstance(event, Event) and _calc24_session.get(event.get_user_id(), "") == "waiting_for_input", permission=GROUP | PRIVATE, priority=5)
@calc24_input.handle()  
async def handle_calc24_input(bot: Bot, event: Event):  
    user_id = event.get_user_id()  
    args = str(event.get_message()).strip()
    if args == '退出':
        del _calc24_session[user_id]
        del _original_array['array']
        await calc24_input.finish('退出成功')
    receive_array = _original_array['array']
    print(receive_array, args)
    b_data = class_calc24.b_main(args, receive_array)
    if b_data == 'no':
        await calc24_input.send('输入无效，请重新输入')
    else:
        await calc24_input.send(b_data)  
        del _original_array['array']
        del _calc24_session[user_id] 