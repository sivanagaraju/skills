# Curriculum Bridge & Dynamic MathsTerms Contract

> **Contract Law:** No concept may be assumed without a verified bridge.  
> Every lecture package in `Mathematical-Foundation-for-GenerativeAI` (or any advanced module) must provide explicit, zero-leap navigational hyperlinks to foundational concepts discussed in earlier series (`Mathematical-foundation-ml`) or catalogued in [`MathsTerms/`](../../MathsTerms/).

---

## 1. The Two Knowledge Repositories

When generating or upgrading study packages, the agent must treat two local directories as foundational knowledge bases:

### 1.1 Sibling Curriculum Series: `Mathematical-foundation-ml`
Contains 13 foundational lectures that establish the mathematical bedrock:
1. `02-Lec01-Overview-Function-Approximation`: Slogan $\to$ Model $\to$ Algorithm, Supervised learning formulation.
2. `03-Lec02-Recap-Probability-Theory-Part1`: Sample space $\Omega$, Events, Probability Axioms, Random Variables.
3. `04-Lec03-Recap-Probability-Theory-Part2`: Discrete vs Continuous, PMF vs PDF, Expectations, Variance.
4. `05-Lec04-Recap-Probability-Theory-Part3`: Joint, Marginal, Conditional distributions, Bayes Theorem.
5. `06-Lec05-Recap-Probability-Theory-Part2`: Linearity of Expectation, Covariance, Independence.
6. `07-Lec06-XRay-Sample-From-Distribution`: Sampling mechanics, Empirical histograms, Data generation process.
7. `08-Lec07-IID-Assumption`: Independent and Identically Distributed assumption, Factorization of joint likelihood.
8. `09-Lec08-Distribution-Estimation`: Parametric vs Non-parametric estimation, Density modeling vs Function approximation.
9. `10-Lec09-Density-Function`: Likelihood function, Log-likelihood, Why probabilities are not densities.
10. `11-Lec10-Challenges-of-ML`: Curse of dimensionality, Overfitting, Generalization, Inductive bias.
11. `12-Lec11-Entropy`: Claude Shannon information theory, Self-information, Entropy as average code length.
12. `13-Lec12-KL-Divergence`: Kullback-Leibler divergence, Relative entropy, Asymmetry, Forward vs Reverse KL.
13. `14-Lec13-Minimization-of-KL`: Mathematical proof of equivalence between MLE and Forward KL minimization.

### 1.2 Dedicated Deep-Dive Encyclopedia: `MathsTerms/`
Contains standalone, 7-section visual reference guides organized into 6 core domains:
- `01-Primal-Analysis-and-Foundations`: Probability basics, Logarithms, Convexity, Jensen's Inequality.
- `02-Linear-Algebra-Geometry-and-Tensors`: Vector norms, Inner products, Tensors & Shapes, Eigendecomposition, SVD.
- `03-Multivariate-Calculus-and-Optimization`: Derivatives, Gradients, Jacobians, Hessians, Gradient Descent, Softmax, Argmax.
- `04-Probability-and-Statistical-Estimation`: Random variables, Distributions, Joint/Marginal, Likelihood, MLE, NLL.
- `05-Information-Theory-and-Divergences`: KL Divergence, Jensen-Shannon, f-Divergence, Wasserstein Distance, Fenchel Conjugates.
- `06-Deep-Architectures-and-Generative-Models`: Convolutions, Normalization (Batch/Layer/Spectral), Minimax GANs, Latent Variable Models, ELBO, Reparameterization Trick, FID.

---

## 2. Dynamic Discovery & Bridging Protocol

During Phase 4 (Topic Planning) and Phase 5 (Claim Mining) of any lecture:

```
                  [Video Transcript & Claims]
                               │
               Scan for Assumed Prerequisite Concepts
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
   [Foundational ML Theory]             [Mathematical Term / Symbol]
            │                                     │
 Does it match earlier topic in        Does it exist in MathsTerms/?
  Mathematical-foundation-ml?                     │
            │                           ┌─────────┴─────────┐
      ┌─────┴─────┐                     ▼                   ▼
     YES          NO                  EXISTS             MISSING
      │           │                     │                   │
   Generate    Evaluate if          Generate direct     1. Register in Backlog
  Curriculum   MathsTerms link      relative link       2. Author new file
    Bridge     is sufficient       ../../MathsTerms/       per 7-section standard
  ../../       or self-contained    <category>/<file>   3. Link in PREREQS/NOTES
  Math-ml/
```

