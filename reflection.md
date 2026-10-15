\# Lab 5 — Reflection on Static Code Analysis



\## 1. What is static code analysis?



Static code analysis examines source code without executing the program to identify potential programming defects, security vulnerabilities and style violations. It complements runtime testing because it can detect risky patterns and maintainability problems that may not appear during a particular test execution.



\## 2. What did Pylint, Bandit and Flake8 help identify?



Pylint identified code-quality problems such as missing docstrings, inconsistent naming, unused variables, mutable default arguments and exception-handling concerns. Bandit identified security risks including unsafe dynamic evaluation, weak hashing, insecure random-number generation, shell execution and hardcoded secrets. Flake8 identified style violations, including overlong lines and formatting problems.



\## 3. Which findings were most important to fix?



The shell execution and unsafe `eval()` findings were important because unsafe handling could allow unintended commands or code to execute. The hardcoded secret also required attention because credentials should not be embedded in source code or printed to the console. The insecure hash and random-number generation findings were addressed using more appropriate alternatives.



\## 4. How did the fixes improve the program?



The changes improved readability through consistent naming, documentation and formatting. They reduced security risks by removing unsafe evaluation and shell execution, replacing MD5 with SHA-256, using a security-oriented random generator and loading the token from an environment variable. The changes also improved function behavior by avoiding a mutable default argument and handling exceptions more specifically.



\## 5. What are the limitations of static analysis?



Static analysis can identify suspicious patterns but cannot prove that a program is entirely secure or correct. Its results need to be interpreted in context, and runtime tests are still required to verify actual behavior. External dependencies, configuration mistakes and logical errors may also require additional testing or review.



\## Conclusion



Using Pylint, Bandit and Flake8 together provided complementary checks for code quality, security and style. After the changes, the reported Pylint score was 9.84/10, Bandit reported no issues, and Flake8 reported zero violations. Pylint still reported a warning for the global statement, which remains documented as a limitation of the final version.



