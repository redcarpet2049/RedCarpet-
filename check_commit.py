# check_commit.py
# Randomly generates a fake movie review score

import random

MOVIES = [
    "Inception", "Interstellar", "The Matrix",
    "Blade Runner 2049", "Dune", "Oppenheimer"
]

def generate_review(movie: str) -> dict:
    return {
        "movie": movie,
        "score": round(random.uniform(6.0, 10.0), 1),
        "votes": random.randint(1000, 500000),
        "verdict": random.choice(["Must Watch", "Great", "Solid", "Decent"])
    }

if __name__ == "__main__":
    pick = random.choice(MOVIES)
    review = generate_review(pick)
    print(f"Movie   : {review['movie']}")
    print(f"Score   : {review['score']} / 10")
    print(f"Votes   : {review['votes']:,}")
    print(f"Verdict : {review['verdict']}")
