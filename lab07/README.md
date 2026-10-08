# Lab 7: A Cooling Cup of Coffee

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

A thermometer logger left in a mug of coffee saved its readings in a file.
Read the file into Python, write a table that compares the measurements with
a model, keep a logbook of runs — and write a test for your file reader.

Everything in this lab comes from **§5.3 and §5.4**: `open`, `with`, looping
over a file, `readline`, `split` with a separator, negative indices, `write`,
`'\n'`, and `'w'` versus `'a'`.

**This lab is online. Due Friday October 9, 9:00 pm.** If you want help, I am
on Zoom (link in the syllabus) during lab time, Friday 11:30–12:20 — join if you
like.

---

## Step 1 — Get this week's lab

From inside your `math170-yourname` folder:

```
git pull upstream main
```

The `lab07` folder appears, with three files: `lab07.ipynb`, `lab07_coffee.py`
and `coffee_log.txt`. Your earlier work is untouched — Git only brings across
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

Open `lab07/lab07.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab07` folder. Run the first code cell before anything else; it prints the
folder the notebook is working in, which must be `lab07`.

There are four tasks. Tasks 1–3 have the `def` line given. **Task 4 is a test
function, and you write the whole function**, `def` line included — use exactly
the name the task gives. Run the TEST cell after each task.

**Never open `coffee_log.txt` for writing.** That is the data.

---

## Step 3 — Build `lab07_coffee.py`

Near the end of the notebook there is a **build cell**: run it, and it collects
the four functions you wrote and writes them into `lab07_coffee.py` in this
folder. Then run the **check cell** after it, and `pytest`.

**That file is what gets graded**, not the notebook. If you change an answer
later, fix it in the task cell and run the build cell again.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab07/lab07_coffee.py
git commit -m "Complete Lab 7"
git push
```

`git status` will list several new `.txt` files — `coffee_table.txt`,
`logbook.txt`, the `check_` files, your test's small log. Your code wrote them.
They stay on your laptop, together with your notebook. Stage the one file
Gradescope needs, by name. **Avoid `git add .`** — it sweeps in everything else
sitting in the folder, and anything you push is in your repository's history for
good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab07/lab07_coffee.py` is
there with your code in it. Gradescope reads your repository, so if the file is
not on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 07 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab07_coffee.py` directly instead. That
works just as well.

You may resubmit as many times as you like until 9:00 pm. The last one counts.

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
  versions of `read_log`. Those checks do not change your score.

---

## If something breaks

- **`FileNotFoundError: ... 'coffee_log.txt'`** — the notebook is not running in
  the `lab07` folder. The first code cell prints where it is running; open the
  notebook again from inside `lab07`.
- **`coffee_log.txt` is empty or wrong** — something opened it with `'w'`. Get
  the original back from inside `math170-yourname`:
  `git restore lab07/coffee_log.txt`
- **`ValueError: could not convert string to float`** in Task 1 — a line that is
  not a reading reached `float`. Which one? The error message quotes it.
- **`TypeError: write() argument must be str, not float`** — `write` only takes
  strings. Build the line with an f-string first.
- **Your table, or your logbook, is all on one line** — `write` does not add a
  line break. You do.
- **Your logbook keeps only the last run** — the file is opened in a mode that
  erases it.
- **The build cell says `MISSING test_read_log`** — the function is not defined
  under that exact name. Check the spelling on your `def` line, run that cell,
  then run the build cell again.
- **`ModuleNotFoundError: No module named 'lab07_coffee'`** — the notebook and
  `lab07_coffee.py` must be in the same folder, and you must run from inside
  `lab07`.
- **`No module named pytest`** — run `%pip install pytest` in a new cell of the
  notebook, then try again. (Anaconda normally includes it.)
- **`git pull` stops with "Your local changes ... would be overwritten"** — a
  file you edited was also changed in the course repository. Ask me (Zoom during lab
  time, or email) before doing anything else.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
