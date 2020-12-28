# This Python Project is a discord bot mainly created for educational purpose.
# USE IT AT YOUR OWN RISK

from discord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_message(msg):
    if ":" == msg.content[0] and ":" == msg.content[-1]:
        emoji_name = msg.content[1:-1]
        for emoji in msg.guild.emojis:
            if emoji_name == emoji.name:
                if emoji.animated:
                    await msg.delete()
                    await msg.channel.send(str(emoji))
    await bot.process_commands(msg)

# I discovered randomly that we can resend specific emojis

bot.run("TOKEN")
