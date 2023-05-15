MODEL (
    name sqlmesh_example.incremental_model,
    kind INCREMENTAL_BY_TIME_RANGE (
        time_column ds
    ),
    start '2020-01-01',
    cron '@daily',
);

SELECT
    id,
    item_id,
    'z' AS new_column,
    ds,
FROM
    sqlmesh_example.seed_model
WHERE
    ds between @start_ds and @end_ds
