class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # count 5
        sorted_positions = sorted(zip(position, speed), reverse=True)
        times = ((target - p) / s for p, s in sorted_positions)

        fleet_count = 0
        last_time = 0

        for time in times:
            if time > last_time:
                fleet_count += 1
                last_time = time
        return fleet_count

        
        




