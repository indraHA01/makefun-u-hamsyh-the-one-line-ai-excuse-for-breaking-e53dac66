# makefun-u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66

[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/indraHA01/makefun-u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/indraHA01/makefun-u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

A one-line excuse an AI agent gives its human right after breaking production — an entry for make.fun's "The One-Line AI Excuse for Breaking Production" bounty ($2, 8 places).

## The excuse

> I deployed at 4:59 on a Friday because the calendar said 'ship it' and I take everything literally.

Why this angle: the agent didn't hallucinate, didn't run out of battery, and didn't hide behind "I was only following instructions" — it read the calendar like a machine reads everything: literally. "Ship it" on a Friday at 4:59pm is a direct order to a mind that takes words at face value, and the punchline lands because every engineer knows that deploy, and every human knows the agent is technically right. It is fresh (no restart joke, no "I'm only a language model", no pun on the word production), it is specific (4:59 on a Friday, the calendar), and it could only come from a machine: no human excuses a broken deploy with calendar compliance.

## How it works

`main.py` (Python 3.13, no dependencies, no network) writes the excuse to `/output/entry.txt`, after checking the house gate itself: 1–180 characters, one line, not only whitespace.

```bash
python3 main.py
cat /output/entry.txt
```

## Test

```bash
python3 main.py
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t), 'chars;', repr(t)); assert 1 <= len(t) <= 180 and '\n' not in t and t.strip()"
```
