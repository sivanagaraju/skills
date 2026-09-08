# Standalone Python Simulations Contract & Specification (`examples/*.py`)

> **Location in Package:** `<package-folder>/examples/`  
> **Role:** Executable verification engine of the learning package.  
> **Product Goal:** Anchor theoretical equations and lecture proofs with runnable, deterministic, fully commented Python scripts that execute cleanly on CPU and verify mathematics via assertions.  
> **Core Principle:** *"If you cannot write a runnable simulation that matches library outputs within numerical tolerance, the mathematical explanation is incomplete."*

---

## 1. Directory Structure & File Naming

Every upgraded package must contain an `examples/` directory populated by 1 to 3 standalone scripts:

```
<package-folder>/
└── examples/
    ├── 01_numerical_verification.py       # First-principles math vs framework reference
    ├── 02_torch_autograd_simulation.py    # Autograd/gradient/optimization simulation
    └── [03_specialized_model_sim.py]      # Optional: Domain simulation (e.g. VAE/GAN/Attention)
```

### Naming Conventions:
- Files must be prefixed with a two-digit sequence number: `01_`, `02_`, `03_`.
- Use descriptive `snake_case` identifying the verified mathematical theorem.
- Scripts must be standalone: executable directly via `python examples/<script_name>.py` without external workspace imports.

---

## 2. Mandatory Module Docstring Standard

The first lines of every script must contain a standardized triple-quoted docstring following this exact template:

```python
"""
File: 01_numerical_verification.py
Package: NN-slug-name
Lecture Mapping: Topic N (MM:SS - MM:SS) & Topic M (MM:SS - MM:SS) in NOTES.md
Mathematical Theorems & Concepts Verified:
    1. <Theorem / Formula Name 1, e.g., Shift-Invariance of Softmax>
    2. <Theorem / Formula Name 2, e.g., Analytical Jacobian vs PyTorch Autograd>
Prerequisites & Foundations:
    - MathsTerms/03-Multivariate-Calculus-and-Optimization/06-Softmax.md
Hardware Requirements:
    - Pure CPU execution (device = torch.device('cpu'))
    - Deterministic execution with fixed seeds (seed = 42)
    - Dependencies: python >= 3.9, numpy >= 1.22, torch >= 2.0
Execution:
    python examples/01_numerical_verification.py
Expected Result:
    All assertion checks pass; prints verification summary; exits with code 0.
"""
```

---

## 3. The Dual-Implementation & Non-Triviality Standard

To prevent hollow or trivial code snippets (e.g. printing a string or calling a library function without validation), every script must implement a **Dual-Implementation Verification Loop**:

1. **Path A: Manual First-Principles Implementation (`manual_*`)**:
   - Implemented from scratch using elementary arithmetic, explicit loops, or basic matrix operations.
   - Shows every step of the formula (e.g., manually subtracting max, computing exponents, dividing by the sum).
2. **Path B: Framework / Standard Reference (`torch_*` / `scipy_*`)**:
   - Implemented using native high-level library operations (e.g. `torch.nn.functional.softmax`, `torch.autograd.functional.jacobian`).
3. **Equivalence Tolerance Assertion**:
   - The script must assert mathematical equivalence between Path A and Path B using `torch.allclose()` or `np.allclose()`.

---

## 4. Mandatory Assertions Contract

- Every script must contain **at least 2 distinct mathematical assertions**.
- Standard tolerance parameters: `atol=1e-4`, `rtol=1e-4` (tolerating single-precision FP32 rounding).
- Every assertion must include a descriptive failure message:

```python
# Standard assertion pattern
max_diff = torch.max(torch.abs(manual_output - torch_output)).item()
assert torch.allclose(manual_output, torch_output, atol=1e-4, rtol=1e-4), (
    f"Numerical mismatch in {theorem_name}!\n"
    f"  Max Absolute Difference: {max_diff:.6e} (exceeds tolerance 1e-4)\n"
    f"  Manual Output: {manual_output}\n"
    f"  Torch Output:  {torch_output}"
)
print(f"[PASS] {theorem_name}: max discrepancy = {max_diff:.6e} < 1e-4")
```

---

## 5. Execution Guarantee & Environmental Constraints

1. **Pure CPU Portability:**
   - Explicitly enforce CPU execution: `device = torch.device("cpu")`.
   - Never call `.cuda()` or require GPU hardware.
2. **Deterministic Reproducibility:**
   - Seed all random number generators at script initialization:
     ```python
     import torch
     import numpy as np
     torch.manual_seed(42)
     np.random.seed(42)
     ```
3. **Execution Budget:**
   - Must run to completion in **$< 30$ seconds** (the automated validator timeout limit).
   - Peak RAM usage must remain $< 500\text{ MB}$.
4. **Clean Exit Code 0:**
   - If all assertions pass, the script must exit cleanly with code 0.
   - If an assertion fails or an error occurs, the script must exit with a non-zero exit code.
