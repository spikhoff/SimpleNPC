class NPC:
    def __init__(self, name, health, position, dialogue=None, behavior='friendly', quests=None):
        self._name = name
        self._health = health
        self._position = position
        self._dialogue = dialogue or ["Hello, adventurer!"]
        self._dialogue_index = 0
        self._behavior = behavior
        self._inventory = []
        self._quests = quests or []

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def position(self):
        return self._position

    @property
    def behavior(self):
        return self._behavior

    def move(self, new_position):
        self._log_action(f"moves from {self.position} to {new_position}.")
        self._position = new_position

    def take_damage(self, damage):
        self._health -= damage
        self._log_action(f"takes {damage} damage. Health is now {self.health}.")
        if self.health <= 0:
            self._log_action("has died.")

    def speak(self):
        message = self._dialogue[self._dialogue_index]
        self._log_action(f"says: '{message}'")
        self._dialogue_index = (self._dialogue_index + 1) % len(self._dialogue)

    def add_to_inventory(self, item):
        self._inventory.append(item)
        self._log_action(f"added '{item}' to inventory.")

    def show_inventory(self):
        print(f"{self.name}'s inventory: {self._inventory}")

    def give_quest(self):
        if self._quests:
            quest = self._quests.pop(0)
            self._log_action(f"gives the quest: '{quest}'")
        else:
            self._log_action("has no quests to give.")

    def interact(self):
        if self._behavior == 'friendly':
            self.speak()
            self.give_quest()
        elif self._behavior == 'hostile':
            print(f"{self.name} attacks!")

    def _log_action(self, action):
        print(f"{self.name} {action}")


# Example usage:
npc = NPC(
    name="Guard",
    health=100,
    position=(0, 0),
    dialogue=["Welcome to our town!", "Need any help?", "Stay safe out there!"],
    behavior='friendly',
    quests=["Defeat the dragon", "Collect 10 herbs"]
)

#
