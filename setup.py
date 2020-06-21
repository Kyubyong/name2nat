import setuptools

with open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'flair',
]

setuptools.setup(
    name="name2nat",
    version="0.5.1",
    author="Kyubyong Park",
    author_email="kbpark.linguist@gmail.com",
    description="Nationality Prediction from Name",
    install_requires=REQUIRED_PACKAGES,
    license='Apache License 2.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kyubyong/name2nat",
    packages=setuptools.find_packages(),
    package_data={'name2nat': ['name2nat/best-model.pt', 'name2nat/name2nats.pkl']},
    python_requires=">=3.6",
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)