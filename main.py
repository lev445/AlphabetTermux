# Im fucking writing this at 1am
import os
import subprocess
import sys
import pwd
import readline

def main(): # Main point
    user_info = pwd.getpwuid(os.getuid())
    user = user_info.pw_name
    print(f"Welcome to AlphabetTermux! x {user}@AlphabetTermux") 
    while True:
        try:
            cwd = os.getcwd() # Get absolute path
            home = os.path.expanduser("~")
            if cwd.startswith(home):
                cwd = cwd.replace(home, "~", 1)
            # Check: if root: #; if user: $
            if os.getuid() == 0:
                prompt = input(f"[{user}@AlphabetTermux] {cwd}# ")
            else:
                prompt = input(f"[{user}@AlphabetTermux] {cwd}$ ")
            if not prompt.strip():
                continue
            if prompt == "AboutTerminal":
                print("AlphabetTermux - simple terminal")
                print("GPL-3 license! Open-software.")
                print("Github: ")
                print("Version: v0.1-beta")
                continue
            if prompt.strip().startswith("cd "): # Checking cd
                path = prompt.strip().split(" ", 1)[1]
                try:
                    os.chdir(os.path.expanduser(path))
                except Exception as cd_error:
                    print(f"!! cd error: {cd_error}") # Catch cd error
                continue
            if prompt.strip() == "cd":
                os.chdir(os.path.expanduser("~"))
                continue
            if prompt.strip():
                try:
                    subprocess.run(prompt, shell=True)
                except Exception as cmd_error:
                    print(f"Command error: {cmd_error}") # If command send error
            if prompt.strip() == "exit":
                print("bye-bye")
                break
            if prompt.strip() == "clear":
                print("\033[H\033[J", end="")
                print("\033[H\033[J", end="") # Clear screen with ANSI
                continue
        except (KeyboardInterrupt, EOFError):
            print("\nSIGINT detected, exit..")
            print('bye-bye')
            break
        except Exception as e:
            print(f"\nAlphabetTermux get error: {e}")
            break

if __name__ == "__main__":
    main() # Call main point



