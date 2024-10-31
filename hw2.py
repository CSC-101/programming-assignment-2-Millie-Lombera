import data
from typing import Optional
from data import Point, Rectangle, Duration, Song


# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1: Point, point2: Point)-> Rectangle:
    left_x = min(point1.x,point2.x)
    right_x= max(point1.x,point2.x)

    left_y=  max(point1.y,point2.y)
    right_y= min(point1.y,point2.y)

    top_left= Point(left_x,left_y)
    bottom_right= Point(right_x,right_y)

    return Rectangle(top_left,bottom_right)
# Part 2
#time1= Duration(0,12,4)
#time2= Duration(0,4,18)
#Duration(1,20,10)
#Duration(0,4,9)
def shorter_duration_than(time1: Duration,time2: Duration)-> bool:
    seconds_t1 = time1.hours * 3600 + time1.minutes * 60 + time1.seconds
    seconds_t2 = time2.hours * 3600 + time2.minutes * 60 + time2.seconds
    return seconds_t1 > seconds_t2

# Part 3
def song_shorter_than(songs: list[Song],upper_bound: Duration)-> list[Song]:
    return [song for song in songs if song.total_seconds() < upper_bound.total_seconds()]
# Part 4
def running_time(songs: list[Song],playlist: list[int])-> Duration:
    total_duration = Duration(0,0,0)

    for song_idx in playlist:
        if 0 <= song_idx < len(songs):
            total_duration.hours += songs[song_idx].duration.hours
            total_duration.minutes += songs[song_idx].duration.minutes
            total_duration.seconds += songs[song_idx].duration.seconds

    total_duration.minutes += total_duration.seconds // 60
    total_duration.seconds %= 60
    total_duration.hours += total_duration.minutes // 60
    total_duration.minutes %= 60

    return total_duration
# Part 5
def validate_route(city_links:list[list[str]], route: list[str])->bool:
    link_set = set(tuple(sorted(link)) for link in city_links)

    if len(route) <= 1:
        return True

    for i in range(len(route) - 1):
        pair = tuple(sorted([route[i], route[i + 1]]))
        if pair not in link_set:
            return False

    return True

# Part 6
def longest_repetition(nums: list[int]) -> Optional[int]:
    if not nums:
        return None

    max_length = 0
    max_index = None
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_index = i - current_length
            current_length = 1

    if current_length > max_length:
        max_index = len(nums) - current_length

    return max_index
