from itertools import permutations, combinations
import sys

class MagicGrid:
	grid_size = [3,3]
	grid = [[]]

	def __init__(self):
		self.reset()

	def reset(self):
		a = self.grid_size[0]
		b = self.grid_size[1]
		self.grid = [[0 for x in range(a)] for y in range(b)]

	def display(self):
		print('-' * 20)
		print('     '.join(['|'] * 4))
		print(' |  '.join(['','a','b','c','']))
		for i in range(self.grid_size[0]):
			print(self.grid[i])

	def set_numbers(self, coords, numbers):
		for i in range(len(coords)):
			c = coords[i]
			self.grid[c[0]][c[1]] = numbers[i]


class MagicNumber:

	def __init__(self, section, grid_numbers, sum):
		self.section = section
		self.grid_numbers = grid_numbers
		self.combos = []
		self.sum = sum

class MagicNumbers:

	def __init__(self, grid):
		self._numbers = [0] * 10
		self._index = 0
		self._got_it = False

		self._grid = grid

		self._four_numbers = []

		self._four_numbers.append(MagicNumber((0,0), [(0,0),(0,1),(1,0),(1,1)],None))
		self._four_numbers.append(MagicNumber((0,1), [(0,1),(0,2),(1,1),(1,2)],None))
		self._four_numbers.append(MagicNumber((1,0), [(1,0),(1,1),(2,0),(2,1)],None))
		self._four_numbers.append(MagicNumber((1,1), [(1,1),(1,2),(2,1),(2,2)],None))

	def __getitem__(self, index):
		return self._four_numbers[index]

	def __setitem__(self, index, value):
		self._four_numbers[index] = value

	def __iter__(self):
		return self

	def __next__(self):
		try:
			s = self._four_numbers[self._index]
		except IndexError:
			raise StopIteration()
		self._index += 1
		return s

	def display(self):
		self._grid.display()

	def set_numbers_in_grid(self,coords,numbers):
		self._grid.set_numbers(coords,numbers)

	def unset_numbers_in_grid(self,coords):
		numbers = [0] * len(coords)
		self._grid.set_numbers(coords,numbers)

	def reset_grid(self):
		self._grid.reset()

	def set_numbers_in_use(self,numbers):
		for n in numbers:
			self._numbers[n] = 1

	def unset_numbers_in_use(self,numbers):
		for n in numbers:
			self._numbers[n] = 0

	def reset_numbers_in_use(self):
		for i in range(10):
			self._numbers[i] = 0

	def set_sums(self,sums):
		for i in range(len(sums)):
			self._four_numbers[i].sum = sums[i]

	def get_section(self, coords):
		for n in self._four_numbers:
			if (n.section[0] == coords[0] and n.section[1] == coords[1]):
				return n

	def get_combos(self):
		for c in combinations(range(1, 10), 4):
			[
                n.combos.append(c) \
                for n in self._four_numbers \
				if sum(c) == n.sum
            ]

	def sort_sections(self):
		sorted_nums = []
		s = sorted(self._four_numbers,
			key=lambda x: len(x.combos))[0]
		sorted_nums.append(s)

		x = 0 if s.section[0] else 1
		y = 0 if s.section[1] else 1
		sorted_nums.append(self.get_section((x,y)))

		x = 0 if s.section[0] else 1
		y = s.section[1]
		sorted_nums.append(self.get_section((x,y)))

		x = s.section[0]
		y = 0 if s.section[1] else 1
		sorted_nums.append(self.get_section((x,y)))

		self._four_numbers = sorted_nums

	def filter_combos(self, i):

		combos = []

		must_haves = []

		for c in self._four_numbers[i].grid_numbers:
			n = self._grid.grid[c[0]][c[1]]
			if n:
				self._numbers[n] = 2
				must_haves.append(n)

		cant_haves = [n for n in range(len(self._numbers)) if self._numbers[n] == 1]

		#print(self._four_numbers[i].grid_numbers)
		#print(self._four_numbers[i].combos)
		#print(must_haves)
		#print(cant_haves)

		for c in self._four_numbers[i].combos:
			if ((set(must_haves).issubset(c)) and
				(not any(elem in c for elem in cant_haves))):
				c2 = [x for x in c if x not in must_haves]
				combos.append(c2)

		# reset used numbers because they got
		# set to 2 earlier. (hack!)
		for n in must_haves:
			self._numbers[n] = 1

		return combos

	def filter_coords(self, coords):
		avail_coords = []
		for c in coords:
			if not self._grid.grid[c[0]][c[1]]:
				avail_coords.append(c)

		return avail_coords

	def guess_numbers(self, i):

		#print(i)

		section = self._four_numbers[i]
		#print(section.sum)
		combos = self.filter_combos(i)
		#print(combos)
		coords = self.filter_coords(section.grid_numbers)
		#print(coords)

		for c in combos:
			for p in permutations(c):

				self.set_numbers_in_use(p)
				self.set_numbers_in_grid(coords, p)

				if (i+1) == len(self._four_numbers):
					self._got_it = True
				else:
					self.guess_numbers(i+1)

				if self._got_it:
					return

				self.unset_numbers_in_use(p)
				self.unset_numbers_in_grid(coords)

	def do_your_magic(self):

		self.reset_grid()
		self.reset_numbers_in_use()

		self.guess_numbers(0)

		return self._got_it


def main(magic_sums):

	magic = MagicNumbers(MagicGrid())
	magic.set_sums(magic_sums)
	magic.get_combos()
	magic.sort_sections()

	success = magic.do_your_magic()

	if success == True:
		print('Final Result')
		print(magic_sums)
		magic.display()
	else:
		print(f"Could not find solution for {magic_sums}")


if __name__ == "__main__":

    #magic_sums = [17,25,18,29]
	magic_sums = [int(i) for i in sys.argv[1:5]]

	main(magic_sums)

