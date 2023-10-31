import discord
import random

from discord.ui import Button, View

class CringeSaveButtonView(discord.ui.View):

    def __init__(self, name, level):
        self.name = name
        self.level = level
        discord.ui.View.__init__(self)

    @discord.ui.button(label="Save!", style=discord.ButtonStyle.primary)
    async def button_callback(self, button, interaction):
        dices=[1, 4, 6, 8, 10]

        difficulty = 2
        if(self.level > 1 and self.level < 6):
            difficulty = 5 * (self.level - 1)
        elif(self.level > 5):
            difficulty = 20
        else:
            difficulty = 2

        roll = random.randint(1, 20)

        if(roll == 20 or roll >= difficulty):
            await interaction.response.send_message(f"Saving throw passed! {roll} vs {difficulty}.")
            return
        
        if(roll == 1 or roll < difficulty):
            damage = random.randint(1, dices[self.level - 1])
            await interaction.response.send_message(f"Saving throw failed! {roll} vs {difficulty}. Take {str(damage)} (1d{str(dices[self.level - 1])}) cringe damage!")
        
        await interaction.response.send_message("Something went wrong...")
        