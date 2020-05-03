import tkinter
import animals
import trackphysics
from gui import gui_results


class InputRow:
    """
    Manages a textfield and a dropdown menu aligned in a grid view
    """

    def __init__(self, options, position):
        """

        :param options: List containing options for the dropdown
        :param position: Position in grid row
        """
        self.animal = tkinter.StringVar(roster)
        self.animal.set(options[0])

        self.dropdown = tkinter.OptionMenu(roster, self.animal, *options)
        self.dropdown.config(width=20, font=('Helvetica', 12))
        self.dropdown.grid(row=position, column=0)

        self.field = tkinter.Entry(roster)
        self.field.grid(row=position, column=1)


# TODO remove a user
def add_choice():
    """
    Adds another set of animal name and species pickers for the user to interact with
    """
    racer_species.append(InputRow(species, 4 + len(racer_species)))


def run_race():
    """
    Runs a race using user input
    """
    racetrack = trackphysics.Track(list(map(int, track_entry.get().split(","))))
    racers = []
    for racer in racer_species:
        animal = racer.animal.get()
        name = racer.field.get()

        racers.append(animals.Racer(name, animal))

    results = racetrack.run_race(racers)

    roster.destroy()

    gui_results.display_results(results)


if __name__ == "__main__":
    # Set up window
    roster = tkinter.Tk()
    roster.title("Race Track")

    # Dropdown options
    species = ["Dog", "Cat", "Turtle", "Rabbit", "Elephant"]

    # Header
    roaster_header = tkinter.Label(roster, text="Race Controls", font='Helvetica 18 bold')
    roaster_header.grid(row=0, column=0, columnspan=2, pady=(10, 10))

    # Track Entry
    roaster_header = tkinter.Label(roster, text="Track", font='Helvetica 14')
    roaster_header.grid(row=1, column=0)
    track_entry = tkinter.Entry(roster)
    track_entry.grid(row=1, column=1)
    track_entry.insert(tkinter.END, '0, 1, 2, 3, 4, 0')

    # Buttons
    add_racer = tkinter.Button(
        text="Add Another Racer",
        fg="black",
        bg="white",
        highlightbackground="blue",
        width=20,
        height=2,
        command=add_choice
    )
    add_racer.grid(row=2, column=0)

    start_race = tkinter.Button(
        text="Start Race!",
        fg="black",
        bg="green",
        highlightbackground="green",
        width=20,
        height=2,
        command=run_race
    )
    start_race.grid(row=2, column=1)

    # Header
    roaster_header = tkinter.Label(roster, text="Racer Roster", font='Helvetica 18 bold')
    roaster_header.grid(row=3, column=0, columnspan=2, pady=(10, 10))

    # Add one racer by default
    racer_species = []
    add_choice()

    roster.mainloop()
