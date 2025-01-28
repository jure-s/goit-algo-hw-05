import timeit

def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    last = {pattern[i]: i for i in range(m)}
    i = m - 1
    while i < n:
        k = m - 1
        j = i
        while k >= 0 and text[j] == pattern[k]:
            j -= 1
            k -= 1
        if k == -1:
            return j + 1
        i += m - min(k, last.get(text[i], -1) + 1)
    return -1

def knuth_morris_pratt_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    lps = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1

def rabin_karp_search(text, pattern, prime=101):
    m, n = len(pattern), len(text)
    if m == 0:
        return -1
    d = 256
    p = t = 0
    h = 1
    for _ in range(m - 1):
        h = (h * d) % prime
    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime
    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t < 0:
                t += prime
    return -1

# Завантаження тексту для тестування
with open("task_3/стаття 1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()

with open("task_3/стаття 2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()

existing_substring = "алгоритм"  # Приклад існуючого підрядка
non_existing_substring = "відсутній"  # Вигаданий підрядок

# Функція для вимірювання часу виконання
def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=10)

# Вимірювання для статті 1
results_1 = {
    "Boyer-Moore": (measure_time(boyer_moore_search, text1, existing_substring),
                    measure_time(boyer_moore_search, text1, non_existing_substring)),
    "KMP": (measure_time(knuth_morris_pratt_search, text1, existing_substring),
            measure_time(knuth_morris_pratt_search, text1, non_existing_substring)),
    "Rabin-Karp": (measure_time(rabin_karp_search, text1, existing_substring),
                   measure_time(rabin_karp_search, text1, non_existing_substring)),
}

# Вимірювання для статті 2
results_2 = {
    "Boyer-Moore": (measure_time(boyer_moore_search, text2, existing_substring),
                    measure_time(boyer_moore_search, text2, non_existing_substring)),
    "KMP": (measure_time(knuth_morris_pratt_search, text2, existing_substring),
            measure_time(knuth_morris_pratt_search, text2, non_existing_substring)),
    "Rabin-Karp": (measure_time(rabin_karp_search, text2, existing_substring),
                   measure_time(rabin_karp_search, text2, non_existing_substring)),
}

# Функція для форматованого виводу результатів
def print_results(title, results):
    print(f"\n{title}")
    print("=" * 50)
    print(f"{'Алгоритм':<15}{'Існуючий (сек)':<20}{'Вигаданий (сек)':<20}")
    print("-" * 50)
    for algorithm, times in results.items():
        print(f"{algorithm:<15}{times[0]:<20.6f}{times[1]:<20.6f}")
    print("=" * 50)

# Виведення результатів у форматованому вигляді
print_results("Результати для статті 1", results_1)
print_results("Результати для статті 2", results_2)
