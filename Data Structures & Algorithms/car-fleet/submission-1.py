class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # count 2
        # sort the input first
        sorted_positions = sorted(zip(position, speed), key=lambda t: t[0], reverse=True)
        # get each time to compare
        car_times = [(target - p) / s for p, s in sorted_positions]
        fleet_count = 0
        last_car_time = 0
        for time in car_times:
            if time > last_car_time:
                fleet_count += 1
                last_car_time = time
        return fleet_count



