import os
from psutil import sensors_battery


def main():
    percentage = sensors_battery().percent
    plugged = sensors_battery().power_plugged

    if not plugged:
        if percentage <= 30:
            current_output_volume = get_output_volume()  # get current volume level
            set_output_volume(10)  # drop volume to 10%

            os.system(f'say "Battery is {percentage}%" -v {get_random_voice()}')
            show_notification(title="Plug me", text=f"Because battery is {percentage}%")

            set_output_volume(current_output_volume)  # restore volume to previous level
    else:
        if percentage >= 80:
            current_output_volume = get_output_volume()  # get current volume level
            set_output_volume(10)  # drop volume to 10%

            os.system(f'say "Battery is {percentage}%" -v {get_random_voice()}')
            show_notification(title="Unplug me", text=f"Because battery is {percentage}%")

            set_output_volume(current_output_volume)  # restore volume to previous level


def get_random_voice() -> str:
    import secrets

    voices = [
        'Alice',
        'Anna',
        'Cellos',
        'Daniel',
        'Samantha',
        'Moira',
        'Mónica',
    ]

    return secrets.choice(voices)


def show_notification(title: str, text: str, sound="quack") -> None:
    os.system(f"""
              osascript -e 'display notification "{text}" with title "{title}" sound name "{sound}"'
              """)


def set_output_volume(percent: str) -> None:
    os.system(f'osascript -e "set volume output volume {percent}"')


def get_output_volume() -> str:
    import subprocess

    return subprocess.run(
        ['osascript', '-e', 'output volume of (get volume settings)'],
        capture_output=True,
        text=True
    ).stdout.strip()


if __name__ == "__main__":
    main()
