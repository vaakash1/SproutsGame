import unittest

from game_state import Line, Dot
class TestSproutsGame(unittest.TestCase):
    def test_lines_intersect_diagonally(self):
        l1 = Line(Dot(0, 0), Dot(1, 1))
        l2 = Line(Dot(0, 1), Dot(1, 0))
        self.assertTrue(l1.intersects(l2))
        self.assertTrue(l2.intersects(l1))

    def test_parallel_lines_do_not_intersect(self):
        l3 = Line(Dot(0, 0), Dot(1, 0))
        l4 = Line(Dot(0, 1), Dot(1, 1))
        self.assertFalse(l3.intersects(l4))
        self.assertFalse(l4.intersects(l3))

    def test_lines_sharing_endpoint_do_not_intersect(self):
        l5 = Line(Dot(0, 0), Dot(0, 1))
        l6 = Line(Dot(0, 0), Dot(1, 1))
        self.assertFalse(l5.intersects(l6))
        self.assertFalse(l6.intersects(l5))

    def test_collinear_non_overlapping_lines_do_not_intersect(self):
        l7 = Line(Dot(0, 0), Dot(1, 1))
        l8 = Line(Dot(1, 1), Dot(2, 2))
        self.assertFalse(l7.intersects(l8))
        self.assertFalse(l8.intersects(l7))

    def test_collinear_overlapping_lines_intersect(self):
        l9 = Line(Dot(0, 0), Dot(1.1, 1.1))
        l10 = Line(Dot(1, 1), Dot(2, 2))
        self.assertTrue(l9.intersects(l10))
        self.assertTrue(l10.intersects(l9))
        
    def test_negative_coords_false(self):
        l11 = Line(Dot(-1, -1), Dot(0, 0))
        l12 = Line(Dot(0, 0), Dot(1, 1))
        self.assertFalse(l11.intersects(l12))
        self.assertFalse(l12.intersects(l11))

    def test_negative_coords_false(self):
        l13 = Line(Dot(-1, -1), Dot(0, 0))
        l14 = Line(Dot(1, 1), Dot(2, 2))
        self.assertFalse(l13.intersects(l14))
        self.assertFalse(l14.intersects(l13))
        
    def test_game_case_1_true(self):
        l15 = Line(Dot(500, 400), Dot(300, 400))
        l16 = Line(Dot(400, 500), Dot(400, 300))
        self.assertTrue(l15.intersects(l16))
        self.assertTrue(l16.intersects(l15))
        
    def test_game_floating_point_tolerance(self):
        l17 = Line(Dot(470.71067811865476, 470.71067811865476), Dot(400.0, 500.0))
        l18 = Line(Dot(329.28932188134524, 470.71067811865476), Dot(470.71067811865476, 329.28932188134524))
        self.assertFalse(l17.intersects(l18))
        self.assertFalse(l18.intersects(l17))

    def test_game_case_2_false(self):
        l19 = Line(Dot(500.0, 400.0), Dot(400.0, 500.0))
        l20 = Line(Dot(329.28932188134524, 470.71067811865476), Dot(329.28932188134524, 329.28932188134524))
        self.assertFalse(l19.intersects(l20))
        self.assertFalse(l20.intersects(l19))

unittest.main()
