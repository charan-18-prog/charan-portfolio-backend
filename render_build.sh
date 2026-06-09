#!/usr/bin/env bash
set -euo pipefail

# Render build helper: install rust in $HOME, install maturin, then install python deps
export CARGO_HOME="$HOME/.cargo"
export RUSTUP_HOME="$HOME/.rustup"

echo "Installing rustup to $RUSTUP_HOME and cargo to $CARGO_HOME"
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
export PATH="$CARGO_HOME/bin:$PATH"

echo "Upgrading pip and installing maturin"
python -m pip install --upgrade pip setuptools wheel
python -m pip install maturin

echo "Installing Python requirements"
python -m pip install -r requirements.txt

echo "Build script finished"
