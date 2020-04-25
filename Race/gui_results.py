import tkinter


def display_results(results):
    results_window = tkinter.Tk()
    results_window.title("Results")

    header = tkinter.Label(results_window, text="Leaderboard", font='Helvetica 18 bold')
    header.pack()

    place = 1
    for time in sorted(results):
        for racer_name in results[time]:
            result = tkinter.Label(results_window,
                                   text='{}. {} finished in {} seconds!'.format(place, racer_name, time))
            result.pack()
        place += len(results[time])
