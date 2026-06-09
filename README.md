# Backend Docker instructions

This Docker setup builds and runs the FastAPI backend using Python 3.11 (prebuilt wheels preferred).

Build the image from repo root:

```bash
cd backend
docker build -t charan-portfolio-backend:latest .
```

Run the container:

```bash
docker run --rm -p 8000:8000 charan-portfolio-backend:latest
```

API will be available at `http://localhost:8000`.

Notes:
- Using Python 3.11 avoids compiling Rust extensions like `pydantic_core` on most systems because prebuilt wheels are available.
- If you prefer to deploy on Render without Docker, add Rust toolchain installation and set `CARGO_HOME`/`RUSTUP_HOME` to a writable location in the build command (or switch the service runtime to Python 3.11/3.12).
