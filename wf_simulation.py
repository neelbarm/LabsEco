"""
Wright-Fisher drift + selection simulation for Lab 9 (Population Genetics).

This is a faithful Python reproduction of the model behind the course's web app,
evobiR `wf_model` (https://evobir.shinyapps.io/wf_model/, server.R -> ShinyPopGen):

  - n diploid individuals  -> 2n gene copies (drift variance ~ A(1-A)/2n)
  - each generation: form Hardy-Weinberg offspring at the current allele freq A,
    weight offspring by genotype fitness (AA, Aa, aa), then resample n adults with
    replacement -> next generation.
  - a replicate is "fixed" when final A = 1 (value == n) and "lost" when A = 0.

Run:  python3 wf_simulation.py
Because drift is stochastic, exact fix/loss counts vary between runs; the patterns
(and the numbers recorded in the completed worksheet) are representative draws.
"""

import random


def shiny_popgen(fitness, initial_A, pop, gen=100, iterations=10, rng=None):
    """Return the final value (#A alleles / 2) for each of `iterations` replicates."""
    rng = rng or random
    wAA, wAa, waa = fitness
    finals = []
    for _ in range(iterations):
        adults = ([1] * round(pop * initial_A ** 2)
                  + [2] * round(pop * 2 * initial_A * (1 - initial_A))
                  + [3] * round(pop * (1 - initial_A) ** 2))
        last = None
        for _ in range(gen):
            A = (2 * adults.count(1) + adults.count(2)) / (pop * 2)
            babies = ([1] * round(pop * A ** 2)
                      + [2] * round(pop * 2 * A * (1 - A))
                      + [3] * round(pop * (1 - A) ** 2))
            if not babies:
                babies = adults
            weights = [wAA if b == 1 else wAa if b == 2 else waa for b in babies]
            adults = rng.choices(babies, weights=weights, k=pop)
            last = adults.count(1) + 0.5 * adults.count(2)
        finals.append(last)
    return finals


def run_five(fitness, initial_A, pop, seed):
    """5 runs x 10 replicates; return list of (fixed, lost) per run."""
    rng = random.Random(seed)
    out = []
    for _ in range(5):
        finals = shiny_popgen(fitness, initial_A, pop, rng=rng)
        fixed = sum(1 for v in finals if v == pop)
        lost = sum(1 for v in finals if v == 0)
        out.append((fixed, lost))
    return out


SIMS = [
    ("Simulation 1", (1.0, 1.0, 1.0), 0.5, 100),
    ("Simulation 2", (1.0, 1.0, 1.0), 0.5, 1000),
    ("Simulation 3", (1.0, 1.0, 1.0), 0.1, 100),
    ("Simulation 4", (1.0, 1.0, 1.0), 0.1, 1000),
    ("Simulation 5", (1.0, 0.9, 0.9), 0.5, 100),
    ("Simulation 6", (1.0, 0.8, 0.8), 0.5, 100),
]

if __name__ == "__main__":
    for i, (name, fit, a0, pop) in enumerate(SIMS):
        rows = run_five(fit, a0, pop, seed=100 + i)
        print(f"\n{name}: n={pop}, f(A)0={a0}, fitness AA/Aa/aa={fit}")
        print(f"  {'Run':6s}{'fixed f(A)=1':>14s}{'lost f(A)=0':>14s}")
        for r, (fx, ls) in enumerate(rows, 1):
            print(f"  Run {r:<3d}{fx:>13d}{ls:>14d}")
