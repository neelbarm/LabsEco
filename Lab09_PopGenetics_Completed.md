# Lab 9: Population Genetics

Name: ________________________   Date: ________________________

Simulator: Wright-Fisher model (evobiR wf_model), https://evobir.shinyapps.io/wf_model/

Each "Run" is one execution of the simulation, which is 10 replicate populations carried for 100 generations. For each run I counted how many of the 10 lines ended at Generation 100 with allele A fixed (f(A) = 1) or lost (f(A) = 0). Lines that were neither fixed nor lost still had both alleles.

## Simulation 1: n = 100, f(A) = 0.5, no selection (all fitness = 1.0)

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 0 | 0 |
| Run 2 | 0 | 3 |
| Run 3 | 1 | 1 |
| Run 4 | 2 | 0 |
| Run 5 | 0 | 1 |

Do you always obtain the same result? Why?

No. The counts change from run to run. Drift works by random sampling: each generation, the alleles that get passed to the next one are a chance sample of the parents, so every line wanders on its own and each run of 10 lines is a fresh draw. A starts at 0.5 and no genotype has an edge, so it is as likely to drift up to fixation as down to loss. At n = 100 the sampling error is small enough that after 100 generations most lines are still in the middle with both alleles present.

## Simulation 2: n = 1000, f(A) = 0.5, no selection

Prediction: A bigger population has less sampling error, so the frequencies should barely move. I expect few or no lines to reach 0 or 1 in 100 generations, with most sitting close to 0.5.

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 0 | 0 |
| Run 2 | 0 | 0 |
| Run 3 | 0 | 0 |
| Run 4 | 0 | 0 |
| Run 5 | 0 | 0 |

What happened? Compare with Simulation 1.

Nothing fixed and nothing was lost. All 50 lines stayed bunched around 0.5 instead of fanning out to the edges the way they did at n = 100. Going from n = 100 to n = 1000 cut the drift down to almost nothing. Drift has a bigger effect in small populations than in large ones.

## Simulation 3: n = 100, f(A) = 0.1, no selection

Prediction: A starts rare at 0.1. An allele's chance of fixing equals its current frequency, so I expect about 1 line in 10 to fix A and the other 9 to lose it. Loss should win out.

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 0 | 10 |
| Run 2 | 0 | 7 |
| Run 3 | 0 | 8 |
| Run 4 | 0 | 8 |
| Run 5 | 0 | 4 |

What happened? Compare with Simulation 1.

Loss dominated: 37 of the 50 lines lost A, 13 still carried both alleles, and none fixed within 100 generations. Starting at 0.1 instead of 0.5 (Simulation 1) made loss far more common, which fits the rule that an allele's fixation chance equals its starting frequency. The 10% or so that would fix given enough time mostly could not climb from 0.1 all the way to 1.0 in only 100 generations, so they show up as lines that are still segregating. A rare allele in a small population is an easy thing to lose.

## Simulation 4: n = 1000, f(A) = 0.1, no selection

Prediction: Same rare start at 0.1, but n = 1000 makes drift weak. The allele should mostly sit near 0.1 without fixing or being lost.

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 0 | 1 |
| Run 2 | 0 | 0 |
| Run 3 | 0 | 0 |
| Run 4 | 0 | 0 |
| Run 5 | 0 | 0 |

What happened? Compare with Simulation 3.

Barely anything changed. One line out of 50 lost A, none fixed, and the rest held near 0.1. Simulation 3 lost the same rare allele in 37 of 50 lines at n = 100, so the bigger population kept it around much longer. Large populations hold onto their variation, while small ones bleed it off by chance.

## Simulation 5: n = 100, f(A) = 0.5, fitness AA = 1.0, Aa = 0.9, aa = 0.9

Is this selection for or against allele A? What do you predict? Why?

Selection favors A. AA has the top fitness at 1.0 while Aa and aa both sit at 0.9, so an individual needs two copies of A to get the benefit. That makes A a recessive advantageous allele and puts a against it. I expect A to climb and fix in most or all lines, and to do it more consistently than drift alone would.

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 10 | 0 |
| Run 2 | 9 | 0 |
| Run 3 | 10 | 0 |
| Run 4 | 10 | 0 |
| Run 5 | 9 | 0 |

What happened? Compare with Simulation 1 (equal selection coefficients).

A fixed in nearly every line: 48 of 50 fixed, none lost, 2 still segregating. Simulation 1 used the same n and the same 0.5 start with no selection and gave a random, near-even split. A fitness gap of only 0.1 was enough to send A to fixation almost every time. With selection the outcome had a clear direction; with drift alone it was a coin flip.

## Simulation 6: n = 100, f(A) = 0.5, fitness AA = 1.0, Aa = 0.8, aa = 0.8

Prediction: The fitness gap doubles to 0.2, so selection pushes harder. A should fix in every line and get there sooner.

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 10 | 0 |
| Run 2 | 10 | 0 |
| Run 3 | 10 | 0 |
| Run 4 | 10 | 0 |
| Run 5 | 10 | 0 |

What happened? Compare with Simulation 5.

A fixed in all 50 lines, with none lost and none left segregating. The 0.2 gap did the job faster and more cleanly than the 0.1 gap in Simulation 5. A wider fitness gap gives selection the upper hand over drift, so the favored allele fixes sooner and more surely.

## Concluding Questions

After completing this lab, how do you think population size affects genetic drift?

Population size sets how strong drift is. In the small populations (n = 100, Simulations 1 and 3), the luck of which individuals happened to breed threw the frequencies around, and lines fixed or lost A within 100 generations. In the large populations (n = 1000, Simulations 2 and 4) that luck averaged out, the frequencies held steady, and almost nothing fixed or was lost in the same span. Smaller populations drift faster, which is why a shrinking or isolated population can lose useful alleles by chance alone.

What is the fixation probability of an allele?

Without selection, an allele's chance of eventually fixing equals its current frequency. At 0.5 that is a 50% chance (Simulation 1); at 0.1 it is a 10% chance of fixing and 90% of being lost (Simulation 3). Loss is the flip side, with a probability of 1 minus the frequency. Fixation can take a long time, so inside a 100-generation window most rare alleles disappear before they ever reach it.

How does fitness affect the fixation probability of an allele?

Fitness pulls that probability away from the neutral value. A beneficial allele fixes more often than its starting frequency alone would predict. In Simulations 5 and 6, A began at 0.5 but fixed in nearly every line because it carried an advantage. A harmful allele does the reverse and usually gets weeded out. Widen the fitness gap and selection takes over from drift, which makes the result easier to predict. The two forces still act at once, though, and in a very small population drift can beat weak selection and fix a harmful allele or wipe out a good one. That is the conservation worry: small, isolated populations can lose the variation they would need to adapt as their environment changes.
