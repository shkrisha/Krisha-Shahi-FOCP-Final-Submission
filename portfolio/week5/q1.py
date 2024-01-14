#Q)1)Using command-line arguments involves the sys module.
# Review the docs for this module and using the information in there write a short program that when run from the command-line reports what operating system platform is being used.

import sys

def display_operating_system_platform():
    # Get the operating system platform
    platform_used = sys.platform
    print(f"Operating System Platform: {platform_used}")

if __name__ == "__main__":
    display_operating_system_platform()

