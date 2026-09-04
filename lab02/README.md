# Lab 2: Caffeine in the Bloodstream

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

The first lab you write yourself. Everything in it comes from **Chapter 2** —
formulas, variables and types, formatted output, and the `math` module.

You drink a cold brew at 3 pm. At 11 pm you are wide awake. How much of it is
still in you? By the end of the hour Python will answer that.

---

## Step 1 — Get this week's lab

You already have a `math170-yourname` folder from Lab 1. From inside it:

```
git pull upstream main
```

The `lab02` folder appears. Your Lab 1 work is untouched — Git only brings
across what is new.

**`git pull` says you are not in a repository?** You are in the wrong folder.
`cd` into `math170-yourname` first.

---

## Step 2 — Work through the notebook

Open `lab02/lab02.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab02` folder.

There are five tasks — four graded, plus an optional fifth. Each gives you a
`def` line and a docstring; you write the lines underneath. Run the TEST cell
after each task to see how you did.

We have not covered functions yet — that is Chapter 4 — so the notebook explains
what those `def` lines are doing. You are only filling in formulas.

---

## Step 3 — Build `lab02_caffeine.py`

Near the end of the notebook there is a **build cell**: run it, and it collects
the five functions you wrote and writes them into `lab02_caffeine.py` in this
folder. Then run the **check cell** after it.

**That file is what gets graded**, not the notebook. Run every task cell first,
so all five functions exist. If you change an answer later, fix it in the task
cell and run the build cell again — the file is rewritten each time.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab02/lab02_caffeine.py
git commit -m "Complete Lab 2"
git push
```

Check `git status` first, then stage the one file Gradescope needs, by name.
Your notebook stays on your laptop. **Avoid `git add .`** — it sweeps in
everything else sitting in the folder, and anything you push is in your
repository's history for good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab02/lab02_caffeine.py` is
there with your code in it. Gradescope reads your repository, so if the file is
not on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 02 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab02_caffeine.py` directly instead. That
works just as well.

You may resubmit as many times as you like. The last one counts.

---

## Grading

This lab is graded on **completion**, not correctness.

- **Tasks 1–4 are worth 25 points each**, earned by doing real work on the task.
  Your answer does not have to be right.
- **Task 5 is optional** and carries no points.
- A task left exactly as the starter wrote it earns nothing for that task, so an
  attempt beats a blank every time.
- A file that does not run, or no file at all, earns **0** overall.
- Gradescope shows which checks passed and which failed so you can see what to
  fix. Those checks do not change your score.

So if a check is red and lab is over, submit anyway.

---

## If something breaks

- **`ModuleNotFoundError: No module named 'lab02_caffeine'`** in the last cell —
  the notebook and the file must be in the same folder. Open the `lab02` folder
  itself, not the folder above it.
- **The check cell still prints `None`** — that task cell was never run, or its
  placeholder `return None` is still underneath your code. Run the task cell,
  then the build cell, then the check.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
