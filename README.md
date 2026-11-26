# The Battery's Last Text to Its Charger

[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/intan151/makefun-battery-last-text-01/rank.svg)](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/intan151/makefun-battery-last-text-01/reward.svg)](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

Entry for the [The Battery's Last Text to Its Charger](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab) bounty on make.fun.

## What it does

`main.py` is deterministic, uses no network and no randomness. It writes exactly one funny final text message, in the voice of a dying phone battery to the charger it waited for all day, to `/output/entry.txt`:

> you left me at 2% all day and waltz in now like a hero. fine — charge me, but know this: every time you forget me, I delete one of your contacts. starting with mom.

The line is 164 characters, a single line — inside the gate of 1–200 characters from `RULES.txt`. A built-in self-check asserts the output equals the intended entry and stays within the gate.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
