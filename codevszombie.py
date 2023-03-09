import sys
import math
import enum
import time

def dbg(m: str):
    print(f"[DBG] {m}", file=sys.stderr, flush=True)

class PersonType(enum.Enum):
    UNDEFINED = 0
    HUMAN = 1
    ZOMBIE = 2
    ASH = 3 # Because he's much more than a simple human

class Person:
    def __init__(self, ptype=PersonType.UNDEFINED, id=0, x=0, y=0) -> None:
        self.type = ptype
        self.id = id
        self.x = x
        self.y = y
    def setCoordinates(self, x : int, y : int):
        self.x = x
        self.y = y
    def dbgPrint(self):
        dbg(f"{self.type} #{self.id} [{self.x},{self.y}]")

if __name__ == "__main__":
    game_loop = 0
    dhumans = dict()
    dzombies = dict()
    Ash = Person(PersonType.ASH)

    #############
    # Game loop #
    #############
    while True:
        starting_time = time.perf_counter()
        # Ash's coordinates
        x, y = [int(i) for i in input().split()]
        Ash.setCoordinates(x, y)
        Ash.dbgPrint()

        # Number of alived humans
        human_count = int(input())
        dbg(f"Number of humans = {human_count}")
        # For each human : its UID and its coordinates
        for i in range(human_count):
            human_id, human_x, human_y = [int(j) for j in input().split()]
            dhumans.setdefault(human_id, Person(PersonType.HUMAN, human_id, human_x, human_y))
            dhumans.get(human_id).dbgPrint()
        # Number of 'alived' zombies
        zombie_count = int(input())
        # For each zombie : its UID, its current coordinates, its next coordinates
        for i in range(zombie_count):
            zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
            dzombies.setdefault(zombie_id, Person(PersonType.ZOMBIE, zombie_id, zombie_x, zombie_y))
            dzombies.get(zombie_id).dbgPrint()
        
        # Your destination coordinates
        print("0 0")
        game_loop += 1
        delta = time.perf_counter() - starting_time
        dbg(f"Turn #{game_loop} ended in {delta * 1000} ms")
