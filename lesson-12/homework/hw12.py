
import threading
from math import isqrt
from collections import Counter

primes = []
lock = threading.Lock()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end):
    local_primes = []
    for num in range(start, end):
        if is_prime(num):
            local_primes.append(num)
    with lock:
        primes.extend(local_primes)

def threaded_prime_checker(start, end, num_threads):
    step = (end - start) // num_threads
    threads = []

    for i in range(num_threads):
        thread_start = start + i * step
        thread_end = end if i == num_threads - 1 else thread_start + step
        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Topilgan tub sonlar:")
    print(sorted(primes))


# Exercise 2: Threaded File Processing (Word Count)

word_counts = Counter()
lock = threading.Lock()

def count_words(lines):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)

    with lock:
        word_counts.update(local_counter)

def threaded_word_counter(file_path, num_threads):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        step = len(lines) // num_threads
        threads = []

        for i in range(num_threads):
            start = i * step
            end = len(lines) if i == num_threads - 1 else (i + 1) * step
            thread = threading.Thread(target=count_words, args=(lines[start:end],))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("\nSo‘zlar soni:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Fayl topilmadi. Iltimos, to‘g‘ri fayl manzilini kiriting.")



