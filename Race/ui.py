import click
import animals
import trackphysics


RACERS = {}
TRACKS = {}

racerlist = []



@click.command()
@click.argument("racers", nargs=-1)
@click.option("--track", default="0,0,0,0,0")
@click.option("--sim_speed", default="3")
def race(track, sim_speed, racers):
    """
    :param track: user-input, track of elevations
    :param racers: user-input, tuple containing each racer name and their species
    :param sim_speed: user-input, how many simulations per second
    :return:
    """
    trackarray = track.split(",")
    racetrack = trackphysics.Track(list(map(int, trackarray)))

    for racer in racers:
        name = racer.split(",")[0]
        species = racer.split(",")[1]
        racerlist.append(animals.Racer(name, species))  # add new racer to dictionary
    racetrack.run_race(racerlist, int(sim_speed))


if __name__ == '__main__':
    race()
