import pandas as pd
import statsmodels.api as sm


REQUIRED_COLUMNS = [
    "student_id",
    "study_hours",
    "attendance",
    "sleep_hours",
    "exam_score",
]


def run_analysis(data: pd.DataFrame) -> dict:
    """Run the preregistered linear regression analysis."""

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    data = data[REQUIRED_COLUMNS].copy()

    # Remove invalid/missing observations according to the preregistration.
    data = data.dropna(
        subset=[
            "student_id",
            "study_hours",
            "attendance",
            "sleep_hours",
            "exam_score",
        ]
    )

    model_data = data[
        (data["study_hours"] >= 0)
        & (data["attendance"] >= 0)
        & (data["attendance"] <= 100)
        & (data["sleep_hours"] >= 0)
        & (data["exam_score"] >= 0)
        & (data["exam_score"] <= 100)
    ].copy()

    X = model_data[
        ["study_hours", "attendance", "sleep_hours"]
    ]

    X = sm.add_constant(X)

    y = model_data["exam_score"]

    model = sm.OLS(y, X).fit()

    coefficient = model.params["study_hours"]
    confidence_interval = model.conf_int().loc["study_hours"]

    return {
        "effect_estimate": float(coefficient),
        "confidence_interval_lower": float(confidence_interval.iloc[0]),
        "confidence_interval_upper": float(confidence_interval.iloc[1]),
        "p_value": float(model.pvalues["study_hours"]),
        "sample_size": int(len(model_data)),
    }


if __name__ == "__main__":
    input_file = "data/raw/synthetic_students.csv"

    data = pd.read_csv(input_file)

    results = run_analysis(data)

    print(results)
