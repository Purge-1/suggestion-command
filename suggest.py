@client.command()
async def suggest(ctx, arg):
    channel = client.get_channel(channel id)
    embed=discord.Embed(title="a new suggestion!", description=f'{arg} - ', color=0xffae00)
    embed.set_author(name=f'Suggestion by {ctx.author}', icon_url=f'{ctx.author.avatar_url}')
    embed.set_footer(text="Do suggest to do a suggestion!")
    await channel.send(embed=embed)
    await ctx.message.add_reaction("✅")