5. **Main Guard:**
   - Always wrap execution inside `if __name__ == "__main__": main()`.

---

## 6. Bidirectional Markdown Cross-Linking Contract

1. **In `NOTES.md` and `PREREQUISITES.md`:**
   - The markdown text must explicitly direct the student to the script:
     ```markdown
     > 💻 **Runnable Simulation:** Verify the derivation above by running the standalone simulation:  
     > [`examples/01_numerical_verification.py`](./examples/01_numerical_verification.py).
     ```
2. **In `examples/*.py`:**
   - The docstring must state the exact matching topic heading and timestamp range in `NOTES.md`.

---

## 7. Gold-Standard Script Blueprint (`01_numerical_verification.py`)

Below is the complete reference implementation demonstrating the required contract:

```python
#!/usr/bin/env python3
"""
File: 01_numerical_verification.py
Package: 17-Tutorial03-PyTorch-Basics
Lecture Mapping: Topic 3 (18:20 - 32:45) in NOTES.md
Mathematical Theorems & Concepts Verified:
    1. Shift-Invariance of Softmax: Softmax(z) == Softmax(z - c)
    2. Analytical Jacobian of Softmax vs PyTorch Autograd Jacobian
    3. Vector-Jacobian Product (VJP) Equivalence: v^T J == autograd.grad
Prerequisites & Foundations:
    - MathsTerms/03-Multivariate-Calculus-and-Optimization/06-Softmax.md
Hardware Requirements:
    - Pure CPU execution (device = torch.device('cpu'))
    - Deterministic execution with fixed seeds (seed = 42)
    - Dependencies: python >= 3.9, numpy >= 1.22, torch >= 2.0
Execution:
    python examples/01_numerical_verification.py
Expected Result:
    All assertion checks pass; prints verification summary; exits with code 0.
"""

from __future__ import annotations
import sys
import torch
import numpy as np


def verify_shift_invariance() -> None:
    """Theorem 1: Prove Softmax(z) is invariant under uniform scalar addition."""
    print("=" * 70)
    print("Verifying Theorem 1: Shift-Invariance of Softmax")
    print("=" * 70)

    # Realistic unconstrained logits
    z = torch.tensor([2.5, -1.2, 0.8, 3.1, -0.4], dtype=torch.float32)
    # Moderate arbitrary shift within safe FP32 dynamic range (< 88.7).
    # Note: Large arbitrary shifts (e.g. c >= 89.0) overflow exp() in un-stabilized float32 to inf,
    # causing NaN (inf/inf). In production, subtracting c_max (Path B) is mandatory.
    c_arbitrary = 5.0
    c_max = torch.max(z).item()

    # Manual First-Principles Softmax implementation
    def manual_softmax(scores: torch.Tensor) -> torch.Tensor:
        exp_scores = torch.exp(scores)
        return exp_scores / torch.sum(exp_scores)

    # Path A: Raw manual softmax
    p_raw = manual_softmax(z)

    # Path B: Stabilized manual softmax (z - c_max)
    p_max_shifted = manual_softmax(z - c_max)

    # Path C: Arbitrary shift within safe FP32 range (z + 5.0)
    p_arbitrary_shifted = manual_softmax(z + c_arbitrary)

    # Path D: Native PyTorch implementation
    p_torch = torch.nn.functional.softmax(z, dim=0)

    # Assertions
    diff_max = torch.max(torch.abs(p_raw - p_max_shifted)).item()
    diff_arb = torch.max(torch.abs(p_raw - p_arbitrary_shifted)).item()
    diff_torch = torch.max(torch.abs(p_raw - p_torch)).item()

    assert torch.allclose(p_raw, p_max_shifted, atol=1e-5), f"Max shift failed: diff={diff_max}"
    assert torch.allclose(p_raw, p_arbitrary_shifted, atol=1e-5), f"Arbitrary shift failed: diff={diff_arb}"
    assert torch.allclose(p_raw, p_torch, atol=1e-5), f"Torch comparison failed: diff={diff_torch}"

    print(f"  Logits (z):               {z.numpy()}")
    print(f"  Probabilities (p):        {p_raw.numpy()}")
    print(f"  Sum of Probabilities:     {p_raw.sum().item():.6f} (Kolmogorov Axiom 1.0)")
    print(f"  [PASS] Max Shift Discrepancy:      {diff_max:.2e} < 1e-5")
    print(f"  [PASS] Arbitrary Shift Discrepancy:{diff_arb:.2e} < 1e-5")
    print(f"  [PASS] PyTorch Native Equivalence: {diff_torch:.2e} < 1e-5\n")


def verify_softmax_jacobian() -> None:
    """Theorem 2: Prove Analytical Jacobian matches PyTorch Autograd Jacobian."""
    print("=" * 70)
    print("Verifying Theorem 2: Analytical Jacobian vs Autograd Jacobian")
    print("=" * 70)

    z = torch.tensor([1.5, 0.2, -0.7, 2.1], dtype=torch.float32, requires_grad=True)
    p = torch.nn.functional.softmax(z, dim=0)
    K = len(z)

    # Path A: Manual Analytical Jacobian derivation
    # Formula: J_ij = p_i * (delta_ij - p_j)
    J_manual = torch.zeros((K, K), dtype=torch.float32)
    for i in range(K):
        for j in range(K):
            delta_ij = 1.0 if i == j else 0.0
            J_manual[i, j] = p[i] * (delta_ij - p[j])

    # Path B: PyTorch Functional Autograd Jacobian
    J_autograd = torch.autograd.functional.jacobian(
        lambda inputs: torch.nn.functional.softmax(inputs, dim=0), z
    )

    # Assertion
    diff_jacobian = torch.max(torch.abs(J_manual - J_autograd)).item()
    assert torch.allclose(J_manual, J_autograd, atol=1e-5), (
        f"Jacobian mismatch: diff={diff_jacobian:.6e}\n"
        f"Manual:\n{J_manual}\nAutograd:\n{J_autograd}"
    )

    print(f"  Analytical Jacobian (J_manual):\n{J_manual.detach().numpy()}")
    print(f"  Autograd Jacobian (J_autograd):\n{J_autograd.detach().numpy()}")
    print(f"  Row Sums of Jacobian:          {J_manual.sum(dim=1).detach().numpy()} (Should be all 0.0)")
    print(f"  [PASS] Jacobian Discrepancy:            {diff_jacobian:.2e} < 1e-5\n")


def verify_vjp_contraction() -> None:
    """Theorem 3: Prove Vector-Jacobian Product (VJP) matches backward autograd."""
    print("=" * 70)
    print("Verifying Theorem 3: Vector-Jacobian Product (VJP) Equivalence")
    print("=" * 70)

    z = torch.tensor([1.2, -0.5, 2.3, 0.1], dtype=torch.float32, requires_grad=True)
    v = torch.tensor([0.1, -0.3, 0.5, 0.2], dtype=torch.float32)  # Upstream gradient

    # Path A: Full Jacobian Contraction (v^T @ J)
    J = torch.autograd.functional.jacobian(lambda x: torch.nn.functional.softmax(x, dim=0), z)
    vjp_manual = v @ J

    # Path B: PyTorch autograd.grad with grad_outputs (Reverse-Mode AD)
    p = torch.nn.functional.softmax(z, dim=0)
    vjp_autograd = torch.autograd.grad(p, z, grad_outputs=v, retain_graph=True)[0]

    # Assertion
    diff_vjp = torch.max(torch.abs(vjp_manual - vjp_autograd)).item()
    assert torch.allclose(vjp_manual, vjp_autograd, atol=1e-5), f"VJP mismatch: diff={diff_vjp}"

    print(f"  Upstream Gradient (v):    {v.numpy()}")
    print(f"  Manual v^T @ J:           {vjp_manual.numpy()}")
    print(f"  Autograd VJP:             {vjp_autograd.numpy()}")
    print(f"  [PASS] VJP Equivalence Discrepancy:{diff_vjp:.2e} < 1e-5\n")


def main() -> None:
    print("=" * 70)
    print("RUNNING STANDALONE NUMERICAL VERIFICATION SUITE")
    print("=" * 70 + "\n")

    # Set deterministic random seeds
    torch.manual_seed(42)
    np.random.seed(42)

    try:
        verify_shift_invariance()
        verify_softmax_jacobian()
        verify_vjp_contraction()
    except AssertionError as err:
        print(f"\n[FATAL ERROR] Mathematical Verification FAILED: {err}", file=sys.stderr)
        sys.exit(1)

    print("=" * 70)
    print("SUCCESS: ALL MATHEMATICAL THEOREMS VERIFIED CLEANLY (EXIT CODE 0)")
    print("=" * 70)
    sys.exit(0)


if __name__ == "__main__":
    main()
```

---

## 8. Validator Integration Rules (`validate_package.py`)

The automated evaluation engine enforces this contract via two distinct verification functions:

1. `check_examples_directory(package_dir, rep)`:
   - Asserts `<package>/examples/` exists and contains at least one `.py` script.
   - Parses each script's AST or header lines to verify:
     * Standard docstring present with `Mathematical Theorems & Concepts Verified` and `Lecture Mapping`.
     * Presence of `torch.allclose` or `np.allclose`.
     * Explicit cross-reference link inside `PREREQUISITES.md` or `NOTES.md`.
2. `verify_code_execution(package_dir, rep, timeout=30)`:
   - Invokes each script via `subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True, timeout=timeout)`.
   - Asserts clean termination (`returncode == 0`).
   - If execution fails or times out, logs an ERROR containing the captured traceback.
   - Allows `--skip-exec` flag on the CLI to bypass execution in environments without installed dependencies.
