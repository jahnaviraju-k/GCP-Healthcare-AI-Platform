-- Average readmission rate by age group
SELECT
  CASE
    WHEN age < 40 THEN "Under 40"
    WHEN age BETWEEN 40 AND 60 THEN "40-60"
    ELSE "60+"
  END AS age_group,
  AVG(readmitted) AS avg_readmission_rate
FROM `your_project.healthcare_dataset.patients`
GROUP BY age_group;
