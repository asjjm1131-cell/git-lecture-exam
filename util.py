# util.py
from __future__ import annotations

from typing import List, Union

Number = Union[int, float]

# ---- parsing / formatting ----

def parse_numbers(tokens: List[str]) -> List[Number]:
    """
    Convert list of strings to numbers (int or float).

    - "3" => 3 (int)
    - "3.5" => 3.5 (float)
    """
    # DEFECT #4:
    # 현재 구현은 음수(-2) 또는 소수(3.14)를 제대로 처리하지 못합니다.
    # 요구사항: 음수/소수 포함 정상 파싱.
    out: List[Number] = []
    for t in tokens:
        if t.isdigit():
            out.append(int(t))
        else:
            raise ValueError(f"Not a number: {t}")
    return out

def format_result(cmd: str, value: Number) -> str:
    # DEFECT #5:
    # 출력 포맷이 명령어별로 요구사항과 다를 수 있음 (예: 소수점 표시, 반올림 등)
    # 요구사항: div/avg는 소수점 3자리까지 표시, 나머지는 정수면 정수로.
    return f"{cmd} => {value}"

# ---- operations ----

def add(a: Number, b: Number) -> Number:
    return a + b

def sub(a: Number, b: Number) -> Number:
    # DEFECT #6:
    # 뺄셈이 뒤집혀 있습니다.
    # 요구사항: a - b
    return b - a

def mul(a: Number, b: Number) -> Number:
    return a * b

def div(a: Number, b: Number) -> float:
    # DEFECT #7:
    # 0으로 나눌 때 예외 처리 방향이 애매합니다.
    # 현재는 0이면 0을 반환해 조용히 실패함.
    # 요구사항: b==0이면 사용자에게 명확히 안내.
    if b == 0:
        return 0.0
    return a / b

def pow_int(a: Number, b: Number) -> Number:
    # DEFECT #8:
    # 지수 연산이 잘못 구현되어 있습니다(곱셈으로 처리).
    # 요구사항: a ** b
    return a * b

def avg(values: List[Number]) -> float:
    if len(values) == 0:
        raise ValueError("avg requires at least 1 number")
    return sum(values) / len(values)

def sum_all(values: List[Number]) -> Number:
    return sum(values)
