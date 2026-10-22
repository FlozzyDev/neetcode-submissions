class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # count 3
        sorted_positions = sorted(zip(position, speed), key=lambda t: t[0], reverse=True)
        car_times = ((target - p) / s for p, s in sorted_positions)

        fleet_count = 0
        last_fleet_speed = 0

        for time in car_times:
            if time > last_fleet_speed:
                fleet_count += 1 
                last_fleet_speed = time
        return fleet_count





