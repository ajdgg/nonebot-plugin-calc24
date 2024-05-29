<div align="center" style="padding-top: 60px">

<img width="120px" src="https://raw.githubusercontent.com/ajdgg/data/903bb9969285cb47f8938018f76c2218146987eb/AwajieLogo.png" alt="">

# nonebot-plugin-calc24

_✨ NoneBot 插件简单描述 ✨_

<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

### 安装

- 使用 nb-cli

```
nb plugin install nonebot-plugin-calc24
```

- 使用 pip

```
pip install nonebot-plugin-calc24
```

### 使用
该插件实现的小游戏的游戏规则为一人一题。在插件启动时使用[24点]命令启动游戏。

使用加减乘除使给出的数等于24，在游戏进行时可以直接回复[退出]来退出游戏或者[换一题]来更换新的题目。

如果在5分钟内未回答会自动退出。

使用[24点 help]命令可以查看帮助。

有bug请发邮箱[1095530449@qq.com]

## 命令
- 24点 help：显示帮助
- 24点：开始游戏
- 换一题：更换新的题目
- 退出：在连续模式结束游戏
- 24点 连续模式：开启连续模式
- 24点 关闭连续模式：关闭连续模式

## 更新
### 2024-05-26
- 更新模式切换判断
- └ 缺点：插件在自己或bot重启后会默认关闭连续模式
### 2024-05-19
- 添加是否进行连续回答模式
