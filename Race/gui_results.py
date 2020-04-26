import tkinter


def display_results(results):
    """
    Displays results from a race in a tkinter window
    :param results:
    """
    # Setup window
    results_window = tkinter.Tk()
    results_window.title("Results")

    # Header
    header = tkinter.Label(results_window, text="Leaderboard", font='Helvetica 18 bold')
    header.pack()

    # Sort thru results and display them
    place = 1
    for time in sorted(results):
        for racer_name in results[time]:
            result = tkinter.Label(results_window,
                                   text='{}. {} finished in {} seconds!'.format(place, racer_name, time))
            result.pack()
        place += len(results[time])
