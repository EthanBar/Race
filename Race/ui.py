import click
import animals

racers = {}

@click.command()
def race():
    while click.confirm("Would you like to register a racer?"):
        name = click.prompt("What is your racer's name?")
        # TODO - error checking
        species = click.prompt("What species is your racer? 1. Dog 2. Cat 3. Turtle 4. Rabbit. Enter a number:",
                                type=int)

        racers[name] = animals.Racer(name, species) # add new racer to dictionary
        print(racers[name].speed)

    while click.confirm("Would you like to run a race?"):
        # TODO -  implement race
        click.echo("race!")


if __name__ == '__main__':
    race()
