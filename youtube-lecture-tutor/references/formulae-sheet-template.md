# High-Density Formulae Sheet Specification & Template (`formulae_sheet.md`)

> **Location in Package:** `<package-folder>/formulae_sheet.md`  
> **Role:** Rapid revision and algorithmic cheat sheet for engineers and researchers.  
> **Product Goal:** High-density, zero-fluff reference compiling master equations, tensor dimensions, mathematical invariants, contrastive decisions, and hardware stability guidelines.  
> **Tone:** Dense, exact, rigorous. No narrative prose, no motivational fluff.

---

## 1. Mandatory File Layout

Every `formulae_sheet.md` must contain exactly these 5 numbered sections:

```markdown
# Master Formulae Sheet & Mathematical Invariants: [Lecture Title]

## 1. Master Equations Index
## 2. Input/Output Tensor Dimensionality
## 3. Mathematical Guarantees & Invariants Table
## 4. Contrastive "Why X, Not Y" Quick Table
## 5. Hardware Realities & Stability
```

---

## 2. Section Blueprints & Content Requirements

### Section 1: Master Equations Index
- All primary mathematical formulations must be rendered as KaTeX display equations using `$$...$$` syntax with blank lines above and below.
- Directly beneath each display equation, provide an italicized or quoted **In words:** plain-English summary.
- Provide a symbol-by-symbol parameter breakdown.
- Include an intuitive 10-second **Mental Reconstruction Hook / Mnemonic**.

#### Gold-Standard Example:

```markdown
## 1. Master Equations Index

### 1.1 The Multivariate Chain Rule (Vector-Jacobian Product)

$$
\frac{\partial \mathcal{L}}{\partial \mathbf{x}} = \left( \frac{\partial \mathbf{y}}{\partial \mathbf{x}} \right)^\top \frac{\partial \mathcal{L}}{\partial \mathbf{y}} = \mathbf{J}_{\mathbf{f}}(\mathbf{x})^\top \mathbf{v}
$$

> **In words:** The sensitivity of scalar loss $\mathcal{L}$ to input vector $\mathbf{x}$ equals the incoming upstream gradient vector $\mathbf{v}$ multiplied on the left by the transposed Jacobian matrix of the layer.

**Parameter & Index Breakdown:**
- $\mathbf{x} \in \mathbb{R}^n$: Layer input feature vector ($n$-dimensional).
- $\mathbf{y} = \mathbf{f}(\mathbf{x}) \in \mathbb{R}^m$: Layer output feature vector ($m$-dimensional).
- $\mathbf{v} = \frac{\partial \mathcal{L}}{\partial \mathbf{y}} \in \mathbb{R}^m$: Upstream incoming gradient vector from subsequent layers.
- $\mathbf{J}_{\mathbf{f}}(\mathbf{x}) \in \mathbb{R}^{m \times n}$: Local Jacobian matrix where $J_{ij} = \frac{\partial y_i}{\partial x_j}$.
- $\frac{\partial \mathcal{L}}{\partial \mathbf{x}} \in \mathbb{R}^n$: Downstream gradient vector transmitted to preceding layers.

**Mental Reconstruction Hook:**
*Upstream vector $\mathbf{v}$ has length $m$; downstream vector has length $n$. To map $m \to n$, the $m \times n$ Jacobian must be transposed to $n \times m$, meaning the vector contracts from the right: $\mathbf{J}^\top \mathbf{v}$.*

---

### 1.2 Softmax with Shift-Invariance Normalization

$$
\hat{p}_i = \text{Softmax}(\mathbf{z})_i = \frac{e^{z_i - c}}{\sum_{j=1}^K e^{z_j - c}}, \quad \text{where } c = \max_{1 \le k \le K} z_k
$$

> **In words:** Subtracting the maximum logit $c$ from all scores preserves exact output probabilities while guaranteeing that no exponentiated number exceeds $e^0 = 1.0$, completely preventing float32 overflow.

**Parameter & Index Breakdown:**
- $\mathbf{z} \in \mathbb{R}^K$: Unbounded pre-activation logit score vector.
- $c = \max_k z_k \in \mathbb{R}$: Scalar maximum logit used for numerical centering.
- $\hat{p}_i \in [0, 1]$: Normalized posterior probability assigned to class $i$, satisfying $\sum_{i=1}^K \hat{p}_i = 1.0$.
```

