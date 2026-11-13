# Lab 11: Morse Code

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

Read the Morse code from a file into a dictionary, turn text into dots and
dashes, flip the dictionary around, and turn Morse back into text — then decode
a message from me.

Everything in this lab comes from **§7.1**, **§7.3** and **§7.4**: dictionaries,
reading a file into a dictionary, and taking strings apart and putting them back
together.

**Due at the end of lab, Friday November 6.**

---

## Step 1 — Get this week's lab

From inside your `math170-yourname` folder:

```
git pull upstream main
```

The `lab11` folder appears, with three files: `lab11.ipynb`, `lab11_morse.py`
and the data file `morse_code.txt`. Your earlier work is untouched — Git only
brings across what is new.

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

Open `lab11/lab11.ipynb` — in VS Code, or with `jupyter notebook` from inside
the `lab11` folder. Run the first code cell before anything else; it prints the
folder the notebook is working in, which must be `lab11`, and checks that
`morse_code.txt` is there.

There are four tasks, each with its `def` line and docstring given — fill in
the body, and leave the `def` line as it is. Run the TEST cell after each task.
The cell that decodes my message is already written for you: just run it.

---

## Step 3 — Build `lab11_morse.py`

Near the end of the notebook there is a **build cell**: run it, and it collects
the four functions you wrote and writes them into `lab11_morse.py` in this
folder. Then run the **check cell** after it.

**That file is what gets graded**, not the notebook. If you change an answer
later, fix it in the task cell and run the build cell again.

---

## Step 4 — Push it to your own repository

From inside `math170-yourname`:

```
git status
git add lab11/lab11_morse.py
git commit -m "Complete Lab 11"
git push
```

`git status` will also list your notebook, `lab11.ipynb`, as modified. It stays
on your laptop. Stage the one file Gradescope needs, by name. **Avoid
`git add .`** — it sweeps in everything else sitting in the folder, and
anything you push is in your repository's history for good.

This goes to `origin`, your repository. (`upstream` is the course repository —
you pull from it, you never push to it.)

Refresh your repository on GitHub and check that `lab11/lab11_morse.py` is there
with your code in it. Gradescope reads your repository, so if the file is not
on GitHub there is nothing to grade.

**Pushing is not submitting.**

---

## Step 5 — Submit on Gradescope

Open **gradescope.com directly in your browser** — **not through Canvas**, or
the GitHub connection will be refused.

**MATH 170 → Lab 11 → Submit**, then choose **GitHub**, your repository
`math170-yourname`, and the `main` branch.

Gradescope takes a **snapshot** at that moment. Push more work afterwards and you
must submit again — pushing alone changes nothing on Gradescope.

If GitHub will not connect, upload `lab11_morse.py` directly instead. That works
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

- **`ValueError: too many values to unpack` in `read_code`** — the comment line
  at the top of the file has many words. Skip it.
- **Codes like `'.-\n'`** — the newline at the end of each line is still
  attached. Use `split()` with no argument, or `strip()`.
- **`KeyError: 'h'` in `encode`** — the dictionary has capital letters only.
  Use `upper()` first.
- **`KeyError: ' '` in `encode`, or `KeyError: '/'` in `decode`** — a space
  between words is written `/` in Morse. Handle it before you look anything up.
- **`RuntimeError: dictionary changed size during iteration` in `invert`** —
  build a new dictionary instead of adding keys to the one you are looping over.
- **`NameError` in the check cell, or on Gradescope** — the function uses
  something you made outside it in the notebook. The build cell copies functions
  only. Move it inside the function, run its cell, then the build cell again.
- **The build cell says `MISSING ...`** — that function is not defined under
  its exact name. Put the `def` line back as it was given, run that cell, then
  run the build cell again.
- **`FileNotFoundError: ... morse_code.txt`** — the notebook is not running
  from inside `lab11`. Close it and open it again from that folder.
- **`ModuleNotFoundError: No module named 'lab11_morse'`** — the notebook and
  `lab11_morse.py` must be in the same folder, and you must run from inside
  `lab11`.
- **`git pull` stops with "Your local changes ... would be overwritten"** — a
  file you edited was also changed in the course repository. Ask me before doing
  anything else.
- **`Permission denied` when pushing** — you are pushing to the course
  repository. Run `git remote -v`; `origin` should be *your* repository.
- **Gradescope will not connect to GitHub** — you opened it through Canvas. Open
  gradescope.com directly.
