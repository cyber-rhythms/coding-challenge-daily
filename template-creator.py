import os

# Define template for code review in the .py script.
py_template = """# Submission.

\"\"\"
Code Review.

Strengths:
Deficiencies:
Remarks:
Solution:
\"\"\"
"""

if __name__ == "__main__":
    try:
        name = input("Good to see you're back for another round. Slow and steady. Now input name of the folder, scripts and notebook for creation: ")
        cwd = os.getcwd()

        # Create directory.
        dir_path = os.path.join(cwd, name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        # Create named .ipynb and .py files.
        ipynb_path = os.path.join(dir_path, f"{name}.ipynb")
        py_path = os.path.join(dir_path, f"{name}.py")

        with open(ipynb_path, "w") as f:
            pass

        with open(py_path, "w") as f:
            f.write(py_template)
            pass
        
    except KeyboardInterrupt:
        print("\n Operation cancelled. Exiting.")