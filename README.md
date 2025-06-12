# pytest-cov-test - Simplified demonstration of GitPython#2052

This is a simplified demonstration of the mechanism underlying the bug fixed in
[gitpython-developers/GitPython#2052](https://github.com/gitpython-developers/GitPython/pull/2052)
where a test that runs a subprocess, making an assertion about what the
subprocess writes to stderr, can fail due to `CoverageWarning` messages
produced in the subprocess by `pytest-cov`.

## The failure

As there, it is specifically on Cygwin that this currently fails, since the
warning is not typically generated otherwise. The failure looks like:

```text
>       assert proc.stderr == f"{sys.executable=}\n"
E       assert "/home/ek/rep...bin/python'\n" == "sys.executab...bin/python'\n"
E
E         + /home/ek/repos-cygwin/pytest-cov-test/.venv/lib/python3.9/site-packages/coverage/core.py:96: CoverageWarning: Couldn't import C tracer: No module named 'coverage.tracer' (no-ctracer)
E         +   warn(f"Couldn't import C tracer: {IMPORT_ERROR}", slug="no-ctracer", once=True)
E           sys.executable='/home/ek/repos-cygwin/pytest-cov-test/.venv/bin/python'

test_indirect.py:14: AssertionError
```

## License

[0BSD](LICENSE)
