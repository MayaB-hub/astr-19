
import math  

def main():
    start = 0
    end = 2 * math.pi
    steps = 1000

    step_size = (end - start) / (steps - 1)

    print("x\t sin(x)")
    print("__________________")

    for i in range(steps):
        x = start + i * step_size
        y = math.sin(x)
        print(f"{x:.5f}\t {y:.5f}")

main()
