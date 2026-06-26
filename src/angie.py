#!/usr/bin/env python3

import random
import subprocess
import sys
from pathlib import Path

APP_NAME = "Angie"
IMG_DIR = Path.home() / ".config/swaync/images"

MESSAGES = {
    "login": [
        ("angie_motiv.png", "Welcome back. Angie is online."),
        ("angie_motiv.png", "System ready. Let's make progress."),
    ],
    "roast": [
        ("angie_warn.png", "Interesting. Avoiding work again?"),
        ("angie_sad.png", "Angie believed in your productivity arc."),
    ],
    "focus": [
        ("angie_motiv.png", "Focus mode. No random tab wandering."),
        ("angie_warn.png", "Lock in. The internet can wait."),
    ],
    "random": [
        ("angie_motiv.png", "Small progress still counts."),
        ("angie_warn.png", "Posture check. Fix the shrimp back."),
        ("angie_sad.png", "Drink water. Your body is not a forgotten server."),
    ],
}


def notify(icon_name, message):
    icon_path = IMG_DIR / icon_name

    subprocess.run([
        "notify-send",
        "-a", APP_NAME,
        "-i", str(icon_path),
        APP_NAME,
        message,
    ], check=False)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "random"
    choices = MESSAGES.get(mode, MESSAGES["random"])
    icon, message = random.choice(choices)
    notify(icon, message)


if __name__ == "__main__":
    main()