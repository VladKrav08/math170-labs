# Lab 12: A Thanksgiving Kitchen

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

Write three small classes for the kitchen — a turkey thawing in the fridge, a
pitcher of sweet tea, and a meat thermometer that corrects its own readings —
and a test function that catches a broken thermometer.

Everything in this lab comes from **§8.1–8.5**: writing a class with a
constructor and methods, protected attributes, the special methods `__add__`
and `__call__`, and test functions for classes.

**Due at the end of lab, Friday November 13.**

---

## Step 1 — Get this week's lab

From inside your `math170-yourname` folder:

```
git pull upstream main
```

The `lab12` folder appears, with two files: `lab12.ipynb` and
`lab12_kitchen.py`. Your earlier work is untouched — Git only brings across
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

Open `lab12/lab12.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab12` folder. Run the first code cell before anything else; it prints the
folder the notebook is working in, which must be `lab12`.

There are four tasks. In each one the `class` line, the `def` lines and the
docstrings are given — fill in the body of each method, and leave those lines
as they are. After you change a class, run its cell again, then its TEST cell.
The last cell before Submitting puts your three classes to work and is already
written for you: just run it.

---

## Step 3 — Build `lab12_kitchen.py`

Near the end of the notebook there is a **build cell**: run it, and it collects
your three classes and your test function and writes them into
`lab12_kitchen.py` in this folder. Then run the **check cell** after it.

**That file is what gets graded**, not the notebook. If you change an answer
later, fix it in the task cell and run the build cell again.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab12/lab12_kitchen.py
git commit -m "Complete Lab 12"
git push
```

`git status` will also list your notebook, `lab12.ipynb`, as modified. It stays
on your laptop. Stage the one file Gradescope needs, by name. **Avoid
`git add .`** — it sweeps in everything else sitting in the folder, and
anything you push is in your repository's history for good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab12/lab12_kitchen.py` is
there with your code in it. Gradescope reads your repository, so if the file is
not on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 12 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab12_kitchen.py` directly instead. That
works just as well.

You may resubmit as many times as you like. The last one counts.

---

## Grading

This lab is graded on **completion**, not correctness.

- **Each of the four tasks is worth 25 points**, earned by doing real work on it.
  Your answer does not have to be right.
- A task left exactly as the starter wrote it — or a class or function whose
  name was changed — earns nothing for that task.
- A file that does not run, or no file at all, earns **0** overall.
- Gradescope shows which checks passed and which failed so you can see what to
  fix. Those checks do not change your score.

Attendance in lab is required in order to submit — sign the attendance sheet.

---

## If something breaks

- **`NameError: name 'pounds' is not defined`** (or `_slope`, `_cups`, ...)
  inside a method — an attribute needs `self.` in front: `self._pounds`.
- **`AttributeError: 'Turkey' object has no attribute '_hours'`** — every
  attribute must be made in the constructor, `__init__`. Check the spelling and
  the underscore.
- **`TypeError: unsupported operand type(s) for +: 'Pitcher' and 'Pitcher'`** —
  `p1 + p2` needs a method called `__add__`, with two underscores on each side.
- **`TypeError: 'Thermometer' object is not callable`** — `probe(160)` needs a
  method called `__call__`, with two underscores on each side.
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
- **`NameError` in the check cell, or on Gradescope** — a class uses something
  you made outside it in the notebook. The build cell copies the classes and the
  test function only. Move it inside, run its cell, then the build cell again.
- **`ModuleNotFoundError: No module named 'lab12_kitchen'`** — the notebook and
  `lab12_kitchen.py` must be in the same folder, and you must run from inside
  `lab12`.
- **`git pull` stops with "Your local changes ... would be overwritten"** — a
  file you edited was also changed in the course repository. Ask me before doing
  anything else.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
