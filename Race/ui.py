import click


@click.command()
def race():
    while click.confirm("Would you like to register a racer?"):
        # TODO - implement register
        click.echo("register!")
    while click.confirm("Would you like to run a race?"):
        # TODO -  implement race
        click.echo("race!")


if __name__ == '__main__':
    race()
