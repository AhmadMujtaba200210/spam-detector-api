import subprocess
import sys
import requests
from packaging import version


def get_latest_pip_version():
    try:
        response = requests.get("https://pypi.org/pypi/pip/json")
        latest_version = response.json()["info"]["version"]
        return latest_version
    except Exception as e:
        print(f"Error fetching latest pip version: {e}")
        return None


def main():
    try:
        pip_version_output = subprocess.check_output([sys.executable, '-m', 'pip', '--version']).decode('utf-8')
        local_pip_version = pip_version_output.split(' ')[1]

        latest_pip_version = get_latest_pip_version()

        if latest_pip_version and version.parse(local_pip_version) < version.parse(latest_pip_version):
            subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    except Exception as e:
        print(f"Error checking/upgrading pip: {e}")

    # now check packages before moving to deployment
    try:
        installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode('utf-8').split(
            '\n')

        with open("requirements.txt", "r") as file:
            required_packages = file.readlines()

        for package in required_packages:
            if package.strip() not in installed_packages:
                subprocess.run([sys.executable, '-m', 'pip', 'install', package.strip()])

        with open("last_updated", "w"):
            pass
    except Exception as e:
        print(f"Error checking/updating requirements: {e}")


if __name__ == "__main__":
    main()
