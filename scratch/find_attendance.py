from backend.firebase_service import get_firestore

db = get_firestore()

print("--- COLLECTIONS DISCOVERY ---")
collections = db.collections()
for coll in collections:
    print(f"ROOT COLLECTION: '{coll.id}'")
    docs = list(coll.limit(10).stream())
    print(f"  Found {len(docs)} documents (limit 10)")
    for doc in docs:
        print(f"    - {doc.id}")
        # List sub-collections
        sub_colls = doc.reference.collections()
        for sub in sub_colls:
            print(f"      - Sub-coll: '{sub.id}'")
            sub_docs = list(sub.limit(5).stream())
            for sd in sub_docs:
                print(f"        - Sub-doc: {sd.id}")

print("--- END ---")
