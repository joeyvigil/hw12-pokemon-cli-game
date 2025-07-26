import requests                         #pip install requests
from ascii_magic import AsciiArt        #pip install ascii-magic
import pyfiglet                         #pip install pyfiglet
import random
import os

class Pokemon:
    """Represents a Pokemon with basic stats, gets information from api"""
    
    def __init__(self, pokemon_identifier):
        self.name = None
        self.id = None
        self.hp = None
        self.attack = None
        self.defense = None
        self.speed = None
        self.weight = None
        self.height = None
        self.sprite_url = None
        self.type = None
        
        url  = f'https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}'
        response= requests.get(url)
        # print(response.status_code)
        
        if response.status_code==200:
            data = response.json()
            # print(data['name'])
            for stat in data['stats']:
                if(stat['stat']['name']=='hp'):
                    hp = stat['base_stat']
                if(stat['stat']['name']=='attack'):
                    attack = stat['base_stat']
                if(stat['stat']['name']=='defense'):
                    defense = stat['base_stat']
                if(stat['stat']['name']=='speed'):
                    speed = stat['base_stat']
            types =''
            for a_type in data['types']:
                types= types+" "+a_type['type']['name']

            self.name = data['name']
            self.id = data['id']
            self.hp = hp
            self.attack = attack
            self.defense = defense
            self.speed = speed
            self.weight = data['weight']
            self.height = data['height']
            self.sprite_url = data['sprites']['other']['official-artwork']['front_default']
            self.type = types
            
        else:
            print("response code: ",response.status_code)

    def info(self):
        if self.name !=None:
            print(pyfiglet.figlet_format(self.name.title(), font="bulbhead"))
            try:
                AsciiArt.from_url(self.sprite_url).to_terminal(columns=35) #30
            except:
                pass
            print(f'''============ {self.name.title()} (ID: {self.id}) ============
    HP: {self.hp}\t\tSpeed: {self.speed}
    Attack: {self.attack}\t\tDefense: {self.defense}
    Height (m): {self.height/10}\tWeight (kg): {self.weight/10}  
    Type: {self.type}
            ''')
        
class Player:
    """Represents a player with a collection of Pokemon"""
    
    def __init__(self, name):
        self.name = name
        self.collection = []  # List of Pokemon objects
    
    def add_pokemon(self, pokemon):
        """Add a Pokemon to the collection (max 6 Pokemon)"""
        if len(self.collection) < 6:
            self.collection.append(pokemon)
            print(f"{pokemon.name} added to {self.name}'s collection!")
            return True
        else:
            print(f"Collection is full! Can't add {pokemon.name}")
            return False
    
    def show_collection(self):
        for i,pokemon in enumerate(self.collection):
            # 1. Pikachu (ID: 25) - electric type
            print(f"{i+1}. {pokemon.name.title()} (ID {pokemon.id}) - {pokemon.type} type")
    
    def remove_pokemon(self, index): 
        '''[0,1,2,3] want to remove last, remove_pokemon(3), if 3 <= len(4)-1 True, goes in loop'''
        if index >=0 and index <=len(self.collection)-1:
            return self.collection.pop(index)


