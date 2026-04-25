AI Problem Solving Repository

 Project Overview
This repository contains implementations of Artificial Intelligence problem-solving techniques using Python.  
Each problem is structured clearly with description, algorithm, implementation, and output.

 Problem 4: Crypt Arithmetic Puzzle Solver (CSP)

 Problem Description
Cryptarithmetic puzzles are mathematical problems where digits are replaced by letters.

Example:
SEND + MORE = MONEY

Each letter represents a unique digit (0–9).  
The goal is to assign digits to letters such that the arithmetic equation is correct.

---

 Objectives
- Accept user input dynamically
- Solve using AI techniques
- Ensure all constraints are satisfied
- Display valid mappings and results

---

 Constraints
- Each letter must map to a **unique digit**
- Digits range from **0–9**
- No number should start with **0**
- The equation must be mathematically valid

---

 Algorithm Used
 Constraint Satisfaction Problem (CSP)

We model the puzzle as a CSP:
- Variables:** Letters (S, E, N, D, M, O, R, Y)
- Domain:** Digits (0–9)
-Constraints:**
  - All letters have different values
  - Leading letters ≠ 0
  - Sum of terms equals result
 Approach:
1. Extract all unique letters
2. Generate permutations of digits
3. Assign digits to letters
4. Check constraints
5. Validate equation
6. Return solution

 Flow of Execution
1. User enters puzzle
2. Program extracts letters
3. Generates possible digit combinations
4. Filters invalid assignments
5. Checks arithmetic correctness
6. Displays solution

 Technologies Used
- Python
- itertools (for permutations)
- website link : https://vaishnavimanimaran.github.io/AI_ProblemSolving_RA2411026050237/


