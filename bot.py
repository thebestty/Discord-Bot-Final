import discord
import random
import os

def run_discord_bot():
    TOKEN = os.getenv("DISCORD TOKEN")

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        content = message.content.strip()

        if content.startswith("/announce"):
            name = content.split(content.find(" "))
            name = name[1]
            await message.channel.send(content + " has now arrived into the server, say hello!")
            return

        if content.startswith("/showaround"):
            await message.channel.send("The general is where you talk about anything, the study channel is for helping others study.")
            return

        if content.startswith("/help"):
            await message.channel.send(f"@xxvrxx help {client}.")
            return
        
        if content.startwith("/answerquestion"):
            question = content.split(content.find(" "))
            question = question[1]
            if question[0].isdigit():
                 # -------- ADD --------
        if question[1] == "+"
            nums = content.split()[1:]
            if len(nums) != 2:
                await message.channel.send("Usage: !add 5 3")
                return
            try:
                num1 = float(nums[0])
                num2 = float(nums[1])
                result = num1 + num2
                await message.channel.send(f"The sum is {result}")
            except ValueError:
                await message.channel.send("Please provide valid numbers.")
            return
 
        # -------- SUBTRACT --------
        if question[1] == "-"
            nums = content.split()[1:]
            if len(nums) != 2:
                await message.channel.send("Usage: !subtract 5 3")
                return
            try:
                num1 = float(nums[0])
                num2 = float(nums[1])
                result = num1 - num2
                await message.channel.send(f"The difference is {result}")
            except ValueError:
                await message.channel.send("Please provide valid numbers.")
            return
 
        # -------- MULTIPLY --------
        if question[1] == "*"
            nums = content.split()[1:]
            if len(nums) != 2:
                await message.channel.send("Usage: !multiply 5 3")
                return
            try:
                num1 = float(nums[0])
                num2 = float(nums[1])
                result = num1 * num2
                await message.channel.send(f"The product is {result}")
            except ValueError:
                await message.channel.send("Please provide valid numbers.")
            return
 
        # -------- DIVIDE --------
        if question[1] == "/"
            nums = content.split()[1:]
            if len(nums) != 2:
                await message.channel.send("Usage: !divide 5 3")
                return
            try:
                num1 = float(nums[0])
                num2 = float(nums[1])
                if num2 == 0:
                    await message.channel.send("You cannot divide by zero.")
                    return
                result = num1 / num2
                await message.channel.send(f"The quotient is {result}")
            except ValueError:
                await message.channel.send("Please provide valid numbers.")
            return
