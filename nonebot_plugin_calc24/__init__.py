import asyncio
from .file_handle import file_handle
from nonebot import on_command, on_message
from nonebot.rule import to_me
from nonebot.params import CommandArg
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State 
from nonebot.plugin import PluginMetadata
from .xj_calc24 import xj_calc24
class_calc24 = xj_calc24()
__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-calc24",
    description="该插件实现的小游戏的游戏规则为一人一题。在插件启动时使用[/24点]命令启动游戏。使用加减乘除使给出的数等于24，在游戏进行时可以直接回复[退出]来退出游戏或者[换一题]来更换新的题目。如果在5分钟内未回答会自动退出。",
    usage="加载插件后使用/calc24或/24点开始游戏，在游戏中可以使用‘退出’退出游戏。",
    type="application",
    homepage="https://github.com/ajdgg/nonebot-plugin-calc24",
)
_timers = {}
_calc24_session = {} 
_original_array = {}

file_handle = file_handle()
c_m_data = file_handle.file_reading("calc24-data.json", "continuous-mode")
    
async def timeout_task(user_id, task):
    await asyncio.sleep(300) 
    if user_id in _calc24_session and _calc24_session[user_id] == "waiting_for_input":
        del _calc24_session[user_id]
        del _original_array['array']
calc24 = on_command("24点", rule=to_me(),  priority=10, block=True)  
@calc24.handle()  
async def handle_first_receive(bot: Bot, event: Event, state: T_State, args = CommandArg()):  
    if  str(args) == 'help':
        await calc24.finish("该插件实现的小游戏的游戏规则为一人一题。在插件启动时使用[24点]命令启动游戏。使用加减乘除使给出的数等于24，在游戏进行时可以直接回复[退出]来退出游戏或者[换一题]来更换新的题目。如果在5分钟内未回答会自动退出。\n ===指令===\n 24点：开始游戏\n ===游戏进行时===\n 退出：退出游戏\n 换一题：更换新的题目\n ===设置===\n 24点 连续模式：开启连续模式\n 24点 退出连续模式：退出连续模式")
    elif str(args) == '连续模式':
        if c_m_data:
            await calc24.finish("连续模式已是开启了哦")
        else:
            file_handle.file_change("calc24-data.json", "continuous-mode", True)
            await calc24.finish("连续模式开启")
    elif str(args) == '退出连续模式':
        if c_m_data:
            file_handle.file_change("calc24-data.json", "continuous-mode", False)
            await calc24.finish("连续模式关闭")
        else:
            await calc24.finish("连续模式已是关闭的哦")
    a_data = class_calc24.calc_a_main()
    _original_array['array'] = a_data
    user_id = event.get_user_id()  
    sender_nickname = event.sender.nickname
    await calc24.send(f'{sender_nickname}请计算：\n {str(a_data)}')
    _calc24_session[user_id] = "waiting_for_input"
    task = asyncio.create_task(timeout_task(user_id, asyncio.current_task()))
    _timers[user_id] = task
calc24_input = on_message(rule=lambda event: isinstance(event, Event) and _calc24_session.get(event.get_user_id(), "") == "waiting_for_input", priority=5)
@calc24_input.handle()  
async def handle_calc24_input(bot: Bot, event: Event):  
    user_id = event.get_user_id()  
    sender_nickname = event.sender.nickname
    args = str(event.get_message()).strip()
    if user_id in _timers:
        task = _timers[user_id]
        task.cancel()
        del _timers[user_id]
    if args == '退出':
        del _calc24_session[user_id]
        del _original_array['array']
        await calc24_input.finish('退出成功')
    elif args == '换一题':  
        a_data = class_calc24.calc_a_main()
        _original_array['array'] = a_data
        await calc24_input.send(str(a_data))
    else:
        receive_array = _original_array['array']
        print(receive_array, args)
        b_data = class_calc24.calc_b_main(args, receive_array)
        if b_data == 'NO':
            await calc24_input.send('输入无效，请重新输入')
        elif b_data == 'CONTINUOUS_OPERATOR':
            await calc24_input.send('连续操作符，请重新输入')
        elif b_data == 'ERROR':
            await calc24_input.send('答案错误，请重新输入')
        else:
            if c_m_data:
                a_data = class_calc24.calc_a_main()
                _original_array['array'] = a_data
                await calc24.send(f'{sender_nickname}答对了呢，下一题是：{str(a_data)}')
            else:
                del _calc24_session[user_id]
                del _original_array['array']
                await calc24_input.finish(f'{sender_nickname}答对了呢，游戏结束')
    _calc24_session[user_id] = "waiting_for_input"
    task = asyncio.create_task(timeout_task(user_id, asyncio.current_task()))
    _timers[user_id] = task