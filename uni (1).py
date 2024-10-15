#▓▓   ▓▓    ▓▓     ▓▓   ▓▓                   
#▓▓   ▓▓    ▓▓   ▓▓▓▓   ▓▓ 
#▓▓   ▓▓    ▓▓▓▓   ▓▓   ▓▓        
#   ▓▓      ▓▓      ▓▓   ▓▓  

#meta developer: @Strazh0979Tell
from .. import loader, utils
from asyncio import sleep
import random

@loader.tds
class Cat(loader.Module):
    """Uni cat :3"""
    strings = {'name': 'uni'}

    @loader.command(alias='уни')
    async def  uni(self, message):
        """- вызвать котика :3"""
        await utils.answer(message, "<b>Uploading Uni cat :3</b>")
        await message.delete()
        media_files = (
            "https://0x0.st/s/aXLdv2M_GK4NxPIywRcVHA/X3N2.jpg",
            "https://0x0.st/s/-MQk0lgv4NbdCHRWXz6mig/X3NL.jpg",
            "https://0x0.st/s/aXLdv2M_GK4NxPIywRcVHA/X3N2.jpg",
            "https://0x0.st/s/g2nrJSdWi5X-Sfrbrp7sKg/X3Tk.jpg",
            "https://0x0.st/s/m6dwFddPFxsIpV78lXWF2Q/X3TD.jpg",
            "https://0x0.st/s/BGpXmzSP7LCCpxmpGRVdgg/X3TG.jpg",
            "https://0x0.st/s/bNwPhlT9tBISQRZIWRDnsw/X3T6.jpg",
            "https://0x0.st/s/6wRVCwWJbvF9M1Rslqq5vQ/X3T0.jpg",
            "https://0x0.st/s/3t9pzxO1i2fKRoxgQ0jL8Q/X3TU.jpg",
            "https://0x0.st/s/owZDXlUQ6POA-UJy4u9yzw/X3Tl.jpg",
            "https://0x0.st/s/xqg78ZkW97BhGc15TxvjmQ/X3TI.jpg",
            "https://0x0.st/s/bNwPhlT9tBISQRZIWRDnsw/X3T6.jpg",
            "https://0x0.st/s/1Wb25ajDlC_4RLqqnyz6kg/XEXd.jpg",
            "https://0x0.st/s/6FXIN-WCwFBz68s9kFqDgw/XEX7.jpg",
            "https://0x0.st/s/HgwlPuxVH6BAU1H11eSr8w/XEXh.jpg",
            "https://0x0.st/s/uiaGPzG-S4VhgaylnXClTg/XEXF.jpg",
            "https://0x0.st/s/-L0pG7fO-16-GHzbhw48TQ/XEXC.jpg",
            "https://0x0.st/s/dNFxEjU829GR-ORgjusfqQ/XE8r.jpg",
            "https://0x0.st/s/Pf6udBZIHC6u7XLK6V2iwg/X66Z.jpg",
            "https://0x0.st/s/ewJfdQwo3ziOiK08VB5Xxw/X66P.jpg",
            "https://0x0.st/s/5a2MaozCL1ZIEEj5wrwQ9Q/X66K.jpg",
            "https://0x0.st/s/gwT2x2sTxMuBHX0L2A-z6w/X668.jpg",
            "https://0x0.st/s/2aLCk6-XZ1ATMFWKcuqm7g/X66X.jpg",
            "https://0x0.st/s/_9tmunyHMK38TY-rvXmtdQ/X66H.jpg",
            "https://0x0.st/s/I76J8sf4powZ_loSBXV6OA/X66o.jpg",
            "https://0x0.st/s/G-85kdpnTW6cyWN5p1mizw/X66-.jpg",
            "https://0x0.st/s/F-ehfy0xjCwNc-K9FPGCig/X66z.jpg",
            "https://0x0.st/s/ri5t3YZ1kg9HCoh599-vLQ/X66i.jpg",
            "https://0x0.st/s/6jTanfoktNt0hlXMNNSg1A/X66s.jpg",
            "https://0x0.st/s/OT6gk3QfL9LbFJoQGRSRaA/X66r.jpg",
            "https://0x0.st/s/td2hZC8t6w3J0ZrnC0rxKQ/X6EC.jpg",
            "https://0x0.st/s/JZyAKZwQzu_XhF5hIMQHTQ/X6EF.jpg",
            "https://0x0.st/s/Bz-o7AtvzH00Gwrgbyoxag/X6EG.jpg",
            "https://0x0.st/s/lWdxpDFkwy66z3pZQ1TWXw/X6E6.jpg",
            "https://0x0.st/s/lWdxpDFkwy66z3pZQ1TWXw/X6E6.jpg",
            "https://0x0.st/s/Bz-o7AtvzH00Gwrgbyoxag/X6EG.jpg",
            "https://0x0.st/s/iQgNmQOT84hyEM9fZ2UJsA/X6E0.jpg",
            "https://0x0.st/s/we6lqDsoWoABQ3yQVrtVEQ/X6El.jpg",
            "https://0x0.st/s/Bz-o7AtvzH00Gwrgbyoxag/X6EG.jpg",
            "https://0x0.st/s/8V0Aoya5OXcC9fagjRg72g/X6Ek.jpg",
            "https://0x0.st/s/LIDkwPZJXIrfsCrmAYZ0fw/X65E.jpg",
            "https://0x0.st/s/VQhvPtRk55QiTIn2_Uvp1A/X6E5.jpg",
            "https://0x0.st/s/4IAtrc7eZNMfK2ZxKtXytQ/X65Y.jpg",
            "https://0x0.st/s/fZz4kSEj6g4Ekh4aMhoASA/X65x.jpg",
            "https://0x0.st/s/z4_p0Lyv5v0T5S0oo751yQ/X65w.jpg",
            "https://0x0.st/s/ydWncQWDAE00l0xLlEGGcg/X65v.jpg",
            "https://0x0.st/s/_Qc_hHNtasQH2l4SkhYbOQ/X65t.jpg",
            "https://0x0.st/s/zn3DoRwpe57h4OoVmZatZg/X65y.jpg",
            "https://0x0.st/s/TXT4Gjd6PJMN2xfsSmp1aw/X654.jpg"
            
        )
        
        await self.client.send_file(message.peer_id, random.choice(media_files), caption="<b>uni cat :3</b>")
