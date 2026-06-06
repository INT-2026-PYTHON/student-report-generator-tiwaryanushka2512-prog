"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass
from .stats import average_per_student, subjects_offered, top_scorer, passing_students

def format_report(records: list[dict]) -> str:
    total_records = len(records)
    sorted_subjects = sorted(list(subjects_offered(records)))
    subjects_str = ", ".join(sorted_subjects)
    
    averages = average_per_student(records)
    averages_lines = []
    for student in sorted(averages.keys()):
        averages_lines.append(f"  {student} : {averages[student]}")
    averages_str = "\n".join(averages_lines)
    
    top_name, top_avg = top_scorer(records)
    passers = passing_students(records, threshold=60.0)
    passers_str = ", ".join(passers)
    
    report = (
        f"=== Gradebook Report ===\n"
        f"Total records: {total_records}\n"
        f"Subjects offered: {subjects_str}\n\n"
        f"Averages:\n{averages_str}\n\n"
        f"Top scorer: {top_name} ({top_avg})\n"
        f"Passing students (>= 60.0): {passers_str}"
    )
    return report