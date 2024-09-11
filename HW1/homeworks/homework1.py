from text_adventure_games import (
    games, parsing, actions, things, blocks, viz
)

cottage = things.Location(
    "Cottage",
    "You are standing in a small cottage."
)
garden_path = things.Location(
    "Garden Path",
    "You are standing on a lush garden path. There is a cottage here.",
)
fishing_pond = things.Location(
    "Fishing Pond",
    "You are at the edge of a small fishing pond."
)
winding_path = things.Location(
    "Winding Path",
    "You are walking along a winding path. There is a tall tree here.",
)
top_of_tree = things.Location(
    "Top of the Tall Tree",
    "You are the top of the tall tree."
)
drawbridge = things.Location(
    "Drawbridge",
    "You are standing on one side of a drawbridge leading to ACTION CASTLE.",
)
courtyard = things.Location(
    "Courtyard",
    "You are in the courtyard of ACTION CASTLE."
)
tower_stairs = things.Location(
    "Tower Stairs",
    "You are climbing the stairs to the tower. There is a locked door here.",
)
tower = things.Location(
    "Tower",
    "You are inside a tower."
)
dungeon_stairs = things.Location(
    "Dungeon Stairs",
    "You are climbing the stairs down to the dungeon."
)
dungeon = things.Location(
    "Dungeon",
    "You are in the dungeon. There is a spooky ghost here."
)
feasting_hall = things.Location(
    "Great Feasting Hall",
    "You stand inside the Great Feasting Hall."
)
throne_room = things.Location(
    "Throne Room",
    "This is the throne room of ACTION CASTLE."
)
death = things.Location(
    "The Afterlife",
    "You are dead. GAME OVER."
)
death.set_property("game_over", True)


# Map of Locations
cottage.add_connection("out", garden_path)
garden_path.add_connection("south", fishing_pond)
garden_path.add_connection("north", winding_path)
winding_path.add_connection("up", top_of_tree)
winding_path.add_connection("east", drawbridge)
top_of_tree.add_connection("jump", death)
drawbridge.add_connection("east", courtyard)
courtyard.add_connection("up", tower_stairs)
courtyard.add_connection("down", dungeon_stairs)
courtyard.add_connection("east", feasting_hall)
tower_stairs.add_connection("up", tower)
dungeon_stairs.add_connection("down", dungeon)
feasting_hall.add_connection("east", throne_room)

tempgame = games.Game(tower, things.Character(name="Temp Player", description="", persona=""))

from text_adventure_games.viz import Visualizer
viz = Visualizer(tempgame)
graph = viz.visualize()
fishing_pole = things.Item(
    "pole",
    "a fishing pole",
    "A SIMPLE FISHING POLE.",
)
cottage.add_item(fishing_pole)


# Put a branch in a tree that could be used as a weapon
branch = things.Item(
    "branch",
    "a stout, dead branch",
    "IT LOOKS LIKE IT WOULD MAKE A GOOD CLUB.",
)
branch.set_property("is_weapon", True)
branch.set_property("is_fragile", True)
top_of_tree.add_item(branch)


# Put a candle in the feasting hall
candle = things.Item(
    "candle",
    "a strange candle",
    "THE CANDLE IS COVERED IN STARGE RUNES.",
)
candle.set_property("is_lightable", True)
candle.set_property("is_lit", False)
candle.add_command_hint("light candle")
candle.add_command_hint("read runes")
feasting_hall.add_item(candle)

# Put an actual pond at the fishing location
pond = things.Item(
    "pond",
    "a small fishing pond",
    "THERE ARE FISH IN THE POND.",
)
pond.set_property("gettable", False)
pond.set_property("has_fish", True)
pond.add_command_hint("catch fish")
pond.add_command_hint("catch fish with pole")
fishing_pond.add_item(pond)


# A nice rosebush for the garden path
rosebush = things.Item(
    "rosebush",
    "a rosebush",
    "THE ROSEBUSH CONTAINS A SINGLE RED ROSE.  IT IS BEAUTIFUL.",
)
rosebush.set_property("gettable", False)
rosebush.set_property("has_rose", True)
rosebush.add_command_hint("pick rose")
garden_path.add_item(rosebush)


# Throne room wouldn't be that impressive without a throne
throne = things.Item(
    "throne",
    "An ornate golden throne."
)
throne.set_property("gettable", False)
throne.add_command_hint("sit on throne")
throne_room.add_item(throne)


