import os
import sys

# Add current directory to path
sys.path.append(os.getcwd())

try:
    from config.firebase_config import get_firestore
    db = get_firestore()
    print("Firestore connected.")
    
    classes_ref = db.collection("classes")
    docs = list(classes_ref.stream())
    print(f"Found {len(docs)} classes.")
    for doc in docs:
        print(f"Class: {doc.id} => {doc.to_dict()}")

    users_ref = db.collection("users")
    docs = list(users_ref.where("role", "==", "student").stream())
    print(f"Found {len(docs)} students.")

except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
