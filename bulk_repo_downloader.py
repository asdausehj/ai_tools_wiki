import os
import time
import subprocess
from huggingface_hub import hf_hub_download, login, list_repo_files
from pathlib import Path
from tqdm import tqdm

# === CONFIG ===
TOKEN = ""  # ← Put ur huggingface token there with read permissions
INPUT_FILE = "links.txt"
LOG_FILE = Path("download_log.txt")

# === SETUP ===
login(TOKEN)
LOG_FILE.touch(exist_ok=True)

def extract_hf_repo_id(url: str) -> str:
    parts = url.strip().split("/")
    if "huggingface.co" in url and len(parts) >= 5:
        return f"{parts[3]}/{parts[4]}"
    return None

def is_github_url(url: str) -> bool:
    return "github.com" in url and url.count("/") >= 4

def download_hf_model(repo_id: str, index: int, total: int):
    try:
        print(f"[{index}/{total}] ⬇️ HuggingFace: {repo_id}")
        target_dir = Path(repo_id.replace("/", "__"))
        target_dir.mkdir(exist_ok=True)

        files = list_repo_files(repo_id)
        for file in tqdm(files, desc=f"📦 {repo_id}", unit="file"):
            try:
                hf_hub_download(
                    repo_id=repo_id,
                    filename=file,
                    local_dir=target_dir,
                    local_dir_use_symlinks=False
                )
            except Exception as file_err:
                with open(LOG_FILE, "a") as log:
                    log.write(f"[❌ FILE ERROR] {repo_id} → {file} → {file_err}\n")
                print(f"❌ File failed: {file} — {file_err}")

        with open(LOG_FILE, "a") as log:
            log.write(f"[✅ HF SUCCESS] {repo_id} → {len(files)} files → {target_dir}\n")
        print(f"✅ HuggingFace complete: {repo_id}")
    except Exception as e:
        with open(LOG_FILE, "a") as log:
            log.write(f"[❌ HF ERROR] {repo_id} → {e}\n")
        print(f"❌ HuggingFace failed: {repo_id} — {e}")

def download_github_repo(url: str, index: int, total: int):
    try:
        parts = url.strip().rstrip("/").split("/")
        repo_name = parts[-1]
        org_name = parts[-2]
        target_dir = Path(f"github__{org_name}__{repo_name}")
        print(f"[{index}/{total}] ⬇️ GitHub: {org_name}/{repo_name}")
        if target_dir.exists():
            print(f"⚠️ Repo already exists: {target_dir}")
            return
        subprocess.run(["git", "clone", url, str(target_dir)], check=True)
        with open(LOG_FILE, "a") as log:
            log.write(f"[✅ GH SUCCESS] {url} → {target_dir}\n")
        print(f"✅ GitHub complete: {url}")
    except subprocess.CalledProcessError as e:
        with open(LOG_FILE, "a") as log:
            log.write(f"[❌ GIT ERROR] {url} → {e}\n")
        print(f"❌ GitHub failed: {url} — {e}")

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"⚠️ File '{INPUT_FILE}' not found.")
        return

    with open(INPUT_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    total = len(urls)

    for i, url in enumerate(urls, start=1):
        try:
            if "huggingface.co" in url:
                repo_id = extract_hf_repo_id(url)
                if repo_id:
                    download_hf_model(repo_id, i, total)
                else:
                    raise ValueError("Invalid HuggingFace URL format.")
            elif is_github_url(url):
                download_github_repo(url, i, total)
            else:
                raise ValueError("Unsupported URL format.")
        except Exception as e:
            with open(LOG_FILE, "a") as log:
                log.write(f"[❌ URL ERROR] {url} → {e}\n")
            print(f"❌ Invalid URL: {url} — {e}")
        time.sleep(1)

if __name__ == "__main__":
    main()