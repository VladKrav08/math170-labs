# Lab 10: Heat in a Metal Rod

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

The middle of a metal rod is heated to 100 °C with a torch, and then left to
cool while its two ends stay at room temperature. Follow the temperature at
every point of the rod, step by step, keep the whole history in one
two-dimensional array, measure the stretch that is too hot to touch, and watch
it all as a movie.

Everything in this lab comes from **§6.3**, **§6.4** and **§6.5**: piecewise
functions with `np.where`, slicing and copying arrays, two-dimensional arrays,
Boolean indexing — and the movie is made with `FuncAnimation`.

**Due at the end of lab, Friday October 30.**

---

## Step 1 — Get this week's lab

From inside your `math170-yourname` folder:

```
git pull upstream main
```

The `lab10` folder appears, with two files: `lab10.ipynb` and `lab10_rod.py`.
Your earlier work is untouched — Git only brings across what is new.

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

Open `lab10/lab10.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab10` folder. Run the first code cell before anything else; it prints the
folder the notebook is working in, which must be `lab10`.

There are four tasks, each with its `def` line and docstring given — fill in
the body, and leave the `def` line as it is. Run the TEST cell after each task.
The movie at the end is already written for you: just run it.

---

## Step 3 — Build `lab10_rod.py`

Near the end of the notebook there is a **build cell**: run it, and it collects
the four functions you wrote and writes them into `lab10_rod.py` in this
folder. Then run the **check cell** after it.

**That file is what gets graded**, not the notebook. If you change an answer
later, fix it in the task cell and run the build cell again.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab10/lab10_rod.py
git commit -m "Complete Lab 10"
git push
```

`git status` will also list `rod.gif`, the movie the notebook saved. It stays on
your laptop, together with your notebook. Stage the one file Gradescope needs,
by name. **Avoid `git add .`** — it sweeps in everything else sitting in the
folder, and anything you push is in your repository's history for good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab10/lab10_rod.py` is there
with your code in it. Gradescope reads your repository, so if the file is not
on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 10 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab10_rod.py` directly instead. That works
just as well.

You may resubmit as many times as you like. The last one counts.

---

## Grading

This lab is graded on **completion**, not correctness.

- **Each of the four tasks is worth 25 points**, earned by doing real work on it.
  Your answer does not have to be right.
- A task left exactly as the starter wrote it — or a function whose `def` line
  was renamed — earns nothing for that task.
- A file that does not run, or no file at all, earns **0** overall.
- Gradescope shows which checks passed and which failed so you can see what to
  fix. Those checks do not change your score.

Attendance in lab is required in order to submit — sign the attendance sheet.

---

## If something breaks

- **`ValueError: The truth value of an array with more than one element is
  ambiguous`** — an `if`-test was given an array. Use `np.where` instead.
- **`step` gives the right numbers but changes `u` too** — `new = u` does not
  make a new array; it gives the same array a second name. Use `u.copy()`.
- **The rows of `simulate` come out one too few** — `steps` steps give
  `steps + 1` rows: the start, and one row per step.
- **`IndexError` in `hot_zone`** — no point was hotter than the threshold, so
  there is no first one. Check how many there are before you look.
- **`NameError: name 'np' is not defined`** — the file starts with
  `import numpy as np` and nothing else. Write `np.` in front of everything you
  use from NumPy.
- **The build cell says `MISSING ...`** — that function is not defined under
  its exact name. Put the `def` line back as it was given, run that cell, then
  run the build cell again.
- **`ModuleNotFoundError: No module named 'lab10_rod'`** — the notebook and
  `lab10_rod.py` must be in the same folder, and you must run from inside
  `lab10`.
- **`git pull` stops with "Your local changes ... would be overwritten"** — a
  file you edited was also changed in the course repository. Ask me before doing
  anything else.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
