# Master Glossary Specification & Template (`glossary.md`)

> **Location in Package:** `<package-folder>/glossary.md`  
> **Role:** One of the 6 core pillars of the upgraded study package.  
> **Target Audience:** Adult engineers returning to mathematics after 10–15 years.  
> **Product Goal:** Eliminate mathematical isolation by giving every symbol, Greek letter, and technical term a formal definition, a software translation, a spoken phonetic pronunciation, a physical analogy, and a link to a deep-dive math term file.

---

## 1. The 6-Column Schema Contract

Every `glossary.md` file must contain one or more Markdown tables adhering strictly to this 6-column header:

```markdown
| Term / Notation | Formal Definition | Plain-English Software Meaning | Spoken English (Phonetics) | Real-World Analogy | Dedicated MathsTerm Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
```

### Column Specifications:

| # | Column Name | Formatting & Content Law |
|---|-------------|--------------------------|
| 1 | `Term / Notation` | Mathematical notation in KaTeX inline math (`$...$`) or bold technical term. Must represent the exact symbol used in the lecture. |
| 2 | `Formal Definition` | Rigorous mathematical equation, operator definition, or formal domain/range mapping in KaTeX syntax. No vague approximations. |
| 3 | `Plain-English Software Meaning` | Grounded translation into software primitives (e.g. 1D/2D arrays, loops, tensor operations, memory buffers, loss penalties, autograd tracking). Zero circular jargon. |
| 4 | `Spoken English (Phonetics)` | Explicit plain-English phonetic transcription indicating how practitioners pronounce the symbol aloud in lab meetings and seminars. Primary stress must be capitalized (e.g., `PAR-shul`, `DEL EFF`). Include contrastive notes if commonly mispronounced. |
| 5 | `Real-World Analogy` | Tangible physical system or intuitive everyday metaphor (e.g., speedometer, hot/cold shower knobs, flashlight beam, stretched dough, pizza slicing). |
| 6 | `Dedicated MathsTerm Link` | Valid relative markdown link pointing to `../../MathsTerms/<subfolder>/<file>.md`. If the term is a primitive axiom without a standalone file, specify `Primitive Axiom`. |

---

## 2. Mandatory Category Taxonomy

To guarantee structured navigation, `glossary.md` must group all terms under these four category headings:

1. `## 1. Greek Symbols & Mathematical Operators`
2. `## 2. Linear Algebra, Geometry & Tensors`
3. `## 3. Probability Theory & Statistical Estimation`
4. `## 4. Machine Learning & Generative AI Concepts`

---

## 3. Gold-Standard Category Blueprints with Sample Rows

### 3.1 Category 1: Greek Symbols & Mathematical Operators

