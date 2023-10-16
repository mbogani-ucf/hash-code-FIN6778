from hashlib import sha256
from time import perf_counter

def main(name, lz):
    attempts = 1
    prefix = '0' * lz
    while not (hash_ := sha256(f'{name}{attempts}'.encode()).hexdigest()).startswith(prefix):
        attempts += 1
    return name, hash_, attempts

for lz in 5, 6:
    start = perf_counter()
    name, hash_, attempts = main('Marco Daman Sulaiman William nasiudy283', lz)
    end = perf_counter()
    print(f'Found hash: {hash_}')
    print(f'Number of attempts: {attempts}')
    print(f'Execution time: {end-start:.15f} seconds')
    print(f'Final pre-image: {name}{attempts}\n')