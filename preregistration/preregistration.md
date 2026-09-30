Analysis Preregistration
Research Question

Among students during one academic term, is weekly study time associated with final exam score?

The research question and analysis plan are specified before examining the relationship between study time and exam score.

Hypotheses
Null hypothesis (H₀)

There is no association between weekly study time and final exam score.

H₀: β = 0

Alternative hypothesis (H₁)

There is an association between weekly study time and final exam score.

H₁: β ≠ 0

Expected direction

A positive association is expected: students who report more weekly study hours are expected to have higher final exam scores.

This expected direction is based on the substantive hypothesis that additional study time may be associated with improved academic performance.

Population, Sample, and Exclusions
Target population

The target population is students enrolled in an academic course during one academic term.

Unit of analysis

The unit of analysis is one student.

Inclusion criteria

A student will be included if:

A valid student identifier is present.

Weekly study hours are available.

Final exam score is available.

Exclusion criteria

A student will be excluded if:

The student identifier is missing.

Weekly study hours are missing or invalid.

Final exam score is missing or invalid.

The same student appears more than once; only the pre-specified unique observation will be retained.

Observations will not be excluded based on the observed exam score or statistical significance.

Stopping rule

The complete synthetic dataset satisfying the inclusion criteria will be analyzed. No observations will be added or removed based on the observed results.

Variables and Measures
Primary outcome

Variable: exam_score

The primary outcome is the student's final exam score, measured on a 0–100 scale.

The outcome is continuous.

Primary predictor

Variable: study_hours

The primary predictor is the student's reported weekly study time, measured in hours per week.

The predictor will be treated as a continuous variable.

Control variables

The primary model will adjust for:

attendance

sleep_hours

Attendance will represent the percentage of classes attended.

Sleep hours will represent average hours of sleep per night.

Transformations

No transformation will be applied to study_hours, attendance, or sleep_hours in the primary analysis.

The outcome exam_score will remain on its original 0–100 scale.

Missing-data handling

Observations missing the primary outcome or primary predictor will be excluded from the primary analysis.

The number and percentage of missing values will be reported.

Analysis Plan
Descriptive analysis

The following will be reported:

Number of students

Mean and standard deviation of exam score

Mean and standard deviation of study hours

Mean and standard deviation of attendance

Mean and standard deviation of sleep hours

Missing-data counts and percentages

Primary statistical analysis

The primary analysis will use multiple linear regression.

The model will estimate the association between weekly study hours and final exam score while adjusting for attendance and sleep hours.

The model will be specified as:

exam_score = β₀ + β₁(study_hours) + β₂(attendance) + β₃(sleep_hours) + ε

The primary parameter of interest is β₁, the estimated change in exam score associated with one additional hour of weekly study time, holding the pre-specified controls constant.

Statistical assumptions

The following assumptions will be assessed:

Independence of observations

Approximately linear relationship between predictors and outcome

Approximately normally distributed residuals

Constant residual variance

Absence of problematic multicollinearity

Significance level

The primary analysis will use:

α = 0.05

The hypothesis test will be two-sided.

Effect size

The primary effect size will be the regression coefficient for study_hours.

The effect estimate will be reported with a 95% confidence interval.

Uncertainty interval

A 95% confidence interval will be reported for the primary study-hours coefficient.

Robustness checks

The following robustness checks will be performed:

Compare the primary regression results with a model using study hours as the only predictor.

Examine whether influential observations materially affect the estimated study-hours coefficient.

Repeat the analysis using robust standard errors if heteroscedasticity is detected.

Examine residual plots and alternative functional forms.

Any additional analysis not specified here will be labeled exploratory.

Synthetic Data and Data-Blind Pipeline

Because no real internship dataset was provided, this project will use a synthetic dataset created for demonstrating a reproducible research workflow.

The synthetic data will be used to test the analysis pipeline before any outcome pattern is inspected.

The synthetic pipeline will verify that:

Required input columns are present.

Invalid observations are handled according to the preregistration.

Missing values are handled according to the preregistration.

Variables are transformed correctly.

The primary regression model runs successfully.

The expected effect estimate is produced.

A 95% confidence interval is produced.

A p-value is produced.

The sample size is reported.

The pipeline produces a consistent output structure.

Expected output contract

The primary analysis must produce:

effect_estimate
confidence_interval_lower
confidence_interval_upper
p_value
sample_size

Deviations

Any deviation from this preregistered plan will be documented with:

Timestamp	Section	Original plan	Deviation	Reason	Impact
YYYY-MM-DD HH:MM	[Section]	[Original plan]	[Change]	[Reason]	[Impact]

Additional analyses performed after examining outcome relationships will be explicitly labeled as exploratory.

Reproducibility

The project will use Python and version-controlled source code.

The repository will contain:

Raw data

Interim data

Processed data

Analysis notebooks

Source code

Automated tests

Reports

Results

Environment configuration

The synthetic dataset and analysis pipeline will be reproducible using the documented environment.
