import pyrfc
import json
def rfc_read_table(conn,query,fields,table):
    result = conn.call("RFC_READ_TABLE", QUERY_TABLE=table, OPTIONS=query, FIELDS=fields)
    use_fields = result["FIELDS"]
    to_split = result["DATA"]
    data = []
    for row in to_split:
        temp = {}
        for field in use_fields:
            field_name = field["FIELDNAME"]
            field_offset = int(field["OFFSET"])
            field_length = int(field["LENGTH"])
            temp[field_name] = row["WA"][field_offset:field_offset + field_length].strip()
        data.append(temp)
    return data