#▓▓   ▓▓    ▓▓     ▓▓   ▓▓           #▓▓   ▓▓    ▓▓     ▓▓        
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
            "https://0x0.st/s/dNFxEjU829GR-ORgjusfqQ/XE8r.jpg"
        )
        
        await self.client.send_file(message.peer_id, random.choice(media_files), caption="<b>uni cat :3</b>")