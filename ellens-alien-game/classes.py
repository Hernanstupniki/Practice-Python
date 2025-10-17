"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        Alien.total_aliens_created += 1
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

    
    def hit(self):
        self.health = self.health - 1
        return self.health
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def collision_detection(self, object):
        pass


alien = Alien(2, 0)

alien.x_coordinate  # 2
alien.y_coordinate  # 0
alien.health        # 3

alien.hit()
alien.health        # 2
alien.is_alive()   # True

alien.hit()
alien.health        # 1
alien.is_alive()    # True

alien.teleport(5, -4)
alien.x_coordinate  # 5
alien.y_coordinate  # -4



#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

def new_aliens_collection(coordinates):
    alienlist = []
    for coordinate in coordinates:
        x_coordinate = coordinate[0]
        y_coordinate = coordinate[1]
        new_alien = Alien(x_coordinate, y_coordinate)
        alienlist.append(new_alien)
    return alienlist


alien_start_positions = [(4, 7), (-1, 0)]
aliens = new_aliens_collection(alien_start_positions)

for alien in aliens:
    	print(alien.x_coordinate, alien.y_coordinate)
(4, 7)
(-1, 0)
