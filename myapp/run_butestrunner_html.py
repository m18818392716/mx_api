import unittest
from myapp.Public import BSTestRunner

def insertion_sort(data):
    for i in range(1, len(data)):
        position = i - 1
        cur = data[i]

        while position >= 0 and cur < data[position]:
            data[position + 1] = data[position]
            position = position - 1

        data[position + 1] = cur

class InsertSortTest(unittest.TestCase):
    def setUp(self):
        self.data = [3, 7, 21, 8, 5, 40]
        self.sorted_data = [3, 5, 7, 8, 21, 40]
        print('abc')

    def test_insertion_sort(self):
        insertion_sort(self.data)
        self.assertEqual(self.data, self.sorted_data)

    def test_insertion_sort_with_all_zero_data(self):
        data = [0, 0, 0, 0, 0]
        insertion_sort(data)
        self.assertEqual(data, data)
        print('abcd')

if __name__ == '__main__':

    print('*********************')
    unittest.main()

    # BSTestRunner.main()