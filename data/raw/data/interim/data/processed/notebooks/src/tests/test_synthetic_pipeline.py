import pandas as pd

from src.pipeline import run_analysis


def test_synthetic_pipeline_output_contract():
    """Verify that the synthetic pipeline produces the required outputs."""

    synthetic_data = pd.DataFrame(
        {
            "student_id": range(1, 11),
            "study_hours": [4, 6, 8, 10, 12, 5, 7, 9, 11, 14],
            "attendance": [70, 75, 80, 85, 90, 72, 78, 83, 88, 94],
            "sleep_hours": [6, 6, 7, 7, 8, 6, 7, 7, 8, 8],
            "exam_score": [50, 57, 64, 72, 80, 53, 61, 68, 75, 87],
        }
    )

    results = run_analysis(synthetic_data)

    expected_keys = {
        "effect_estimate",
        "confidence_interval_lower",
        "confidence_interval_upper",
        "p_value",
        "sample_size",
    }

    assert set(results.keys()) == expected_keys

    assert isinstance(results["effect_estimate"], float)
    assert isinstance(results["confidence_interval_lower"], float)
    assert isinstance(results["confidence_interval_upper"], float)
    assert isinstance(results["p_value"], float)
    assert isinstance(results["sample_size"], int)

    assert results["sample_size"] == 10
