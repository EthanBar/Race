import click
import animals

racers = {}

@click.command()
def race():
    while click.confirm("Would you like to register a racer?"):
        name = click.prompt("What is your racer's name?")
        speed = click.prompt("How fast is " + name + "?", type=int)
        speed = click.prompt("How much does " + name + " weigh?", type=int)

        # racers[name] = animals.Turtle

    while click.confirm("Would you like to run a race?"):
        # TODO -  implement race
        click.echo("race!")


if __name__ == '__main__':
    race()
