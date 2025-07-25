import requests                         #pip install requests
from ascii_magic import AsciiArt        #pip install ascii-magic
import pyfiglet                         #pip install pyfiglet
import random

class Pokemon:
    """Represents a Pokemon with basic stats, gets information from api"""
    
    def __init__(self, pokemon_identifier):
        self.name = None
        self.id = None
        self.hp = None
        self.attack = None
        self.defense = None
        self.speed = None
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
            self.sprite_url = data['sprites']['other']['official-artwork']['front_default']
            self.type = types
            
        else:
            print("response code: ",response.status_code)

            
    def info(self):
        """Print the Pokemon's information"""
        print(f"{self.name} (ID: {self.id})")
        print(f"   HP: {self.hp}")
        print(f"   Attack: {self.attack}")
        print(f"   Type: {self.type}")
        print(f"   Sprite: {self.sprite_url}")
    
    def fancy_info(self):
        if self.name !=None:
            print(pyfiglet.figlet_format(self.name.title(), font="bulbhead"))
            try:
                AsciiArt.from_url(self.sprite_url).to_terminal(columns=30)
            except:
                pass
            print(f"\n========== {self.name.title()} (ID: {self.id}) ==========")
            print(f"   HP: {self.hp}")
            print(f"   Attack: {self.attack}")
            print(f"   Defense: {self.defense}")
            print(f"   Speed: {self.speed}")
            print(f"   Type: {self.type}")
        
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
        '''[0,1,2,3] want to remove last, remove_pokemon(3) if 3 <= len(4)-1 True, goes in loop'''
        if index >=0 and index <=len(self.collection)-1:
            return self.collection.pop(index)

def main():
    while True:
        pika = Pokemon(random.randint(1,1000))
    # print(pika.sprite_url)
    # AsciiArt.from_url(pika.sprite_url).to_terminal(columns=50)
    # pika.info()
        pika.fancy_info()
        a = input('hi')
    #---------- Start, choose name ----------
    
    #---------- Choose Starter ----------
    
    #---------- Main loop ----------
        # Menu:
        # 1 search
        # 2 view collection
        # 3. remove pokemon from collection
        # 4. quit game
    
    #---------- Start ----------
    
    #---------- Start ----------
    pass

if __name__ == '__main__': 
    main()