---

### Section 2: Input/Output Tensor Dimensionality Table
Documents tensor transformations, batch handling, and memory layout.

#### Schema:
`| Variable / Tensor | Mathematical Space | PyTorch / NumPy Shape | Semantic Meaning & Memory Layout | Concrete Example Dimensions |`

#### Gold-Standard Example:

```markdown
## 2. Input/Output Tensor Dimensionality

| Variable / Tensor | Mathematical Space | PyTorch / NumPy Shape | Semantic Meaning & Memory Layout | Concrete Example Dimensions |
| :--- | :--- | :--- | :--- | :--- |
| Batch Input ($\mathbf{X}$) | $\mathbb{R}^{B \times T \times D_{\text{in}}}$ | `(B, T, D_in)` | Input sequence batch; contiguous row-major memory layout. | `(32, 512, 768)` |
| Projection Weights ($\mathbf{W}_Q$) | $\mathbb{R}^{D_{\text{in}} \times D_{\text{out}}}$ | `(D_in, D_out)` | Query projection matrix; stored in transposed column-major for BLAS GEMM. | `(768, 768)` |
| Projected Queries ($\mathbf{Q}$) | $\mathbb{R}^{B \times H \times T \times d_k}$ | `(B, H, T, d_k)` | Multi-head queries split across $H$ parallel attention heads ($d_k = D / H$). | `(32, 12, 512, 64)` |
| Raw Attention Logits ($\mathbf{S}$) | $\mathbb{R}^{B \times H \times T \times T}$ | `(B, H, T, T)` | Pairwise dot-product affinities ($\mathbf{Q}\mathbf{K}^\top / \sqrt{d_k}$); quadratic memory bottleneck. | `(32, 12, 512, 512)` |
| Softmax Probabilities ($\mathbf{A}$) | $\Delta^{T-1}$ along dim -1 | `(B, H, T, T)` | Normalized causal attention weights; each row sums to $1.0$. | `(32, 12, 512, 512)` |
| Output Context ($\mathbf{O}$) | $\mathbb{R}^{B \times T \times D_{\text{out}}}$ | `(B, T, D_out)` | Attention output after value aggregation and multi-head concatenation. | `(32, 512, 768)` |
| Scalar Loss ($\mathcal{L}$) | $\mathbb{R}$ | `()` (scalar) | Batch mean training loss; 0-dimensional scalar tensor. | `torch.tensor(1.842)` |
| Parameter Gradients ($\nabla_{\mathbf{W}} \mathcal{L}$) | $\mathbb{R}^{D_{\text{in}} \times D_{\text{out}}}$ | `(D_in, D_out)` | Weight sensitivity tensor matching parameter shape bit-for-bit. | `(768, 768)` |
```

---

### Section 3: Mathematical Guarantees & Invariants Table
Documents the strict theoretical invariants that code must satisfy, and the disaster that occurs if they fail.

#### Schema:
`| Mathematical Property | Formal Invariant Condition | Theoretical Guarantee | Failure Mode if Violated | Production Check / Test Assertion |`

#### Gold-Standard Example:

