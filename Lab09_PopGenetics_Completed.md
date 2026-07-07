# Lab 9: Population Genetics

Name: ________________________   Date: ________________________

Simulator: Wright-Fisher model (evobiR wf_model), https://evobir.shinyapps.io/wf_model/

Each "Run" is one execution of the simulation, which is 10 replicate populations run for 100 generations. For each run I recorded how many of the 10 replicates ended with allele A fixed (f(A) = 1) or lost (f(A) = 0) at Generation 100. Replicates that were neither fixed nor lost still had both alleles present.

## Simulation 1: n = 100, f(A) = 0.5, no selection (all fitness = 1.0)

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 0 | 0 |
| Run 2 | 0 | 3 |
| Run 3 | 1 | 1 |
| Run 4 | 2 | 0 |
| Run 5 | 0 | 1 |

Do you always obtain the same result? Why?

No, the number that fix or are lost changes every run. Genetic drift is a random process. Each generation the alleles passed on are a chance sample of the previous generation, so each of the 10 replicate populations follows its own random path, and each run of 10 replicates is an independent random draw. Because A starts at 0.5 with no selection, fixation and loss are equally likely, so across many replicates about as many fix as are lost. Most replicates are still segregating after only 100 generations because n = 100 is large enough that drift moves slowly.

## Simulation 2: n = 1000, f(A) = 0.5, no selection

Prediction: With a much larger population, drift should be weaker, so allele frequencies will change more slowly and very few or no replicates should fix or be lost within 100 generations. Most should stay near 0.5.

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 0 | 0 |
| Run 2 | 0 | 0 |
| Run 3 | 0 | 0 |
| Run 4 | 0 | 0 |
| Run 5 | 0 | 0 |

What happened? Compare with Simulation 1.

No replicate fixed or was lost in any run. All 50 replicates stayed near f(A) = 0.5, and the lines stayed close together instead of spreading out to 0 and 1. Compared with Simulation 1 (n = 100), increasing n to 1000 greatly reduced the effect of drift. This shows that genetic drift is stronger in small populations and weaker in large ones.

## Simulation 3: n = 100, f(A) = 0.1, no selection

Prediction: The allele starts rare (0.1). The probability that an allele eventually fixes equals its frequency, so about 10% of replicates should fix A and about 90% should lose it. Loss should dominate.

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 0 | 10 |
| Run 2 | 0 | 7 |
| Run 3 | 0 | 8 |
| Run 4 | 0 | 8 |
| Run 5 | 0 | 4 |

What happened? Compare with Simulation 1.

Most replicates lost allele A (37 of 50 lost, 13 still segregating, 0 fixed within 100 generations). Compared with Simulation 1, which started at 0.5 and gave a roughly balanced mix, starting rare made loss far more likely. This matches the idea that fixation probability equals starting frequency (0.1 here). The roughly 10% of replicates expected to eventually fix mostly have not climbed all the way from 0.1 to 1.0 in only 100 generations; they are among the still-segregating replicates. This is why rare alleles are easily lost in small populations, which is an important issue in conservation.

## Simulation 4: n = 1000, f(A) = 0.1, no selection

Prediction: Same low starting frequency, but the large population makes drift weak, so the allele should neither fix nor be lost quickly. Most replicates should stay near 0.1.

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 0 | 1 |
| Run 2 | 0 | 0 |
| Run 3 | 0 | 0 |
| Run 4 | 0 | 0 |
| Run 5 | 0 | 0 |

What happened? Compare with Simulation 3.

Almost nothing resolved. Only 1 replicate of 50 was lost, none fixed, and the allele stayed near 0.1 in almost every replicate. Compared with Simulation 3 (n = 100, where 37 of 50 were lost), the larger population protected the rare allele from being lost. In a small population a rare allele is quickly lost by chance; in a large population the same allele lasts much longer. This is why large populations keep genetic variation and small populations lose it.

## Simulation 5: n = 100, f(A) = 0.5, fitness AA = 1.0, Aa = 0.9, aa = 0.9

Is this selection for or against allele A? What do you predict? Why?

This is selection for allele A (and against a). Genotype AA has the highest fitness (1.0), while Aa and aa are lower (0.9), so carrying two A alleles gives the best survival and reproduction. A is favored. (A acts as a recessive beneficial allele here, since only AA gets the advantage.) Prediction: A should increase and fix in most or all replicates, more reliably than under drift alone.

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 10 | 0 |
| Run 2 | 9 | 0 |
| Run 3 | 10 | 0 |
| Run 4 | 10 | 0 |
| Run 5 | 9 | 0 |

What happened? Compare with Simulation 1 (equal selection coefficients).

Allele A fixed in almost every replicate (48 of 50 fixed, 0 lost, 2 still segregating). Compared with Simulation 1, which had the same n and the same starting frequency but no selection and gave a random, roughly balanced result, adding even a small fitness advantage (a difference of 0.1) drove A to fixation. Selection overpowered drift and pushed A up in a predictable direction, while under drift alone the direction was random.

## Simulation 6: n = 100, f(A) = 0.5, fitness AA = 1.0, Aa = 0.8, aa = 0.8

Prediction: The fitness gap is now larger (0.2 instead of 0.1), so selection is even stronger. A should fix even faster and in all replicates.

| Run | # replicates final f(A) = 1 (fixed) | # replicates final f(A) = 0 (lost) |
|-----|:---:|:---:|
| Run 1 | 10 | 0 |
| Run 2 | 10 | 0 |
| Run 3 | 10 | 0 |
| Run 4 | 10 | 0 |
| Run 5 | 10 | 0 |

What happened? Compare with Simulation 5.

Allele A fixed in all 50 replicates, none lost and none left segregating. Compared with Simulation 5 (a fitness difference of 0.1), the larger fitness difference (0.2) drove A to fixation even faster and more completely. The larger the fitness difference, the stronger selection is relative to drift, and the faster and more certain fixation of the favored allele becomes.

## Concluding Questions

After completing this lab, how do you think population size affects genetic drift?

Genetic drift is stronger in small populations and weaker in large populations. In a small population (n = 100, Simulations 1 and 3), the chance sampling of which individuals survive and reproduce causes large, fast, random swings in allele frequency, so alleles fix or are lost quickly. In a large population (n = 1000, Simulations 2 and 4), these random changes average out, frequencies change slowly, and over the same 100 generations almost nothing fixed or was lost. For conservation, this means small or shrinking populations lose genetic variation quickly and can lose helpful alleles by chance.

What is the fixation probability of an allele?

With no selection, the probability that an allele eventually fixes equals its current frequency. An allele at 0.5 has about a 50% chance of fixing (Simulation 1); an allele at 0.1 has about a 10% chance of fixing and a 90% chance of being lost (Simulation 3). Fixation and loss are two sides of the same coin: probability of loss = 1 minus frequency. Fixation can take many generations, so in a short 100-generation window most low-frequency alleles are simply lost.

How does fitness affect the fixation probability of an allele?

Fitness (natural selection) shifts fixation probability away from the neutral expectation of equaling the allele's frequency. A beneficial allele has a fixation probability greater than its starting frequency; in Simulations 5 and 6, allele A started at only 0.5 but fixed in nearly all replicates because it was favored. A harmful allele has a fixation probability lower than its frequency and is likely to be lost. The larger the fitness difference, the more selection dominates over drift and the more predictable the outcome. Selection and drift act together, and in very small populations drift can overpower weak selection and occasionally fix a harmful allele or lose a beneficial one. This matters for conservation, because small or endangered populations can lose helpful genetic variation and build up harmful alleles, making it harder for them to adapt to environmental change.
