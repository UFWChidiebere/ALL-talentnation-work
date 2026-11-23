# **PYTHON FOUNDATION CHALLENGE**

**Week 11 — Build and Ship Your First App (.exe)**

## **Objective**

This week you stop writing scripts that only live in your editor and **build a real app you can double-click**. You will warm up with three short problems, build a small desktop app with a window, buttons and text boxes, and package it into a Windows .exe file. When you get home, you can show it to your friends and family, even on a computer that does not have Python installed.

## **A Word Before You Start**

You already know the hard part: writing logic with functions, loops, lists and dictionaries. An app is just that same logic with a window around it.

* Keep your **logic** (the functions that calculate things) separate from your **window** (the buttons and boxes). This makes the app easier to test and fix.  
* Your first version can be plain and ugly. Get it working, then make it nicer.  
* If you are stuck for more than 15 minutes, write down what is confusing you and ask. A note about what blocked you is useful.  
* Bonus items are optional. Finish the required parts first.

## **Instructions**

* Part A and the logic of your app must be written by you. Do not copy a finished solution.  
* Allowed tools this week: Python's built-in **tkinter** (for the window) and **PyInstaller** (to make the .exe). No other external libraries.  
* Keep everything inside one file called app.py (no spaces in the name). Do not load images, text files, or sounds. Your app should need nothing except the .exe itself.  
* Test your logic with the examples given and with at least two cases of your own.  
* Functions that calculate something must **return** the result. print() and window updates belong outside those functions.

## **Week 12 at a Glance**

| Part | Questions | What you do |
| :---- | :---- | :---- |
| A. Warm-up | 1–3 | Three short logic problems to get your hands moving |
| B. Build | 4 | Pick one project and build it as a window app |
| C. Ship | 5 | Turn app.py into an .exe and test it |
| D. Show | 6 | Prepare a 60-second demo for your friends |

**The progression:** short logic problems → logic plus a window → packaging → presenting your work.

# **Part A — Warm-up**

Three quick problems. Keep each function clean, because the same habits make your app easier to build.

## **1\. FizzBuzz Plus**

**Suggested time:** 15–20 minutes

### **Problem**

Write fizzbuzz\_plus(n) that returns a list of strings for the numbers 1 to n:

* Multiples of 3 include "Fizz", multiples of 5 include "Buzz", multiples of 7 include "Bazz".  
* If a number is a multiple of more than one, join the words in that order.  
* If it is a multiple of none, use the number as a string.

### **Examples**

3   → "Fizz"  
15  → "FizzBuzz"  
21  → "FizzBazz"  
35  → "BuzzBazz"  
105 → "FizzBuzzBazz"  
4   → "4"  
fizzbuzz\_plus(0) → \[\]

### **Constraints**

* Build each result by adding words to a string one rule at a time. Do not write a separate if branch for every combination.  
* Return the list. Print from outside the function.

**What this gauges:** Loops, modulo, and building a string step by step.

## **2\. Smallest, Largest and Average**

**Suggested time:** 15–20 minutes

### **Problem**

Write stats(nums) that returns (smallest, largest, average) for a list of numbers. Round the average to 2 decimal places. For an empty list, return None.

### **Examples**

stats(\[4, 9, 2, 7\])   → (2, 9, 5.5)  
stats(\[5\])            → (5, 5, 5.0)  
stats(\[-3, \-1, \-2\])   → (-3, \-1, \-2.0)  
stats(\[\])             → None

### **Constraints**

* Do not use min(), max(), or sum().  
* Find all three in one loop.  
* Do not change the list passed in.

**What this gauges:** Tracking several values in one pass, and handling empty input safely (you will need this for your app).

## **3\. Vowels and Consonants**

**Suggested time:** 15–20 minutes

### **Problem**

Write count\_letters(text) that returns (vowels, consonants). Count only letters. Ignore spaces, digits and punctuation. Treat uppercase and lowercase the same.

### **Examples**

