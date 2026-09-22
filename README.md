# Introduction to Challenge Exercises

**COMP115** is a foundational course designed to introduce students—both general learners and future computer science majors—to the core ideas of coding.

To support deeper learning, each major chapter includes a **Challenge Exercise**.
These challenges go beyond the basics to introduce key computer science concepts and professional practices.

## In this challenge, you will explore:

* **Visual Studio Code**
  Learn to use the same code editor trusted by professional developers.

* **Working with the Terminal**
  Learn how to issue operating system commands using the terminal, just like professional programmers.

* **Automated Testing**
  Discover how programmers use test cases to verify their code—similar to how you've checked answers in the textbook, but more powerful and automatic.

* **Git & GitHub**
  Use version control to manage and submit your work. You'll learn how to upload and share code using GitHub, the industry-standard platform for collaborative coding.

These challenges not only build your skills but also give you a taste of the tools and practices used in real-world software development.

## Grading for Challenge Exercises

Challenge Exercises are designed for students who wish to go **above and beyond** the general course expectations.

* These exercises are **optional**, but completing them demonstrates a deeper understanding of computer science concepts.
* **Your grade will not be negatively affected** if you choose not to complete them.
* However, to be eligible for an **A or A+** in the course, you are expected to complete at least some of the Challenge Exercises.
* If you choose not to attempt any Challenge Exercises, your final grade will be capped at an **A−**.

# Step 1 – Accept the assignment on GitHub

You will first need to create an account at [https://github.com/](https://github.com/) if you haven’t already.
You'll also need to understand two key terms:

* **GitHub** is a website where programmers share and collaborate on code.
* **Git** is the tool programmers use to interact with GitHub.

After creating your account, click on the assignment link provided.
Accept the assignment. If this is your first time using GitHub Classroom, you may be prompted to link your GitHub account to the class so I can track your progress.

# Step 2 – Launch the code editor

After accepting the assignment, you’ll be taken to your GitHub **repository** (also called a *repo*). A repo is simply a place where your code is stored online.

To start coding:

1. Click the **Codespaces** button near the top of the page.
2. This will launch **VS Code in your browser**—a powerful, professional-grade code editor.

*Note: The first time it launches, it may take a few minutes.*

# Step 3 – Open the code files

Unlike the textbook, where you enter code into the website, real programmers write code in separate files.

* On the left-hand side, you'll see a file called `main.py`.
* Click on it to open it in the center editor area.

To **run the code**, look at the **Terminal** tab at the bottom of your screen. In the terminal, type:

```
python main.py
```

This runs all the code in `main.py` and prints the output in the terminal so you can check the result.

Try it now.

# Step 4 – Verifying your work

Programmers don’t just hope their code works—they **test** it.

To test your code:

1. Open the **Terminal** tab.
2. Type the following command:

```
pytest
```

This will run automated test cases and tell you whether your code works as expected.

At this point, all tests should **fail**—that’s normal. You haven’t fixed the code yet!

# Step 5 – Fix the code

Now it's time to dig in. Look at the code in `main.py` and fix all the errors.

After fixing each issue, **run `pytest` again** to check your progress.
Keep doing this until all the tests pass.

# Step 6 – Submit your work

Once you're satisfied, you can submit your work using Git.

In the terminal, enter the following commands **one at a time**:

```
git add -A
git commit -m 'submit'
git push
```

These commands save and upload your work to GitHub so I can review it.

---

### ✅ Final Tip

  * You don’t have to finish everything in one go. Just make sure you execute the submission commands
    to save your work.

  * If you closed your browser window, you can always go back to your current codespaces by visiting
    your repo and click on "Code" -> "Codespaces" -> "Open in Browser".

    <img src="images/Resume%20Codespaces.png" alt="Codespaces button" width="500">

Good luck, and have fun exploring professional tools and practices!

