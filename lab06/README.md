# Lab 6: A Table for Any Formula

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

Build a program that prints a table of values for any formula you type after
its name on the command line — and write a test that checks it.

```text
python tabulate.py "20*x - 4.9*x**2" 0 4 8
```

Everything in this lab comes from **§4.7, §5.1 and §5.2**: test functions with
`assert`, comparing floats with a tolerance, `pytest`, command line arguments in
`sys.argv`, and turning a string into code with `eval`.

---

## Step 1 — Get this week's lab

From inside your `math170-yourname` folder:

```
git pull upstream main
```

The `lab06` folder appears, with three files: `lab06.ipynb`, `lab06_table.py`
and `tabulate.py`. Your earlier work is untouched — Git only brings across what
is new.

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

Open `lab06/lab06.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab06` folder. Run the first code cell before anything else.

There are four tasks. Tasks 1–3 build the program; the `def` line is given.
**Task 4 is a test function, and you write the whole function**, `def` line
included — use exactly the name the task gives. Run the TEST cell after
each task.

---

## Step 3 — Build `lab06_table.py`, then run it

Near the end of the notebook there is a **build cell**: run it, and it collects
the four functions you wrote and writes them into `lab06_table.py` in this
folder. Then run the **check cell** after it.

**That file is what gets graded**, not the notebook. If you change an answer
later, fix it in the task cell and run the build cell again.

The notebook then has you run your file two ways: your test with `pytest`, and
the program `tabulate.py`, which uses your functions. Do not edit `tabulate.py`.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab06/lab06_table.py
git commit -m "Complete Lab 6"
git push
```

Check `git status` first, then stage the one file Gradescope needs, by name.
Your notebook — and the `.pytest_cache` folder `pytest` creates — stay on your
laptop. **Avoid `git add .`** — it sweeps in everything else sitting in the
folder, and anything you push is in your repository's history for good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab06/lab06_table.py` is
there with your code in it. Gradescope reads your repository, so if the file is
not on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 06 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab06_table.py` directly instead. That
works just as well.

You may resubmit as many times as you like. The last one counts.

---

## Grading

This lab is graded on **completion**, not correctness.

- **Each of the four tasks is worth 25 points**, earned by doing real work on it.
  Your answer does not have to be right.
- A task left exactly as the starter wrote it — or, in Task 4, a function that is
  not in the file under its exact name — earns nothing for that task.
- A file that does not run, or no file at all, earns **0** overall.
- Gradescope shows which checks passed and which failed so you can see what to
  fix. For Task 4 the checks run *your* test against a correct and two broken
  versions of `make_function`. Those checks do not change your score.

So if a check is red and lab is over, submit anyway.

---

## If something breaks

- **`NameError: name 'sin' is not defined`** (or `pi`, `exp`, ...) — run the
  first code cell of the notebook, the one with `from math import *`.
- **`NameError: name 'x' is not defined`** in Task 2 — `eval` computed the
  formula instead of building a function. Reread the task.
- **The build cell says `MISSING test_make_function`** — the
  function is not defined under that exact name. Check the spelling on your
  `def` line, run that cell, then run the build cell again.
- **`AttributeError: module 'lab06_table' has no attribute ...`** in the check
  cell — same cause: that function never made it into the file.
- **`ModuleNotFoundError: No module named 'lab06_table'`** — from the check cell
  or from `tabulate.py`: the notebook, `tabulate.py` and `lab06_table.py` must
  all be in the same folder, and you must run from inside `lab06`.
- **`No module named pytest`** — run `%pip install pytest` in a new cell of the
  notebook, then try again. (Anaconda normally includes it.)
- **`zsh: no matches found`** in the Mac terminal — the formula is not in
  quotes. Write `"x**2"`, not `x**2`.
- **`git pull` stops with "Your local changes ... would be overwritten"** — a
  file you edited was also changed in the course repository. Ask in lab before
  doing anything else.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