# A door that leads to the tower stairs
door = things.Item(
    "door",
    "a door",
    "THE DOOR IS SECURELY LOCKED."
)
door.set_property("gettable", False)
door.set_property("is_locked", True)
door.add_command_hint("unlock door")
tower_stairs.add_item(door)

# Player
player = things.Character(
    name="The player",
    description="You are a simple peasant destined for greatness.",
    persona="I am on an adventure.",
)

# Player's lamp
lamp = things.Item("lamp", "a lamp", "A LAMself.")
lamp.set_property("is_lightable", True)
lamp.set_property("is_lit", False)
lamp.add_command_hint("light lamp")
player.add_to_inventory(lamp)

# A Troll at the drawbridge
troll = things.Character(
    name="troll",
    description="A mean troll",
    persona="I am hungry. The guard promised to feed me if I guard the drawbridge and keep people out of the castle.",
)
troll.set_property("is_hungry", True)
troll.set_property("character_type", "troll")
drawbridge.add_character(troll)


# A guard in the courtyard
guard = things.Character(
    name="guard",
    description="A castle guard",
    persona="I am suspicious of anyone trying to enter the castle. I will prevent keep people from entering and learning the castle's dark secrets.",
)
guard.set_property("is_conscious", True)
guard.set_property("is_suspicious", True)
guard.set_property("character_type", "human")
courtyard.add_character(guard)

# Guard has a key
key = things.Item("key", "a brass key", "THIS LOOKS USEFUL")
guard.add_to_inventory(key)

# Guard has a sword
sword = things.Item("sword", "a short sword", "A SHARP SHORT SWORD.")
sword.set_property("is_weapon", True)
guard.add_to_inventory(sword)


# A Princess in the tower
princess = things.Character(
    name="princess",
    description="A princess who is beautiful and lonely. She awaits her non-gender-stereotypical soulmate.",
    persona="I am the princess. I am grieving my father's death. I feel alone.",
)
princess.set_property("is_royal", True)
princess.set_property("emotional_state", "sad and lonely")
princess.set_property("is_married", False)
princess.set_property("character_type", "human")
tower.add_character(princess)


# A ghost in the dungeon
ghost = things.Character(
    name="ghost",
    description="A ghost with bony, claw-like fingers and who is wearing a crown.",
    persona="I was murdered by the guard. I will haunt this castle until banished. If you linger before my apparition, I will plunge my ghostly hand inside you and stop your heart",
)
ghost.set_property("character_type", "ghost")
ghost.set_property("is_dead", True)
ghost.set_property("is_banished", False)
dungeon.add_character(ghost)

# Ghost's crown
crown = things.Item("crown", "a crown", "A CROWN FIT FOR A KING.")
crown.add_command_hint("wear crown")
ghost.add_to_inventory(crown)


class Unlock_Door(actions.Action):
    ACTION_NAME = "unlock door"
    ACTION_DESCRIPTION = "Unlock a door with a key"
    ACTION_ALIASES = []

    def __init__(self, game, command):
        super().__init__(game)
        # TODO - your code here
        self.character = None
        self.key = None
        self.door = None

        self.character = self.parser.get_character(command)
        self.location = self.character.location
        self.key = self.parser.match_item(
            "key", self.parser.get_items_in_scope(self.character)
        )
        self.door = self.parser.match_item(
            "door", self.parser.get_items_in_scope(self.location)
        )
        # HINT: take a look at text_adventures/actions for some examples of actions!

    def check_preconditions(self) -> bool:
        """
        Preconditions:
        * There must be a door
        * The character must be at the same location as the door
        * The door must be locked
        * The character must have the key in their inventory
        """
        if not self.was_matched(self.door, "There's no door."):
            return False
        if not self.door.location.here(self.character):
            description = "You're not at the location of the door."
            self.game.parser.fail(description)
            return False
        if not self.has_property(self.key, "is_locked"):
            description = "The door is already unlocked."
            self.game.parser.fail(description)
            return False
        if not self.character.is_in_inventory(self.key):
            description = "You don't have a key."
            self.game.parser.fail(description)
            return False
        return True

    def apply_effects(self):
        """
        Effects:
        * Unlocks the door
        """
        self.door.set_property("is_locked", False)
        d = "{character_name} inserts the key into the door and smoothly unlock the door."
        description = d.format(
            character_name=self.character.name.capitalize(),
        )
        return self.parser.ok(description)

