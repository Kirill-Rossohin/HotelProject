import sqlite3
import json
import csv
import os
import yaml
import xml.etree.ElementTree as ET
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "out")
DB = "hotels.db"
TABLE = "reservations"
 
conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row
 
 
def get_record(table, row):
    data = dict(row)
    data.pop("password_hash", None)
    for fk in conn.execute(f"PRAGMA foreign_key_list({table})").fetchall():
        column = fk["from"]
        parent_table = fk["table"]
        parent_column = fk["to"]

        value = data.pop(column)
        parent = conn.execute(
            f"SELECT * FROM {parent_table} WHERE {parent_column} = ?",
            (value,),
        ).fetchone()

        name = column.replace("_id", "")
        if parent is None:
            data[name] = None
        else:
            data[name] = get_record(parent_table, parent)
    return data
 
 
def flatten(data, prefix=""):
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            result.update(flatten(value, prefix + key + "_"))
        else:
            result[prefix + key] = value
    return result
 
 
def add_to_xml(parent, name, value):
    element = ET.SubElement(parent, name)
    if isinstance(value, dict):
        for k, v in value.items():
            add_to_xml(element, k, v)
    else:
        element.text = str(value)
 

rows = conn.execute(f"SELECT * FROM {TABLE}").fetchall()
records = [get_record(TABLE, row) for row in rows]
 
os.makedirs(OUT_DIR, exist_ok=True)

with open(os.path.join(OUT_DIR, "data.json"), "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

with open(os.path.join(OUT_DIR, "data.yaml"), "w", encoding="utf-8") as f:
    yaml.dump(records, f, allow_unicode=True, sort_keys=False)

flat = [flatten(r) for r in records]
fieldnames = []
for row in flat:
    for key in row:
        if key not in fieldnames:
            fieldnames.append(key)
if flat:
    with open(os.path.join(OUT_DIR, "data.csv"), "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(flat)

root = ET.Element(TABLE)
for record in records:
    add_to_xml(root, "item", record)
tree = ET.ElementTree(root)
ET.indent(tree)
tree.write(os.path.join(OUT_DIR, "data.xml"), encoding="utf-8", xml_declaration=True)