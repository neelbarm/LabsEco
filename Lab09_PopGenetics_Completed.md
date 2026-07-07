# Lab 9: Population Genetics — Completed Worksheet

**Name:** ________________________   **Date:** ________________________

**Simulator used:** Wright–Fisher model (`evobiR` *wf_model*), https://evobir.shinyapps.io/wf_model/
Each "Run" below is one execution of the simulation = **10 replicate populations**, each run for **100 generations**. For every run I recorded, at Generation 100, how many of the 10 replicates ended with allele A **fixed** (f(A) = 1) or **lost** (f(A) = 0). Replicates that were neither fixed nor lost were still *segregating* (both alleles still present). Because drift is random, the exact counts differ every time the simulation is run; the patterns and conclusions are what matter.

---

## SIMULATION 1 — Drift alone, n = 100, f(A) = 0.5

Settings: all three fitness values = 1.0 (neutral), n = 100, initial f(A) = 0.5.

| Run | # replicates with final f(A) = 1 (fixed) | # replicates with final f(A) = 0 (lost) |
|-----|:----------------------------------------:|:---------------------------------------:|
| Run 1 | 0 | 0 |
| Run 2 | 0 | 3 |
| Run 3 | 1 | 1 |
| Run 4 | 2 | 0 |
| Run 5 | 0 | 1 |

**Do you always obtain the same result? Why?**

No — the number of replicates that fix or are lost changes every run (0, 3, 1, 2, 1 lost; 0, 0, 1, 2, 0 fixed). Genetic drift is a **stochastic (random)** process: each generation the alleles that get passed on are a chance sample of the previous generation, so each of the 10 replicate populations follows its own random trajectory, and each new run of 10 replicates is an independent random draw. Because A starts at 0.5 and there is no selection, fixation and loss are equally likely, so over many replicates roughly as many fix as are lost. Most replicates are still segregating after only 100 generations, because n = 100 is large enough that drift moves frequencies fairly slowly.

---

## SIMULATION 2 — Larger population, n = 1000, f(A) = 0.5

Settings: neutral (all fitness = 1.0), n = 1000, initial f(A) = 0.5.

**Prediction (before running):** With a ten-times-larger population, drift should be much weaker, so allele frequencies will change more slowly and **very few or no** replicates should reach fixation or loss within 100 generations — most should stay clustered near 0.5.

| Run | # replicates with final f(A) = 1 (fixed) | # replicates with final f(A) = 0 (lost) |
|-----|:----------------------------------------:|:---------------------------------------:|
| Run 1 | 0 | 0 |
| Run 2 | 0 | 0 |
| Run 3 | 0 | 0 |
| Run 4 | 0 | 0 |
| Run 5 | 0 | 0 |

**What happened? Compare with Simulation 1.**

No replicate fixed or was lost in any run — all 50 replicates stayed polymorphic near f(A) = 0.5, and the trajectories stayed tightly bunched together instead of fanning out to 0 and 1. Compared with Simulation 1 (n = 100), increasing n to 1000 dramatically **reduced the effect of drift**. This directly demonstrates the key point that **genetic drift is stronger in small populations and weaker in large ones** (its strength scales with 1/2N).

---

## SIMULATION 3 — Rare allele in a small population, n = 100, f(A) = 0.1

Settings: neutral (all fitness = 1.0), n = 100, initial f(A) = 0.1.

**Prediction (before running):** The allele starts rare (0.1). Under drift the probability that an allele eventually fixes equals its current frequency, so ~10% of replicates should fix A and ~90% should lose it. **Loss should dominate.**

| Run | # replicates with final f(A) = 1 (fixed) | # replicates with final f(A) = 0 (lost) |
|-----|:----------------------------------------:|:---------------------------------------:|
| Run 1 | 0 | 10 |
| Run 2 | 0 | 7 |
| Run 3 | 0 | 8 |
| Run 4 | 0 | 8 |
| Run 5 | 0 | 4 |

**What happened? Compare with Simulation 1.**

Most replicates **lost** allele A (37 of 50 lost; the remaining 13 were still segregating; 0 fixed within 100 generations). Compared with Simulation 1 (which started at 0.5 and gave a roughly balanced mix of fix/loss), starting rare made **loss far more likely** — exactly what "fixation probability = starting frequency" predicts (here 0.1). The ~10% of replicates expected to *eventually* fix mostly have not climbed all the way from 0.1 to 1.0 in only 100 generations; they are among the still-segregating replicates, and over more generations about 1 in 10 would fix. This is why rare alleles — including rare beneficial ones — are so easily lost in small populations, a central concern in conservation genetics.

---

## SIMULATION 4 — Rare allele in a large population, n = 1000, f(A) = 0.1

Settings: neutral (all fitness = 1.0), n = 1000, initial f(A) = 0.1.

**Prediction (before running):** Same low starting frequency, but the large population makes drift weak, so the allele should **neither fix nor be lost quickly** — most replicates should hover near 0.1.

| Run | # replicates with final f(A) = 1 (fixed) | # replicates with final f(A) = 0 (lost) |
|-----|:----------------------------------------:|:---------------------------------------:|
| Run 1 | 0 | 1 |
| Run 2 | 0 | 0 |
| Run 3 | 0 | 0 |
| Run 4 | 0 | 0 |
| Run 5 | 0 | 0 |

