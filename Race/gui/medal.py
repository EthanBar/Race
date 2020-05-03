import tkinter


class MedalDisplay:
    """
    Creates and manages and canvas to display race results with medals
    """

    def __init__(self, window, results):
        """
        Creates the canvas
        :param window: window to display canvas to
        :param results: unsorted results of race
        """
        self.canvas = tkinter.Canvas(window, width=300, height=100)

        # Loop through the top racers, ensuring we don't display over three
        place = 1
        medals_made = 0
        for time in sorted(results, key=lambda x: (x < 0, x)):
            for racer_name in results[time]:
                if medals_made < 3:
                    self._create_medal(50 + medals_made * 100, racer_name, place)
                    medals_made += 1
            place += len(results[time])

    def _create_medal(self, xpos, name, place):
        """
        Creates and individual medal
        :param xpos: the x position to center all elements of the column on
        :param name: the name of the racer
        :param place: the place of the racer
        """
        self.canvas.create_text(xpos, 25, fill="black", font="Arial 14 bold", text=name)
        self.canvas.create_oval(xpos - 25, 50, xpos + 25, 100, fill=self._place_to_color(place))
        self.canvas.create_text(xpos, 75, fill="black", font="Arial 36 bold", text=str(place))

    @staticmethod
    def _place_to_color(place):
        """
        Returns a color corresponding to a place
        :param place: integer place result
        :return: string representation of a hexadecimal color
        """
        if place == 1:
            return "#FCD535"
        if place == 2:
            return "#AAABB0"
        if place == 3:
            return "#DA8020"

    def get_canvas(self):
        """
        Provides access to the canvas
        :return: the canvas object
        """
        return self.canvas
