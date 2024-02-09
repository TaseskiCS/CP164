"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""



class Food:
    """
    Defines an object for a single Food: name, origin, vegetarian, calories.
    """
    # Constants
    ORIGIN = ("Canadian", "Chinese", "Indian", "Ethiopian",
              "Mexican", "Greek", "Japanese", "Italian", "American",
              "Scottish", "New Zealand", "English")

    @staticmethod
    def origins():
        """
        -------------------------------------------------------
        Creates a string list of food origins in the format:
           0 Canadian
           1 Chinese
           2 Indian
           ...
        Use: s = Food.origins()
        Use: print(Food.origins())
        -------------------------------------------------------
        Returns:
            string - A numbered list of valid food origins (str)
        -------------------------------------------------------
        """
        s = ""
        for x in range(0, len(Food.ORIGIN)):
            s += ("{:2d} {}\n".format(x, Food.ORIGIN[x]))

        return s



    def __init__(self, name, origin, is_vegetarian, calories):
        """
        -------------------------------------------------------
        Initialize a food object.
        Use: source = Food(name, origin, is_vegetarian, calories)
        -------------------------------------------------------
        Parameters:
            name - food name (str)
            origin - food origin (int)
            is_vegetarian - whether food is vegetarian (boolean)
            calories - caloric content of food (int >= 0)
        Returns:
            A new Food object (Food)
        -------------------------------------------------------
        """
        assert origin in range(len(Food.ORIGIN)), "Invalid origin ID"
        assert is_vegetarian in (True, False, None), "Must be True or False"
        assert calories is None or calories >= 0, "Calories must be >= 0"

        self.name = name
        self.origin = origin
        self.is_vegetarian = is_vegetarian
        self.calories = calories
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of source data.
        Use: print(source)
        Use: s = str(source)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of source (str)
        -------------------------------------------------------
        """
        s = "{:11s} {}\n{:11s} {}\n{:11s} {}\n{:11s} {}".format("Name: ", self.name, "Origin:", Food.ORIGIN[self.origin], "Vegetarian:", self.is_vegetarian, "Calories:", self.calories)
        
        

        # your code here

        return s

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares this food against another food for equality.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - [right side] Food object to compare to (Food)
        Returns:
            result - True if name and origin match, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.name.lower(), self.origin) == \
            (target.name.lower(), target.origin)
        return result

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if this food precedes or is or equal to another.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - [right side] Food object to compare to (Food)
        Returns:
            result - True if this food precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.name.lower(), self.origin) < \
            (target.name.lower(), target.origin)
        return result

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if this food precedes or is or equal to another.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - [right side] Food object to compare to (Food)
        Returns:
            result - True if this food precedes or is equal to target,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        result = self < target or self == target
        return result

    def write(self, file_variable):
        """
        -------------------------------------------------------
        Writes a single line of food data to an open file.
        Use: source.write(file_variable)
        -------------------------------------------------------
        Parameters:
            file_variable - an open file of food data (file)
        Returns:
            The contents of food are written as a string in the format
              name|origin|is_vegetarian to file_variable.
        -------------------------------------------------------
        """
        print(f"{self.name}|{self.origin}|{self.is_vegetarian}|{self.calories}",
              file=file_variable)
        return

    def key(self):
        """
        -------------------------------------------------------
        Creates a formatted string of food key data.
        Use: key = source.key()
        -------------------------------------------------------
        Returns:
            the formatted contents of food key (str)
        -------------------------------------------------------
        """
        return "{}, {}".format(self.name, self.origin)

    def __hash__(self):
        """
        -------------------------------------------------------
        Generates a hash value from a food name.
        Use: h = hash(source)
        -------------------------------------------------------
        Returns:
            value - the total of the characters in the name string (int > 0)
        -------------------------------------------------------
        """
        value = 0

        for c in self.name:
            value = value + ord(c)
        return value