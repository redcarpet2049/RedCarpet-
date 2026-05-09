# utils.py
# Returns a random fun fact about space

import random

FACTS = [
    "A day on Venus is longer than a year on Venus.",
    "Neutron stars can spin 600 times per second.",
    "The footprints on the Moon will last 100 million years.",
    "One million Earths could fit inside the Sun.",
    "There are more stars in the universe than grains of sand on Earth.",
    "Saturn would float if placed in water — it is less dense.",
    "Light from the Sun takes 8 minutes and 20 seconds to reach Earth.",
]

def random_fact() -> str:
    return random.choice(FACTS)

if __name__ == "__main__":
    print("Space Fact:", random_fact())