count\_letters("Hello, World 123") → (3, 7\)  
count\_letters("AEIOU")            → (5, 0\)  
count\_letters("rhythm")           → (0, 6\)  
count\_letters("")                 → (0, 0\)

### **Constraints**

* Use a loop. No .count() and no .isalpha().  
* Decide if a character is a letter by comparing it between "a" and "z" after making it lowercase.

**What this gauges:** String iteration and keeping two counters at once.

# **Part B — Build the App**

## **4\. Your Window App**

**Suggested time:** 60–75 minutes

### **Problem**

Pick **one** of the four projects below and build it as a window app using tkinter. Your app must have two layers:

1. **Logic layer:** plain functions that do the work and return results. They know nothing about windows.  
2. **Window layer:** the buttons, boxes and labels. It reads what the user typed, calls your logic functions, and shows the result.

### **Choose a project**

**Option A: Shopping Cart**

The cart is a list of dictionaries like {"name": "Rice", "price": 1500, "qty": 3}.

* add\_item(cart, name, price, qty): add the item, or increase the quantity if the name is already there.  
* remove\_item(cart, name): remove the item. Do nothing if it is not there.  
* cart\_total(cart): return the total cost.  
* apply\_discount(total, percent): return the total after the discount.

Add Rice 1500 x2, Beans 800 x1, Rice 1500 x1 → total 5300  
Remove Beans → total 4500  
10% discount on 4500 → 4050.0  
**Option B: To-Do List**

Each task is a dictionary like {"title": "Study", "done": False}.

* add\_task(tasks, title): add a task. Ignore blank titles.  
* mark\_done(tasks, index): mark the task at that position as done.  
* remove\_task(tasks, index): remove the task at that position.  
* count\_remaining(tasks): return how many tasks are not done.

Add "Study", add "Cook", mark\_done index 0 → count\_remaining \= 1  
**Option C: Quiz Game**

Store at least 5 questions in the code, each with its choices and the correct answer.

* check\_answer(question, choice): return True or False.  
* get\_feedback(score, total): return a message for the final score (for example, a different message for a perfect score, a middle score, and a low score).  
* The window shows one question at a time, lets the player pick an answer, and shows the final score at the end.

get\_feedback(5, 5\) → "Perfect score\!"  
get\_feedback(0, 5\) → a kind message encouraging another try  
**Option D: Bill Splitter**

* calculate\_tip(bill, tip\_percent): return the tip amount.  
* total\_with\_tip(bill, tip\_percent): return the bill plus tip.  
* split\_bill(total, people): return what each person pays, rounded to 2 decimals. If people is less than 1, return None.

calculate\_tip(10000, 10\)    → 1000.0  
total\_with\_tip(10000, 10\)   → 11000.0  
split\_bill(11000, 4\)        → 2750.0  
split\_bill(11000, 0\)        → None

### **Minimum window requirements**

Your app must have all of these:

* A window with a **title** and a fixed starting size.  
* At least **two input boxes** (or one input box plus a dropdown or option buttons).  
* At least **three buttons**, including one **Clear / Reset** button.  
* A **display area** that shows results (a Label, Listbox or Text box).  
* **Input checking:** wrong or empty input shows a friendly message using messagebox.showerror(...). The app must **never crash** on bad input.

### **Constraints**

* Keep your logic functions free of tkinter, print() and input().  
* Use try and except ValueError when turning typed text into numbers.  
* No external libraries except tkinter (and PyInstaller later).  
* Do not hardcode answers.

### **Starter skeleton**

This tiny app adds two numbers. Study how the logic function (add\_numbers) is separate from the window code. Then replace it with your own project.

import tkinter as tk  
from tkinter import messagebox

\# \---------- LOGIC (no tkinter in here) \----------  
def add\_numbers(a, b):  
    return a \+ b

