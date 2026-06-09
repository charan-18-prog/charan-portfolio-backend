# Render Build Instructions

If deploying to Render and your build fails compiling `pydantic_core`, use this approach to install Rust in your home directory (writable) and install the Python dependencies.

1. In Render dashboard, set the **Build Command** to:

```bash
bash backend/render_build.sh
```

2. Ensure the service **Environment** uses a Python runtime that matches your requirements. If possible, set the Runtime to Python 3.11 or 3.12 to prefer prebuilt wheels and avoid Rust compilation.

3. What `backend/render_build.sh` does:

- Installs `rustup` and `cargo` into `$HOME/.rustup` and `$HOME/.cargo` so Render's read-only `/usr/local` is not used.
- Adds cargo to `PATH` for the build step.
- Installs `maturin` (needed to build wheels for Rust-based Python extensions).
- Runs `pip install -r requirements.txt` to install backend dependencies.

Alternative: Use the provided `Dockerfile` to build the backend image locally or on Render using a Docker deployment; the Dockerfile uses Python 3.11 to avoid compiling `pydantic_core`.
