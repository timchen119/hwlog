from setuptools import setup
setup(
    name = "hwlog",
    packages = ["hwlog"],
    version = "0.1",
    description = "hwlog",
    author = "Tim Chen",
    author_email = "timchen119@gmail.com",
    url = "https://github.com/timchen119/hwlog",
    download_url = "https://github.com/timchen119/hwlog",
    keywords = ["hardware", "snappy", "snap"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Ubuntu Linux",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description = """\
    This version requires Python 3 or later.
    """,
    entry_points = {
        'console_scripts': [
            'hwlog=hwlog.hwlog:hwlog_main',
        ],
    },
)
