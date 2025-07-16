from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from pubchempy import Compound,get_compounds

@register("PubChempy", "M42", "接入PubChempy查询化合物信息", "1.0.0", "repo url")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.command("pcpsearch")
    async def pcpsearch(self, event: AstrMessageEvent, operation: str = ""):
        '''查询化合物信息，支持CAS，英文名称''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        c=get_compounds(operation,'name')
        yield event.plain_result("化合物名称及别名：",c.synonyms)
