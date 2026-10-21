class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # count 2
        # sort the input first
        sorted_positions = sorted(zip(position, speed), key=lambda t: t[0], reverse=True)
        # get each time to compare with a generator instead of a list
        car_times = ((target - p) / s for p, s in sorted_positions)
        fleet_count = 0
        last_car_speed = 0
        for time in car_times:
            if time > last_car_speed:
                fleet_count += 1
                last_car_speed = time
        return fleet_count



