# scripts/check_dependencies.py

import shutil
import subprocess


REQUIRED_COMMANDS = [

    "ddcutil",

]

OPTIONAL_COMMANDS = [

    "systemctl",

    "notify-send",

]


def check_command(command):

    return (
        shutil.which(command)
        is not None
    )


def print_section(title):

    print()
    print("=" * 50)
    print(title)
    print("=" * 50)


def check_ddcutil():

    print_section(
        "DDCUTIL"
    )

    if not check_command(
        "ddcutil"
    ):

        print(
            "❌ ddcutil not installed"
        )

        return False

    try:

        result = subprocess.run(

            [
                "ddcutil",
                "detect"
            ],

            capture_output=True,

            text=True,

            timeout=10,

        )

        if "Display" in result.stdout:

            print(
                "✅ Monitor detected"
            )

            return True

        print(
            "⚠ ddcutil installed but no monitor found"
        )

        return False

    except Exception as e:

        print(
            f"❌ {e}"
        )

        return False


def check_optional():

    print_section(
        "OPTIONAL"
    )

    for cmd in OPTIONAL_COMMANDS:

        if check_command(cmd):

            print(
                f"✅ {cmd}"
            )

        else:

            print(
                f"⚠ {cmd} missing"
            )


def main():

    print()

    print(
        "Lumina Dependency Check"
    )

    print()

    check_ddcutil()

    check_optional()

    print()


if __name__ == "__main__":

    main()