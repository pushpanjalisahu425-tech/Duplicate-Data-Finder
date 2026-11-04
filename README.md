# Duplicate Data Finder

## Project overview
A Python 3 console application that reads a text file containing one entry per line, finds duplicate entries, reports the total and unique item counts, and saves the first occurrence of each unique entry to `unique.txt`.

## Features
- Reads a user-provided text file (one entry per line).
- Handles a missing file and an empty file with clear messages.
- **Option 1 – Exact match:** treats uppercase/lowercase differences as different entries.
- **Option 2 – Ignore case and extra spaces:** compares entries without case sensitivity and removes leading/trailing spaces before comparing.
- Uses a list, a set-equivalent membership check through comparison keys, loops, and file handling.
- Preserves the order of first appearance in `unique.txt`.
- Reports duplicates with their total occurrence count (for example, `apple (3 times)`).

## Requirements
- Python 3.8 or later
- No external packages required

## Files
- `one.py` – complete application
- `README.md` – project documentation
- `unique.txt` – generated output file (created when a non-empty input file is processed)

## How to run
1. Place `one.py` and your input text file in the same folder, or enter the input file's path when prompted.
2. Open a terminal in that folder.
3. Run:
   ```bash
   python one.py
   ```
4. Choose `1` for exact matching or `2` to ignore case and extra spaces.
5. Enter the input file name, such as `data.txt`.
6. Check the summary on screen and open `unique.txt` for the saved unique entries.

## Example input (`data.txt`)
```text
apple
banana
apple
orange
banana
apple
```

## Expected result for Option 1
```text
Total items: 6 | Unique items: 3
Duplicates: apple (3 times) | banana (2 times)
Unique list saved to unique.txt
```

## Test coverage
The four test cases supplied in the project statement are exercised in `test_results.txt`:
1. Normal input with repeated apple and banana entries.
2. One-line input with no duplicates.
3. Missing input file and empty input file.
4. Case-insensitive input (`Apple`, `apple`, `APPLE`, etc.).

## Notes
- Blank lines are ignored because they do not contain an entry.
- In Option 2, the first spelling/capitalization encountered is retained in `unique.txt` and in the duplicate label.
- Duplicate counts show total occurrences, matching the supplied examples.
