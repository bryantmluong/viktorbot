from libraries import *

RIOT_API_KEY = os.getenv('RIOT_API_KEY')

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

#intro
@bot.event
async def on_ready():
    print("# Join the glorious evolution.")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("# Join the glorious evolution.")

#add command
@bot.command(help="I will add integers for you.")
async def add(ctx, *arr):
    result = 0 
    for i in arr:
        result += int(i)
    await ctx.send(f"result: {result}")

#command to send random viktor voicelines when a message is sent
@bot.command(help="I will state one of my League of Legends voicelines.")
async def voiceline(ctx):
    messages = ["Join the glorious evolution.", 
                "Function over form.", 
                "Submit to my designs.", 
                "Steel can fix all your flaws.",
                "Relinquish the flesh.",
                "They are obsolete.",
                "Adapt, or be removed.",
                "Obliterate!",
                "Behold!",
                "True power!",
                "Consume!",
                "Their bodies are frail."]
    await ctx.send(random.choice(messages))
    
# Remove the default help command so we can create a custom one
bot.remove_command('help')

#help command
@bot.command(help="The commands I provide for you.")
async def help(ctx, command_name: str = None):
    # If a specific command name is given, display the description of that command
    if command_name:
        # Display detailed help for a specific command
            command = bot.get_command(command_name)
            if command:
                embed = discord.Embed(title=f"Help: {command.name}", description=command.help or "No description", color=discord.Color.blue())
                await ctx.send(embed=embed)
            else:
                await ctx.send(f"No command named '{command_name}' found.")
    else:
        # Create an embed to display the commands nicely
        embed = discord.Embed(title="Help", description="### List of my available commands:", color=discord.Color.blue())
    
        # Iterate through all commands and add them to the embed
        for command in bot.commands:
            embed.add_field(name=command.name, value=command.help or "No description.", inline=False)
    
        await ctx.send(embed=embed)



bot.run(BOT_TOKEN)
