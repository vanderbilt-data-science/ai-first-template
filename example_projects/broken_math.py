def calculate_average(numbers):
    total = sum(number)
    return total / len(number)

def main():
    grades = [85, 92, 78, 96, 88, 74, 91, 83, 95, 79]
    avg = calculate_average(grades)
    print(f"Class average: {avg}")
    
if __name__ == "__main__":
    main()
