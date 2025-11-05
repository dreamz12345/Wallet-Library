import pycouchdb
import json
import credentials

def connect_to_db(login, password, host):
    db_name = "bb-" + login
    server = pycouchdb.Server(f"https://{login}:{password}@{host}")
    db = server.database(db_name)
    return db

def get_all_records(db):
    records = []
    for data in db:
        if data["doc"].get("reservedModelType") == "Record":
            records.append(data)
    return records

def print_records(records):
    for record in records:
        print(json.dumps(record, indent=2))

def dump_db_to_file(db, filename="db_dump.json"):
    docs = [doc for doc in db.all()]
    with open(filename, "w") as f:
        json.dump(docs, f, indent=2)

def main():

    LOGIN = credentials.LOGIN
    PASSWORD = credentials.PASSWORD
    HOST = credentials.HOST

    db = connect_to_db(LOGIN, PASSWORD, HOST)

    records = get_all_records(db.all())
    print_records(records)







if __name__ == "__main__":
    main()
