from google.cloud import bigquery
import utils
import json
import glob

client = bigquery.Client()


job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,
    allow_quoted_newlines=True,
    time_partitioning=bigquery.TimePartitioning()
)

with open('./schema.json', 'r', encoding='utf-8') as f:
    json_str = f.read()
job_config.schema = utils.get_schema_field(json.loads(json_str))


path = "../some/dir/*"
files = glob.glob(path + '*')

for file_name in files:
    date = file_name.split('_')[-1][0:8]
    print(file_name)
    print(date)
    table_id = 'dataset.table$' + date

    with open(file_name, "rb") as source_file:
        job = client.load_table_from_file(
            source_file,
            table_id,
            job_config=job_config
    )

    job.result()  # Waits for the job to complete.

    table = client.get_table(table_id)  # Make an API request.
    print(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id
        )
    )
