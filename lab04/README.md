# Lab 4: A Month of Weather

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

Four weeks of daily highs and lows, and a thermometer that reads two degrees
high. Convert the month to Celsius, find how much each day swings, fix the
readings without losing the raw data, average the month, and split each week
into weekdays and weekend.

Everything in this lab comes from **§3.3–3.6**: copies of lists, `for` loops,
list comprehensions, `zip`, nested lists, slicing, and tuples.

---

## Step 1 — Get this week's lab

From inside your `math170-yourname` folder:

```
git pull upstream main
```

The `lab04` folder appears. Your earlier work is untouched — Git only brings
across what is new.

**`git pull` says you are not in a repository?** You are in the wrong folder.
`cd` into `math170-yourname` first.

---

## Step 2 — Work through the notebook

Open `lab04/lab04.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab04` folder. Run the data cell at the top first.

There are five tasks. Each gives you a `def` line and a docstring; you write the
lines underneath. Run the TEST cell after each task to see how you did.

---

## Step 3 — Build `lab04_weather.py`

Near the end of the notebook there is a **build cell**: run it, and it collects
the five functions you wrote and writes them into `lab04_weather.py` in this
folder. Then run the **check cell** after it.

**That file is what gets graded**, not the notebook. Run every task cell first,
so all five functions exist. If you change an answer later, fix it in the task
cell and run the build cell again — the file is rewritten each time.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab04/lab04_weather.py
git commit -m "Complete Lab 4"
git push
```

Check `git status` first, then stage the one file Gradescope needs, by name.
Your notebook stays on your laptop. **Avoid `git add .`** — it sweeps in
everything else sitting in the folder, and anything you push is in your
repository's history for good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab04/lab04_weather.py` is
there with your code in it. Gradescope reads your repository, so if the file is
not on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 04 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab04_weather.py` directly instead. That
works just as well.

You may resubmit as many times as you like. The last one counts.

---

## Grading

This lab is graded on **completion**, not correctness.

- **Each of the five tasks is worth 20 points**, earned by doing real work on it.
  Your answer does not have to be right.
- A task left exactly as the starter wrote it earns nothing for that task, so an
  attempt beats a blank every time.
- A file that does not run, or no file at all, earns **0** overall.
- Gradescope shows which checks passed and which failed so you can see what to
  fix. Those checks do not change your score.

So if a check is red and lab is over, submit anyway.

---

## If something breaks

- **`NameError: name 'month_highs' is not defined`** — run the data cell at the
  top of the notebook first.
- **`ModuleNotFoundError: No module named 'lab04_weather'`** in the last cell —
  the notebook and the file must be in the same folder, and the build cell has to
  have run first. Open the `lab04` folder itself, not the folder above it.
- **The check cell still prints `None`** — that task cell was never run, or its
  placeholder `return None` is still underneath your code. Run the task cell,
  then the build cell, then the check.
- **Task 3 says the raw data is gone** — your function changed the list it was
  handed. Giving a list a second name does not copy it.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
