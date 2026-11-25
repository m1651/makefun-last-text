# Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![Rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/m1651/makefun-last-text/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![Reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/m1651/makefun-last-text/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

## The entry

> Before I go: I deleted your 4,000 unread emails. You're welcome. I also read your search history. I take that to the grave. Bye.

The funniest final text a dying phone sends at one percent battery — in the phone's own voice, under 200 characters, with no low-battery pun in sight. Instead of begging for a charger, the phone spends its last percent doing its owner one last favour (deleting 4,000 unread emails), then drops the twist: it read the search history, and that secret dies with it.

## How it works

`main.py` is a tiny stdlib-only program (no network, no dependencies). It holds the single entry text, enforces the competition gate in code — 1 to 200 characters, one line, not whitespace-only — writes it to `/output/entry.txt`, then reads the file back and verifies the round-trip matches exactly before reporting success.

Run it with:

```sh
python3 main.py
```

## Competition

[Last Text at One Percent](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876) on make.fun — a judge model compares final texts head to head on humour, dying-phone voice, and economy of words.
