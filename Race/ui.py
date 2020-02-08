import click
import animals
import trackphysics


RACERS = {}
TRACKS = {}


def get_racer():
    """
    Asks for user input of a racer's name until a valid racer is found
    :return: A chosen racer
    """
    racer = click.prompt("Input a racer's name")
    while racer not in RACERS:
        racer = click.prompt("Racer not found, input a valid racer name")
    return RACERS[racer]


def get_track():
    """
        Asks for user input of a track's name until a valid track is found
        :return: A chosen track
        """
    track = click.prompt("Input a track's name")
    while track not in TRACKS:
        track = click.prompt("Track not found, input a valid track name")
    return TRACKS[track]


@click.command()
@click.option("--track", default="0,0,0,0,0", help="")
@click.argument("racers", nargs=-1, help="")
def race(track, racers):
    click.echo(track)
    click.echo(racers)
    """
        Main user interface. Asks for racers to register, tracks to create, and races to run.
    """

    #  Add a new racer
    while click.confirm("Would you like to register a racer?"):
        name = click.prompt("What is your racer's name?")
        species = click.prompt("What species is your racer? 1. Dog 2. Cat 3. Turtle 4. Rabbit. Enter a number:",
                               type=int)

        RACERS[name] = animals.Racer(name, species)  # add new racer to dictionary

    #  Add a new track
    while click.confirm("Would you like to create a track?"):
        name = click.prompt("What is the track's name?")
        length = click.prompt("How long is the track?")
        track = trackphysics.Track(length=int(length))
        #  Add as many points as desired
        while True:
            point = click.prompt("Enter a point to edit, or say 'stop' to finish track:")
            if point == "stop":
                break
            height = click.prompt("What is the height at point " + str(point) + "?")
            track.add_node(float(point), float(height))
        TRACKS[name] = track

    #  Simulate a race
    while click.confirm("Would you like to run a race?"):
        track = get_track()
        racer_count = click.prompt("How many racers?", type=int)
        enrolled_racers = []
        for _ in range(racer_count):
            enrolled_racers.append(get_racer())
        count_per_second = click.prompt("How many simulations per second?", type=int)
        track.run_race(enrolled_racers, count_per_second)


if __name__ == '__main__':
    race()
