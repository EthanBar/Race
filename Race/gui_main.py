import tkinter
import animals
import trackphysics
import gui_results


class InputRow:

    def __init__(self, options, position):
        self.animal = tkinter.StringVar(roster)
        self.animal.set(options[0])

        # self.name = tkinter.StringVar(window)
        # self.name.set("")

        self.dropdown = tkinter.OptionMenu(roster, self.animal, *options)
        self.dropdown.config(width=20, font=('Helvetica', 12))
        self.dropdown.grid(row=position, column=0)

        self.field = tkinter.Entry(roster)
        self.field.grid(row=position, column=1)


def add_choice():
    racer_species.append(InputRow(species, 3 + len(racer_species)))


def run_race():
    racetrack = trackphysics.Track([0, 1, 2, 3, 4, 0])
    racers = []
    for racer in racer_species:
        animal = racer.animal.get()
        name = racer.field.get()

        racers.append(animals.Racer(name, animal))

    results = racetrack.run_race(racers)

    roster.destroy()

    gui_results.display_results(results)


roster = tkinter.Tk()
roster.title("Race Track")

species = ["Dog", "Cat", "Turtle", "Rabbit", "Elephant"]

roaster_header = tkinter.Label(roster, text="Race Controls", font='Helvetica 18 bold')
roaster_header.grid(row=0, column=0, columnspan=2, pady=(10, 10))

add_racer = tkinter.Button(
    text="Add Another Racer",
    fg="black",
    bg="white",
    highlightbackground="blue",
    width=20,
    height=2,
    command=add_choice
)
add_racer.grid(row=1, column=0)

start_race = tkinter.Button(
    text="Start Race!",
    fg="black",
    bg="green",
    highlightbackground="green",
    width=20,
    height=2,
    command=run_race
)
start_race.grid(row=1, column=1)

roaster_header = tkinter.Label(roster, text="Racer Roster", font='Helvetica 18 bold')
roaster_header.grid(row=2, column=0, columnspan=2, pady=(10, 10))

racer_species = []
add_choice()

roster.mainloop()
