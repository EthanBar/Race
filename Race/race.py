import animals
import manager


# Tests
turtle = animals.Turtle("Jared")
rabbit = animals.Rabbit("Jack")

track1 = manager.RaceTrack(10, -50)
track2 = manager.RaceTrack(10, 50)

track1.runrace(turtle, rabbit)
track2.runrace(turtle, rabbit)
