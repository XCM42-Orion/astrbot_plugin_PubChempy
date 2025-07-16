from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from pubchempy import Compound,get_compounds
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

@register("PubChempy", "M42", "接入PubChempy查询化合物信息", "1.0.0", "repo url")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
    
    @filter.command("pcpsearchcid")
    async def pcpsearchcid(self, event: AstrMessageEvent, operation: str = ""):
        '''查询化合物CID，支持CAS，英文名称''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        c=get_compounds(operation,'name')
        yield event.plain_result(f"查询到的CID：{str(c)}")

    @filter.command("pcpsearch")
    async def pcpsearch(self, event: AstrMessageEvent, operation1: str = ""):
        '''根据化合物CID查询化合物别名''' # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        dnum=int(operation1)
        d=Compound.from_cid(dnum)
        yield event.plain_result(f"查询到的化合物名称及别名：{str(d.synonyms)}")
