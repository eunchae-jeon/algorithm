def solution(bridge_length, weight, truck_weights):
    sum_weight = 0
    bridge = [0] * bridge_length
    seconds = 0
    for truck in truck_weights:
        while True:
            if bridge[seconds%bridge_length] > 0:
                sum_weight -= bridge[seconds%bridge_length]
                bridge[seconds%bridge_length] = 0
            if truck + sum_weight <= weight:
                bridge[seconds%bridge_length] = truck
                sum_weight += truck
                seconds += 1
                break
            seconds += 1

    return seconds + bridge_length

print(solution(2,	10,	[7,4,5,6]))