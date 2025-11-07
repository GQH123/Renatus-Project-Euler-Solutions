# Problem 130. Composites with Prime Repunit Property
# Link: https://projecteuler.net/problem=130
# Answer: 149253
# Language: Python
# Author: Renatus
# Date: 2025-08-29 22:22:50

from math import gcd
from functools import lru_cache


min_prime_index = []
max_prime_index = []
is_prime = []
primes = []
phi = []


# Euler's Prime Sieve
def preprocess_primes(n=int(1e6)):  # sieve all primes in [1, n]
    global min_prime_index, max_prime_index, primes, is_prime, phi
    min_prime_index = [-1] * (n + 1)
    max_prime_index = [-1] * (n + 1)
    is_prime = [True] * (n + 1)
    phi = [0] * (n + 1)
    phi[1] = 1
    primes = []
    is_prime[0] = is_prime[1] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            min_prime_index[i] = len(primes) - 1
            max_prime_index[i] = len(primes) - 1
            phi[i] = i - 1
        for p_index, p in enumerate(primes):
            if i * p > n:
                break
            is_prime[i * p] = False
            min_prime_index[i * p] = p_index
            max_prime_index[i * p] = max_prime_index[i]
            if i % p == 0:
                phi[i * p] = phi[i] * p
                break
            else:
                phi[i * p] = phi[i] * (p - 1)


def fast_power_mod(x, y, mod):
    result = 1
    while y > 0:
        if (y & 1) == 1:
            result = (result * x) % mod
        x = (x * x) % mod
        y >>= 1
    return result


def brute_force_eumerate_n():
    preprocess_primes(int(1e7))
    n = 2
    count = 0
    answer = 0
    while n <= int(1e7):
        if gcd(n, 10) != 1 or is_prime[n]:
            n += 1
            continue
        A_n = n * 3 if n % 3 == 0 else n
        phi_n = phi[n] * 3 if n % 3 == 0 else phi[n]
        for d in range(1, phi_n):
            if d * d > phi_n:
                break
            if phi_n % d != 0:
                continue
            
            f = d
            # print(f'f = {f}, mod = {fast_power_mod(10, f, 9 * n)}')
            if fast_power_mod(10, f, 9 * n) == 1:
                A_n = min(A_n, f)
            
            f = phi_n // d
            # print(f'f = {f}, mod = {fast_power_mod(10, f, 9 * n)}')
            if fast_power_mod(10, f, 9 * n) == 1:
                A_n = min(A_n, f)
        
        # print(f'found A({n}) = {A_n}')
        if (n - 1) % A_n == 0:
            answer += n
            count += 1
            print(f'found {count}-th composite values of n={n} for which n-1 is divisible by A({n}) = {A_n}')
            if count == 25:
                print(f'answer = {answer}')
                return
        n += 1
        # return


if __name__ == '__main__':
    brute_force_eumerate_n()
    pass


