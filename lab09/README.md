# Lab 9: Hours of Daylight

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

How many hours of daylight does Atlanta get on each day of the year, and how
does that compare with Anchorage, far to the north, or Sydney, in the southern
hemisphere? Compute a whole year at once with NumPy arrays, find when the days
change fastest, and plot all three cities in one figure.

Everything in this lab comes from **§6.1** and **§6.2**: NumPy arrays,
`linspace` and `zeros`, vectorized functions, and plotting with Matplotlib.

**Due at the end of lab, Friday October 23.**

---

## Step 1 — Get this week's lab

From inside your `math170-yourname` folder:

```
git pull upstream main
```

The `lab09` folder appears, with two files: `lab09.ipynb` and
`lab09_daylight.py`. Your earlier work is untouched — Git only brings across
what is new.

**`git pull` says you are not in a repository?** You are in the wrong folder.
`cd` into `math170-yourname` first.

**`git pull` says "Need to specify how to reconcile divergent branches"?** Run
this once, then pull again:

```
git config --global pull.rebase false
git pull upstream main
```

If an editor opens asking for a merge message, save and close it.

---

## Step 2 — Work through the notebook

Open `lab09/lab09.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab09` folder. Run the first code cell before anything else; it prints the
folder the notebook is working in, which must be `lab09`.

There are four tasks. Tasks 1, 2 and 4 have the `def` line given. **In Task 3
you write the whole function**, `def` line included — use exactly the name the
task gives. Run the TEST cell after each task.

---

## Step 3 — Build `lab09_daylight.py`

Near the end of the notebook there is a **build cell**: run it, and it collects
the four functions you wrote and writes them into `lab09_daylight.py` in this
folder. Then run the **check cell** after it.

**That file is what gets graded**, not the notebook. If you change an answer
later, fix it in the task cell and run the build cell again.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab09/lab09_daylight.py
git commit -m "Complete Lab 9"
git push
```

`git status` will also list the `.png` images the notebook saved. They stay on
your laptop, together with your notebook. Stage the one file Gradescope needs,
by name. **Avoid `git add .`** — it sweeps in everything else sitting in the
folder, and anything you push is in your repository's history for good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab09/lab09_daylight.py` is
there with your code in it. Gradescope reads your repository, so if the file is
not on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 09 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab09_daylight.py` directly instead. That
works just as well.

You may resubmit as many times as you like. The last one counts.

---

## Grading

This lab is graded on **completion**, not correctness.

- **Each of the four tasks is worth 25 points**, earned by doing real work on it.
  Your answer does not have to be right.
- A task left exactly as the starter wrote it — or, in Task 3, a function that is
  not in the file under its exact name — earns nothing for that task.
- A file that does not run, or no file at all, earns **0** overall.
- Gradescope shows which checks passed and which failed so you can see what to
  fix. Those checks do not change your score.

Attendance in lab is required in order to submit — sign the attendance sheet.

---

## If something breaks

- **`TypeError: only 0-dimensional arrays can be converted to Python scalars`**
  — a function from `math` was given an array. Use the one from `numpy`.
- **`NameError: name 'np' is not defined`** in the check cell, or on
  Gradescope — the file starts with `import numpy as np` and
  `import matplotlib.pyplot as plt` and nothing else. Write `np.sin`, not
  `sin` after a `from numpy import ...` line of your own.
- **Your hours of daylight come out `nan`** — `np.arccos` was given a number
  bigger than 1. Did you turn both angles from degrees into radians?
- **Summer and winter are swapped** — check the minus sign inside `arccos`.
- **The image file is blank** — `plt.savefig` was called after `plt.show()`.
  Save first, then show.
- **No legend appears** — each curve needs a `label=...` in its `plt.plot`, and
  then one call to `plt.legend()`.
- **The build cell says `MISSING daily_change`** — the function is not defined
  under that exact name. Check the spelling on your `def` line, run that cell,
  then run the build cell again.
- **`ModuleNotFoundError: No module named 'lab09_daylight'`** — the notebook and
  `lab09_daylight.py` must be in the same folder, and you must run from inside
  `lab09`.
- **`git pull` stops with "Your local changes ... would be overwritten"** — a
  file you edited was also changed in the course repository. Ask me before doing
  anything else.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
