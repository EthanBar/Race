import click
from Race import animals
from Race import trackphysics


racers = {}
tracks = {}


def get_racer():
    racer = click.prompt("Input a racer's name")
    while racer not in racers:
        racer = click.prompt("Racer not found, input a valid racer name")
    return racers[racer]

def get_track():
    track = click.prompt("Input a track's name")
    while track not in tracks:
        track = click.prompt("Track not found, input a valid track name")
    return tracks[track]


@click.command()
def race():
    while click.confirm("Would you like to register a racer?"):
        name = click.prompt("What is your racer's name?")
        species = click.prompt("What species is your racer? 1. Dog 2. Cat 3. Turtle 4. Rabbit. Enter a number:",
                               type=int)

        racers[name] = animals.Racer(name, species)  # add new racer to dictionary

    while click.confirm("Would you like to create a track?"):
        name = click.prompt("What is the track's name?")
        length = click.prompt("How long is the track?")
        track = trackphysics.Track(length=float(length))
        while True:
            point = click.prompt("Enter a point to edit, or say 'stop' to finish track:")
            if point == "stop":
                break
            height = click.prompt("What is the height at point " + str(point) + "?")
            track.add_node(float(point), float(height))
        tracks[name] = track

    while click.confirm("Would you like to run a race?"):
        track = get_track()
        racer_count = click.prompt("How many racers?", type=int)
        enrolled_racers = []
        for i in range(racer_count):
            enrolled_racers.append(get_racer())
        count_per_second = click.prompt("How many simulations per second?", type=int)
        track.run_race(enrolled_racers, count_per_second)


if __name__ == '__main__':
    race()
