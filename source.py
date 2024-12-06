# Th3_d33p3r_y0u_l00k_th3_d4rk3r_1t_g3ts...
# s0m3t1m3s_th3_truth_1s_h1dd3n_1n_pl41n_s1ght

import mmap as _______;
import os;
import random as _____;
import signal as _________;
import threading as ________;
import time as ______;

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# 01101101 01100001 01111001 01100010 01100101
# 01110100 01101000 01100101 00100000 01110010
# 01100101 01110011 01110100 00100000 01101001
# 01110011 00100000 01101000 01100101 01110010 01100101

λ = type('λ', (), {'δ': lambda x: eval(x)})()
Ω = lambda x: x if isinstance(x, str) else ''.join(chr(ord(c)) for c in str(x))
Σ = lambda x: bytes([ord(c) ^ 42 for c in x])


class Δ:
    def __init__(self):
        self.μ = [0] * 16
        self.π = _______.mmap(-1, 4096)
        self.θ = 0
        self.ξ = []
        self.ψ = {}
        self.φ = []
        self.ω = 3
        self.γ = ________.Thread(target=self._α)
        self.γ.daemon = True
        self.γ.start()
        _________.signal(2, self._β)

    def _α(self):
        while True:
            if self._δ():
                self._ε()
            ______.sleep(_____.random())

    def _β(self, σ, τ):
        self.μ = [_____.randint(0, 0xFFFFFFFF) for _ in range(16)]

    def _δ(self):
        try:
            return ______.time() - ______.time() > 0.1
        except:
            return True

    def _ε(self):
        self.μ = [_____.randint(0, 255) for _ in range(16)]


def η():
    if Δ()._δ():
        print("Nice try! :)")
        return

    # Original flag string (don't look here!)
    ζ = "flag{M4st3r_0f_B1n4ry_Ch40s_2024}"

    # Multiple layers of transformations
    κ = [ord(c) for c in ζ]
    ι = [x ^ 42 for x in κ]
    θ = [x ^ 0x55 for x in ι]
    ρ = bytes([x ^ 0x33 for x in θ])

    # Additional encryption layers
    σ = os.urandom(32)
    τ = AESGCM(σ)
    υ = os.urandom(12)
    φ = τ.encrypt(υ, ρ, None)

    with open("binary_maze", "wb") as f:
        f.write(φ)
    with open("binary_maze.iv", "wb") as f:
        f.write(υ)


# cr3d1ts: th3_cr34t0r_0f_th1s_puzzl3_h4s_l3ft_s0m3_tr4c3s
if __name__ == "__main__":
    η()

# f1n4l_h1nt: l00k_cl0s3ly_4t_th3_tr4nsf0rm4t10ns
# r3m3mb3r: th3_k3y_t0_und3rst4nd1ng_1s_1n_th3_p4tt3rns
#
# ...01011111 01100101 01101110 01100100...
