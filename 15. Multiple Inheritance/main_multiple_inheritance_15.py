'''
    Python support multiple inheritance, satu class mewarisi (inherit) banyak class

    Misal class Hero mewarisi attribute dan method dari class Tipe_hero dan Team
'''

class Team():
    '''
        Class team
    '''
    def setTeam(self, team: str) -> None:
        '''
            Method untuk set team
        '''
        self.team = team

    def showTeam(self) -> str:
        '''
            Method untuk menampilkan team dari object
        '''
        return self.team


class Type_Hero:
    '''
        Class dari tipe hero
    '''
    def setType(self, type: str) -> None:
        '''
            Method untuk Set tipe hero
        '''
        self.type = type

    def showType(self) -> str:
        '''
            Method untuk menampilkan tipe dari object
        '''
        return self.type

class Hero(Team, Type_Hero):
    '''
        Class Hero, mewarisi (inherit) dari class Team dan class Type_Hero
    '''
    def __init__(self, name:str) -> None:
        '''
            Constructor object
        '''
        self.name = name

layla = Hero("Layla") # Instansiasi object
layla.setTeam("Biru") # Set team
layla.setType("Marksman") # set tipe hero

print(f"Team dari {layla.name} adalah: {layla.showTeam()}") # Team dari Layla adalah: Biru
print(f"Type dari {layla.name} adalah: {layla.showType()}") # Type dari Layla adalah: Marksman