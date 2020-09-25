from google.cloud.bigquery.schema import SchemaField
from google.cloud import bigquery


def get_schema_field(schema_dict):
    array = []

    for e in schema_dict:
        nested_array = []

        if e['type'] != 'RECORD':
            array.append(SchemaField(e['name'], e['type'], mode=e['mode']))
            continue

        for ne in e['fields']:
            nested_array.append(
                SchemaField(ne['name'], ne['type'], mode=ne['mode'])
            )

        array.append(
            SchemaField(
                e['name'],
                e['type'],
                mode=e['mode'],
                fields=nested_array
            )
        )

    return array