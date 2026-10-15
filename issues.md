\# Lab 5 — Static Code Analysis Issue Table



\*\*File analysed:\*\* `flight\_reservation\_system.py`



\*\*Tools used:\*\* Pylint, Bandit and Flake8



\*Line numbers below refer to the original source file before the fixes.\*



| Issue | Type | Line(s) | Description | Fix Approach |

|---|---|---|---|---|

| Shell command execution (B605) | Security — High | 63 | `os.system()` executed a shell command using string concatenation, creating a command-injection risk. | Replaced shell execution with native Python output. |

| Weak MD5 hash (B324) | Security — High | 52 | MD5 is unsuitable when collision resistance is required. | Replaced MD5 with SHA-256 for the passenger hash. |

| Unsafe `eval()` (B307) | Security — Medium | 46–48 | `eval()` could execute arbitrary code supplied as an expression. | Replaced dynamic evaluation with a controlled calculation. |

| Insecure PIN generation (B311) | Security | 55–56 | The standard `random` generator is not intended for security-sensitive random values. | Replaced it with `secrets.SystemRandom()` for PIN generation. |

| Hardcoded secret (B105) | Security | 75 | A secret token was embedded in the source code. | Loaded the token through an environment variable and stopped printing its plaintext value. |

| Mutable default argument (W0102) | Code quality / defect | 15 | A mutable list used as a default argument could retain state between function calls. | Changed the default to `None` and initialized the list inside the function. |

| Bare exception handling (W0702 / E722) | Code quality | 31 | A bare exception could conceal unexpected errors. | Replaced it with specific exception handling. |

| Missing docstrings and naming violations | Code quality | Multiple | Missing documentation and non-standard identifiers reduced readability and maintainability. | Added docstrings and renamed functions and variables to follow Python naming conventions. |

| Overlong lines and formatting violations | Style | Multiple | Several lines exceeded the configured line-length limit. | Reformatted the code and reran Flake8. |



\## Final Verification



| Tool | Final result |

|---|---|

| Pylint | 9.84/10; W0603 remains for the global statement |

| Bandit | No issues identified |

| Flake8 | Zero violations reported |



The final source file was executed successfully according to the recorded runtime test. The three tools were rerun after the changes to verify code quality, security and formatting.



