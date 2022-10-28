# SqGrid

[![PyPI - Version](https://img.shields.io/pypi/v/sqgrid.svg)](https://pypi.org/project/sqgrid)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sqgrid.svg)](https://pypi.org/project/sqgrid)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Description

This is a puzzle solving algorithm. The puzzle is a 3x3 grid of empty boxes, with another box at each of the interior vertices. Each box at each vertex contains a number. The puzzle is to fill in the empty boxes with the numbers 1-9 so that the numbers surrounding each vertex add up to the number in the vertex box.

## Background

My son brought home a math puzzle once, and while it wasn't very difficult, I wondered what it would take to get a computer to solve it. This was my first foray in Python programming.

## Algorithm

The algorithm is actually much more complicated than probably necessary. But I guess it has some purpose too.

I basically went about trying to build the algorithm by thinking about how I would solve it, and turning that into computer code more or less. The main difference, however, is that a computer can hold a much bigger store of numbers in memory than a human can, and can also test and retest many different combinations. So the goal is to build upon those strengths. However, it is also imperative to not over extend the computers abilities and try to make the algorithm somewhat efficient, because eventually things scale beyond even the computer's abilities.

Conceptually, there are four sections to the puzzle grid, each being a grouping of numbers surrounding the sum at the vertex. These sections overlap because every box except the corners is part of at least one other sum.

The steps are as follows:

1. For each vertex sum, build a list of the fill-in numbers that add up to the sum and could be used to fill in that number.

2. Start with the section with the least number of possible sum combinations. Cycling through each combo, begin testing each permutation for a possible solution. 

3. Fill the numbers in the section with the combo numbers.

4. Since this number shares only number from the opposite corner section, search that section for combos that contain the shared number and none of the other numbers. If any combinations are found, cycle through all permutations and fill in the section. If no combos are found, start over at step two with the next permutation.

5. Repeat step four with the next two sections, backing out if no combos are found.

6. A successful solution has been found if all four sections get filled in.

First off, we can take advantage of the fact that we are working with a preset list of numbers that will eventually fill in the boxes, and not a indeterinate set. So using these numbers, the program cycles through every combination of every set of the fill-in numbers and builds a list of potential sets that add up to the four sums. These combined lists are of course unordered so it not necessary to search through every permutation of the list of numbers, but only each set of numbers in no particular order.

After the list of possible addend combos is calculated for each vertex sum, the sections are sorted according to the priority in which the sections should be tested for possible solutions. The section with the lowest number of possible sum combos is given starting priority.

Then, the opposing corner is tried because it will share the fewest numbers with the starting section. The third section shares numbers equally with the first two, so the section with the fewewst combinations is chosen next, and the finally the last section is added.

We run through the box to start trying out these different combos to see where each one fits. Starting with the first chosen section, each addend combo is tested by using every permution of the number ordering. For each permutation, the numbers are placed in a box in the section. Then the next combos from the next section are given. Since the first section and the second only share one number in common, each combo in the second section is searched for that number, and every combination that contains other numbers already placed is rejected. If any combos are found, they are tried as the first, with of course keeping the shared number in that shared space. For each combination, the third section is searched for combos that contain all of the numbers that have been placed. If any are found, they are tried and tested. And finally the fourth section is tested in the same way

If at any point, a combination is not found to contain the numbers that it shares points with or numbers that are not already laid out, the program gives up on the previous section's attempt and tries another one of its combos. If there are no more combos to try, it resets the previous one.

This goes on until a combination is found to satisfy the sums and the program prints out a matrix of the ordered numbers.

Interestingly, there are often multiple ways to solve each puzzle. But this program stops at the first solution.

## Efficiency

The final question is about the efficiency of the algorithm. Well, after I had implemented it, I began to wonder why I hadn't just run a full list of permutations for 1-9 just to see what would work. Well, that would have been a lot smarter, because there are not many possible combinations, only 362,880 (9!) for a 3x3 grid. But the number grows rapidly as the size of the puzzle grows, until it becomes unmanageable, with a 4x4 box having 2.092279e+13 possibities.

## Installation

```console
pip install sqgrid
```

## License

`sqgrid` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
