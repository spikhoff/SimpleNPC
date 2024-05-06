class NPC:
    def __init__(self, name, health, position):
        self._name = name
        self._health = health
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def position(self):
        return self._position

    def move(self, new_position):
        self._log_action(f"moves from {self.position} to {new_position}.")
        self._position = new_position

    def take_damage(self, damage):
        self._health -= damage
        self._log_action(f"takes {damage} damage. Health is now {self.health}.")
        if self.health <= 0:
            self._log_action("has died.")

    def speak(self, message="Hello, adventurer!"):
        self._log_action(f"says: '{message}'")

    def _log_action(self, action):
        print(f"{self.name} {action}")

# Example usage:
npc = NPC(name="Guard", health=100, position=(0, 0))

# Make the NPC speak with a custom message
npc.speak(message="Welcome to our village!")

# Move the NPC to a new position
npc.move(new_position=(10, 5))

# Make the NPC take damage
npc.take_damage(damage=20)
