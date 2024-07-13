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

    def test_maze_remove_entrance_exit(self):
        num_cols = 16
        num_rows = 16
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                m4._cells[0][0].has_top_wall,
                False,
        )
        self.assertEqual(
                m4._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
                False,
        )

    def test_maze_reset_walls(self):
        num_cols = 16
        num_rows = 12
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10, None, 0)
        self.assertEqual(
                m5._cells[0][0]._visited,
                False,
        )
        self.assertEqual(
                m5._cells[num_cols - 1][num_rows - 1]._visited,
                False,
        )

if __name__ == "__main__":
    unittest.main()

