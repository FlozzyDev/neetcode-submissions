class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sorted positions
        sorted_positions = sorted(zip(position, speed), key=lambda t: t[0], reverse=True)
        # Get times for each car
        car_times = [(target - p) / s for p, s in sorted_positions]
        # count number of fleets, track slowest time (if a car is slower, we have a new fleet)
        num_fleets = 0
        slow_speed = 0
        # loop through times and increase fleet if slower
        for time in car_times:
            if time > slow_speed:
                num_fleets += 1
                slow_speed = time
        return num_fleets


