"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    pass


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    pass


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    pass


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    # TODO: implement
    pass
def average_per_student(records: list[dict]) -> dict[str, float]:
    student_data = {}
    for r in records:
        name = r["name"]
        score = r["score"]
        if name not in student_data:
            student_data[name] = []
        student_data[name].append(score)
    return {name: round(sum(scores) / len(scores), 2) for name, scores in student_data.items()}

def subjects_offered(records: list[dict]) -> set[str]:
    return {r["subject"] for r in records}

def top_scorer(records: list[dict]) -> tuple[str, float]:
    averages = average_per_student(records)
    if not averages:
        return ("", 0.0)
    top_student = max(averages, key=averages.get)
    return (top_student, averages[top_student])

def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    averages = average_per_student(records)
    passers = [name for name, avg in averages.items() if avg >= threshold]
    return sorted(passers)