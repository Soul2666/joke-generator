import time
import random
import subprocess

def generate_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He will stop at nothing to avoid them!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why don't eggs tell jokes? Because they might crack up!",
    ]
    return random.choice(jokes)

def display_joke(joke):
    command = f"display notification \"{joke}\" with title \"Joke of the Hour\""
    subprocess.call(["osascript", "-e", command])

def main():
    while True:
        joke = generate_joke()
        display_joke(joke)
        time.sleep(3600)  # Sleep for 1 hour (3600 seconds)

if __name__ == "__main__":
    main()
