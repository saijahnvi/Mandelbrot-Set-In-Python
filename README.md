# Mandelbrot-Set-In-Python

High-performance Python & Numba implementation of the Mandelbrot fractal with interactive Matplotlib zoom callbacks.

# ⚡ Interactive Numba Mandelbrot Viewer

<p align="center">
  <img src="https://github.com/user-attachments/assets/23aa2c50-e5a7-4d54-85e0-3b273aa77a3b" width="700" alt="Mandelbrot Main Preview"/>
</p>

---

## Features

* **Instant Parallel Rendering:** Uses Numba's `@njit(parallel=True)` and `numba.prange` to distribute pixel calculations across all available CPU cores.
* **Smooth Interactive Zoom:** Matplotlib viewport event hooks automatically recalculate only the active region as you pan and zoom.
* **Math Optimizations:** Replaces complex magnitude checks (`abs(z) > 2`) with squared distance comparisons (`z.real^2 + z.imag^2 > 4`) to bypass heavy square-root operations inside computational loops.
* **Event Loop Safe:** Prevents infinite recursive callback locks during Matplotlib view updates using event blocking.

---

## Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/7b915adb-ee48-459e-8dc8-3eb6a123bb59" alt="Deep Zoom Fractal Detail" width="45%" />
  &nbsp; &nbsp;
  <img src="https://github.com/user-attachments/assets/91e42c54-67e2-4639-a1ee-6ee43d15ee87" alt="Deep Zoom" width="45%" />
</p>

---

## ⚡ Performance Benchmark

| Method | Resolution | Max Steps | Compute Time |
| :--- | :--- | :--- | :--- |
| **Pure Python Loops** | 1000x1000 | 1,000 | ~12.5 seconds |
| **Numba JIT (Single Thread)** | 1000x1000 | 1,000 | ~0.42 seconds |
| **Numba JIT + Parallel CPU** | 1000x1000 | 1,000 | **~0.05 seconds :)** |

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/interactive-numba-mandelbrot.git](https://github.com/your-username/interactive-numba-mandelbrot.git)
   cd interactive-numba-mandelbrot
