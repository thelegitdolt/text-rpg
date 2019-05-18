class MotionTracker:
    """Track the motion of an object, as determined by some text-based commands.

    Must be able to:
      - retrieve the x and y coordinates
      - retrieve the current direction as a string: "north", "south", "east",
        or "west"
      - turn left or right
      - move one unit in the direction it's facing (as on a coordinate plane)
    Initially, the object is facing north and is at (0,0). See the examples
    below for clarification.

    >>> mt = MotionTracker()
    >>> mt.get_direction()
    'north'
    >>> mt.get_x()
    0
    >>> mt.get_y()
    0
    >>> mt.move()
    >>> mt.move()
    >>> mt.get_x()
    0
    >>> mt.get_y()
    2
    >>> mt.turn_left()
    >>> mt.get_direction()
    'west'
    >>> mt.move()
    >>> mt.get_x()
    -1
    >>> mt.get_y()
    2
    >>> mt.turn_left()
    >>> mt.get_direction()
    'south'

    Some of these will get pretty tedious - lots of if/elif/else. Sorry :(.
    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "north"

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_direction(self):
        return self.direction

    def turn_left(self):
        if self.direction == "north":
            self.direction = "west"
        elif self.direction == "west":
            self.direction = "south"
        elif self.direction == "south":
            self.direction = "east"
        elif self.direction == "east":
            self.direction = "north"

    def turn_right(self):
        if self.direction == "north":
            self.direction = "east"
        elif self.direction == "west":
            self.direction = "north"
        elif self.direction == "south":
            self.direction = "west"
        elif self.direction == "east":
            self.direction = "south"

    def move(self, stepSize = 1):
        if self.direction == "north":
            self.y += stepSize
        elif self.direction == "west":
            self.x -= stepSize
        elif self.direction == "south":
            self.y -= stepSize
        elif self.direction == "east":
            self.x += stepSize

class Player:
    def __init__(self):
         self.health = 10
         self.mt = MotionTracker()

    def take_damage(self, damage):
        self.health -= damage
        print("you took {} damage!".format(damage))

    def is_dead(self):
        return self.health <= 0


def process_command(mt: MotionTracker, command: str) -> str:
    #go forward, turn right, turn left, where am i
    #if it's go forward
    if command == "go forward":
        mt.move()
        return "done"
    elif command == "go right":
        mt.turn_right()
        mt.move()
        return "done"
    elif command == "go left":
        mt.turn_left()
        mt.move()
        return "done"
    elif command == "go backwards":
        mt.turn_right()
        mt.turn_right()
        mt.move()
        return "done"
    elif command == "where am i"
        return "You are at ({}, {})".format(mt.get_x(),mt.get_y())

p = Player()
while not p.is_dead():
    command = input("What do you want to do?\n> ")
    result = process_command(p.mt, command)
    print(result)
    if (p.mt.get_x(), p.mt.get_y()) == (1,1):
        p.take_damage(10)

print("Noob You Failed")