"""
    found 1-th composite values of n=91 for which n-1 is divisible by A(91) = 6
    found 2-th composite values of n=259 for which n-1 is divisible by A(259) = 6
    found 3-th composite values of n=451 for which n-1 is divisible by A(451) = 10
    found 4-th composite values of n=481 for which n-1 is divisible by A(481) = 6
    found 5-th composite values of n=703 for which n-1 is divisible by A(703) = 18
    found 6-th composite values of n=1729 for which n-1 is divisible by A(1729) = 18
    found 7-th composite values of n=2821 for which n-1 is divisible by A(2821) = 30
    found 8-th composite values of n=2981 for which n-1 is divisible by A(2981) = 10
    found 9-th composite values of n=3367 for which n-1 is divisible by A(3367) = 6
    found 10-th composite values of n=4141 for which n-1 is divisible by A(4141) = 20
    found 11-th composite values of n=4187 for which n-1 is divisible by A(4187) = 13
    found 12-th composite values of n=5461 for which n-1 is divisible by A(5461) = 42
    found 13-th composite values of n=6533 for which n-1 is divisible by A(6533) = 46
    found 14-th composite values of n=6541 for which n-1 is divisible by A(6541) = 30
    found 15-th composite values of n=6601 for which n-1 is divisible by A(6601) = 330
    found 16-th composite values of n=7471 for which n-1 is divisible by A(7471) = 30
    found 17-th composite values of n=7777 for which n-1 is divisible by A(7777) = 12
    found 18-th composite values of n=8149 for which n-1 is divisible by A(8149) = 28
    found 19-th composite values of n=8401 for which n-1 is divisible by A(8401) = 15
    found 20-th composite values of n=8911 for which n-1 is divisible by A(8911) = 198
    found 21-th composite values of n=10001 for which n-1 is divisible by A(10001) = 8
    found 22-th composite values of n=11111 for which n-1 is divisible by A(11111) = 5
    found 23-th composite values of n=12403 for which n-1 is divisible by A(12403) = 78
    found 24-th composite values of n=13981 for which n-1 is divisible by A(13981) = 30
    found 25-th composite values of n=14701 for which n-1 is divisible by A(14701) = 60
    found 26-th composite values of n=14911 for which n-1 is divisible by A(14911) = 30
    found 27-th composite values of n=15211 for which n-1 is divisible by A(15211) = 390
    found 28-th composite values of n=15841 for which n-1 is divisible by A(15841) = 120
    found 29-th composite values of n=19201 for which n-1 is divisible by A(19201) = 30
    found 30-th composite values of n=21931 for which n-1 is divisible by A(21931) = 30
    found 31-th composite values of n=22321 for which n-1 is divisible by A(22321) = 48
    found 32-th composite values of n=24013 for which n-1 is divisible by A(24013) = 174
    found 33-th composite values of n=24661 for which n-1 is divisible by A(24661) = 30
    found 34-th composite values of n=27613 for which n-1 is divisible by A(27613) = 52
    found 35-th composite values of n=29341 for which n-1 is divisible by A(29341) = 60
    found 36-th composite values of n=34133 for which n-1 is divisible by A(34133) = 1484
    found 37-th composite values of n=34441 for which n-1 is divisible by A(34441) = 60
    found 38-th composite values of n=35113 for which n-1 is divisible by A(35113) = 24
    found 39-th composite values of n=38503 for which n-1 is divisible by A(38503) = 138
    found 40-th composite values of n=41041 for which n-1 is divisible by A(41041) = 30
    found 41-th composite values of n=45527 for which n-1 is divisible by A(45527) = 26
    found 42-th composite values of n=46657 for which n-1 is divisible by A(46657) = 96
    found 43-th composite values of n=48433 for which n-1 is divisible by A(48433) = 48
    found 44-th composite values of n=50851 for which n-1 is divisible by A(50851) = 30
    found 45-th composite values of n=50881 for which n-1 is divisible by A(50881) = 80
    found 46-th composite values of n=52633 for which n-1 is divisible by A(52633) = 408
    found 47-th composite values of n=54913 for which n-1 is divisible by A(54913) = 88
    found 48-th composite values of n=57181 for which n-1 is divisible by A(57181) = 30
    found 49-th composite values of n=63139 for which n-1 is divisible by A(63139) = 102
    found 50-th composite values of n=63973 for which n-1 is divisible by A(63973) = 18
    found 51-th composite values of n=65311 for which n-1 is divisible by A(65311) = 30
    found 52-th composite values of n=66991 for which n-1 is divisible by A(66991) = 30
    found 53-th composite values of n=67861 for which n-1 is divisible by A(67861) = 26
    found 54-th composite values of n=68101 for which n-1 is divisible by A(68101) = 150
    found 55-th composite values of n=75361 for which n-1 is divisible by A(75361) = 240
    found 56-th composite values of n=79003 for which n-1 is divisible by A(79003) = 99
    found 57-th composite values of n=82513 for which n-1 is divisible by A(82513) = 108
    found 58-th composite values of n=83119 for which n-1 is divisible by A(83119) = 21
    found 59-th composite values of n=94139 for which n-1 is divisible by A(94139) = 22
    found 60-th composite values of n=95161 for which n-1 is divisible by A(95161) = 30
    found 61-th composite values of n=97273 for which n-1 is divisible by A(97273) = 42
    found 62-th composite values of n=97681 for which n-1 is divisible by A(97681) = 1320
    found 63-th composite values of n=100001 for which n-1 is divisible by A(100001) = 10
    found 64-th composite values of n=101101 for which n-1 is divisible by A(101101) = 12
    found 65-th composite values of n=101491 for which n-1 is divisible by A(101491) = 30
    found 66-th composite values of n=102173 for which n-1 is divisible by A(102173) = 41
    found 67-th composite values of n=108691 for which n-1 is divisible by A(108691) = 30
    found 68-th composite values of n=113201 for which n-1 is divisible by A(113201) = 50
    found 69-th composite values of n=115627 for which n-1 is divisible by A(115627) = 42
    found 70-th composite values of n=115921 for which n-1 is divisible by A(115921) = 30
    found 71-th composite values of n=118301 for which n-1 is divisible by A(118301) = 140
    found 72-th composite values of n=118957 for which n-1 is divisible by A(118957) = 46
    found 73-th composite values of n=122221 for which n-1 is divisible by A(122221) = 10
    found 74-th composite values of n=126217 for which n-1 is divisible by A(126217) = 72
    found 75-th composite values of n=128713 for which n-1 is divisible by A(128713) = 12
    found 76-th composite values of n=130351 for which n-1 is divisible by A(130351) = 30
    found 77-th composite values of n=131821 for which n-1 is divisible by A(131821) = 60
    found 78-th composite values of n=134821 for which n-1 is divisible by A(134821) = 28
    found 79-th composite values of n=134863 for which n-1 is divisible by A(134863) = 78
    found 80-th composite values of n=137137 for which n-1 is divisible by A(137137) = 24
    found 81-th composite values of n=137149 for which n-1 is divisible by A(137149) = 132
    found 82-th composite values of n=138481 for which n-1 is divisible by A(138481) = 120
    found 83-th composite values of n=139231 for which n-1 is divisible by A(139231) = 1365
    found 84-th composite values of n=145181 for which n-1 is divisible by A(145181) = 20
    found 85-th composite values of n=147001 for which n-1 is divisible by A(147001) = 168
    found 86-th composite values of n=148417 for which n-1 is divisible by A(148417) = 192
    found 87-th composite values of n=152551 for which n-1 is divisible by A(152551) = 90
    found 88-th composite values of n=158497 for which n-1 is divisible by A(158497) = 32
    found 89-th composite values of n=162401 for which n-1 is divisible by A(162401) = 2320
    found 90-th composite values of n=164761 for which n-1 is divisible by A(164761) = 120
    found 91-th composite values of n=166499 for which n-1 is divisible by A(166499) = 166
    found 92-th composite values of n=170017 for which n-1 is divisible by A(170017) = 16
    found 93-th composite values of n=172081 for which n-1 is divisible by A(172081) = 60
    found 94-th composite values of n=179881 for which n-1 is divisible by A(179881) = 24
    found 95-th composite values of n=188191 for which n-1 is divisible by A(188191) = 153
    found 96-th composite values of n=188269 for which n-1 is divisible by A(188269) = 58
    found 97-th composite values of n=188461 for which n-1 is divisible by A(188461) = 108
    found 98-th composite values of n=188501 for which n-1 is divisible by A(188501) = 250
    found 99-th composite values of n=196651 for which n-1 is divisible by A(196651) = 30
    found 100-th composite values of n=201917 for which n-1 is divisible by A(201917) = 22
    found 101-th composite values of n=216001 for which n-1 is divisible by A(216001) = 60
    found 102-th composite values of n=216931 for which n-1 is divisible by A(216931) = 30
    found 103-th composite values of n=225589 for which n-1 is divisible by A(225589) = 66
    found 104-th composite values of n=226273 for which n-1 is divisible by A(226273) = 32
    found 105-th composite values of n=229633 for which n-1 is divisible by A(229633) = 276
    found 106-th composite values of n=231337 for which n-1 is divisible by A(231337) = 72
    found 107-th composite values of n=234421 for which n-1 is divisible by A(234421) = 60
    found 108-th composite values of n=237169 for which n-1 is divisible by A(237169) = 486
    found 109-th composite values of n=237817 for which n-1 is divisible by A(237817) = 162
    found 110-th composite values of n=245491 for which n-1 is divisible by A(245491) = 42
    found 111-th composite values of n=247753 for which n-1 is divisible by A(247753) = 444
    found 112-th composite values of n=248677 for which n-1 is divisible by A(248677) = 138
    found 113-th composite values of n=250717 for which n-1 is divisible by A(250717) = 204
    found 114-th composite values of n=251251 for which n-1 is divisible by A(251251) = 150
    found 115-th composite values of n=252601 for which n-1 is divisible by A(252601) = 60
    found 116-th composite values of n=253099 for which n-1 is divisible by A(253099) = 774
    found 117-th composite values of n=269011 for which n-1 is divisible by A(269011) = 366
    found 118-th composite values of n=269569 for which n-1 is divisible by A(269569) = 624
    found 119-th composite values of n=274231 for which n-1 is divisible by A(274231) = 66
    found 120-th composite values of n=281821 for which n-1 is divisible by A(281821) = 30
    found 121-th composite values of n=286903 for which n-1 is divisible by A(286903) = 378
    found 122-th composite values of n=287749 for which n-1 is divisible by A(287749) = 12
    found 123-th composite values of n=287809 for which n-1 is divisible by A(287809) = 32
    found 124-th composite values of n=294409 for which n-1 is divisible by A(294409) = 216
    found 125-th composite values of n=298033 for which n-1 is divisible by A(298033) = 84
    found 126-th composite values of n=301081 for which n-1 is divisible by A(301081) = 20
    found 127-th composite values of n=302177 for which n-1 is divisible by A(302177) = 224
    found 128-th composite values of n=304057 for which n-1 is divisible by A(304057) = 738
    found 129-th composite values of n=314821 for which n-1 is divisible by A(314821) = 1980
    found 130-th composite values of n=334153 for which n-1 is divisible by A(334153) = 4284
    found 131-th composite values of n=340561 for which n-1 is divisible by A(340561) = 528
    found 132-th composite values of n=341503 for which n-1 is divisible by A(341503) = 42
    found 133-th composite values of n=346801 for which n-1 is divisible by A(346801) = 102
    found 134-th composite values of n=351809 for which n-1 is divisible by A(351809) = 46
    found 135-th composite values of n=357641 for which n-1 is divisible by A(357641) = 20
    found 136-th composite values of n=364277 for which n-1 is divisible by A(364277) = 44
    found 137-th composite values of n=366337 for which n-1 is divisible by A(366337) = 12
    found 138-th composite values of n=372731 for which n-1 is divisible by A(372731) = 10
    found 139-th composite values of n=385003 for which n-1 is divisible by A(385003) = 438
    found 140-th composite values of n=390313 for which n-1 is divisible by A(390313) = 24
    found 141-th composite values of n=391141 for which n-1 is divisible by A(391141) = 180
    found 142-th composite values of n=399001 for which n-1 is divisible by A(399001) = 60
    found 143-th composite values of n=401401 for which n-1 is divisible by A(401401) = 600
    found 144-th composite values of n=410041 for which n-1 is divisible by A(410041) = 40
    found 145-th composite values of n=413339 for which n-1 is divisible by A(413339) = 34
    found 146-th composite values of n=420343 for which n-1 is divisible by A(420343) = 1326
    found 147-th composite values of n=437251 for which n-1 is divisible by A(437251) = 110
    found 148-th composite values of n=451091 for which n-1 is divisible by A(451091) = 158
    found 149-th composite values of n=455971 for which n-1 is divisible by A(455971) = 30
    found 150-th composite values of n=458641 for which n-1 is divisible by A(458641) = 252
    found 151-th composite values of n=463241 for which n-1 is divisible by A(463241) = 148
    found 152-th composite values of n=463489 for which n-1 is divisible by A(463489) = 96
    found 153-th composite values of n=481601 for which n-1 is divisible by A(481601) = 200
    found 154-th composite values of n=488881 for which n-1 is divisible by A(488881) = 360
    found 155-th composite values of n=489997 for which n-1 is divisible by A(489997) = 156
    found 156-th composite values of n=491063 for which n-1 is divisible by A(491063) = 202
    found 157-th composite values of n=492101 for which n-1 is divisible by A(492101) = 140
    found 158-th composite values of n=497377 for which n-1 is divisible by A(497377) = 32
    found 159-th composite values of n=497503 for which n-1 is divisible by A(497503) = 498
    found 160-th composite values of n=497927 for which n-1 is divisible by A(497927) = 22
    found 161-th composite values of n=505363 for which n-1 is divisible by A(505363) = 78
    found 162-th composite values of n=507529 for which n-1 is divisible by A(507529) = 84
    found 163-th composite values of n=509971 for which n-1 is divisible by A(509971) = 534
    found 164-th composite values of n=511969 for which n-1 is divisible by A(511969) = 24
    found 165-th composite values of n=512461 for which n-1 is divisible by A(512461) = 60
    found 166-th composite values of n=520801 for which n-1 is divisible by A(520801) = 30
    found 167-th composite values of n=522349 for which n-1 is divisible by A(522349) = 228
    found 168-th composite values of n=530881 for which n-1 is divisible by A(530881) = 3360
    found 169-th composite values of n=532171 for which n-1 is divisible by A(532171) = 54
    found 170-th composite values of n=552721 for which n-1 is divisible by A(552721) = 240
    found 171-th composite values of n=567721 for which n-1 is divisible by A(567721) = 24
    found 172-th composite values of n=585631 for which n-1 is divisible by A(585631) = 30
    found 173-th composite values of n=586993 for which n-1 is divisible by A(586993) = 336
    found 174-th composite values of n=588193 for which n-1 is divisible by A(588193) = 66
    found 175-th composite values of n=589537 for which n-1 is divisible by A(589537) = 96
    found 176-th composite values of n=595231 for which n-1 is divisible by A(595231) = 30
    found 177-th composite values of n=597871 for which n-1 is divisible by A(597871) = 273
    found 178-th composite values of n=601657 for which n-1 is divisible by A(601657) = 132
    found 179-th composite values of n=603961 for which n-1 is divisible by A(603961) = 60
    found 180-th composite values of n=607321 for which n-1 is divisible by A(607321) = 120
    found 181-th composite values of n=632641 for which n-1 is divisible by A(632641) = 32
    found 182-th composite values of n=634351 for which n-1 is divisible by A(634351) = 75
    found 183-th composite values of n=642001 for which n-1 is divisible by A(642001) = 200
    found 184-th composite values of n=658801 for which n-1 is divisible by A(658801) = 240
    found 185-th composite values of n=665401 for which n-1 is divisible by A(665401) = 150
    found 186-th composite values of n=670033 for which n-1 is divisible by A(670033) = 198
    found 187-th composite values of n=679861 for which n-1 is divisible by A(679861) = 30
    found 188-th composite values of n=710533 for which n-1 is divisible by A(710533) = 486
    found 189-th composite values of n=721801 for which n-1 is divisible by A(721801) = 600
    found 190-th composite values of n=736291 for which n-1 is divisible by A(736291) = 202
    found 191-th composite values of n=741751 for which n-1 is divisible by A(741751) = 430
    found 192-th composite values of n=748657 for which n-1 is divisible by A(748657) = 432
    found 193-th composite values of n=749521 for which n-1 is divisible by A(749521) = 180
    found 194-th composite values of n=754369 for which n-1 is divisible by A(754369) = 96
    found 195-th composite values of n=764491 for which n-1 is divisible by A(764491) = 30
    found 196-th composite values of n=765703 for which n-1 is divisible by A(765703) = 618
    found 197-th composite values of n=827281 for which n-1 is divisible by A(827281) = 30
    found 198-th composite values of n=838201 for which n-1 is divisible by A(838201) = 300
    found 199-th composite values of n=841633 for which n-1 is divisible by A(841633) = 96
    found 200-th composite values of n=847693 for which n-1 is divisible by A(847693) = 108
    found 201-th composite values of n=852841 for which n-1 is divisible by A(852841) = 60
    found 202-th composite values of n=853381 for which n-1 is divisible by A(853381) = 60
    found 203-th composite values of n=868001 for which n-1 is divisible by A(868001) = 155
    found 204-th composite values of n=873181 for which n-1 is divisible by A(873181) = 220
    found 205-th composite values of n=880237 for which n-1 is divisible by A(880237) = 84
    found 206-th composite values of n=886033 for which n-1 is divisible by A(886033) = 112
    found 207-th composite values of n=903169 for which n-1 is divisible by A(903169) = 32
    found 208-th composite values of n=906193 for which n-1 is divisible by A(906193) = 336
    found 209-th composite values of n=909709 for which n-1 is divisible by A(909709) = 246
    found 210-th composite values of n=924001 for which n-1 is divisible by A(924001) = 336
    found 211-th composite values of n=929633 for which n-1 is divisible by A(929633) = 556
    found 212-th composite values of n=963857 for which n-1 is divisible by A(963857) = 214
    found 213-th composite values of n=974611 for which n-1 is divisible by A(974611) = 30
    found 214-th composite values of n=976873 for which n-1 is divisible by A(976873) = 312
    found 215-th composite values of n=981317 for which n-1 is divisible by A(981317) = 202
    found 216-th composite values of n=989017 for which n-1 is divisible by A(989017) = 58
    found 217-th composite values of n=997633 for which n-1 is divisible by A(997633) = 576
    found 218-th composite values of n=997981 for which n-1 is divisible by A(997981) = 60
    found 219-th composite values of n=999001 for which n-1 is divisible by A(999001) = 18
    found 220-th composite values of n=1004329 for which n-1 is divisible by A(1004329) = 78
    found 221-th composite values of n=1005697 for which n-1 is divisible by A(1005697) = 96
    found 222-th composite values of n=1024651 for which n-1 is divisible by A(1024651) = 990
    found 223-th composite values of n=1033669 for which n-1 is divisible by A(1033669) = 306
    found 224-th composite values of n=1038331 for which n-1 is divisible by A(1038331) = 90
    found 225-th composite values of n=1039441 for which n-1 is divisible by A(1039441) = 30
    found 226-th composite values of n=1039849 for which n-1 is divisible by A(1039849) = 222
    found 227-th composite values of n=1041043 for which n-1 is divisible by A(1041043) = 186
    found 228-th composite values of n=1042417 for which n-1 is divisible by A(1042417) = 456
    found 229-th composite values of n=1056331 for which n-1 is divisible by A(1056331) = 726
    found 230-th composite values of n=1069993 for which n-1 is divisible by A(1069993) = 462
    found 231-th composite values of n=1080697 for which n-1 is divisible by A(1080697) = 148
    found 232-th composite values of n=1081649 for which n-1 is divisible by A(1081649) = 268
    found 233-th composite values of n=1082809 for which n-1 is divisible by A(1082809) = 648
    found 234-th composite values of n=1090051 for which n-1 is divisible by A(1090051) = 390
    found 235-th composite values of n=1096681 for which n-1 is divisible by A(1096681) = 228
"""