\# \---------- WINDOW CODE \----------  
def on\_add():  
    try:  
        a \= float(entry\_a.get())  
        b \= float(entry\_b.get())  
    except ValueError:  
        messagebox.showerror("Invalid input", "Please enter numbers only.")  
        return  
    result\_label.config(text="Result: " \+ str(add\_numbers(a, b)))

def on\_clear():  
    entry\_a.delete(0, tk.END)  
    entry\_b.delete(0, tk.END)  
    result\_label.config(text="Result: ")

root \= tk.Tk()  
root.title("My First App")  
root.geometry("320x240")

tk.Label(root, text="First number:").pack()  
entry\_a \= tk.Entry(root)  
entry\_a.pack()

tk.Label(root, text="Second number:").pack()  
entry\_b \= tk.Entry(root)  
entry\_b.pack()

tk.Button(root, text="Add", command=on\_add).pack(pady=5)  
tk.Button(root, text="Clear", command=on\_clear).pack()

result\_label \= tk.Label(root, text="Result: ")  
result\_label.pack(pady=10)

root.mainloop()

### **Test before moving on**

Run python app.py and try the following. Fix anything that fails before you package the app.

* Normal input works.  
* Empty boxes show a friendly message.  
* Letters typed into a number box show a friendly message.  
* Clear / Reset really clears everything.

### **Bonus**

* Make pressing the **Enter** key trigger your main button: root.bind("\<Return\>", lambda event: on\_add()) (use your own function name).  
* Give your window a nicer look with colors (bg=, fg=) and a bigger font (font=("Arial", 14\)).  
* Add a label at the bottom that says Built by \<your name\>.

**What this gauges:** Separating logic from the interface, handling bad input, and connecting buttons to functions.

# **Part C — Ship It**

## **5\. Turn Your App into an .exe**

**Suggested time:** 20–30 minutes

### **Problem**

Package your finished app.py into a single .exe file that runs when you double-click it, without needing Python.

### **Steps**

1. **Check your file.** Your app must be saved as app.py and must run correctly with python app.py.  
2. **Open a terminal** (Command Prompt or PowerShell) in the same folder as app.py.  
3. **Install PyInstaller:**

pip install pyinstaller  
If pip is not recognized, try:

python \-m pip install pyinstaller

4. **Build the app:**

pyinstaller \--onefile \--windowed \--name MyApp app.py  
What the options mean:

* \--onefile packs everything into a single .exe.  
* \--windowed stops a black console window from opening behind your app.  
* \--name MyApp sets the file name. Change MyApp to your app's name.  
5. **Find your app.** When the build finishes, open the new **dist** folder. Your file is dist\\MyApp.exe.  
6. **Test it properly.** Copy MyApp.exe to your Desktop and double-click it. Run through the same tests you did in Part B.  
7. **Send it to yourself.** Put the .exe on a flash drive, or send it to your phone or email, so you have it at home.

### **Things to know**

* The first launch of a packaged app can take a few seconds. That is normal.  
* Build the .exe on a **Windows** computer. Building on a Mac or Linux machine gives you a different kind of file that will not run on Windows.  
* Windows or your antivirus may show a warning for apps you made yourself because they are not signed. If it blocks the file, choose the option to run it anyway or ask your instructor.  
* You will also see new build folder and a .spec file. You can ignore them. Only the .exe inside dist matters.

### **If something goes wrong**

| Problem | What to try |
| :---- | :---- |
| pip is not recognized | Use python \-m pip install pyinstaller |
| pyinstaller is not recognized | Use python \-m PyInstaller \--onefile \--windowed \--name MyApp app.py |
| The .exe opens and closes instantly | Rebuild without \--windowed, run it from the terminal, and read the error message |
| The app works with python app.py but not as an .exe | Check that you did not load any image or text file. Everything must live in the code |
| The .exe file is missing | Look inside the dist folder, not the main folder |
| The window looks different from before | Usually fine. Check that every button still works |

### **Bonus**

Give the app a custom icon by adding \--icon myicon.ico to the build command (you need an .ico file in the same folder).

