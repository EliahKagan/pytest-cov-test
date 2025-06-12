#!/usr/bin/env python

import subprocess
import sys


def test_subprocess():
    proc = subprocess.run(
        [sys.executable, "reveal_interpreter.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert proc.stderr == f"{sys.executable=}\n"


def test_subprocess_nosite():
    proc = subprocess.run(
        [sys.executable, "-S", "reveal_interpreter.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert proc.stderr == f"{sys.executable=}\n"
