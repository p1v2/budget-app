"""
Calculates code quality score
Fails if code so bad
"""
import sys

from pylint import lint

# Extract fail_under arg
FAIL_UNDER = float([arg for arg in sys.argv if arg.startswith('--fail-under')][0].split("=")[1])
# And all another argv
ARGV = [arg for arg in sys.argv if not arg.startswith('--fail-under')]

if len(ARGV) < 2:
    raise ValueError("Module to evaluate needs to be the first argument")

RUN = lint.Run(ARGV[1:], do_exit=False)
SCORE = RUN.linter.stats['global_note']  # Yes this is a terrible name for the score

if SCORE < FAIL_UNDER:
    print(f"The required code rate is {FAIL_UNDER}.")
    print(f"The actual code rate is {SCORE}")
    print()
    print("Your code is so bad.")
    print("Please check the output above and fix the code style.")
    sys.exit(1)