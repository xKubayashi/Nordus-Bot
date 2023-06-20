import nextcord
from nextcord.ext import commands
from nextcord import File
from PIL import Image, ImageFont, ImageDraw
import textwrap

class Speak(commands.Cog):
    def __init__(self, client):
        self.client = client

    # //speak hello world!
    @commands.cooldown(1, 5, commands.BucketType.user) # Ogranicza czas wywoływania tej samej komendy od 1-5 sekund
    @commands.command(name="speak", description="Norduś pierdoli")
    async def speak(self, ctx, *args):
        msg = " ".join(args)
        font = ImageFont.truetype("Kablammo-Regular-VariableFont_MORF.ttf", 20)
        img = Image.open("Nordus3kopia.png")
        cx, cy = (320, 128)

        lines = textwrap.wrap(msg, width=45)
        print(lines)
        w, h = font.getsize(msg)
        y_offset = (len(lines)*h)/2
        y_text = cy-(h/2) - y_offset

        for line in lines:
            draw = ImageDraw.Draw(img)
            w, h = font.getsize(line)
            draw.text((cx-(w/2), y_text), line, (16777215, 16777215, 16777215), font=font) #16777215 - biały
            #draw.text((cx, cy), msg, (16777215, 16777215, 16777215), font=font) #16777215 - biały
            img.save("Nordus3kopia-edited.png")
            y_text += h

        with open("Nordus3kopia-edited.png", "rb") as f:
            img = File(f)
            await ctx.channel.send(file=img)  

def setup(client):
    client.add_cog(Speak(client))