def main():
    #---------- Start, choose name ----------
    os.system('cls||clear')
    print(pyfiglet.figlet_format('PokePrompt', font="slant"))
    trainer = input("What is your trainers name? ")
    trainer = Player(trainer)
    
    #---------- Choose Starter ----------
    print(f'''
Oak: Here, take one of these rare Pokémon:
1) Bulbasaur
2) Charmander
3) Squirtle
          ''')
    choose = ''
    while (choose!='1' and choose!='2' and choose!='3'):
        choose = input("What Pokémon do you want? (1,2,3): ")
    if choose =='1':
        trainer.add_pokemon(Pokemon('bulbasaur'))
    if choose =='2':
        trainer.add_pokemon(Pokemon('charmander'))
    if choose =='3':
        trainer.add_pokemon(Pokemon('squirtle'))
        
    #---------- Main loop ----------
    while True:
        os.system('cls||clear')
        print(f'''
---------- Main Menu: ----------
1) Search for new Pokémon
2) View Collection
3) Set Pokémon Free (remove from collection)
4) Quit Game
          ''')
        choose = ''
        while (choose!='1' and choose!='2' and choose!='3' and choose!='4'):
            choose = input("What do you want to do? (1,2,3,4): ")
        # ------ 1) Search for new Pokémon -------
        if choose =='1':
            os.system('cls||clear')
            print("A wild Pokémon appears...")
            wild = Pokemon(random.randint(1,1025))
            wild.info()
            choose = ''
            while (choose!='yes' and choose!='no'):
                choose = input(f"Do you want to attempt to catch {wild.name}? (40%) (yes/no): ")
            if choose =='yes':
                if (random.random()<.4): #40% catch rate, 25% was too low
                    print(f"{wild.name} was caught!")
                    trainer.add_pokemon(wild)
                else:
                    print(f"Oh no! {wild.name} broke free!")
            input('')
                    
        # ------ 2) View Collection -------
        if choose =='2':
            os.system('cls||clear')
            print(f"===== {trainer.name.title()}'s Collection =====")
            trainer.show_collection()
            choose = ''
            while (choose!='no' and choose!='1' and choose!='2' and choose!='3' and choose!='4' and choose!='5' and choose!='6'):
                choose = input(f"Which Pokémon do you want to inspect? (1-6,no): ")
            if choose =='1':
                if len(trainer.collection)>=1:
                    trainer.collection[0].info()
                    input('')
            if choose =='2':
                if len(trainer.collection)>=2:
                    trainer.collection[1].info()
                    input('')
            if choose =='3':
                if len(trainer.collection)>=3:
                    trainer.collection[2].info()
                    input('')
            if choose =='4':
                if len(trainer.collection)>=4:
                    trainer.collection[3].info()
                    input('')
            if choose =='5':
                if len(trainer.collection)>=5:
                    trainer.collection[4].info()
                    input('')
            if choose =='6':
                if len(trainer.collection)>=6:
                    trainer.collection[5].info()
                    input('')
            if choose =='no':
                pass   
                        
            
        # ------ 3) Set Pokémon Free (remove from collection) -------
        if choose =='3':
            os.system('cls||clear')
            print(f"===== {trainer.name.title()}'s Collection =====")
            trainer.show_collection()
            choose = ''
            while (choose!='no' and choose!='1' and choose!='2' and choose!='3' and choose!='4' and choose!='5' and choose!='6'):
                choose = input(f"Which Pokemon do you want to set free? (1-6,no): ")
            if choose =='1':
                if len(trainer.collection)>=1:
                    print(f"{trainer.collection[0].name} removed from {trainer.name}'s collection")
                    trainer.remove_pokemon(0)
                    input('')
            if choose =='2':
                if len(trainer.collection)>=2:
                    print(f"{trainer.collection[1].name} removed from {trainer.name}'s collection")
                    trainer.remove_pokemon(1)
                    input('')
                    
            if choose =='3':
                if len(trainer.collection)>=3:
                    print(f"{trainer.collection[2].name} removed from {trainer.name}'s collection")
                    trainer.remove_pokemon(2)
                    input('')
            if choose =='4':
                if len(trainer.collection)>=4:
                    print(f"{trainer.collection[3].name} removed from {trainer.name}'s collection")
                    trainer.remove_pokemon(3)
                    input('')
            if choose =='5':
                if len(trainer.collection)>=5:
                    print(f"{trainer.collection[4].name} removed from {trainer.name}'s collection")
                    trainer.remove_pokemon(4)
                    input('')
            if choose =='6':
                if len(trainer.collection)>=6:
                    print(f"{trainer.collection[5].name} removed from {trainer.name}'s collection")
                    trainer.remove_pokemon(5)
                    input('')
            
        # ------ 4) Quit Game -------
        if choose =='4':
            break


if __name__ == '__main__': 
    main()

