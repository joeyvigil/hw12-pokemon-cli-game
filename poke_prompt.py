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
        
        response= get_pokemon_data(pokemon_identifier)
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

def get_pokemon_data(pokemon_identifier):
    return requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_identifier}')
            
            
        
class Player:
    """Represents a player with a collection of Pokemon"""
    
    def __init__(self, name):
        self.name = name
        self.collection = []  # List of Pokemon objects
    
    def add_pokemon(self, pokemon):
        """Add a Pokemon to the collection (max 6 Pokemon)"""
        if len(self.collection) < 6:
            self.collection.append(pokemon)
            print(f"{pokemon.name} added to {self.name.title()}'s collection!")
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

class PokemonGame:
    def __init__(self):
        self.player = None
        self.wild_pokemon = None
        
    def start_game(self):
        os.system('cls||clear')
        print(pyfiglet.figlet_format('PokePrompt', font="slant"))
        trainer = input("What is your trainers name? ")
        self.player = Player(trainer)
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
            self.player.add_pokemon(Pokemon('bulbasaur'))
        if choose =='2':
            self.player.add_pokemon(Pokemon('charmander'))
        if choose =='3':
            self.player.add_pokemon(Pokemon('squirtle'))
        
    def  go_hunting(self):
        os.system('cls||clear')
        print("A wild Pokémon appears...")
        self.wild_pokemon = Pokemon(random.randint(1,151))
        self.wild_pokemon.info()
        choose2 = ''
        while (choose2!='yes' and choose2!='no'):
            choose2 = input(f"Do you want to attempt to catch {self.wild_pokemon.name}? (40%) (yes/no): ")
        if choose2 =='yes':
            self.try_catch_pokemon()
        input('')
        
    def  try_catch_pokemon(self):
        if (random.random()<.4): #40% catch rate, 25% was too low
            print(f"{self.wild_pokemon.name} was caught!")
            self.player.add_pokemon(self.wild_pokemon)
        else:
            print(f"Oh no! {self.wild_pokemon.name} broke free!")
    
    def  view_collection(self):
        os.system('cls||clear')
        print(f"===== {self.player.name.title()}'s Collection =====")
        self.player.show_collection()
        choose3 = ''
        while (choose3!='no' and choose3!='1' and choose3!='2' and choose3!='3' and choose3!='4' and choose3!='5' and choose3!='6'):
            choose3 = input(f"Which Pokémon do you want to inspect? (1-{len(self.player.collection)},no): ")
        if choose3 =='1':
            if len(self.player.collection)>=1:
                self.player.collection[0].info()
                input('')
        if choose3 =='2':
            if len(self.player.collection)>=2:
                self.player.collection[1].info()
                input('')
        if choose3 =='3':
            if len(self.player.collection)>=3:
                self.player.collection[2].info()
                input('')
        if choose3 =='4':
            if len(self.player.collection)>=4:
                self.player.collection[3].info()
                input('')
        if choose3 =='5':
            if len(self.player.collection)>=5:
                self.player.collection[4].info()
                input('')
        if choose3 =='6':
            if len(self.player.collection)>=6:
                self.player.collection[5].info()
                input('')
        if choose3 =='no':
            pass   
        
    def  remove_pokemon_menu(self):
        os.system('cls||clear')
        print(f"===== {self.player.name.title()}'s Collection =====")
        self.player.show_collection()
        choose4 = ''
        while (choose4!='no' and choose4!='1' and choose4!='2' and choose4!='3' and choose4!='4' and choose4!='5' and choose4!='6'):
            choose4 = input(f"Which Pokemon do you want to set free? (1-{len(self.player.collection)},no): ")
        if choose4 =='1':
            if len(self.player.collection)>=1:
                print(f"{self.player.collection[0].name} removed from {self.player.name}'s collection")
                self.player.remove_pokemon(0)
                input('')
        if choose4 =='2':
            if len(self.player.collection)>=2:
                print(f"{self.player.collection[1].name} removed from {self.player.name}'s collection")
                self.player.remove_pokemon(1)
                input('')
                
        if choose4 =='3':
            if len(self.player.collection)>=3:
                print(f"{self.player.collection[2].name} removed from {self.player.name}'s collection")
                self.player.remove_pokemon(2)
                input('')
        if choose4 =='4':
            if len(self.player.collection)>=4:
                print(f"{self.player.collection[3].name} removed from {self.player.name}'s collection")
                self.player.remove_pokemon(3)
                input('')
        if choose4 =='5':
            if len(self.player.collection)>=5:
                print(f"{self.player.collection[4].name} removed from {self.player.name}'s collection")
                self.player.remove_pokemon(4)
                input('')
        if choose4 =='6':
            if len(self.player.collection)>=6:
                print(f"{self.player.collection[5].name} removed from {self.player.name}'s collection")
                self.player.remove_pokemon(5)
                input('')

def main():
    #---------- Start, choose name, Choose Starter----------
    game = PokemonGame()
    game.start_game()

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
            game.go_hunting()
              
        # ------ 2) View Collection -------
        if choose =='2':
            game.view_collection()
            
        # ------ 3) Set Pokémon Free (remove from collection) -------
        if choose =='3':
            game.remove_pokemon_menu()
            
        # ------ 4) Quit Game -------
        if choose =='4':
            break


if __name__ == '__main__': 
    main()

