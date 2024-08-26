# external includes.
import pyrfc
import json

# internal includes
import connect
import rfc_read_table

#opening connection to sap
conn = connect.connect()

#setting up query and other options to rfc_read_table
query = [{ "TEXT": "MATNR EQ '3HAC080600-001'"}]
query = query + [{"TEXT": " AND SPRAS EQ 'E'"}]
fields = ["MATNR", "SPRAS", "MAKTX"]
table = "MAKT"

# Fetching information from sap and storing it in "data"
data = rfc_read_table.rfc_read_table(conn,query,fields,table)

for row in data:
    print(row)


