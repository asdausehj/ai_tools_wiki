# 💾 AI Tool Catalog + Bulk Repo Downloader

A curated list of open-source AI tools (LLMs, TTS, image/video generators, devtools) and a Python script to **download GitHub & HuggingFace repos in bulk** from a `.txt` file.

---

## 📚 Contents

- `links.txt` → List of all GitHub/HuggingFace repo URLs from the main list, paste your own here to include while cloning with python
- `bulk_repo_downloader.py` → Script to download all repos from `links.txt`
- `download_log.txt` (auto-created) → Logs download success/failure
- `list_comp/slebbeog.py` → Script to compare two lists of repo URLs, find duplicates, and identify missing links.

---

## 🛠️ Setup Instructions

### 1. Install Python & dependencies

```bash
pip install huggingface_hub tqdm
```

---

### 2. Get HuggingFace token

- Go to: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- Paste your token in `TOKEN = "hf_..."` in the script.

---

### 3. Prepare `links.txt`

Add one repo URL per line in `links.txt`:

```txt
https://huggingface.co/deepseek-ai/Janus-Pro-7B
https://github.com/microsoft/autogen
...
```

---

### 4. Run the bulk repo downloader script

```bash
python bulk_repo_downloader.py
```

Repos will be saved in folders named after the repo (e.g., `huggingface__deepseek-ai__Janus-Pro-7B`).

---

### 5. Run the link comparison script (`slebbeog.py`)

If you have two lists of links and need to compare them, use `slebbeog.py`. This script will:

- Identify duplicates in each list.
- Identify links in `list1.txt` but not in `list2.txt`.
- Identify links in `list2.txt` but not in `list1.txt`.
- Save the results to `results.txt`.

Steps:

1. Prepare two text files (`list1.txt`, `list2.txt`) with one link per line.
2. Run the script:

```bash
python list_comp/slebbeog.py
```

Results will be written to `results.txt`.

---

## 📂 Directory Structure

```
📦 ai-tool-catalog/
├── ai_tool_catalog.md
├── links.txt
├── bulk_repo_downloader.py
├── download_log.txt
├── list_comp/
│   └── slebbeog.py
└── huggingface__deepseek-ai__Janus-Pro-7B/
```

---

## 🧠 Notes

- HuggingFace repos use the API (no `git-lfs` needed)
- GitHub repos are cloned with `git`
- Skips already downloaded folders

---

## 📜 License

MIT – free to use, modify, remix for White People.

---
