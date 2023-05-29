def Num24416():
    n = int(input())

    def dynamic_solution(n):
        fibonacci_numbers = [0 for i in range(n + 1)]
        fibonacci_numbers[0] = 1
        fibonacci_numbers[1] = 1
        result = 0

        for idx in range(3, n + 1):
            fibonacci_numbers[idx] = (
                fibonacci_numbers[idx - 1] + fibonacci_numbers[idx - 2]
            )

            result += 1

        return result

    def recursive_solution(n):
        return (
            1
            if n == 1 or n == 2
            else recursive_solution(n - 1) + recursive_solution(n - 2)
        )

    recursive_count = recursive_solution(n)
    dynamic_count = dynamic_solution(n)

    result = str(recursive_count) + " " + str(dynamic_count)

    print(result)


Num24416()