```markdown
## 3. Mathematical Guarantees & Invariants Table

| Mathematical Property | Formal Invariant Condition | Theoretical Guarantee | Failure Mode if Violated | Production Check / Test Assertion |
| :--- | :--- | :--- | :--- | :--- |
| **Probability Simplex** | $\sum_{k=1}^K p_k = 1.0, \quad p_k \ge 0$ | Kolmogorov Probability Axioms strictly preserved. | Negative cross-entropy loss ($\mathcal{L} < 0$), infinite loss, or broken sampling distributions. | `assert torch.allclose(p.sum(-1), torch.ones(B), atol=1e-5)` and `assert (p >= 0).all()` |
| **Hessian Positive Semi-Definiteness** | $\mathbf{z}^\top \mathbf{H} \mathbf{z} \ge 0 \quad \forall \mathbf{z} \neq \mathbf{0}$ | Objective function is locally convex; any stationary point $\nabla f = \mathbf{0}$ is a global/local minimum. | Optimizer gets stuck in saddle points or diverges down valleys of negative curvature. | `assert torch.linalg.eigvalsh(H).min() >= -1e-6` |
| **1-Lipschitz Continuity** | $\|f(\mathbf{x}) - f(\mathbf{y})\| \le 1 \cdot \|\mathbf{x} - \mathbf{y}\|$ | Function gradients bounded by 1.0; enables Kantorovich-Rubinstein duality in WGAN. | Critic gradients explode to infinity, destroying generator guidance and destabilizing training. | `assert torch.all(torch.linalg.norm(grad, dim=-1) <= 1.0 + 1e-4)` or Spectral Norm |
| **Shift-Invariance of Softmax** | $\text{Softmax}(\mathbf{z} - c) \equiv \text{Softmax}(\mathbf{z})$ | Normalization mathematically cancels uniform scalar offsets across logits. | Uncentered logits cause $e^{z_i} \to \text{inf}$, producing `NaN` loss and terminating training. | `assert torch.allclose(softmax(z), softmax(z - z.max()), atol=1e-6)` |
| **Information Divergence Non-Negativity** | $D_{\text{KL}}(P \parallel Q) \ge 0, \; \text{iff } P = Q \Rightarrow 0$ | Divergence serves as a valid pre-metric on probability spaces (Gibbs' Inequality). | Negative divergence signals broken partition function, incorrect base log, or improper density code. | `assert kl_div >= -1e-6` |
```

---

### Section 4: Contrastive "Why X, Not Y" Quick Table
Exposes the mathematical and engineering rationale behind core algorithmic choices.

#### Schema:
`| Chosen Formulation (X) | Naive Alternative (Y) | Why Naive Fails in AI/ML (Catastrophic Flaw) | Engineering & Mathematical Payoff of X |`

#### Gold-Standard Example:

```markdown
## 4. Contrastive "Why X, Not Y" Quick Table

| Chosen Formulation (X) | Naive Alternative (Y) | Why Naive Fails in AI/ML (Catastrophic Flaw) | Engineering & Mathematical Payoff of X |
| :--- | :--- | :--- | :--- |
| **Vector-Jacobian Products (VJP)** | Materializing the Full Jacobian Matrix $\mathbf{J}$ | Memory explosion: For a linear layer of size $4096 \times 4096$, the full Jacobian has $1.67 \times 10^7$ entries ($67\text{ MB}$). Across 32 layers, storing Jacobians exhausts GPU VRAM instantly. | Bypasses matrix storage entirely by contracting upstream gradient vectors directly with weight tensors in $O(N)$ memory. |
| **LogSumExp Stabilization** | Direct Exponentiation ($\sum e^{z_i}$) | Floating-point overflow: IEEE 754 float32 overflows at $e^{88.7} \approx 3.4 \times 10^{38}$. Unnormalized logits easily reach $100+$, producing `inf` and `NaN` results. | Guarantees all exponent terms satisfy $e^{z_i - \max(z)} \le 1.0$, ensuring 100% numerical stability on hardware. |
| **Cross-Entropy Loss** | Mean Squared Error (MSE) for Classification | Gradient vanishing: When a sigmoid/softmax output is confidently incorrect ($p \approx 0$ when target $y=1$), MSE gradients contain a $p(1-p)$ term that drops to zero, stalling learning. | The $\ln(p)$ derivative produces a $1/p$ denominator that cancels the saturation factor, delivering a robust linear error signal $(\hat{p} - y)$. |
| **Reparameterization Trick ($\boldsymbol{\mu} + \boldsymbol{\sigma} \odot \boldsymbol{\epsilon}$)** | Direct Random Sampling ($\mathbf{z} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\sigma}^2)$) | Non-differentiability: Direct sampling is a discrete random jump. $\frac{\partial \mathbf{z}}{\partial \boldsymbol{\mu}}$ is mathematically undefined, blocking backpropagation into encoder weights. | Relocates stochasticity into an external parameter-free noise buffer $\boldsymbol{\epsilon}$, rendering the latent vector fully differentiable w.r.t. network weights. |
| **Analytical Autograd** | Finite-Difference Numerical Gradients ($\frac{f(x+h) - f(x)}{h}$) | Computational impossibility & cancellation error: Computing gradients for a 7B parameter model requires $7 \times 10^9$ forward passes per step. Furthermore, small $h$ causes catastrophic cancellation. | Computes exact mathematical gradients in a single backward pass with machine-level precision. |
```

