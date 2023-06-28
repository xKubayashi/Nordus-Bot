import nextcord
from nextcord.ext import commands
from nextcord import ButtonStyle
from nextcord.ui import Button, View


class WWW(commands.Cog):
    def __init__(self, client):
        self.client = client

    # support - przyciski
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(name="www", description="`(url)`")
    async def www(self, ctx):
        dupa = Button(label="Strona Nordynawii", url="https://nordslavpl.wixsite.com/nordynawia", style=ButtonStyle.blurple)
        pupa = Button(label="Kanał YT Kubayashi", url="https://www.youtube.com/channel/UCN83WmVXG44ZuWzc-JyJRfQ")

        myview = View(timeout=180)
        myview.add_item(dupa)
        myview.add_item(pupa)

        await ctx.send("# Witryny:", view=myview)

def setup(client):
    client.add_cog(WWW(client))