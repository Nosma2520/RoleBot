import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

# Create a counter variable to keep track of the number of accepted students
accepted_students = 0

# Create a dictionary of school abbreviations and roles
school_roles = {
    "scs": "SCS",
    "cit": "CIT",
    "cfa": "CFA",
    "dietrich": "Dietrich",
    "heinz": "Heinz",
    "tepper": "Tepper",
    "mellon": "MCS"
}

@bot.event
async def on_member_join(member):
    # Send a DM to the new member asking for their name
    await member.send("Hi there! What is your name?")

    def check(m):
        return m.author == member and isinstance(m.channel, discord.DMChannel)

    # Wait for the member to respond with their name
    msg = await bot.wait_for('message', check=check)
    name = msg.content

    # Send a DM to the new member asking for their school/major
    await member.send("What is your school? (SCS - School of Computer Science, CIT - College of Engineering, CFA - College of Fine Arts, Dietrich - Dietrich College of Humanities & Social Sciences, Heinz - Heinz College of Information Systems and Public Policy, Mellon - Mellon College of Science, Tepper - Tepper School of Business)")

    # Wait for the member to respond with their school
    msg = await bot.wait_for('message', check=check)
    school = msg.content
    # Iterate over the school_roles dictionary and assign roles based on the school abbreviation
    for key, value in school_roles.items():
        if key in school.lower():
            role = discord.utils.get(member.guild.roles, name=value)
            break
        else:
            await member.send("Something went wrong plz contact an admin to get roled. Sry :cry:")
    # Send a DM to the new member asking for their class year
    await member.send("What is your class year?")

    # Wait for the member to respond with their class year
    msg = await bot.wait_for('message', check=check)
    class_year = msg.content

    # Send a DM to the new member asking for their type of student
    await member.send("What type of student are you? (e.g. current or prospective)")

    # Wait for the member to respond with their type of student
    msg = await bot.wait_for('message', check=check)
    type_of_student = msg.content

        
     # Assign the new member a role based on their type of student
    if "current" in type_of_student.lower():
        role = discord.utils.get(member.guild.roles, name="Current Student")
    elif "prospective" in type_of_student.lower():
        role = discord.utils.get(member.guild.roles, name="Prospective Student")
        # Increment the accepted_students counter
        global accepted_students
        accepted_students += 1
        # Post the accepted student's information in a channel
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(f"Accepted Student {accepted_students}: Name: {name}, School/Major: {school}, Class Year: {class_year}, Type of Student: {type_of_student}")
    else:
        await member.send("Something went wrong plz contact an admin to get roled. Sry :cry:")
bot.run('BOT_TOKEN')
