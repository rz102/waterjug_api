import unittest
from main import get_neighbors, water_jug_solver

# Unit testing
class TestCalculations(unittest.TestCase):

    def test_neighbors(self):
        self.assertEqual(
            get_neighbors((1, 2), 4, 4),
            [
                ((4, 2), 'Fill bucket X'),
                ((1, 4), 'Fill bucket Y'),
                ((0, 2), 'Empty bucket X'),
                ((1, 0), 'Empty bucket Y'),
                ((0, 3), 'Transfer from bucket X to bucket Y'),
                ((3, 0), 'Transfer from bucket Y to bucket X')
            ],
            'get_neighbors function is wrong')

    def test_algo(self):
        self.assertEqual(
            water_jug_solver(2, 10, 4),
            [
                {'step': 1, 'bucketX': 2, 'bucketY': 0, 'action': 'Fill bucket X'},
                {'step': 2, 'bucketX': 0, 'bucketY': 2, 'action': 'Transfer from bucket X to bucket Y'},
                {'step': 3, 'bucketX': 2, 'bucketY': 2, 'action': 'Fill bucket X'},
                {'step': 4, 'bucketX': 0, 'bucketY': 4, 'action': 'Transfer from bucket X to bucket Y'}
            ],
            'water_jug_solver is wrong'
        )