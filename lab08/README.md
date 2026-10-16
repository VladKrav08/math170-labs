# Lab 8: Measuring g with a Pendulum

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

A physics section timed a pendulum and typed their measurements into a shared
sheet, `pendulum_data.txt`. Some lines are wrong. Compute $g$ from every line
that makes sense, report every line that does not, and keep going past the bad
ones. Then write a test that checks your code refuses nonsense.

Everything in this lab comes from **§5.5**: `try` and `except`, catching a named
error, `except ... as e`, catching more than one kind of error, and `raise`.

**Due at the end of lab, Friday October 16.**

---

## Step 1 — Get this week's lab

From inside your `math170-yourname` folder:

```
git pull upstream main
```

The `lab08` folder appears, with three files: `lab08.ipynb`,
`lab08_pendulum.py` and `pendulum_data.txt`. Your earlier work is untouched —
Git only brings across what is new.

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

Open `lab08/lab08.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab08` folder. Run the first code cell before anything else; it prints the
folder the notebook is working in, which must be `lab08`.

There are four tasks. Tasks 1–3 have the `def` line given. **Task 4 is a test
function, and you write the whole function**, `def` line included — use exactly
the name the task gives. Run the TEST cell after each task.

---

## Step 3 — Build `lab08_pendulum.py`

Near the end of the notebook there is a **build cell**: run it, and it collects
the four functions you wrote and writes them into `lab08_pendulum.py` in this
folder. Then run the **check cell** after it, and `pytest`.

**That file is what gets graded**, not the notebook. If you change an answer
later, fix it in the task cell and run the build cell again.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab08/lab08_pendulum.py
git commit -m "Complete Lab 8"
git push
```

`git status` will also list `check_sheet.txt`, which a TEST cell wrote. It stays
on your laptop, together with your notebook. Stage the one file Gradescope
needs, by name. **Avoid `git add .`** — it sweeps in everything else sitting in
the folder, and anything you push is in your repository's history for good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab08/lab08_pendulum.py` is
there with your code in it. Gradescope reads your repository, so if the file is
not on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 08 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab08_pendulum.py` directly instead. That
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
  fix. For Task 4 the checks run *your* test against a correct and three broken
  versions of `g_from`. Those checks do not change your score.

Attendance in lab is required in order to submit — sign the attendance sheet.

---

## If something breaks

- **`FileNotFoundError: ... 'pendulum_data.txt'`** — the notebook is not running
  in the `lab08` folder. The first code cell prints where it is running; open the
  notebook again from inside `lab08`.
- **`ZeroDivisionError` in Task 3** — a period of 0 reached the formula. Task 1
  is supposed to refuse it first.
- **Task 3 stops at the first bad line** — your `except` does not catch every
  kind of error that `parse_line` and `g_from` can raise.
- **Your message has a stray `"` on the next line** — the `'\n'` from the end of
  the line is inside it. Use `line.strip()`.
- **Your test lets a broken `g_from` through, and it uses `except:`** — a bare
  `except:` also catches the `AssertionError` from your own `assert`. Name the
  error you expect.
- **The build cell says `MISSING test_g_from`** — the function is not defined
  under that exact name. Check the spelling on your `def` line, run that cell,
  then run the build cell again.
- **`ModuleNotFoundError: No module named 'lab08_pendulum'`** — the notebook and
  `lab08_pendulum.py` must be in the same folder, and you must run from inside
  `lab08`.
- **`No module named pytest`** — run `%pip install pytest` in a new cell of the
  notebook, then try again.
- **`git pull` stops with "Your local changes ... would be overwritten"** — a
  file you edited was also changed in the course repository. Ask me before doing
  anything else.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
