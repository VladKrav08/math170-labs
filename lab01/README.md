# Lab 1: Getting Set Up

**MATH 170 — Introduction to Scientific Computing**
**Fall 2026**

Today is about tools, not code. The point is that everything works before we
start writing programs next week.

**You are given the answer.** `calculator.py` in this folder is finished, working
code. You are not writing anything today. You are submitting a file we hand you,
so we can confirm the whole pipeline works for you specifically.

Work through the steps in order. `lab01.ipynb` picks up at Step 6.

---

## Step 1 — Create a GitHub account

Go to **github.com** and sign up.

- **Sign up using your Emory or personal email.** Both work for this course.

  *Keep in mind:* your access to `@emory.edu` ends after you graduate, while a
  personal address stays with you. Whichever you start with, you can add the
  other to your account later — so this is not a permanent choice.
- Pick a username you would not mind an employer seeing
- Verify the email — you cannot submit without it

Already have an account? Move on.

---

## Step 2 — Check Python

You installed Python through **Anaconda** in class. Confirm it works.

Open a terminal — **Terminal** on Mac, **Anaconda Prompt** on Windows (not
PowerShell: Anaconda does not put Python on the general Windows path) — and run:

```
python --version
```

**You should see** `Python 3.10` or higher. Anaconda ships its own Python; that
is the one you want.

**If instead you see** `command not found`, `is not recognized`, or the Microsoft
Store opens, Python is not on this terminal's path. On Windows, check that you
are in Anaconda Prompt rather than PowerShell. On Mac, close the terminal and
open a **new** one — the installer only affects sessions started after it ran.
If it still fails, ask.

**If you installed from python.org instead**, that works too. On Mac the command
is `python3 --version`.

---

## Step 3 — Check your editor

You installed **VS Code** in class. Two things to confirm:

1. Microsoft's **Python extension** is installed — click the squares icon in the
   left sidebar, search `Python`, install the one published by Microsoft. It
   brings notebook support with it, so you do not need a separate Jupyter
   extension.
2. The first time you run a notebook cell, VS Code asks which **kernel** to use.
   Choose the Anaconda Python from Step 2. If it offers to install `ipykernel`,
   say yes.

**Prefer Jupyter?** Anaconda already includes it — nothing to install. From
inside a lab folder:

```
jupyter notebook
```

It opens in your browser. To stop it, return to the terminal and press
<kbd>Ctrl</kbd>+<kbd>C</kbd> twice.

---

## Step 4 — Install and configure Git

Git is the tool that moves files between your computer and GitHub.

Check whether you already have it:

```
git --version
```

If not:

- **Mac:** run `xcode-select --install`
- **Windows:** download from **git-scm.com** and accept the defaults
- **Linux:** `sudo apt install git`

Then tell Git who you are. It stamps every save with this, so use the same email
as your GitHub account:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global pull.rebase false
```

The third line tells Git what to do when you pull new labs while your own
repository also has new commits: combine the two (a *merge*). Without it, a
recent Git refuses to pull and stops with *"Need to specify how to reconcile
divergent branches."*

You only do this once per computer.

---

## Step 5 — Get the labs, and set up your own repository

You will end up with **one folder** that pulls labs from the course repository
and pushes your work to your own.

### 5a. Create your repository on GitHub

On **github.com**, click **+** → **New repository**.

- Name it `math170-yourname`
- Set it to **Private**
- Leave everything else alone — do **not** add a README
- Click **Create repository**

Leave that page open; you will need the URL in a moment.

### 5b. Clone the course repository

In a terminal, move to wherever you keep your coursework, then:

```
git clone https://github.com/jimena-martin-emory/math170-labs.git math170-yourname
cd math170-yourname
```

This downloads every lab posted so far into a folder named after you.

### 5c. Point the folder at your own repository

Right now this folder is connected to the course repository. Give the course
repo the name `upstream` (you pull from it), and add your own as `origin` (you
push to it):

```
git remote rename origin upstream
git remote add origin https://github.com/YOURNAME/math170-yourname.git
git push -u origin main
```

Check it worked:

```
git remote -v
```

You should see `upstream` pointing at the course repository and `origin` at
yours. Refresh your repository page on GitHub — the lab files are now there.

**Why two?** `upstream` is where labs come from. `origin` is where your work
goes. You cannot push to the course repository, and you would not want to — your
work is yours.

### Each following week

```
git pull upstream main
```

The new lab folder appears. **Your finished work is not touched.** Git only
transfers what changed, and a new lab is a new folder — it has nothing to say
about the labs you have already done.

---

## Step 6 — Open the notebook and run the code

### What a notebook is

`lab01.ipynb` is a **Jupyter notebook** — a document made of *cells*. Some cells
are text (like this paragraph). Others are **code cells**: boxes of Python you
can run one at a time, with the result appearing right underneath.

Nothing runs on its own. You run each cell yourself, in order.

### Opening it

**In VS Code:** **File → Open Folder**, choose your `math170-yourname` folder,
then click `lab01/lab01.ipynb` in the sidebar on the left.

**In Jupyter:** in a terminal, move into the lab folder and start it:

```
cd math170-yourname/lab01
jupyter notebook
```

A page opens in your browser. Click `lab01.ipynb`.

*Tip for the `cd` line:* on Mac, type `cd ` (with a space) and then drag the
folder from Finder onto the terminal window — it fills in the path for you.

### Running a cell

1. Click once inside a code cell — it gets a border, showing it is selected
2. Press <kbd>Shift</kbd>+<kbd>Enter</kbd>

   (or click the small **▶** play button at the cell's left edge)
3. Output appears directly below the cell

The first time you do this, you will be asked to choose a **kernel** — this is
the notebook asking *which Python should I use?* Pick the Anaconda Python from
Step 2. If VS Code offers to install `ipykernel`, say yes.

While a cell is running you will see `[*]` next to it. When it finishes, that
becomes a number like `[1]` — which is just the order cells were run in.

### What you should see

Run the cells from top to bottom. The important one imports the calculator we
gave you and uses it:

```python
from calculator import Calculator

