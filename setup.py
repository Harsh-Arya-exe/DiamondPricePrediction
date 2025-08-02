from setuptools import setup

"""This function was to get the requirements from the files and give to the
install_requires attribute but i causes problem in github actions or pipelines
so we had to hardcode them

HYPHEN_E_DOT = "- .e"


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            stripped = line.strip()  # removing the \n character line returned
            # by f.readlines()
            if stripped and HYPHEN_E_DOT in stripped:  # This is saying that
                # is the line after stripping is not empty and also it does
                # not contains the HYPHEN_E_DOT then enter the IF block
                continue
            requirements.append(stripped)
    return requirements
"""

setup(
    name="DiamondPricePrediction",  # name of the project/package
    version="0.0.1",  # version number
    description="mlops practice for diamond price prediction",  # description
    long_description="mlops practice",  # long_description could be a READ.ME
    author="Harsh Arya",  # author name
    author_email="harsh.arya1004@gmail.com",  # author email
    install_requires=['scikit-learn', 'numpy', 'pandas']
)
