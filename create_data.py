
import random
from dataclasses import dataclass


@dataclass
class Version:
    name: str
    icon: str
    version_number: str


def generate_data():
    header = ["Name", "Icon", "Version Number"]

    scikit_version = Version("scikit-base",
                 "https://pypi-camo.global.ssl.fastly.net/128c7a5a38ea6322af5986a955b494613bed18a7/68747470733a2f2f72656"
                 "164746865646f63732e6f72672f70726f6a656374732f736b626173652f62616467652f3f76657273696f6e3d6c6174657374",
                 "0.5.1")
    seaborn_version = Version(
        "seaborn",
        "https://pypi-camo.global.ssl.fastly.net/02ec5c82dcdde42bf89a8ac78767bd1260007d09/68747470733a2f2f67697468756"
        "22e636f6d2f6d7761736b6f6d2f736561626f726e2f776f726b666c6f77732f43492f62616467652e737667",
        "0.12.2"
    )

    matplotlib_version = Version(
        "matplotlib",
        "https://pypi-camo.global.ssl.fastly.net/a66f2bf3db04c5e5519f1db84d3e9b5b437ce132/68747470733a2f2f62616467652e6"
        "67572792e696f2f70792f6d6174706c6f746c69622e737667",
        "3.7.2"
    )

    lib_versions = [scikit_version, seaborn_version, matplotlib_version]

    return lib_versions