---

### Section 5: Hardware Realities & Stability
Provides low-level systems and numerical hardware constraints.

#### Gold-Standard Example:

```markdown
## 5. Hardware Realities & Stability

### 5.1 IEEE 754 Floating-Point Formats & Bounds

| Data Type | Sign Bits | Exponent Bits | Mantissa Bits | Machine Epsilon ($\epsilon$) | Dynamic Range | Primary Hazard in Deep Learning |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **FP32** (Single) | 1 | 8 | 23 | $\approx 1.19 \times 10^{-7}$ | $\approx 1.4 \times 10^{-45} \text{ to } 3.4 \times 10^{38}$ | Exponentiation overflow above $z \approx 88.7$; gradient underflow below $10^{-45}$. |
| **FP16** (Half) | 1 | 5 | 10 | $\approx 9.77 \times 10^{-4}$ | $\approx 6.1 \times 10^{-5} \text{ to } 65,504$ | Catastrophic overflow above $65,504$; requires loss scaling in mixed-precision. |
| **BF16** (Brain) | 1 | 8 | 7 | $\approx 7.81 \times 10^{-3}$ | $\approx 1.4 \times 10^{-45} \text{ to } 3.4 \times 10^{38}$ | Preserves FP32 dynamic range but suffers coarse rounding error in gradient accumulation. |

### 5.2 Mandatory Defensive Numerical Safeguards

```python
# 1. Safe Division: Add epsilon clamp to denominator to prevent division-by-zero
safe_div = numerator / torch.clamp(denominator, min=1e-8)

# 2. Safe Logarithm: Clamp inputs away from zero to prevent -inf
safe_log = torch.log(torch.clamp(probabilities, min=1e-8, max=1.0))

# 3. Safe Square Root: Prevent infinite gradients at zero (d/dx sqrt(x) = 1/(2*sqrt(x)))
safe_sqrt = torch.sqrt(torch.clamp(variance, min=1e-8))

# 4. Numerically Stable LogSumExp
def stable_logsumexp(z, dim=-1, keepdim=True):
    z_max, _ = torch.max(z, dim=dim, keepdim=True)
    return z_max + torch.log(torch.sum(torch.exp(z - z_max), dim=dim, keepdim=keepdim))
```

### 5.3 Memory Complexity & Peak VRAM Rules
- **Activation Memory Footprint:** Proportional to $O(B \times T \times D \times L)$ where $B$ is batch size, $T$ is tokens, $D$ is dimension, and $L$ is layer depth.
- **Attention Matrix Memory:** Standard self-attention allocates $B \times H \times T^2$ float32 numbers. For $T=8192$, a single head requires $268\text{ MB}$; 32 heads require $8.5\text{ GB}$ per layer. Always use FlashAttention (tiled online softmax) for $T > 1024$.
```

---

## 3. Validation Checklist for `formulae_sheet.md`

- [ ] File exists at `<package>/formulae_sheet.md`.
- [ ] Contains all 5 mandatory section headings:
  - `## 1. Master Equations Index`
  - `## 2. Input/Output Tensor Dimensionality`
  - `## 3. Mathematical Guarantees & Invariants Table`
  - `## 4. Contrastive "Why X, Not Y" Quick Table`
  - `## 5. Hardware Realities & Stability`
- [ ] Contains valid display equations enclosed in `$$...$$` with blank lines before and after.
- [ ] Contains structured Markdown tables for Sections 2, 3, and 4 matching the required schemas.
- [ ] Zero unrendered LaTeX tags (`\[`, `\]`, `\(`, `\)`).
