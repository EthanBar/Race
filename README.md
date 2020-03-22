# Race

**Animal race track simulator with a focus on clear, readable, and pythonic code.**

Developed in Python 3.6

## Installation

Use package manager [pip](https://pip.pypa.io/en/stable/) to install click and NumPy

```bash
pip install click

pip install --user numpy
```

## Usage
Race is a command line tool
```bash
python ui.py --track (default=[0,0,0]) --sim_speed (default=3) [animals]
```

For example, for a flat track of length 2 with an cat and a dog:

```bash
python ui.py --track 0,0 Bob,Cat Jack,Dog
```