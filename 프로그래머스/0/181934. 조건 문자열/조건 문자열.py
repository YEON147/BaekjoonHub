def solution(ineq, eq, n, m):
    op = ineq if eq == "!" else ineq + "="
    return 1 if eval(f"{n} {op} {m}") else 0