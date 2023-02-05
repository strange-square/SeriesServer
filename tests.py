import unittest
import random
import lib

class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.series = lib.SeriesList()
        self.l = [["s1", 20], ["s2", 10], ["s3", 50]]
        self.names = ["s1", "s2", "s3"]

    def test_add_w_s(self):
        for s in self.l:
            response = self.series.add_series(s[0], s[1])

        for s in self.l:
            response = self.series.add_to_see(s[0])
            self.assertEqual(response, "ok")

        for s in self.l:
            response = self.series.add_watched(s[0])
            self.assertEqual(response, "ok")

        response = self.series.get_to_see()
        self.assertSetEqual(response, set([self.l[0][0], self.l[1][0], self.l[2][0]]))
        response = self.series.get_watched()
        self.assertSetEqual(response, set([self.l[0][0], self.l[1][0], self.l[2][0]]))

    def test_wrong_add_w(self):
        response = self.series.add_watched("serial")
        self.assertEqual(response, "not at list")

    def test_wrong_add_s(self):   
        response = self.series.add_to_see("serial")
        self.assertEqual(response, "not at list")

    def test_gen(self):
        response = lib.generator_series(self.series)
        self.assertIn(response, self.names)


    def episodes(self):
        response = self.series.get_next_ep("s1")
        self.assertEqual(response, "1")

        response = self.series.watch_episode("s1", 4)
        self.assertEqual(response, "ok")

        response = self.series.get_next_ep("s1")
        self.assertEqual(response, "5")

        response = self.series.get_next_ep("s0")
        self.assertEqual(response, "There is no such series")

    def raiting(self):
        response = self.series.set_raiting ("s2", 5)
        self.assertEqual(response, "ok")

        response = self.series.get_raiting("s2")
        self.assertEqual(response, "5")

        response = self.series.get_raiting ("s0")
        self.assertEqual(response, "There is no such series")




if __name__ == '__main__':
    unittest.main()
