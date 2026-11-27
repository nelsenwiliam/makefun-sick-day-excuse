#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes one line (1-200 chars) to /output/entry.txt: a sick-day excuse
a boss might half believe and a coworker would laugh at.

The program holds ten candidate lines, scores each one against the
judge's published brief (half-believable, fresh idea, twist near the
end, sounds like a real text message, no wasted words), and writes
the strongest line.
"""

import os

# Ten candidate excuses. Each is a single line a person could text
# their boss, judged below against the brief's five criteria.
CANDIDATES = [
    "Can't come in today \u2014 my smartwatch diagnosed me with 'severe "
    "horizontal' and honestly, who am I to argue with science?",
    "Won't be in today. My fridge broke, the food went bad, and I ate "
    "the evidence.",
    "Calling in sick: my cat walked across my keyboard and submitted "
    "my resignation to my own inbox, so now I'm grieving.",
    "Can't make it in \u2014 I tried to adult today and my body filed a "
    "formal complaint. HR is still reviewing it.",
    "Won't be in. I sneezed so hard my back went out, and now I'm the "
    "only person here who can't sit down or stand up.",
    "Calling in sick today: I dreamt I was at work all night, so "
    "technically I've already done a full shift.",
    "Can't come in \u2014 my houseplants staged an intervention and I'm "
    "not allowed to leave until I water them and apologise.",
    "Won't be in today. I got locked out of my own body by a "
    "two-factor authentication I never set up.",
    "Calling in sick: my dentist said no chewing for a week and I "
    "refuse to attend meetings I can't eat my way through.",
    "Can't make it in today \u2014 my bed just filed for custody of me "
    "and frankly, the bed has a strong case.",
]

# Scores out of 5 per criterion, in the brief's own order:
# 1. half-believable reason a coworker would laugh at
# 2. fresh idea (not fever / dog / dead grandmother)
# 3. twist lands on one read, funniest word near the end
# 4. sounds like a real person typing a message
# 5. no wasted words
SCORES = {
    0: (4, 4, 3, 4, 4),   # smartwatch: fresh, but the joke is a bit long
    1: (3, 4, 3, 3, 3),   # fridge: funny, but the setup eats the punch
    2: (3, 4, 3, 3, 3),   # cat resignation: cute, twist arrives too early
    3: (3, 3, 3, 4, 3),   # body filed a complaint: solid, not the freshest
    4: (5, 3, 4, 5, 4),   # sneeze/back: most believable, idea is familiar
    5: (3, 5, 4, 4, 4),   # dreamt I worked: fresh, punchline lands last
    6: (2, 4, 3, 3, 3),   # houseplants: charming, not half-believable
    7: (3, 5, 4, 3, 4),   # locked out of my body: fresh, slightly techy
    8: (4, 4, 3, 4, 3),   # dentist: believable, punchline a little soft
    9: (4, 5, 5, 5, 5),   # bed filed for custody: fresh, twist last,
                          # sounds like a real text, every word works
}


def pick_best():
    """Return the highest-scoring candidate (ties: the earliest)."""
    best_index = max(SCORES, key=lambda i: sum(SCORES[i]))
    return CANDIDATES[best_index]


def main():
    line = pick_best()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(line)


if __name__ == "__main__":
    main()
