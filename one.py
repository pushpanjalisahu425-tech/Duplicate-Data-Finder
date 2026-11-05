# =========================================================
#  ✨ PROJECT TITLE: DUPLICATE DATA FINDER ✨
# ---------------------------------------------------------
#  📝 STUDENT DETAILS:
#  • Name         : Pushpanjali Sahu
#  • ERP No.      : Ru_26_00491
#  • Section      : B
#  • University   : Rungta International Skills University
#
#  👨‍🏫 SUBMITTED TO:
#  • Faculty      : Satyaprakash Sir
# =========================================================

import os
from collections import Counter

def process_duplicate_finder():
    # -----------------------------------------------------
    # 📌 STEP 1: USER INPUT & FILE HANDLING
    # -----------------------------------------------------
    filename = input("Enter file name: ").strip()

    # Handling Test Case 3(a): File does not exist
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. Please enter a valid file name.")
        return

    try:
        with open(filename, 'r') as file:
            # Lines ko read karke empty lines remove karna
            lines = [line.rstrip('\n') for line in file if line.strip() != '']
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Handling Test Case 3(b): Empty file
    if not lines:
        print("File is empty. Nothing to check.")
        return

    # -----------------------------------------------------
    # 📌 STEP 2: SELECT MODE / MENU OPTION
    # -----------------------------------------------------
    print("\nSelect Option:")
    print("1. Option 1 (Exact match)")
    print("2. Option 2 (Ignore case and extra spaces)")
    choice = input("Enter option (1 or 2): ").strip()

    # -----------------------------------------------------
    # 📌 STEP 3: DATA PROCESSING LOGIC
    # -----------------------------------------------------
    processed_items = []
    
    if choice == '2':
        # Option 2: Case strip & extra spaces remove karna
        for item in lines:
            clean_item = " ".join(item.split()).lower()
            processed_items.append(clean_item)
    else:
        # Option 1: Exact match (Original values keep karna)
        processed_items = [line.strip() for line in lines]

    total_items = len(processed_items)
    unique_set = set(processed_items)
    unique_items_count = len(unique_set)

    # -----------------------------------------------------
    # 📌 STEP 4: OUTPUT DISPLAY & DUPLICATES COUNTING
    # -----------------------------------------------------
    print(f"\nTotal items: {total_items} | Unique items: {unique_items_count}")

    # Duplicates calculate karna using Counter logic
    counts = Counter(processed_items)
    duplicates = [f"{item} ({count} times)" for item, count in counts.items() if count > 1]

    if duplicates:
        print("Duplicates: " + " | ".join(duplicates))
        
        # Unique list ko unique.txt me save karna
        try:
            with open("unique.txt", "w") as out_file:
                for item in set(lines if choice == '1' else processed_items):
                    out_file.write(item + "\n")
            print("Unique list saved to unique.txt")
        except Exception as e:
            print(f"Error saving file: {e}")
    else:
        print("No duplicates found.")

# =========================================================
# 🚀 MAIN EXECUTION BLOCK
# =========================================================
if __name__ == "__main__":
    process_duplicate_finder()
