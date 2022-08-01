import time
import random
import sys


def print_pause(message):
    print(message)
    time.sleep(2)


def start(hamtaro_villain):
    print_pause("Your name is Hamtaro, you are a young"
                " hamster from a small fishing village in Japan."
                " You are from a long line of Samurai warriors,"
                " but you're the grunt of the family."
                " There has just been a major wind storm,"
                " and you have been blown all the way to Tokyo."
                " The city is in ruins, and there are numerous predators"
                " looking to take advantage of the situation,"
                " and find new hamster prey."
                " The city needs your help. What will you do?")
    print_pause(f"Local hamsters report {hamtaro_villain} is near by,"
                " and he has been attacking hamsters seeking refuge.")
    print_pause(" To the north of you is an abandoned 7/11. "
                " It could have some important supplies for the fight ahead.")
    print_pause(" To the west of you is a historical temple. "
                " It reminds you of temples from your grandfather's stories.")
    print_pause(" Your only weapon is your grandfather's kaiken dagger left you in his estate."
                " However, it's rusty and decaying.\n")


def store_or_temple(weapon, hamtaro_villain):
    print_pause("Enter 1 to enter the 7/11.")
    print_pause("Enter 2 to go to the temple.")
    print_pause("What path do you choose?")
    player_input = validate_input("(Please enter 1 or 2.)", ["1", "2"])
    if player_input == "1":
        store(weapon, hamtaro_villain)
    else:
        temple(weapon, hamtaro_villain)


def store(weapon, hamtaro_villain):
    print_pause("You approach the door of the store.")
    print_pause("You are about to enter the store"
                f" and out jumps {hamtaro_villain}.")
    print_pause(f"Kyaa!! Yikes!!!! This store has been taken over by {hamtaro_villain}!"
                " This is hostile territory."
                " The fight has come to you.")
    print_pause(f"{hamtaro_villain} attacks!")
    if weapon == "kaiken":
        print_pause("You're not feeling very much like samurai now,"
                    " you're the smallest in the family and armed with "
                    f"only your grandfather's rusty {weapon}. Everything in you wants to run.")
        fight_or_run(weapon, hamtaro_villain)
    else:
        fight_or_run(weapon, hamtaro_villain)


def fight_or_run(weapon, hamtaro_villain):
    player_input = validate_input(
        "Would you like to (1) fight or (2) run away?\n", ["1", "2"])
    if player_input == "1":
        if weapon == "kaiken":
            hamtaro_villain_win(hamtaro_villain)
            play_again()
        else:
            player_win(hamtaro_villain)
            play_again()
    else:
        run_away(weapon, hamtaro_villain)


def run_away(weapon, hamtaro_villain):
    print_pause("You run back to safety, and hide behind piles of rubble."
                " By the luck of your fur, you were able to evade the attacker.\n")
    store_or_temple(weapon, hamtaro_villain)


def temple(weapon, hamtaro_villain):
    print_pause("You advance cautiously into the temple."
                " All along the walls are illustrations of famous "
                " warriors and the history of Japan.")
    if weapon == "kaiken":
        print_pause("The temple is desolate and dusty. The roof is damaged and caving."
                    " The display cases are also covered in dust."
                    " No one has cared for the temple in a long time.")
        print_pause("A small glimmer from one of the cases catches your eye.")
        print_pause(" You dust off the case. It's the master katana sword of your ancestors! "
                    " This is your family's historical temple."
                    " This katana is storied to have magical powers.")
        print_pause("You replace the katana dagger with the kaiken"
                    " in the display with a note "
                    " and take the katana sword with you.")
        print_pause("You walk back to the piles of rubble, where you began.")
        weapon = "master katana"

    else:
        here_before()
        weapon = "master katana"
    store_or_temple(weapon, hamtaro_villain)


def here_before():
    print_pause("This place seems familiar. You were here a short while ago."
                " It's your family's ancestral temple."
                " You don't remember?"
                " Maybe you bumped your head in the storm."
                " You already explored and claimed the katana."
                " There's nothing more explore here.")
    print_pause("You return to the piles of rubble,"
                " where you began.\n")


def player_win(hamtaro_villain):
    print_pause(f"As the {hamtaro_villain} moves to attack, "
                " you take out the master katana.")
    print_pause("The master katana begins to glow"
                " with energy as you're holding it."
                " It super charges you with superior strength."
                " The ancient stories are true! It is magical!")
    print_pause(f"{hamtaro_villain} recognizes the master katana"
                " and that you are a true samurai."
                " It runs away in fear,"
                " leaving the town with the other villains."
                " The hamsters of the town come out from hiding"
                " and cheer, praising you as 'Hamtaro the Hero.'")
    print_pause(f"You have rid the town of the {hamtaro_villain}. You are victorious!")


def play_again():
    player_input = validate_input(
        "Want to play again? (y/n)", ["y", "n"])
    if player_input == "y":
        print_pause("Sugoi!!!\nLet samurai games begin!\n")
        hamtaro_hero_start()
    else:
        print_pause("Arigato gozaimasu! See you later, mata ne")
        sys.exit()


def hamtaro_villain_win(hamtaro_villain):
    print_pause("You give all your fury might and fight!")
    print_pause(f"but your kaiken is no match for the {hamtaro_villain}.")
    print_pause("You've been defeated and not lived up to the samurai legacy.")


def validate_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option not in options:
            print_pause("Please enter a valid input\n")
        else:
            return option


def hamtaro_hero_start():
    hamtaro_villain_list = ["Billy the Buzzard", "Ruby the Red Fox", "Olly the Owl", "Dillon the Dog", "Carl the Cat"]
    hamtaro_villain = random.choice(hamtaro_villain_list)
    weapon = "kaiken"
    start(hamtaro_villain)
    store_or_temple(weapon, hamtaro_villain)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hamtaro_hero_start()
