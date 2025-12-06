# https://adventofcode.com/2025/day/5

def read_file(filename="input.txt"):
    fresh_ranges_IDs = []
    available_IDs = []
    with open(f"2025/day5/{filename}", "r") as f:
        for r in f.readlines():
            if not r.strip():
                continue
            if r and "-" in r:
                fresh_ranges_IDs.append(tuple(map(int, r.strip().split("-"))))
            elif r and "-" not in r:
                available_IDs.append(int(r.strip()))
    return fresh_ranges_IDs, available_IDs

def is_id_fresh(fresh_ranges_IDs, current_id):
    for start, end in fresh_ranges_IDs:
        if start <= current_id  and current_id <= end:
            return True
    return False

def calc_fresh_ids(fresh_IDs:list):
    merged_IDs = []
    for f_start, f_end in fresh_IDs:
        m_min, m_max, removed, overlapped = float('inf'), 0, set(), False
        for m_start, m_end in merged_IDs:
            if m_start <= f_start and f_end <= m_end: # IDs overlapped by merged range
                overlapped = True
                break
            elif f_start <= m_start and m_end <= f_end: # IDs overlap a merged range
                m_min, m_max = f_start, f_end
                removed.add((m_start, m_end))
            elif m_start <= f_start and f_start <= m_end and f_end > m_end: # partial overlap right
                m_min = m_start if m_start < m_min else m_min
                m_max = f_end if m_max < f_end else m_max
                removed.add((m_start, m_end))
            elif m_start <= f_end and f_end <= m_end and f_start < m_start: # partial overlap left
                m_min = f_start if m_min > f_start else m_min
                m_max = m_end if m_end > m_max else m_max
                removed.add((m_start, m_end))
        if len(removed) > 0:
            for r in removed:
                merged_IDs.remove(r)
            merged_IDs.append((m_min, m_max)) # add new merged range
        else:
            if not overlapped:
                merged_IDs.append((f_start, f_end))
    return sum([end-start+1 for start,end in merged_IDs])

def part1():
    fresh_IDs, available_IDs = read_file()
    result = sum([1 for id in available_IDs if is_id_fresh(fresh_IDs, id)])
    print(f"Part 1: {result}")

def part2():
    fresh_IDs, available_IDs = read_file()
    result = calc_fresh_ids(fresh_IDs)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    part1()
    part2()