# Lab 5: Curving a Quiz

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

Twelve made-up students, one 20-point quiz, and an instructor wondering whether
to curve it. Turn points into percentages and percentages into letters, write a
function that applies *any* curve you hand it, find the lowest and highest
score, and build the square-root curve with a `lambda`.

Everything in this lab comes from **§4.1–4.5**: defining and calling functions,
local and global variables, keyword and default arguments, returning more than
one value, `if`/`elif`/`else`, and functions as arguments to functions.

---

## Step 1 — Get this week's lab

From inside your `math170-yourname` folder:

```
git pull upstream main
```

The `lab05` folder appears. Your earlier work is untouched — Git only brings
across what is new.

**`git pull` says you are not in a repository?** You are in the wrong folder.
`cd` into `math170-yourname` first.

**`git pull` says "Need to specify how to reconcile divergent branches"?** Your
repository has your own commits from earlier labs, and the course repository
has new ones. Tell Git to combine them — once per computer — and pull again:

```
git config --global pull.rebase false
git pull upstream main
```

If an editor opens asking for a merge message, save and close it. (Lab 1's
README now includes this line in its Git setup step.)

---

## Step 2 — Work through the notebook

Open `lab05/lab05.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab05` folder. Run the data cell at the top first.

There are five tasks. **New this week:** in Tasks 1 and 5 you write the whole
function yourself, `def` line included — use exactly the name the task gives.
In Tasks 2–4 the `def` line and doc string are given and you write the lines
underneath. Run the TEST cell after each task to see how you did.

---

## Step 3 — Build `lab05_grades.py`

Near the end of the notebook there is a **build cell**: run it, and it collects
the five functions you wrote and writes them into `lab05_grades.py` in this
folder. Then run the **check cell** after it.

**That file is what gets graded**, not the notebook. Run every task cell first,
so all five functions exist. If you change an answer later, fix it in the task
cell and run the build cell again — the file is rewritten each time.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab05/lab05_grades.py
git commit -m "Complete Lab 5"
git push
```

Check `git status` first, then stage the one file Gradescope needs, by name.
Your notebook stays on your laptop. **Avoid `git add .`** — it sweeps in
everything else sitting in the folder, and anything you push is in your
repository's history for good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab05/lab05_grades.py` is
there with your code in it. Gradescope reads your repository, so if the file is
not on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 05 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab05_grades.py` directly instead. That
works just as well.

You may resubmit as many times as you like. The last one counts.

---

## Grading

This lab is graded on **completion**, not correctness.

- **Each of the five tasks is worth 20 points**, earned by doing real work on it.
  Your answer does not have to be right.
- A task left exactly as the starter wrote it — or, in Tasks 1 and 5, a function
  that is not in the file under its exact name — earns nothing for that task.
- A file that does not run, or no file at all, earns **0** overall.
- Gradescope shows which checks passed and which failed so you can see what to
  fix. Those checks do not change your score.

So if a check is red and lab is over, submit anyway.

---

## If something breaks

- **`NameError: name 'points' is not defined`** — run the data cell at the top
  of the notebook first.
- **The build cell says `MISSING percent`** (or `root_curve`) — the function is
  not defined under that exact name. Check the spelling on your `def` line, run
  that cell, then run the build cell again.
- **`AttributeError: module 'lab05_grades' has no attribute ...`** in the check
  cell — same cause: that function never made it into the file. Fix the name,
  run its cell, run the build cell, run the check again.
- **`ModuleNotFoundError: No module named 'lab05_grades'`** in the last cell —
  the notebook and the file must be in the same folder. Open the `lab05` folder
  itself, not the folder above it.
- **`percent() missing 1 required positional argument: 'out_of'`** — `out_of`
  needs a default value in the `def` line.
- **The check cell prints `None`** — that task cell was never run, or its
  placeholder `return None` is still underneath your code.
- **`git pull` stops with "Your local changes ... would be overwritten"** — a
  file you edited was also changed in the course repository. Ask in lab before
  doing anything else.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
