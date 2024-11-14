"""
Docstrings - explinations of functions
    1. What the function does
    2. The received parameters and data types
    3. What is returned and the data type.
"""
# Global vars
jedi_name = "Luke Skywalker"
jedi_rank = "Jedi Knight"
force_power = 100
# Functions should only do one thing
def greet_all_jedi():
    """
    Greets
    """
    print("Hello Jedi")

def attack(target, weapons="lightsaber"):
    """
    Perform an attack on a target with a specified weapon.
    Parameters:
    target (str): The target being attacked.
    weapon (str): The weapon being used. Defaults to "lightsaber".
    
    Returns:
    str: The action of the attack.
    """
    jedi_name = "Obi Wan Kenobi" # local variable
    return f"{jedi_name} attacks {target} with a {weapons}"

# Take the argument outside
print(attack("Darth Vader"))
# print(attack{"Dark Maul" ", stomach slice"})
print(f"The global var jedi_name {jedi_name} was not affected")

def add_force_power(*points):
    print(points[0])
    print(points[1])



    total_power = sum(points)
    global force_power  # uses global force_power, not the local
    force_power += total_power
    return force_power

print(f"Jedis Force power after battle: {add_force_power(50, 75, 25, 12, 6)}")
print(f"The global var force power has changed to {force_power}")


def use_force(power, **kwargs):
    """
    Use the Force to perform an action with additional effects.
    Parameters:
    power (str): The type of Force power.
    **kwargs: Additional named arguments (e.g., 'duration', 'intensity').
        - accepts "key = value" arguments and puts them in a dictionary
    Returns:
    str: Description of the Force action.
    """
    action_details = ""
    
    for key, value in kwargs.items():
        action_details += key + " : "
        action_details += value + " | "  
  
    
    # another way of doing this using a shorthand method
    #action_details = ' | '.join(f"{key}: {value}" for key, value in kwargs.items())
    
    return f"{jedi_name} uses {power} with the following effects: {action_details}."
print(use_force("Telekinesis", duration="5 seconds", intensity="High"))


"""
{
    jey: value,
    2nd_key: 2nd_value,

    Example below
}


{
    duration: "5 seconds",
    intensity: "High",
}
"""

    

