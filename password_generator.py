---

## 2️⃣ `password_generator.py`

```python
#!/usr/bin/env python3
import sys
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.progress import track
import random, string, time, os

console = Console()

# Check folder
if os.path.basename(os.getcwd()) != "password-generator":
    console.print("[red]Error:[/red] You must run this program from the 'password-generator' folder!")
    exit(1)

use_rich = "--rich" in sys.argv

def generate_password(length=12, letter_case="both", use_numbers=True, use_symbols=True):
    chars = string.ascii_lowercase
    if letter_case.lower() == "uppercase":
        chars = string.ascii_uppercase
    elif letter_case.lower() == "both":
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    if use_rich:
        console.print(Panel("[bold cyan]Password Generator 🔐[/bold cyan]\nBy B dev", expand=False))
        length = int(Prompt.ask("[yellow]What length do you want for your password?[/yellow]", default="12"))
        use_symbols = Confirm.ask("[green]Do you want symbols?[/green]", default=True)
        letter_case = Prompt.ask("[green]Choose letter case (lowercase / uppercase / both)[/green]",
                                 choices=["lowercase", "uppercase", "both"], default="both")

        console.print("\n[blue]Generating your password...[/blue]")
        for _ in track(range(20), description="Creating..."):
            time.sleep(0.05)

        password = generate_password(length, letter_case, use_numbers=True, use_symbols=use_symbols)
        console.print("\n[bold magenta]Your password is:[/bold magenta]")
        console.print(Panel(f"[white on black]{password}[/white on black]", expand=False))
    else:
        # Basic CLI
        length = int(input("Enter password length: "))
        use_symbols = input("Use symbols? (y/n): ").lower() == "y"
        letter_case = input("Letter case (lowercase / uppercase / both): ").lower()
        password = generate_password(length, letter_case, use_numbers=True, use_symbols=use_symbols)
        print(f"Your password: {password}")

if __name__ == "__main__":
    main()
