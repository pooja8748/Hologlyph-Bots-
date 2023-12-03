import math

def compute_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

if __name__ == '_main_':
    test_cases = int(input())
    for i in range(test_cases):
        input_str = input()
        x1, y1, x2, y2 = map(int, input_str.split())
        
        distance = compute_distance(x1, y1, x2, y2)
        print(f"Distance: {distance:.2f}")