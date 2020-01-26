import click
from Race import animals
from Race import trackphysics

racers = {}


def get_racer():
    racer = click.prompt("Input a racer")
    while racer not in racers:
        racer = click.prompt("Racer not found, input a racer")
    return racers[racer]


@click.command()
def race():
    while click.confirm("Would you like to register a racer?"):
        name = click.prompt("What is your racer's name?")
        # TODO - error checking
        species = click.prompt("What species is your racer? 1. Dog 2. Cat 3. Turtle 4. Rabbit. Enter a number:",
                               type=int)

        racers[name] = animals.Racer(name, species)  # add new racer to dictionary

    while click.confirm("Would you like to run a race?"):
        racer_count = click.prompt("How many racers?", type=int)
        enrolled_racers = []
        for i in range(racer_count):
            enrolled_racers.append(get_racer())
        track = trackphysics.Track(length=10)
        track.add_node(xpos=9, height=10)
        track.add_node(xpos=7, height=0)
        print(track.find_slope(8))
        print(track.find_slope(2))
        print(track.find_slope(8.9))
        # track.runrace(enrolled_racers[0], enrolled_racers[1])


if __name__ == '__main__':
    race()
