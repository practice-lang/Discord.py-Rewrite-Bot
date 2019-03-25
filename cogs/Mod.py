import discord
import asyncio
from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kik_member=True)
    async def kick(self, ctx, member: discord.member, *, reason="없음"):
        await member.kick(reason=reason)
        await ctx.send("킥")
    
    @commands.command()
    @commands.has_permissions(ban_member=True)
    async def ban(self, ctx, member: discord.member, *, reason="없음"):
        await member.ban(reason=reason)
        await ctx.send("밴")

def setup(bot):
    bot.add_cog(Mod(bot))
