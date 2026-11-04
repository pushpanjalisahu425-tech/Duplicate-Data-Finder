"""Duplicate Data Finder

Reads one entry per line from a text file, identifies repeated entries,
optionally compares entries without regard to case/extra spaces, and writes
first-occurrence unique entries to unique.txt.

Run: python one.py
"""


def read_entries(file_name):
    """Read non-empty lines from a text file and return them as a list.

    Leading/trailing whitespace is removed from each entry. Blank lines are
    ignored so they are not treated as data entries.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            entries = []
            for line in file:
                # Remove only the line ending. Keep other spaces so Option 1
                # can perform an exact comparison; Option 2 trims them later.
                entry = line.rstrip("\r\n")
                if entry.strip() != "":
                    entries.append(entry)
            return entries
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Please enter a valid file name.")
        return None


def make_comparison_key(entry, ignore_case):
    """Return the key used for comparing two entries."""
    if ignore_case:
        return entry.strip().casefold()  # Option 2 ignores outer spaces and case.
    return entry  # Option 1 compares the complete entry exactly.


def analyze_entries(entries, ignore_case):
    """Return unique entries and duplicate counts, preserving input order.

    A duplicate count is the total number of occurrences, e.g. 'apple
    (3 times)' means apple appeared three times in the input file.
    """
    unique_entries = []
    comparison_keys = []
    occurrence_counts = []

    for entry in entries:
        key = make_comparison_key(entry, ignore_case)

        # Find whether this comparison key has already been recorded.
        if key in comparison_keys:
            position = comparison_keys.index(key)
            occurrence_counts[position] += 1
        else:
            comparison_keys.append(key)
            unique_entries.append(entry.strip() if ignore_case else entry)
            occurrence_counts.append(1)

    duplicates = []
    for index in range(len(unique_entries)):
        if occurrence_counts[index] > 1:
            duplicates.append((unique_entries[index], occurrence_counts[index]))

    return unique_entries, duplicates


def save_unique_entries(unique_entries, output_file="unique.txt"):
    """Save unique entries to a new text file, one entry per line."""
    with open(output_file, "w", encoding="utf-8") as file:
        for entry in unique_entries:
            file.write(entry + "\n")


def display_results(entries, unique_entries, duplicates, output_file):
    """Print the summary in a clear, consistent format."""
    print(f"Total items: {len(entries)} | Unique items: {len(unique_entries)}")

    if len(duplicates) == 0:
        print("No duplicates found")
    else:
        duplicate_text = []
        for entry, count in duplicates:
            duplicate_text.append(f"{entry} ({count} times)")
        print("Duplicates: " + " | ".join(duplicate_text))

    print(f"Unique list saved to {output_file}")


def main():
    """Run the Duplicate Data Finder menu-driven application."""
    print("=" * 42)
    print("          DUPLICATE DATA FINDER")
    print("=" * 42)
    print("1. Exact match")
    print("2. Ignore case and extra spaces")

    choice = input("Enter menu option (1 or 2): ").strip()
    if choice not in ("1", "2"):
        print("Invalid menu option. Please choose 1 or 2.")
        return

    file_name = input("Enter input file name: ").strip()
    if file_name == "":
        print("File name cannot be empty. Please enter a valid file name.")
        return

    entries = read_entries(file_name)
    if entries is None:
        return

    if len(entries) == 0:
        print("File is empty. Nothing to check.")
        return

    ignore_case = (choice == "2")
    unique_entries, duplicates = analyze_entries(entries, ignore_case)

    output_file = "unique.txt"
    save_unique_entries(unique_entries, output_file)
    display_results(entries, unique_entries, duplicates, output_file)


if __name__ == "__main__":
    main()
