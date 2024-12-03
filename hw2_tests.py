import data
import hw2
import unittest

from data import Point, Rectangle,Duration,Song
from hw2 import create_rectangle, shorter_duration_than, song_shorter_than, running_time, validate_route, \
    longest_repetition


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_createRectangle(self):
        test1= create_rectangle(Point(2,2),Point(10,10))
        actual = Rectangle(Point(2,10),Point(10,2))
        self.assertEqual(test1,actual)

    def test_createreactangleAbnormal(self):
        test2= create_rectangle(Point(3,5),Point(3,9))
        actual = Rectangle(Point(3,9),Point(3,5))
        self.assertEqual(test2,actual)

        test3= create_rectangle(Point(10,5),Point(1,5))
        actual= Rectangle(Point(1,5),Point(10,5))
        self.assertEqual(test3,actual)

    # Part 2
    def test_shorter_duration_than1(self):
        #No Hour Test
        test1 = shorter_duration_than(Duration(0,12,4),Duration(0,4,18))
        expected1 = True
        self.assertEqual(expected1,test1)

        #False Test
        test2 = shorter_duration_than(Duration(0,4,18),Duration(0,12,4))
        expected2 = False
        self.assertEqual(expected2,test2)

        #Hour Test(s)
    def test_shorter_duration_than2(self):
        test1 = shorter_duration_than(Duration(1,20,10),Duration(0,4,9))
        expected1 = True
        self.assertEqual(expected1,test1)

        test2 = shorter_duration_than(Duration(1,20,10),Duration(2,30,0))
        expected2 = False
        self.assertEqual(expected2,test2)

    # Part 3
    def test_songs_shorter_than1(self):
        d1 = Duration(0,2,30)
        d2 = Duration(0,3,40)
        d3 = Duration(0,10,3)
        artist_song1 = Song("Dr.Dre","song 1",d1)
        artist_song2 = Song("Dr.G", "song 2", d2)
        artist_song3 = Song("Dr.F", "song 3", d3)

        songs = [artist_song1,artist_song2,artist_song3]
        test1 = song_shorter_than(songs,Duration(0,4,0))
        expected = [artist_song1,artist_song2]
        self.assertEqual(expected,test1)

    def test_songs_shorter_than2(self):
        d1 = Duration(0,2,30)
        d2 = Duration(0,3,40)
        d3 = Duration(0,10,3)
        artist_song1 = Song("Dr.Dre","song 1",d1)
        artist_song2 = Song("Dr.G", "song 2", d2)
        artist_song3 = Song("Dr.F", "song 3", d3)

        songs = [artist_song1,artist_song2,artist_song3]
        test2 = song_shorter_than(songs, Duration(0, 10, 4))
        expected = [artist_song1, artist_song2, artist_song3]
        self.assertEqual(expected, test2)
# 8 min 40 sec, 3min,3min20,3min 10 sec
    # Part 4
        #
    def test_running_time1(self):
        songs = [Song("LIA","Lost in April", Duration(0,4,20)),
                 Song("stop","June", Duration(0,3,0)),
                 Song("we","Wind", Duration(0,3,20)),
                 Song("cindy","Airplanes", Duration(0,3,10))]
        playlist = [0, 2, 1, 3, 0]
        actual = running_time(songs, playlist)
        self.assertEqual(Duration(0,18,10), actual)

    def test_running_time2(self):
        songs = [Song("LIA", "Lost in April", Duration(0, 4, 20)),
                 Song("stop", "June", Duration(0, 3, 0)),
                 Song("we", "Wind", Duration(0, 3, 20)),
                 Song("cindy", "Airplanes", Duration(0, 3, 10))]
        playlist2 = [3,2,1]
        actual = running_time(songs, playlist2)
        self.assertEqual(Duration(0, 9, 30), actual)
    # Part 5
    def test_validate_route(self):
        citys = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']]
        test1 = validate_route(citys, [])
        self.assertEqual(True, test1)

    def test_validate_route2(self):
        citys = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']]
        test2 = validate_route(citys, ['san luis obispo', 'atascadero'])
        self.assertEqual(False,test2)

    # Part 6
    def test_longest_repetition(self):
        list_test1 = [1, 1, 2, 2, 1, 1, 1, 3]
        actual = longest_repetition(list_test1)
        self.assertEqual(4,actual)

    def test_longest_repetition2(self):
        list_test2 = []
        actual = longest_repetition(list_test2)
        self.assertEqual(None,actual)



if __name__ == '__main__':
    unittest.main()