### Rule A: The Sibling Course Prerequisite Bridge
If the lecture mentions or relies upon:
- Probability spaces, axioms, or expectations $\to$ link to `../../Mathematical-foundation-ml/03-Lec02-Recap-Probability-Theory-Part1/NOTES.md` or `04-Lec03-Recap-Probability-Theory-Part2/NOTES.md`.
- IID assumption, sampling, or empirical data distributions $\to$ link to `../../Mathematical-foundation-ml/08-Lec07-IID-Assumption/NOTES.md`.
- Density estimation or likelihood maximization $\to$ link to `../../Mathematical-foundation-ml/09-Lec08-Distribution-Estimation/NOTES.md` and `10-Lec09-Density-Function/NOTES.md`.
- Entropy, KL divergence, or divergence minimization $\to$ link to `../../Mathematical-foundation-ml/12-Lec11-Entropy/NOTES.md`, `13-Lec12-KL-Divergence/NOTES.md`, and `14-Lec13-Minimization-of-KL/NOTES.md`.

### Rule B: Dynamic `MathsTerms/` Discovery & Creation
1. **Catalog Lookup:** Scan `MathsTerms/CONCEPT_MAP.md` and all subdirectories.
2. **Existing Terms:** Generate explicit relative markdown links (e.g., `[KL Divergence](../../MathsTerms/05-Information-Theory-and-Divergences/01-KL_Divergence.md)`).
3. **Missing Terms:** If a mathematical term or operator is load-bearing in the lecture but absent from `MathsTerms/`:
   - It is **forbidden** to leave the learner with undefined terminology.
   - Author a new standalone reference file in the appropriate `MathsTerms/` category folder adhering to the **7-section visual gold standard** (`Softmax.md` model):
     - §1: Title & High-Impact 3-Stage Visual ASCII Pipeline.
     - §2: 👶 **ELI5 Intuition** (Physical analogy / concrete real-world story).
     - §3: 🔍 **Plain-English Breakdown & Notation Rosetta Stone Table**.
     - §4: 📐 **Formal Mathematical Formulation, Properties & Guarantees**.
     - §5: 🔗 **Connecting the Dots: How this Concept Powers Modern ML & Generative AI**.
     - §6: 💻 **Complete Standalone Executable Python/PyTorch Verification Script**.
     - §7: 🩺 **Diagnostic Mini-Checks & Common Traps**.
   - Update `MathsTerms/CONCEPT_MAP.md` to register the new term.
   - Cross-link the newly created file in `PREREQUISITES.md`, `NOTES.md`, and `glossary.md`.

---

## 3. Placement in Study Packages

### In `PREREQUISITES.md`
Place immediately after the Math Terminology Rosetta Stone table:

```markdown
## 🌉 Curriculum & Sibling Course Prerequisite Bridges

If you need a refresher on the foundational concepts leading up to this lecture, consult these sibling course notes and mathematical deep-dives:

| Assumed Concept | Primary Series Foundation | MathsTerms Deep-Dive | 1-Sentence Intuition Refresher |
| :--- | :--- | :--- | :--- |
| **IID Assumption** | [Lec 07: IID Assumption](../../Mathematical-foundation-ml/08-Lec07-IID-Assumption/NOTES.md) | [Probability Basics](../../MathsTerms/01-Primal-Analysis-and-Foundations/01-Probability_Basics_and_Axioms.md) | Enables factoring joint probability into individual independent sample products. |
| **KL Divergence** | [Lec 12: KL Divergence](../../Mathematical-foundation-ml/13-Lec12-KL-Divergence/NOTES.md) | [KL Divergence](../../MathsTerms/05-Information-Theory-and-Divergences/01-KL_Divergence.md) | Measures the information penalty of approximating true data distribution $P$ with model $Q$. |
```

### In `references.md`
Category 1 of `references.md` must be dedicated to:
`## 1. 🌉 Curriculum & Cross-Series Prerequisite Bridges`
Listing every relevant sibling lecture and MathsTerm with deep contextual guidance on why the student should revisit it.

### In `NOTES.md` (Inline)
Whenever an assumed concept is invoked in topic deep dives, link directly:
`...as derived in [Lec 13: Minimization of KL](../../Mathematical-foundation-ml/14-Lec13-Minimization-of-KL/NOTES.md) and [MLE](../../MathsTerms/04-Probability-and-Statistical-Estimation/05-MLE.md)...`
