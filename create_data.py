
import random
from dataclasses import dataclass


@dataclass
class Version:
    name: str
    icon: str
    version_number: str


def generate_data():
    header = ["Name", "Icon", "Version Number"]
    icons = ["https://pypi-camo.global.ssl.fastly.net/128c7a5a38ea6322af5986a955b494613bed18a7/68747470733a2f2f72656164746865646f63732e6f72672f70726f6a656374732f736b626173652f62616467652f3f76657273696f6e3d6c6174657374",
             "https://pypi-camo.global.ssl.fastly.net/02ec5c82dcdde42bf89a8ac78767bd1260007d09/68747470733a2f2f6769746875622e636f6d2f6d7761736b6f6d2f736561626f726e2f776f726b666c6f77732f43492f62616467652e737667",
             "https://pypi-camo.global.ssl.fastly.net/a66f2bf3db04c5e5519f1db84d3e9b5b437ce132/68747470733a2f2f62616467652e667572792e696f2f70792f6d6174706c6f746c69622e737667",
             "https://pypi-camo.global.ssl.fastly.net/a0380ab0088be20d43e83644341dfbe5f9201935/68747470733a2f2f696d672e736869656c64732e696f2f707970692f646d2f70737574696c2e737667",
             "https://pypi-camo.global.ssl.fastly.net/fdf3563e1ff1014f9fea67ae756480466301b504/68747470733a2f2f696d672e736869656c64732e696f2f707970692f646d2f6e756d70792e7376673f6c6162656c3d50795049253230646f776e6c6f616473",
             "https://pypi-camo.global.ssl.fastly.net/74b6ebf66597af5b0cd5ea7350e65807012fa323/68747470733a2f2f6769746875622e636f6d2f7469616e676f6c6f2f666173746170692f776f726b666c6f77732f546573742f62616467652e7376673f6576656e743d70757368266272616e63683d6d6173746572",
             ]

    names = ["asd", "def", "wer", "tzu", "jkl", "bnm"]
    versions = ["1.2.3", "4.5.6", "7.8.9", "1.3.4", "2.6.7", "3.8.9"]

    all_versions = [Version(random.choice(names), random.choice(icons), random.choice(versions)) for i in range(100)]

    return all_versions
