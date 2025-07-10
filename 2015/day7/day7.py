# https://adventofcode.com/2015/day/7


def evaluate(wires: dict, cache: dict, w: str):
    if w.isdigit():
        return int(w)  # If w is a number, return it directly
    if w not in cache:
        expr = wires[w]
        if "AND" in expr:
            a, b = expr.split(" AND ")
            res = evaluate(wires, cache, a) & evaluate(wires, cache, b)
        elif "OR" in expr:
            a, b = expr.split(" OR ")
            res = evaluate(wires, cache, a) | evaluate(wires, cache, b)
        elif "LSHIFT" in expr:
            a, b = expr.split(" LSHIFT ")
            res =  evaluate(wires, cache, a) << evaluate(wires, cache, b)
        elif "RSHIFT" in expr:
            a, b = expr.split(" RSHIFT ")
            res = evaluate(wires, cache, a) >> evaluate(wires, cache, b)
        elif "NOT" in expr:
            a = expr.split("NOT ")[1]
            res = ~evaluate(wires, cache, a) & 0xFFFF
        else: # It's a direct assignment
            res = evaluate(wires, cache, expr)
        cache[w] = res
    return cache[w]

def read_input():
    wires = dict()
    with open("2015/day7/input.txt") as f:
        lines = f.readlines()
        for l in lines:
            expr, target = l.strip().split(" -> ")
            wires[target] = expr
    return wires

wires = read_input()
wire_a_val = evaluate(wires, dict(), "a")
print("Part 1:", wire_a_val)
wires["b"] = str(wire_a_val)
print("Part 2:", evaluate(wires, dict(), "a"))