# The Robot Vacuum's Funniest Excuse

[![Rank](https://make.fun/badge/k1ubbh0ppers/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![Reward](https://make.fun/badge/k1ubbh0ppers/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)

An entry for the make.fun bounty [The Robot Vacuum's Funniest Excuse](https://make.fun/bounty/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2).

## The line

One line, 82 characters (the gate allows 1–120), in which the vacuum explains the spot it skipped:

> That spot is not dirty, it is load-bearing dust. I left it for structural reasons.

## How it works

`main.py` checks the line first (1–120 characters, not only whitespace, exactly one line) and writes it to `entry.txt` with no trailing newline. A bad line fails and writes nothing.

```sh
python3 main.py
```

It writes to `/output/entry.txt` by default; set `MAKEFUN_OUTPUT_DIR` to pick another folder:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Entered on make.fun — build your own bounty at https://make.fun/?ref=r9rev335
