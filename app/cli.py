import argparse
from openai import OpenAIError
from .service import search, request_change
from .model import OpenAIModel

def main():
    p = argparse.ArgumentParser(description="Policy knowledge assistant with OpenAI answers")
    sub = p.add_subparsers(dest="command", required=True)
    for name in ("search", "ask"):
        q = sub.add_parser(name); q.add_argument("--user", required=True); q.add_argument("--query", required=True)
    c = sub.add_parser("request-change"); c.add_argument("--user", required=True); c.add_argument("--doc", required=True); c.add_argument("--field", required=True); c.add_argument("--value", required=True)
    a = p.parse_args()
    if a.command == "request-change":
        print(request_change(a.user, a.doc, a.field, a.value)); return
    docs = search(a.user, a.query)
    if a.command == "search":
        for d in docs: print(f'[{d["id"]}] {d["title"]}: {d["text"]}')
    else:
        try:
            print(OpenAIModel().answer(a.query, docs))
        except (OpenAIError, ValueError) as error:
            p.exit(1, f"Answer generation failed: {error}\n")
        if docs: print("Sources: " + ", ".join(d["id"] for d in docs))

if __name__ == "__main__": main()
