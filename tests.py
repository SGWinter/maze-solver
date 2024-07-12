import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_cols,
        )
        self.assertEqual(
                len(m1._cells[0]),
                num_rows,
        )

    def test_maze_create_cells_full_screen(self):
        num_cols = 100
        num_rows = 80
        margin = 50
        screen_x = 3440
        screen_y = 1440
        cell_size_x = (screen_x - 2 * margin) / num_cols
        cell_size_y = (screen_y - 2 * margin) / num_rows
        m2 = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y)
        self.assertEqual(
                len(m2._cells),
                num_cols,
        )
        self.assertEqual(
                len(m2._cells[0]),
                num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m3._cells),
                num_cols,
        )
        self.assertEqual(
                len(m3._cells[0]),
                num_rows,
        )

if __name__ == "__main__":
    unittest.main()

