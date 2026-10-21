# Knowledge Assistant Challenge (Starter)

This is a small enterprise knowledge assistant with local retrieval and real OpenAI answer generation.

## Setup

You will need a OpenAI API key with some credit for this application. Copy `.env.example` to `.env`. Set `OPENAI_API_KEY` in `.env` to an API key with access to the configured model. `OPENAI_MODEL` defaults to `gpt-4.1-mini`; change it to another Responses API-compatible model available to your account.

## Run

```powershell
python -m app.cli search --user alice --query "expense approval"
python -m app.cli ask --user alice --query "What is the travel meal limit?"
```

## Visible tests

```powershell
python -m unittest discover -s tests -v
```

## Data model

Each policy is a separate Markdown document in `app/data/`, with YAML front matter
containing `id`, `title`, `allowed_groups`, and `owner`. The loader exposes the
Markdown body as `text`, preserving the document dictionary interface used by
retrieval and the model. Edit policy prose in these files, not in a JSON corpus.
Users and group membership are defined in `app/data/users.json`. 