@client.event
async def on_message(message):
    if message.author is message.server.get_member('173451290268008448'):
        print('Success')
        await client.add_reaction(message,'⭐')
    else:
        print('Failed')