```markdown
## 1. Greek Symbols & Mathematical Operators

| Term / Notation | Formal Definition | Plain-English Software Meaning | Spoken English (Phonetics) | Real-World Analogy | Dedicated MathsTerm Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\nabla f(\mathbf{x})$ (Gradient Vector) | $\nabla f(\mathbf{x}) = \left[ \frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n} \right]^\top \in \mathbb{R}^n$ | Vector of partial derivatives giving the direction and rate of fastest loss increase; output of `torch.autograd.grad`. | **DEL EFF** or **GRAD-ee-yunt OF EFF** *(Never say "triangle eff" or "upside down delta")* | The compass needle pointing directly up the steepest incline on a foggy hiking hill. | [Derivatives & Gradients](../../MathsTerms/03-Multivariate-Calculus-and-Optimization/02-Derivatives_Gradients_and_Jacobians.md) |
| $\partial$ / $\frac{\partial f}{\partial x_i}$ (Partial Derivative) | $\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(\mathbf{x} + h \mathbf{e}_i) - f(\mathbf{x})}{h}$ | Rate of change of the output when mutating one single tensor index while keeping all other indices frozen. | **PAR-shul** / **PAR-shul EFF BY PAR-shul EX EYE** *(Never say "curly d" or plain "d")* | Turning the hot water shower knob while keeping the cold water knob locked in place. | [Derivatives & Gradients](../../MathsTerms/03-Multivariate-Calculus-and-Optimization/02-Derivatives_Gradients_and_Jacobians.md) |
| $\sum_{i=1}^N$ (Summation) | $\sum_{i=1}^N x_i = x_1 + x_2 + \dots + x_N$ | Accumulator loop summing tensor elements: `total = torch.sum(x)` or `x.sum()`. | **SUM-AY-shun FROM EYE E-kwuls ONE TOO EN** or **SIG-muh** | Adding up every item price on a grocery receipt into a single checkout total. | Primitive Axiom |
| $\mathbb{E}_{\mathbf{x} \sim p}[f(\mathbf{x})]$ (Expectation) | $\mathbb{E}[f(\mathbf{x})] = \int_{\mathcal{X}} f(\mathbf{x}) p(\mathbf{x}) \, d\mathbf{x}$ | Expected long-run average of a feature function across samples; approximated in code by batch mean `torch.mean()`. | **EX-pek-TAY-shun OF EFF OF EX WEHR EX IS DRAWN FROM PEE** *(Never say "big E of X")* | The average payout of a casino roulette wheel calculated across 1,000,000 continuous spins. | [Probability Basics](../../MathsTerms/01-Primal-Analysis-and-Foundations/01-Probability_Basics_and_Axioms.md) |
| $\sim$ (Distributed As) | $\mathbf{x} \sim P$ denotes random variable $\mathbf{x}$ obeys probability measure $P$. | Instantiating and sampling from a distribution object: `x = dist.sample()`. | **IS DIS-trib-yoo-ted AZ** or **TIL-duh** | Shaking and rolling a specific loaded six-sided die whose face weights are fixed. | [Random Variables](../../MathsTerms/04-Probability-and-Statistical-Estimation/01-Random_Variables_and_Distributions.md) |
| $\in \mathbb{R}^d$ (Set Membership) | $\mathbf{x} \in \mathbb{R}^d \iff \mathbf{x} = [x_1, \dots, x_d]^\top, x_i \in \mathbb{R}$ | Type assertion that a tensor has float32 dtype and 1D shape `(d,)`. | **IN AR DEE** *(Never say "element of R to the d")* | Verifying that an employee ID belongs to the active company database table. | [Vectors & Matrices](../../MathsTerms/02-Linear-Algebra-Geometry-and-Tensors/01-Vectors_and_Matrices.md) |
```

### 3.2 Category 2: Linear Algebra, Geometry & Tensors

```markdown
## 2. Linear Algebra, Geometry & Tensors

| Term / Notation | Formal Definition | Plain-English Software Meaning | Spoken English (Phonetics) | Real-World Analogy | Dedicated MathsTerm Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\mathbf{J} \in \mathbb{R}^{m \times n}$ (Jacobian Matrix) | $J_{ij} = \frac{\partial f_i}{\partial x_j}$ for $\mathbf{f}: \mathbb{R}^n \to \mathbb{R}^m$ | 2D matrix of first-order partial derivatives mapping an input perturbation vector to an output change vector. | **JAY IN AR EM BY EN** or **juh-KOH-bee-un MAY-triks** | A local distortion grid showing how a sheet of rubber stretches, skews, and rotates when pulled. | [Jacobian Matrix](../../MathsTerms/03-Multivariate-Calculus-and-Optimization/03-Jacobian_Matrix.md) |
| $\mathbf{H} \in \mathbb{R}^{n \times n}$ (Hessian Matrix) | $H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$ | 2D square matrix of second derivatives describing local surface curvature and optimal gradient step sizes. | **AITCH IN AR EN BY EN** or **HESH-un MAY-triks** | Feeling whether a physical surface curves upward like a soup bowl or drops off like a horse saddle. | [Derivatives & Gradients](../../MathsTerms/03-Multivariate-Calculus-and-Optimization/02-Derivatives_Gradients_and_Jacobians.md) |
| $\|\mathbf{x}\|_2$ ($L_2$ Euclidean Norm) | $\|\mathbf{x}\|_2 = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{\mathbf{x}^\top \mathbf{x}}$ | Geometric magnitude or Euclidean length of a vector: `torch.linalg.norm(x, ord=2)`. | **ELL TOO NORM OF EX** | Measuring the straight-line distance from your front doorstep to a destination as the crow flies. | [Vector Norms](../../MathsTerms/02-Linear-Algebra-Geometry-and-Tensors/02-Vector_Norms_and_Inner_Products.md) |
| $\mathbf{W}^\top$ (Matrix Transpose) | $(\mathbf{W}^\top)_{ij} = \mathbf{W}_{ji}$ | Swapping row and column axes: `W.T` or `W.transpose(0, 1)`, converting shape `(M, N)` to `(N, M)`. | **DOUBLE-yoo TRANS-pose** | Rotating a spreadsheet 90 degrees so that student rows become subject columns. | [Vectors & Matrices](../../MathsTerms/02-Linear-Algebra-Geometry-and-Tensors/01-Vectors_and_Matrices.md) |
| $\mathbf{A} \odot \mathbf{B}$ (Hadamard Product) | $(\mathbf{A} \odot \mathbf{B})_{ij} = A_{ij} \cdot B_{ij}$ | Element-wise array multiplication `A * B` (distinct from matrix multiplication `A @ B`). | **AY HAD-uh-mard BEE** or **AY EL-uh-ment-wize MULT-ih-ply BEE** | Applying a pixel-by-pixel brightness mask over a photograph. | [Tensors & Shapes](../../MathsTerms/02-Linear-Algebra-Geometry-and-Tensors/04-Tensors_and_Shapes.md) |
| $\det(\mathbf{A})$ (Determinant) | $\det(\mathbf{A}) = \sum_{\sigma \in S_n} \text{sgn}(\sigma) \prod_{i=1}^n A_{i, \sigma(i)}$ | The scalar volume scaling factor caused by a linear transformation; negative values imply space inversion. | **de-TUR-mi-nunt OF AY** | How many times larger an inflated balloon becomes relative to its uninflated volume. | [Vectors & Matrices](../../MathsTerms/02-Linear-Algebra-Geometry-and-Tensors/01-Vectors_and_Matrices.md) |
```

