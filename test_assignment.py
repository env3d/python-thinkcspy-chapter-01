import subprocess
import pytest

@pytest.fixture(scope="module")
def qa_pairs():
    # Run main.py and collect non-empty output lines
    result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
    lines = [line.strip() for line in result.stdout.strip().splitlines() if line.strip()]
    
    # Group into (question, answer) pairs based on alternating lines
    return list(zip(lines[::2], lines[1::2]))

def test_capilanou_location(qa_pairs):
    q, a = qa_pairs[0]
    assert q.lower().startswith("> where is capilanou main campus")
    assert a.strip().lower() == "north vancouver"  # Correct answer

def test_douglas_adams_answer(qa_pairs):
    q, a = qa_pairs[1]
    assert "douglas adams" in q.lower()
    assert "answer to everything" in q.lower()
    assert a.strip() == "42"  # Correct canonical answer

def test_math_question(qa_pairs):
    q, a = qa_pairs[2]
    assert "2 + 2" in q
    assert a.strip() == "4"
