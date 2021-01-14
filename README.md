# SimpleMemoryTestingEnv

This is a simple OpenAI Gym-compatible environment to test RL agent's memory.

## Usage

`gym` must be installed. CoMaze environment can be created via running inside a `python` interpreter:

```python
>>> import gym
>>> import simple_memory_testing_env
>>> env = gym.make(f"SimpleMemoryTestingEnv-v0")
```

## Installation

### Installing via pip

This package is available in PyPi as `comaze-gym`

```bash
pip install simple_memory_testing_env
```

### Installing via cloning this repository

```bash
git clone https://www.github.com/Near32/SimpleMemoryTestingEnv
cd SimpleMemoryTestingEnv
pip install -e .
```