import numbers

class Vector:
    """A simple class that represents a 3D vector and supports typical vector algebra operations needed in basic physics modeling."""
    def __init__(self, x, y, z):
        if isinstance(x, (int, float)):
            self.x = x
        else:
            raise TypeError
        
        if isinstance(y, (int, float)):
            self.y = y
        else:
            raise TypeError
            
        if isinstance(z, (int, float)):
            self.z = z
        else:
            raise TypeError
        
    def __repr__(self):
        return "Vector({},{},{})".format(self.x, self.y, self.z)
    
    def __str__(self):
        return "<{},{},{}>".format(self.x, self.y, self.z)
    
    def __add__(self, other):
        """Defines addition for the Vector Class."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented
    
    def __sub__(self, other):
        """Defines subtraction for the Vector Class."""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return NotImplemented
    
    def __mul__(self, other):
        """Defines scalar multiplication for the Vector Class."""
        if isinstance(other, numbers.Real):
            return Vector(other*self.x, other*self.y, other*self.z)
        return NotImplemented
    
    def __rmul__(self, other):
        """Defines scalar mulitplication, where the scalar follows the vector for the Vector Class."""
        if isinstance(other, numbers.Real):
            return Vector(other*self.x, other*self.y, other*self.z)
        return NotImplemented
    
    def __truediv__(self, other):
        """Defines scalar division for the Vector Class."""
        if isinstance(other, numbers.Real):
            return Vector(self.x/other, self.y/other, self.z/other)
        return NotImplemented
    
    def __neg__(self):
        """Defines negation for the Vector Class."""
        return Vector(-1*self.x, -1 * self.y, -1 * self.z)
    
    def __iter__(self):
        """Returns an iterator so that the coordinates of the vector object can be looped over iteratively."""
        return iter((self.x, self.y, self.z))
    
    def mag(self):
        """Returns the magnitude of the vector."""
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def dot(self, other):
        """Returns the dot product of the current vector and another vector. Argument must be a Vector class object."""
        if isinstance(other, Vector): 
            return self.x*other.x + self.y*other.y + self.z*other.z
        return NotImplemented
    
    def hat(self):
        """Return a unit vector from the current vector."""
        mag = self.mag()
        return Vector(self.x/mag, self.y/mag, self.z/mag)
    
    def cross(self, other):
        """Returns the cross product of the current vector with another vector. Argument must be a Vector class object."""
        if isinstance(other, Vector):
            cx = self.y*other.z - self.z*other.y
            cy = self.z*other.x - self.x*other.z
            cz = self.x*other.y - self.y*other.x

            return Vector(cx, cy, cz)
        
        return NotImplemented