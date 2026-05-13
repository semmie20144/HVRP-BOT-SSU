import discord
from discord.ext import commands
import os
import time
from dotenv import load_dotenv

# =========================
# LOAD ENV
# =========================
load_dotenv()

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    print("❌ TOKEN not found")
    exit()

print("TOKEN loaded ✔")

# =========================
# BOT SETUP
# =========================
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# READY
# =========================
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"✅ BOT ONLINE: {bot.user}")

# =========================
# /SSU COMMAND
# =========================
@bot.tree.command(name="ssu", description="Server Startup announcement")
async def ssu(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🚨 Server Startup",
        description=(
            "**HVRP is hosting a server startup! Join up for some quality roleplay!**\n\n"
            "**In-game server code:** `zu2dy9hb`\n\n"
            "Join up now to get the server active!\n"
            f"Read <#1502660554765107270> before joining!\n\n"
            "https://www.roblox.com/share?v=v2&code=5ihdm3h6uk58gc"
        ),
        color=discord.Color.blue()
    )

    embed.set_footer(text="made by semmie41")

    # FIX: eerst response, dan message
    await interaction.response.send_message("✅ SSU sent!", ephemeral=True)
    await interaction.channel.send(embed=embed)

# =========================
# /HELP COMMAND
# =========================
@bot.tree.command(name="help", description="Help menu")
async def help_command(interaction: discord.Interaction):

    embed = discord.Embed(
        title="📖 Help Menu",
        description=(
            "**Commands:**\n"
            "`/ssu` → Server Startup\n"
            "`/ping` → Check bot latency\n"
            "`/help` → Help menu"
        ),
        color=discord.Color.green()
    )

    embed.add_field(
        name="📜 Terms of Service",
        value=(
            "By using this bot you agree:\n\n"
            "• No abuse\n"
            "• No spam\n"
            "• Follow Discord rules\n\n"
            "📄 Full Terms of Service:\n"
            "https://1drv.ms/w/c/07b75a7576e1c210/IQAR6zG3IKrlQZwm0JZ6VsQ2AZ9_Muv50ehg8nlX3LGlORk?e=D0KhRc"
        ),
        inline=False
    )

    embed.set_footer(text="made by semmie41")

    await interaction.response.send_message(embed=embed)

# =========================
# /PING COMMAND
# =========================
@bot.tree.command(name="ping", description="Check bot latency")
async def ping(interaction: discord.Interaction):

    start_time = time.time()

    await interaction.response.send_message("🏓 Pong...")

    end_time = time.time()
    latency = round((end_time - start_time) * 1000)

    embed = discord.Embed(
        title="🏓 Pong!",
        description=f"Bot latency: **{latency}ms**",
        color=discord.Color.orange()
    )

    embed.set_footer(text="made by semmie41")

    await interaction.channel.send(embed=embed)

# =========================
# RUN BOT
# =========================
bot.run(TOKEN)