# SqGrid

[![PyPI - Version](https://img.shields.io/pypi/v/sqgrid.svg)](https://pypi.org/project/sqgrid)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sqgrid.svg)](https://pypi.org/project/sqgrid)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Description

This is a puzzle solving program. The puzzle is a 3x3 grid of empty boxes, with another box at each of the interior vertices. Each box at each vertex contains a number.

![Sums puzzle](images/puzzle_sums.png)

The puzzle is to fill in the empty boxes with the numbers 1-9 so that the numbers surrounding each vertex add up to the number in the vertex box.

![Sums puzzle solved](images/puzzle_sums_solved.png)
=======
## Algorithm

## Solution mechanism

Since the program uses trial and error to solve some of it, the first objective is to limit the scope of tries that need to be made. So the first step of the program is, for each vertex sum, to determine what possible combinations of the fillin numbers could even be used to solve the sum. This greatly reduces the number of possibilities that can be applied to the trial and error phase of the solution process. So for example, there is only one possible combination for the sum of 10: [(1, 2, 3, 4)]; there are eight combinations for 24: [(1, 6, 8, 9), (2, 5, 8, 9), (2, 6, 7, 9), (3, 4, 8, 9), (3, 5, 7, 9), (3, 6, 7, 8), (4, 5, 6, 9), (4, 5, 7, 8)].

The second step, then, is to apply the fillin combinations to the puzzle to see which arrangement will fit all the sums. So to do this, the program conceptually breaks the puzzle into sections, each one being the numbers that surround a vertex sum. The program tests each permutaion of the order of combinations for each section until the solution is found.

One note, there are usually many solutions to each puzzle. This program exits after the first one is found.

## Execution

```console
python sqgrid n1 n2 n3 n4
```

Example
```console
python sqgrid 17 25 18 29

    +---------+---------+---------+
    |         |         |         |
    |         |         |         |
    |    1    |    6    |    4    |
    |        __         __        |
    |      /    \     /    \      |
    +-----|  17  |---|  25  |-----+
    |      \ __ /     \ __ /      |
    |         |         |         |
    |    2    |    8    |    7    |
    |        __         __        |
    |      /    \     /    \      |
    +-----|  18  |---|  29  |-----+
    |      \ __ /     \ __ /      |
    |         |         |         |
    |    3    |    5    |    9    |
    |         |         |         |
    |         |         |         |
    +---------+---------+---------+

```

## License

`sqgrid` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