calc = Calculator()
print("1 + 1        =", calc.eval("1 + 1"))
```

Expected output:

```
1 + 1        = 2
(1 + 1) * 4  = 8
1 + 1 * 8    = 9
```

If you see those three numbers, Python is working on your machine and
`calculator.py` is where it should be. That is the whole goal of this step.

### If something goes wrong

**`ModuleNotFoundError: No module named 'calculator'`**
The notebook cannot find `calculator.py`. The two files must sit in the **same
folder**. Check that you opened the `lab01` folder itself, not the folder above
it.

**`NameError: name 'Calculator' is not defined`**
You skipped a cell, or ran them out of order. Cells depend on the ones above
them. Run everything from the top: in VS Code click **Run All**, in Jupyter use
**Kernel → Restart & Run All**.

**Nothing happens when you press Shift+Enter**
Make sure you clicked *inside* the cell first, and that you selected a kernel.

**A red error you do not recognise**
Read the last line of the message — it is usually the useful one — then ask.
Reading error messages is a skill you will use all semester, and today is a good
day to start.

---

## Step 7 — Save your work to GitHub

From inside your `math170-yourname` folder:

```
git status                              # see what changed
git add lab01/calculator.py             # stage the one file, by name
git commit -m "Complete Lab 1"          # save a snapshot
git push                                # send it to your repository
```

Stage files **by name**, never with `git add .` — that sweeps in everything
sitting in the folder, and anything you push stays in your repository's history.

Refresh your repository page on GitHub — your work is there.

**Pushing does not submit the lab.** It backs up your work and builds your
history. Submission happens on Gradescope, next.

---

## Step 8 — Submit on Gradescope

Open **gradescope.com directly in your browser**.
**Not through Canvas** — the GitHub connection does not work inside Canvas.

Open **MATH 170 → Lab 01** and click **Submit**. You have two options.

### Option A — Upload the file

Drag **`calculator.py`** into the upload box. Simplest, and it always works.

### Option B — Submit from GitHub

1. Choose **GitHub**
2. The first time, click **Connect to GitHub** and authorize Gradescope
3. Pick your repository `math170-yourname` and the `main` branch
4. Submit

Gradescope takes a **snapshot** of your repository at that moment. If you push
more work later, you must submit again — pushing alone changes nothing on
Gradescope.

Either way, wait for the autograder to finish. You should see **100 / 100**.

You may resubmit as many times as you like. The last submission counts.

---

## By the end of lab

- [ ] GitHub account created
- [ ] Python runs — `python --version` works in a terminal
- [ ] VS Code working, with Microsoft's Python extension
- [ ] Git installed and configured with your name, email, and `pull.rebase false`
- [ ] Your own repository created, with `origin` and `upstream` set
- [ ] Gradescope shows **100 / 100** for Lab 01
- [ ] Attendance sheet signed

## If something breaks

Ask during lab. That is what today is for. The most common problems:

- **Python not found in the terminal** — on Windows you are probably in
  PowerShell; use Anaconda Prompt. On Mac, open a new terminal window
- **`calculator.py` not found** — it must be in the same folder as the notebook
- **`Permission denied` when pushing** — you are pushing to the course
  repository instead of your own. Run `git remote -v` and check that `origin` is
  *your* repository
- **GitHub will not connect on Gradescope** — you opened Gradescope through
  Canvas; open gradescope.com directly instead
- **`git pull` says "Need to specify how to reconcile divergent branches"** —
  run `git config --global pull.rebase false` once, then pull again. If an
  editor opens asking for a merge message, save and close it

## Try at home

Not needed for today, and not graded.

**Claim the GitHub Student Developer Pack.** Add your Emory address as a
secondary email at github.com/settings/emails, verify it, and apply at
education.github.com/pack. Free private repositories, tools, and credits from a
long list of services. Approval takes a few days and may require a dated student
ID, so start early — nothing in this course depends on it.

**Get Python working on your own machine** if you finished lab on someone else's
computer.
