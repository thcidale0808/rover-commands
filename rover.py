

class Rover:
    x:int
    y:int
    max_x:int
    max_y:int
    direction:str
    NORTH_DIRECTION = 'N'
    SOUTH_DIRECTION = 'S'
    EAST_DIRECTION = 'E'
    WEST_DIRECTION = 'W'
    LEFT_INSTRUCTION = 'L'
    RIGHT_INSTRUCTION = 'R'
    MOVE_INSTRUCTION = 'M'
    X_POSITION = 'x'
    Y_POSITION = 'y'
    DIRECTION = 'direction'

    def __init__(self,max_x:int, max_y:int, x:int, y:int, direction:str):
        self.x = x
        self.y = y
        self.direction = direction
        self.max_x = max_x
        self.max_y = max_y

    def move(self) -> None:
        """
        Move the rover coordinate in 1 unit based on its direction
        """
        if self.direction == self.NORTH_DIRECTION:
            self.y += 1
        elif self.direction == self.SOUTH_DIRECTION:
            self.y -= 1
        elif self.direction == self.EAST_DIRECTION:
            self.x += 1
        elif self.direction == self.WEST_DIRECTION:
            self.x -= 1

    def rotate(self, instruction:str) -> None:
        """
        Rotate rover direction based on the given instruction
        """
        if self.direction == self.NORTH_DIRECTION:
            self.direction = self.EAST_DIRECTION if instruction == self.RIGHT_INSTRUCTION else self.WEST_DIRECTION
        elif self.direction == self.SOUTH_DIRECTION:
            self.direction = self.WEST_DIRECTION if instruction == self.RIGHT_INSTRUCTION else self.EAST_DIRECTION
        elif self.direction == self.EAST_DIRECTION:
            self.direction = self.SOUTH_DIRECTION if instruction == self.RIGHT_INSTRUCTION else self.NORTH_DIRECTION
        elif self.direction == self.WEST_DIRECTION:
            self.direction = self.NORTH_DIRECTION if instruction == self.RIGHT_INSTRUCTION else self.SOUTH_DIRECTION

    def move_to_target(self, instructions:str) -> None:
        """
        Move the rover to the target coordinates
        """
        #loop through all instructions
        for instruction in instructions:
            #check if needs to move or rotate
            if instruction == self.MOVE_INSTRUCTION:
                self.move()
            elif instruction == self.LEFT_INSTRUCTION or instruction == self.RIGHT_INSTRUCTION:
                self.rotate(instruction)
        
        #raise exception if the final coordinates exceed plateau size
        if self.x >self.max_x or self.y >self.max_y:
            raise Exception('Invalid instructions for rover') 

    def to_dict(self) -> dict:
        """
        Create dictionary of the current coordinates
        """
        rover_dict = dict()
        rover_dict[self.X_POSITION] = self.x 
        rover_dict[self.Y_POSITION] = self.y
        rover_dict[self.DIRECTION] = self.direction
        return rover_dict