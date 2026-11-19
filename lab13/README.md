# Lab 13: How Fast Are the Days Getting Shorter?

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

Grow the family of classes for numerical differentiation from lecture: one
method that every member inherits, a new member that looks one step back, a
member built on top of `Central2`, and a test for the whole family. Then hand
the family Lab 9's hours of daylight in Atlanta and find out how fast the days
are getting shorter.

Everything in this lab comes from **§9.1–9.2**: class hierarchies and
inheritance, `super()`, and classes for numerical differentiation, together with
`__call__` and test functions from Chapter 8.

**Due at the end of lab, Friday November 20.**

---

## Step 1 — Get this week's lab

From inside your `math170-yourname` folder:

```
git pull upstream main
```

The `lab13` folder appears, with two files: `lab13.ipynb` and
`lab13_daylight.py`. Your earlier work is untouched — Git only brings across
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

Open `lab13/lab13.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab13` folder. Run the first code cell before anything else; it prints the
folder the notebook is working in, which must be `lab13`.

There are four tasks. In each one the `class` line, the `def` lines and the
docstrings are given — fill in the body of each method, and leave those lines
as they are. After you change a class, run its cell again, then its TEST cell.

A subclass keeps the base class it was made from: if you change `Diff` (Task 1)
and run its cell again, run the `Backward1` and `Richardson` cells again too.

The cell after Task 4 puts the family to work on the hours of daylight in
Atlanta and is already written for you: just run it.

---

## Step 3 — Build `lab13_daylight.py`

Near the end of the notebook there is a **build cell**: run it, and it collects
your classes and your test function and writes them into `lab13_daylight.py` in
this folder. Then run the **check cell** after it.

**That file is what gets graded**, not the notebook. If you change an answer
later, fix it in the task cell and run the build cell again.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab13/lab13_daylight.py
git commit -m "Complete Lab 13"
git push
```

`git status` will also list your notebook, `lab13.ipynb`, as modified. It stays
on your laptop. Stage the one file Gradescope needs, by name. **Avoid
`git add .`** — it sweeps in everything else sitting in the folder, and
anything you push is in your repository's history for good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab13/lab13_daylight.py` is
there with your code in it. Gradescope reads your repository, so if the file is
not on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 13 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab13_daylight.py` directly instead. That
works just as well.

You may resubmit as many times as you like. The last one counts.

---

## Grading

This lab is graded on **completion**, not correctness.

- **Each of the four tasks is worth 25 points**, earned by doing real work on it.
  Your answer does not have to be right.
- A task left exactly as the starter wrote it — or a class or function whose
  name was changed — earns nothing for that task. `Forward1` and `Central2` come
  with the lab and are not graded.
- A file that does not run, or no file at all, earns **0** overall.
- Gradescope shows which checks passed and which failed so you can see what to
  fix. Those checks do not change your score.

Attendance in lab is required in order to submit — sign the attendance sheet.

---

## If something breaks

- **A TEST cell says the class "was made from an older `Diff`"** — you ran the
  Task 1 cell again after making `Backward1` or `Richardson`. Run their cells
  again, then the TEST cell.
- **`RecursionError` in `Richardson`** — `self(x)` inside `__call__` calls
  Richardson's own `__call__` again, forever. Central2's is
  `super().__call__(x)`.
- **`NameError: name 'f' is not defined`** (or `h`) inside a method — `f` and
  `h` are attributes: `self.f`, `self.h`. Or copy them first, as `Forward1`
  does: `f, h = self.f, self.h`.
- **`TypeError: 'Diff' object is not callable`** — `values` was used on a plain
  `Diff`, which has no `__call__`. Use it on a `Forward1`, a `Backward1`, ...
- **`TypeError: ... takes 1 positional argument but 2 were given`** — a `def`
  line lost its `self`. Put the line back as it was given.
- **You fixed a class, but nothing changed** — run the class cell again. An
  object keeps the class it was made from, so make new objects after that.
- **The build cell says `partly done` or `unfinished`** — a method still has
  the line `# TODO: your code here`. Delete it, run that cell, then the build
  cell again.
- **The build cell says `MISSING ...`** — that class or function is not defined
  under its exact name. Put the `class` or `def` line back as it was given, run
  that cell, then run the build cell again.
- **`NameError` in the check cell, or on Gradescope** — a class or your test
  uses something you made outside it in the notebook. The build cell copies the
  classes and the test function only. Move it inside, run its cell, then the
  build cell again.
- **`ModuleNotFoundError: No module named 'lab13_daylight'`** — the notebook and
  `lab13_daylight.py` must be in the same folder, and you must run from inside
  `lab13`.
- **`git pull` stops with "Your local changes ... would be overwritten"** — a
  file you edited was also changed in the course repository. Ask me before doing
  anything else.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
