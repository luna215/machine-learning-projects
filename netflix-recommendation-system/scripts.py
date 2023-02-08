import subprocess

def main():
    subprocess.run(["python", "-m", "netflix_recommendation_system", ">", "output.txt"])