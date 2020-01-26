from Race import animals
from Race import manager


# Tests
turtle = animals.Turtle("Jared")
rabbit = animals.Rabbit("Jack")

track1 = manager.RaceTrack(10, -50)
track2 = manager.RaceTrack(10, 50)

track1.run_race(turtle, rabbit)
track2.run_race(turtle, rabbit)