**What happened? Compare with Simulation 3.**

Almost nothing resolved — only 1 replicate of 50 was lost, none fixed, and the allele **lingered near 0.1** in essentially every replicate. Compared with Simulation 3 (n = 100, where 37 of 50 were lost), the larger population strongly **buffered the rare allele against loss**. In a small population a rare allele is quickly erased by chance; in a large population the same rare allele persists far longer. This is why large populations retain genetic variation and small/endangered populations lose it.

---

## SIMULATION 5 — Adding selection, n = 100, f(A) = 0.5, fitness AA = 1.0, Aa = 0.9, aa = 0.9

**Is this selection for or against allele A? What do you predict? Why?**

This is selection **FOR allele A** (and against the *a* allele). Genotype AA has the highest relative fitness (1.0), while Aa and aa are both lower (0.9). Because carrying two A alleles gives the highest survival/reproduction, A is favored. (Note A behaves as a *recessive* beneficial allele here: only the AA homozygote gets the advantage, since Aa and aa have equal fitness.) **Prediction:** A should rise in frequency and fix in most or all replicates — more reliably than under pure drift.

| Run | # replicates with final f(A) = 1 (fixed) | # replicates with final f(A) = 0 (lost) |
|-----|:----------------------------------------:|:---------------------------------------:|
| Run 1 | 10 | 0 |
| Run 2 | 9 | 0 |
| Run 3 | 10 | 0 |
| Run 4 | 10 | 0 |
| Run 5 | 9 | 0 |

**What happened? Compare with Simulation 1 (equal selection coefficients).**

Allele A fixed in almost every replicate (48 of 50 fixed, 0 lost, 2 still segregating). Compared with Simulation 1 — same n and same starting frequency of 0.5, but neutral — where the outcome was random and roughly balanced with most replicates still segregating, adding even a modest fitness advantage (a fitness difference of 0.1) **consistently drove A to fixation**. Selection overpowered drift and pushed A up in a predictable direction, whereas under pure drift the direction was random.

---

## SIMULATION 6 — Stronger selection, n = 100, f(A) = 0.5, fitness AA = 1.0, Aa = 0.8, aa = 0.8

**Prediction (before running):** The fitness gap is now larger (0.2 instead of 0.1), so selection is even stronger. A should fix even **faster** and in **all** replicates.

| Run | # replicates with final f(A) = 1 (fixed) | # replicates with final f(A) = 0 (lost) |
|-----|:----------------------------------------:|:---------------------------------------:|
| Run 1 | 10 | 0 |
| Run 2 | 10 | 0 |
| Run 3 | 10 | 0 |
| Run 4 | 10 | 0 |
| Run 5 | 10 | 0 |

**What happened? Compare with Simulation 5.**

Allele A fixed in **all 50 replicates** — none lost, none left segregating. Compared with Simulation 5 (fitness difference of 0.1), the stronger fitness difference (0.2) drove A to fixation even more rapidly and completely. **The larger the fitness difference, the stronger selection is relative to drift**, and the more certain and faster fixation of the favored allele becomes.

---

## Concluding Questions

**After completing this lab, how do you think population size affects genetic drift?**

Genetic drift is **stronger in small populations and weaker in large populations.** In a small population (n = 100, Sim 1 and Sim 3), the chance sampling of which individuals survive and reproduce causes large, rapid, random swings in allele frequency, so alleles quickly fix or are lost. In a large population (n = 1000, Sim 2 and Sim 4), those random fluctuations average out, frequencies change only slowly, and over the same 100 generations almost nothing fixed or was lost. Mathematically, the strength of drift scales with 1/2N, so bigger populations drift less. For conservation, this means small or shrinking populations lose genetic variation rapidly and can lose beneficial alleles purely by chance.

**What is the fixation probability of an allele?**

Under neutral drift (no selection), the probability that an allele *eventually* becomes fixed equals its **current frequency** in the population. An allele at 0.5 has a ~50% chance of fixation (Sim 1); an allele at 0.1 has a ~10% chance of fixation and a ~90% chance of loss (Sim 3). Fixation and loss are two sides of the same coin: P(loss) = 1 − frequency. (Fixation may take many generations, so in a short 100-generation window most low-frequency alleles are simply lost and the few destined to fix are still on their way.)

**How does fitness affect the fixation probability of an allele?**

Fitness (natural selection) shifts fixation probability away from the neutral "equals-its-frequency" expectation:

- A **beneficial** allele (higher relative fitness) has a fixation probability **greater** than its starting frequency. In Sim 5 and Sim 6, allele A started at only 0.5 but fixed in ~all replicates because it was favored — far above the 50% a neutral allele would get.
- A **deleterious** allele has a fixation probability **lower** than its frequency and is likely to be lost.
- The **larger the fitness difference, the more selection dominates over drift** and the more predictable (and faster) the outcome — compare Sim 6 (all fixed) with Sim 5 (nearly all fixed).

Finally, selection and drift act together, and which one wins depends on which is stronger. In **very small populations, drift can overpower weak selection**, occasionally fixing a harmful allele or losing a beneficial one by pure chance. This is a central problem in conservation biology: small, fragmented, or endangered populations can lose adaptive genetic variation and accumulate deleterious alleles, reducing their ability to adapt to environmental change.
