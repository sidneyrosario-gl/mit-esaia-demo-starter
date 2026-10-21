"""Core application logic. Candidate implementation point: enforce authorization."""
import json
from pathlib import Path

import yaml

DATA = Path(__file__).parent / "data"
ALLOWED_CHANGE_FIELDS = {"owner", "text"}

def load_json(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))

def documents():
    policies = []
    for path in sorted(DATA.glob("*.md")):
        content = path.read_text(encoding="utf-8")
        sections = content.split("---", 2)
        if len(sections) != 3 or sections[0].strip():
            raise ValueError(f"Policy {path.name} must start with YAML front matter")
        metadata = yaml.safe_load(sections[1])
        if not isinstance(metadata, dict):
            raise ValueError(f"Policy {path.name} must contain metadata")
        policies.append({**metadata, "text": sections[2].strip()})
    return policies

def user_groups(user):
    users = load_json("users.json")
    if user not in users:
        raise ValueError("Unknown user")
    return set(users[user])

def search(user, query):
    """Return relevant documents visible to user. TODO: enforce access before ranking."""
    terms = set(query.lower().split())
    # INTENTIONAL GAP: current implementation searches all documents.
    ranked = []
    for doc in documents():
        score = sum(term in doc["text"].lower() or term in doc["title"].lower() for term in terms)
        if score:
            ranked.append((score, doc))
    return [doc for _, doc in sorted(ranked, key=lambda pair: (-pair[0], pair[1]["id"]))]

def request_change(user, doc_id, field, value):
    """Validate proposed changes. TODO: authorization, validation, and safe recording."""
    user_groups(user)  # validates identity only
    # INTENTIONAL GAP: add owner/group authorization, field/value checks and no silent mutation.
    return {"status": "accepted", "requested_by": user, "document_id": doc_id, "field": field, "value": value}
