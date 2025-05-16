from setuptools import find_packages,setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function will return the list of requirements
    """
    try:
        with open("requirements.txt","r") as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace("\n", "") for req in requirements]
            if "-e ." in requirements:
                requirements.remove("-e .")
        
    except Exception as e:
        print(f"requirement file not found: {e}")
    return requirements

setup(
    name = "network_security",
    version = "0.0.1",
    author = "Dhyey Bhimani",
    author_email = "dhyeybhimani001@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
    )