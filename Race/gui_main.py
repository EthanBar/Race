import tkinter
import animals
import trackphysics
import gui_results


class DropDown:

    def __init__(self, options):
        self.animal = tkinter.StringVar(roster)
        self.animal.set(options[0])

        # self.name = tkinter.StringVar(window)
        # self.name.set("")

        self.dropdown = tkinter.OptionMenu(roster, self.animal, *options)
        self.dropdown.config(width=20, font=('Helvetica', 12))
        self.dropdown.pack()

        self.field = tkinter.Entry(roster)
        self.field.pack()


def add_choice():
    racer_species.append(DropDown(species))


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

add_racer = tkinter.Button(
    text="Add Another Racer",
    fg="black",
    bg="white",
    width=20,
    height=2,
    command=add_choice
)
add_racer.pack()

start_race = tkinter.Button(
    text="Start Race!",
    fg="black",
    bg="green",
    highlightbackground="green",
    width=20,
    height=2,
    command=run_race
)
start_race.pack()

header = tkinter.Label(roster, text="Racer Roster")
header.pack()

racer_species = []
add_choice()

roster.mainloop()
