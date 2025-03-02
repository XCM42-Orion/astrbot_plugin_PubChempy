from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("CHaTNE", "Your Name", "CHTNE自用信息插件", "1.0.0", "repo url")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("about")
    async def about(self, event: AstrMessageEvent):
        '''关于茶町CHaTNE''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        yield event.plain_result(f"茶町CHaTNE是CHTNE化学社基于Koishi和Astrbot框架自研的，支持LLM（大语言模型）的QQbot。未来CHaTNE会添加更多的实用功能。") # 发送一条纯文本消息
