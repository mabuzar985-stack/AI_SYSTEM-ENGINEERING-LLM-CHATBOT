# Submission Guide — Prof. Roberto Pietrantuono

## What the professor's project instructions require

From the provided **AI Systems Engineering — Projects Guidelines** and the professor's submission instructions:

1. The project follows an innovation-driven workflow: requirements analysis, design, prototype development, continuous monitoring/testing, and local deployment.
2. The project should be a best-effort proof of concept rather than necessarily a complete production system.
3. Testing should include ML accuracy assessment where applicable and domain-appropriate quality testing.
4. The project is submitted through a GitHub repository.
5. The **PDF report must contain the GitHub link on the first page**.
6. The PDF filename must be the **SURNAME(s) of the team members**.
7. The PDF is submitted through the professor's Dropbox file-request link.

## Your final submission should therefore be

### 1. GitHub
A public GitHub repository containing the complete project code and documentation.

### 2. PDF
A PDF report whose first page contains the actual GitHub repository URL.

For one student, use a filename such as:

`ABUZAR.pdf`

### 3. Dropbox
Upload the PDF report to the professor's Dropbox request link. The professor's instructions state that the Dropbox request link expires **October 2 at 23:00**.

## Do NOT upload only the ZIP to GitHub

GitHub should show the actual project files and folders. The ZIP can be kept as your backup/submission package, but the repository should contain:

- `chatbot.py`
- `memory.py`
- `context.py`
- `agent.py`
- `rag.py`
- `vector_db.py`
- `mcp.py`
- `api.py`
- `alignment.py`
- `src_attention.py`
- `training/`
- `data/`
- `knowledge_base/`
- `tests/`
- `requirements.txt`
- `README.md`

## Final check before submitting

- [ ] Chatbot starts with `python chatbot.py`
- [ ] I asked several questions and received answers
- [ ] `memory.json` is created and remembers recent conversation
- [ ] `clear` removes conversation memory
- [ ] `pytest -q` passes
- [ ] GitHub repository is accessible
- [ ] PDF first page contains the actual GitHub URL
- [ ] PDF filename is `ABUZAR.pdf` (or surname(s) of all team members)
- [ ] PDF is uploaded through the professor's Dropbox request
- [ ] No API keys/passwords/private memory are in GitHub