### 3.3 Category 3: Probability Theory & Statistical Estimation

```markdown
## 3. Probability Theory & Statistical Estimation

| Term / Notation | Formal Definition | Plain-English Software Meaning | Spoken English (Phonetics) | Real-World Analogy | Dedicated MathsTerm Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $D_{\text{KL}}(P \parallel Q)$ (KL Divergence) | $D_{\text{KL}}(P \parallel Q) = \sum_{x} P(x) \ln \frac{P(x)}{Q(x)}$ | Relative entropy measuring information lost when modeling true distribution $P$ with approximation $Q$. | **KAY ELL DYE-ver-jens OF PEE WITH re-SPEKT TOO KYOO** or **PEE PAR-uh-lel KYOO** | The penalty fee paid at an exchange booth for using an outdated currency exchange rate table. | [KL Divergence](../../MathsTerms/05-Information-Theory-and-Divergences/02-KL_Divergence.md) |
| $\mathcal{L}(\theta; \mathcal{D})$ / $\ell(\theta)$ (Log-Likelihood) | $\ell(\theta) = \sum_{i=1}^N \ln p(x_i \mid \theta)$ | Score assessing how probable the observed training dataset is under network parameter weights $\theta$. | **ELL OF THAY-tuh** / **LOG LIKE-lee-hood OF THAY-tuh** | Testing a master key against 100 door locks and counting how smoothly it turns inside each one. | [Likelihood & Log-Likelihood](../../MathsTerms/04-Probability-and-Statistical-Estimation/04-Likelihood_and_Log_Likelihood.md) |
| $\text{ELBO}(\theta, \phi)$ (Evidence Lower Bound) | $\mathbb{E}_{q_\phi(\mathbf{z}\mid\mathbf{x})}[\ln p_\theta(\mathbf{x}\mid\mathbf{z})] - D_{\text{KL}}(q_\phi(\mathbf{z}\mid\mathbf{x}) \parallel p(\mathbf{z}))$ | VAE training objective balancing data reconstruction fidelity against latent code distribution regularization. | **EL-boh** | A safety trampoline held beneath an acrobat: pushing the trampoline upward forces the acrobat higher. | [ELBO & Variational Inference](../../MathsTerms/06-Deep-Architectures-and-Generative-Models/07-ELBO_and_Variational_Inference.md) |
| $W_1(P, Q)$ (Wasserstein-1 Distance) | $\inf_{\gamma \in \Pi(P, Q)} \mathbb{E}_{(x, y) \sim \gamma}[\|x - y\|]$ | Earth Mover's Distance measuring minimum physical work required to transport probability mass from $P$ to $Q$. | **VAS-ser-stine ONE DIS-tuns** | Calculating the total fuel needed for dump trucks to shovel a pile of dirt into a matching hole. | [Wasserstein Distance](../../MathsTerms/05-Information-Theory-and-Divergences/05-Wasserstein_Distance_and_EMD.md) |
```