**What this gauges:** Following a technical process step by step, using a command line tool, and troubleshooting.

# **Part D — Show It**

## **6\. Your 60-Second Demo**

**Suggested time:** 10–15 minutes

### **Problem**

Prepare to show your app to friends or family. At the top of app.py, write a short comment (5 lines) answering these. They double as your demo script.

1. **What is it called and what does it do?** One sentence.  
2. **The normal use:** what do you click or type to show it working?  
3. **The mistake test:** what bad input will you try to show that it does not crash?  
4. **One thing you are proud of.**  
5. **One thing you would improve next.**

Then practice your demo out loud once. You should be able to explain it in 60 seconds.

### **A good answer to "how did you build it?"**

*"I wrote the logic in Python functions, put a window around it with tkinter, and used PyInstaller to turn it into an .exe so it runs on any Windows computer."*

Try saying that in your own words.

**What this gauges:** Explaining your work clearly, which is just as important as writing the code.

## **Progression**

Short logic problems → separating logic from a window → handling bad input → packaging an app → explaining it to someone else.

## **Time Guide**

| Section | Questions | Suggested Time |
| :---- | :---- | :---- |
| Warm-up | 1–3 | 45 – 60 min |
| Build the app | 4 | 60 – 75 min |
| Ship it | 5 | 20 – 30 min |
| Show it | 6 | 10 – 15 min |
| **Overall** | 1–6 | **About 2 hrs 15 min – 3 hrs** |

If you are short on time, do **Q2** as the only warm-up, then go straight to Q4 and Q5. A working .exe is the main goal today.

## **Self-Assessment Guide**

| Question | Concept being tested | What it tells you |
| :---- | :---- | :---- |
| 1\. FizzBuzz Plus | Loops, modulo, string building | Can you avoid writing every combination by hand? |
| 2\. Smallest, Largest, Average | One-pass tracking, empty input | Can you handle empty input safely? |
| 3\. Vowels and Consonants | String iteration, character checks | Can you track two counts at once? |
| 4\. Window App | Logic vs interface, input checking | Can you keep logic separate and survive bad input? |
| 5\. Make the .exe | Command line, packaging | Can you follow and troubleshoot a technical process? |
| 6\. Demo | Explaining your work | Can you describe what you built in plain words? |

## **How to Read Your Results**

* **Working .exe that handles bad input** → Excellent. You have built and shipped a real app.  
* **App works with python app.py but no .exe yet** → Good progress. Write down the error message from the build and bring it to the next session.  
* **Window opens but buttons do nothing or crash** → Review how a button connects to a function (command=) and how to read an entry box (.get()).  
* **Logic works but no window yet** → You have the hard part. Start from the starter skeleton and swap in your functions one at a time.

## **A Note on "Gauging"**

This is a gauge, not an exam. Struggling is data, not failure. If your app is not finished, write down exactly what blocked you. That list is the real deliverable.

## **Notes for the Instructor**

| Design choice | Reason |
| :---- | :---- |
| Short warm-ups, one main build | Frees most of the session for the app, which is the exciting part. |
| Logic and window kept separate | Reinforces functions and return values, and makes bugs easier to find. |
| Four project options | Lets students pick something they care about; all use lists, dictionaries, loops and functions already covered. |
| No file loading in the app | A one-file .exe is simpler to ship when nothing outside the code is needed. |
| Q6 demo script | Turns the finished app into a communication exercise. |

### **Before the session**

* Confirm the lab computers run **Windows** with Python 3 installed. Run python \-m tkinter to check that a small test window opens.  
* Confirm pip works and that students can download PyInstaller. If the network is slow, install it ahead of time.  
* Build one .exe yourself in advance so you can show the finished result and recognize the common errors.  
* Warn students that antivirus software may flag home-made .exe files. Know how to allow the file on your machines.  
* Students on Mac or Linux can still build the app, but they will need a Windows machine for the .exe.

**End of Week 12 Challenge**