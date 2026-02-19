import subprocess
import os

cwd = "c:/Users/Asus/Desktop/complex_vector_space"
git_exe = "C:/Program Files/Git/cmd/git.exe"

def run_git(args):
    print(f"Running git {' '.join(args)}...")
    try:
        result = subprocess.run([git_exe] + args, cwd=cwd, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running git {' '.join(args)}:")
        print(e.stdout)
        print(e.stderr)

if __name__ == '__main__':
    if not os.path.exists(os.path.join(cwd, ".git")):
        run_git(["init"])
    
    # Check if remote exists
    try:
        subprocess.run([git_exe, "remote", "get-url", "origin"], cwd=cwd, check=True, capture_output=True)
        print("Remote origin exists.")
    except subprocess.CalledProcessError:
        run_git(["remote", "add", "origin", "https://github.com/blackholeinfiverse107-creator/complex_vector_space.git"])

    run_git(["add", "."])
    run_git(["commit", "-m", "Update ComplexVector with immutability and mathematical verification"])
    run_git(["push", "-u", "origin", "master"])
    run_git(["push", "-u", "origin", "main"])