### 3.4 Category 4: Machine Learning & Generative AI Concepts

```markdown
## 4. Machine Learning & Generative AI Concepts

| Term / Notation | Formal Definition | Plain-English Software Meaning | Spoken English (Phonetics) | Real-World Analogy | Dedicated MathsTerm Link |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\text{Softmax}(\mathbf{z})$ | $\sigma(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}$ | Activation function transforming unbounded real logits into normalized probabilities summing to 1.0. | **SOFT-maks OF ZEE** | Slicing a single pizza proportionally according to the hunger level shouted by each diner. | [Softmax](../../MathsTerms/03-Multivariate-Calculus-and-Optimization/06-Softmax.md) |
| $\text{VJP}$ (Vector-Jacobian Product) | $\mathbf{v}^\top \mathbf{J} = \mathbf{v}^\top \left[ \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right]$ | Reverse-mode automatic differentiation step that propagates gradients without materializing the full Jacobian matrix. | **VEE JAY PEE** or **VEK-tor juh-KOH-bee-un PROD-ukt** | Pulling one master puppet control string that rotates 5 marionette joints simultaneously. | [Chain Rule & Backpropagation](../../MathsTerms/03-Multivariate-Calculus-and-Optimization/04-Chain_Rule_and_Backpropagation.md) |
| $\mathbf{z} = \boldsymbol{\mu} + \boldsymbol{\sigma} \odot \boldsymbol{\epsilon}$ (Reparameterization Trick) | $\mathbf{z} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\sigma}^2 \mathbf{I}) \iff \mathbf{z} = \boldsymbol{\mu} + \boldsymbol{\sigma} \odot \boldsymbol{\epsilon}, \, \boldsymbol{\epsilon} \sim \mathcal{N}(\mathbf{0}, \mathbf{I})$ | Separating stochastic sampling into an untracked Gaussian noise buffer so backpropagation can differentiate mean and variance. | **MYOO PLUS SIG-muh EL-uh-ment-wize EP-sil-on** | Having an independent outside dealer roll dice onto a table so the internal game rules stay differentiable. | [Reparameterization Trick](../../MathsTerms/06-Deep-Architectures-and-Generative-Models/08-Reparameterization_Trick.md) |
| $\text{LogSumExp}(\mathbf{x})$ | $\text{LSE}(\mathbf{x}) = c + \ln \sum_{i=1}^n e^{x_i - c}, \quad c = \max_i x_i$ | Numerically stable routine preventing float32 overflow (`inf`) and underflow (`0.0`) when computing log-partition functions. | **LOG SUM EXP OF EX** | Shifting all mountain elevation measurements relative to the highest peak so heights don't overflow your gauge. | [Logarithms & Exponentials](../../MathsTerms/01-Primal-Analysis-and-Foundations/02-Logarithms_and_Exponential_Functions.md) |
```

---

## 4. Authoring & Quality Gate Rules for `glossary.md`

1. **Mandatory Inclusions:**
   - Every mathematical symbol, Greek character, and shorthand notation present in `NOTES.md` and `PREREQUISITES.md` must have an entry in `glossary.md`.
   - Minimum term threshold: A compliant `glossary.md` must contain **at least 10 documented terms** across the categories and a minimum word count of **500 words**.
2. **Strict Column Headers:**
   - The table headers must match the 6 specified tokens (case-insensitive in validator, exact in template).
3. **Phonetic Guide Standards:**
   - Always capitalize stressed syllables.
   - For composite mathematical formulas, provide the spoken phrasing used by researchers, not raw LaTeX tokenization (e.g. `\nabla \cdot \mathbf{F}` is "DYE-ver-jens OF EFF", not "del dot eff").
4. **Link Resolution:**
   - Relative links must strictly target existing files under `../../MathsTerms/`.
   - If a new concept emerges from the lecture that lacks a MathsTerms file, follow the Dynamic MathsTerms Discovery Rule to author the 7-section term file before finalizing the package.
