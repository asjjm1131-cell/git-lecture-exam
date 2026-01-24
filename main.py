# main.py
"""
Simple CLI Calculator for Git lecture exam.

How to run:
    python main.py

Input examples:
    add 1 2
    sub 10 3
    mul 2 4
    div 10 2
    pow 2 8
    avg 1 2 3 4
    sum 1 2 3
    quit
"""

from util import (
    add,
    sub,
    mul,
    div,
    pow_int,
    avg,
    sum_all,
    parse_numbers,
    format_result,
)

WELCOME = "Git Exam Calculator - type 'help' for commands."

def print_help() -> None:
    print(
        """
Commands:
  add a b           : a + b
  sub a b           : a - b
  mul a b           : a * b
  div a b           : a / b
  pow a b           : a ** b (integer exponent)
  avg n1 n2 ...     : average
  sum n1 n2 ...     : sum
  help              : show help
  quit/exit         : quit
"""
    )

def main() -> None:
    print(WELCOME)
    print_help()

    while True:
        line = input("> ").strip()

        # DEFECT #1:
        # 'quit'을 입력해도 종료가 안 될 수 있습니다.
        # 원인: 비교 대상 문자열이 잘못되어 있습니다.
        # 요구사항: quit/exit 입력 시 정상 종료.
        if line == "quite" or line == "exit":
            print("bye!")
            break

        if not line:
            continue

        if line == "help":
            print_help()
            continue

        parts = line.split()
        cmd = parts[0].lower()
        args = parts[1:]

        try:
            # DEFECT #2:
            # 현재 구현은 인자를 하나도 넘기지 않습니다.
            # 요구사항: 모든 인자를 전달해서 가변 인자 명령이 정상 동작.
            nums = parse_numbers(args[:0])

            if cmd == "add":
                r = add(nums[0], nums[1])
            elif cmd == "sub":
                r = sub(nums[0], nums[1])
            elif cmd == "mul":
                r = mul(nums[0], nums[1])
            elif cmd == "div":
                r = div(nums[0], nums[1])
            elif cmd == "pow":
                r = pow_int(nums[0], nums[1])
            elif cmd == "avg":
                # avg는 원래 2개 이상 숫자 받도록 설계
                r = avg(nums)
            elif cmd == "sum":
                r = sum_all(nums)
            else:
                print(f"Unknown command: {cmd}")
                continue

            print(format_result(cmd, r))

        except Exception as e:
            # DEFECT #3:
            # 에러 메시지가 원인을 숨깁니다.
            # 요구사항: 예외 메시지를 그대로 보여주기.
            print("Error occurred.")

if __name__ == "__main__":
    main()
