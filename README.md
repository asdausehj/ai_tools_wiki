# 💾 AI Tool & Model Catalog for MVPs and Development in general

A curated and structured overview of all the **AI models, tools, and platforms** worth noticing, sorted by use case and accessibility. Some scripts for easy repo cloning etc included. 🚬



## 📚 Contents

- [⚠️Setup Instructions, scripts, notes, licensing](#setup-instructions)⚠️
.
.
.
- [🧠 Language Models & Coding Assistants](#-language-models--coding-assistants)

- [🧩 Reasoning, Agents & Tools](#-reasoning-agents--tools)

- [🗣️ Text-to-Speech (TTS)](#️-text-to-speech-tts)

- [🧾 Text2SQL / Querying Natural Language](#-text2sql--querying-natural-language)

- [🎥 Video & Image Generation / Editing](#-video--image-generation--editing)

- [📄 UI / PDF / Frontend Tools](#-ui--pdf--frontend-tools)

- [😈 Deepfake, Face Editing & Identity AI](#-deepfake-face-editing--identity-ai)

- [🔧 Other Dev Tools & APIs](#-other-dev-tools--apis)

- [🗃️ Repos (GitHub + HuggingFace) – Raw List](#repos-github--huggingface---raw-list)

- [🌐 SaaS / Online Tools – Raw List](#-saas--online-tools---raw-list)











## 🧠 Language Models & Coding Assistants

### 🔧 Run Locally:

| Name                | Link                                                                                                                               | Notes                                  |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Janus-Pro-7B        | [https://huggingface.co/deepseek-ai/Janus-Pro-7B](https://huggingface.co/deepseek-ai/Janus-Pro-7B)                                 | Coding & general-purpose LLM           |
| Qwen2.5-Coder-7B    | [https://huggingface.co/Qwen/Qwen2.5-Coder-7B](https://huggingface.co/Qwen/Qwen2.5-Coder-7B)                                       | High performance coding model          |
| Codestral-22B       | [https://huggingface.co/mistralai/Codestral-22B-v0.1](https://huggingface.co/mistralai/Codestral-22B-v0.1)                         | HuggingFace gated, requires acceptance |
| WizardCoder-15B     | [https://huggingface.co/WizardLMTeam/WizardCoder-15B-V1.0](https://huggingface.co/WizardLMTeam/WizardCoder-15B-V1.0)               | Powerful for Python-heavy tasks        |
| CodeLlama-34B       | [https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf](https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf)           | Meta's strong open-source coding model |
| DeepSeek Coder 6.7B | [https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) | Fast & clean coder                     |
| Mixtral-8x7B        | [https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)         | Sparse mixture-of-experts, very good   |
| Mistral-7B          | [https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)             | Efficient & compact                    |
| Gemma 7B            | [https://huggingface.co/google/gemma-7b](https://huggingface.co/google/gemma-7b)                                                   | Good general-purpose LLM               |
| Orca-2-13B          | [https://huggingface.co/microsoft/Orca-2-13b](https://huggingface.co/microsoft/Orca-2-13b)                                         | Reasoning-enhanced model               |
| Falcon-40B-Instruct | [https://huggingface.co/tiiuae/falcon-40b-instruct](https://huggingface.co/tiiuae/falcon-40b-instruct)                             | Strong pre-2024 open model             |

### 🌐 SaaS / Online:

| Name     | Link                                                                                               | Notes                                                |
| -------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| DeepSite | [https://huggingface.co/spaces/enzostvs/deepsite](https://huggingface.co/spaces/enzostvs/deepsite) | Online UI/code generation demo                       |
| Cursor   | [https://cursor.sh](https://cursor.sh)                                                             | AI-first IDE with built-in code assistant (Paid)     |
| Replit   | [https://replit.com](https://replit.com)                                                           | Browser-based collaborative coding (Freemium)        |
| Bolt AI  | [https://bolt.ghost.io](https://bolt.ghost.io)                                                     | Local-first AI devtools (Free)                       |
| Lovable  | [https://www.lovable.so](https://www.lovable.so)                                                   | Natural language coding UI (Paid)                    |
| Windsurf | [https://windsurf.ai](https://windsurf.ai)                                                         | Team-native AI code assistant with memory (Waitlist) |

---

## 🧩 Reasoning, Agents & Tools

### 🔧 Run Locally:

| Name                        | Link                                                                                                                     | Notes                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| Phi-4 Reasoning Plus        | [https://huggingface.co/microsoft/Phi-4-reasoning-plus](https://huggingface.co/microsoft/Phi-4-reasoning-plus)           | Small but powerful for logic/reasoning   |
| DeepSeek Prover             | [https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-671B](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-671B) | Deductive reasoning model                |
| OpenCodeReasoning (Dataset) | [https://huggingface.co/datasets/nvidia/OpenCodeReasoning](https://huggingface.co/datasets/nvidia/OpenCodeReasoning)     | Training/inference reference set         |
| Nemotron CrossThink         | [https://huggingface.co/datasets/nvidia/Nemotron-CrossThink](https://huggingface.co/datasets/nvidia/Nemotron-CrossThink) | Reasoning dataset                        |
| LangGraph                   | [https://github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)                                   | Conversational memory flow orchestration |
| AutoGen                     | [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen)                                             | Multi-agent coding framework             |
| AutoGen Studio              | [https://github.com/microsoft/autogen-studio](https://github.com/microsoft/autogen-studio)                               | GUI for Microsoft AutoGen                |
| DB-GPT                      | [https://github.com/eosphoros-ai/DB-GPT](https://github.com/eosphoros-ai/DB-GPT)                                         | AI chatbot connected to your DB          |

---

## 🗣️ Text-to-Speech (TTS)

### 🔧 Run Locally:

| Name         | Link                                                                               | Notes                                   |
| ------------ | ---------------------------------------------------------------------------------- | --------------------------------------- |
| XTTS v2      | [https://huggingface.co/coqui/XTTS-v2](https://huggingface.co/coqui/XTTS-v2)       | Advanced multilingual voice cloning     |
| XTTS v1      | [https://huggingface.co/coqui/XTTS-v1](https://huggingface.co/coqui/XTTS-v1)       | Lighter version of XTTS v2              |
| Bark         | [https://github.com/suno-ai/bark](https://github.com/suno-ai/bark)                 | Natural-sounding with emotion and style |
| Tortoise TTS | [https://github.com/neonbjb/tortoise-tts](https://github.com/neonbjb/tortoise-tts) | High quality, slow inference            |
| Coqui TTS    | [https://github.com/coqui-ai/TTS](https://github.com/coqui-ai/TTS)                 | Multi-speaker, multilingual             |
| Piper        | [https://github.com/rhasspy/piper](https://github.com/rhasspy/piper)               | Lightweight TTS for embedded setups     |

### 🌐 SaaS / Online:

| Name            | Link                                                                                       | Notes                                                 |
| --------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| OpenVoice (Web) | [https://huggingface.co/myshell-ai/OpenVoice](https://huggingface.co/myshell-ai/OpenVoice) | Fast, multilingual, prompt-guided TTS                 |
| ElevenLabs      | [https://elevenlabs.io](https://elevenlabs.io)                                             | Ultra-realistic voice cloning, emotion control (Paid) |
| PlayHT          | [https://play.ht](https://play.ht)                                                         | Voice cloning and marketplace with API (Paid)         |

---

## 🧾 Text2SQL / Querying Natural Language

### 🔧 Run Locally:

| Name                        | Link                                                                                                                         | Notes                                             |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| T5-LM-Large-text2sql-spider | [https://huggingface.co/gaussalgo/T5-LM-Large-text2sql-spider](https://huggingface.co/gaussalgo/T5-LM-Large-text2sql-spider) | Converts plain text to SQL using Spider DB schema |

### 🌐 SaaS / Online:

| Name              | Link                                                                                 | Notes                     |
| ----------------- | ------------------------------------------------------------------------------------ | ------------------------- |
| thangved/text2sql | [https://huggingface.co/thangved/text2sql](https://huggingface.co/thangved/text2sql) | HuggingFace Space demo UI |

---

## 🎥 Video & Image Generation / Editing

### 🔧 Run Locally:

| Name                | Link                                                                                                                               | Notes                                       |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Stable Diffusion XL | [https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) | High-res image generation                   |
| SuperEdit           | [https://github.com/bytedance/SuperEdit](https://github.com/bytedance/SuperEdit)                                                   | Instruction-based image editing             |
| FramePack           | [https://github.com/lllyasviel/FramePack](https://github.com/lllyasviel/FramePack)                                                 | Efficient AI video generation with low VRAM |
| Text2Video-Zero     | [https://github.com/Picsart-AI-Research/Text2Video-Zero](https://github.com/Picsart-AI-Research/Text2Video-Zero)                   | Zero-shot video from prompt                 |
| Open-Sora           | [https://github.com/hpcaitech/Open-Sora](https://github.com/hpcaitech/Open-Sora)                                                   | Research-grade open text2video pipeline     |
| mochi               | [https://github.com/genmoai/mochi](https://github.com/genmoai/mochi)                                                               | Powerful local text2video generator         |
| MagicAnimate        | [https://github.com/deepghs/MagicAnimate](https://github.com/deepghs/MagicAnimate)                                                 | Animate character from pose + image         |
| MagicEdit           | [https://huggingface.co/ByteDance/MagicEdit](https://huggingface.co/ByteDance/MagicEdit)                                           | Image editing by instruction (open weights) |

### 🌐 SaaS / Online:

| Name      | Link                                                 | Notes                                           |
| --------- | ---------------------------------------------------- | ----------------------------------------------- |
| Runway ML | [https://runwayml.com](https://runwayml.com)         | Gen-2, inpainting, video editing tools (Paid)   |
| Pika Labs | [https://pika.art](https://pika.art)                 | Web-based prompt-to-video generation (Freemium) |
| Synthesia | [https://www.synthesia.io](https://www.synthesia.io) | AI avatars & video narration (Paid)             |
| HeyGen    | [https://www.heygen.com](https://www.heygen.com)     | Text-to-video avatar tool (Paid)                |
| Sunō AI   | [https://suno.ai](https://suno.ai)                   | Text-to-music generation (Free/Paid)            |
---

## 📄 UI / PDF / Frontend Tools

### 🔧 Run Locally:

| Name        | Link                                                                           | Notes                                     |
| ----------- | ------------------------------------------------------------------------------ | ----------------------------------------- |
| react-email | [https://github.com/resend/react-email](https://github.com/resend/react-email) | Build email templates with React          |
| pdfme       | [https://github.com/pdfme/pdfme](https://github.com/pdfme/pdfme)               | Dynamic PDF generation in browser or node |
| WeasyPrint  | [https://github.com/Kozea/WeasyPrint](https://github.com/Kozea/WeasyPrint)     | HTML/CSS to PDF converter                 |

### 🌐 SaaS / Online:

| Name     | Link                                                       | Notes                                          |
| -------- | ---------------------------------------------------------- | ---------------------------------------------- |
| Figma    | [https://figma.com](https://figma.com)                     | Collaborative UI/UX design platform (Freemium) |
| Firebase | [https://firebase.google.com](https://firebase.google.com) | Backend + DB as a service (Free/Paid)          |

---

## 😈 Deepfake, Face Editing & Identity AI

### 🔧 Run Locally:

| Name             | Link                                                                                               | Notes                                                                 |
|------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| FaceSwap         | [https://github.com/deepfakes/faceswap](https://github.com/deepfakes/faceswap/)                   | Classic deepfake toolkit, still maintained, supports training         |
| InsightFace      | [https://github.com/deepinsight/insightface](https://github.com/deepinsight/insightface)         | Modular face detection, recognition (ArcFace), swapping (inswapper)   |
| SimSwap          | [https://github.com/neuralchen/SimSwap](https://github.com/neuralchen/SimSwap)                   | Real-time face swapping with encoder-decoder network                  |
| FaceFusion       | [https://github.com/facefusion/facefusion](https://github.com/facefusion/facefusion)             | Streamlined local face swap tool, built on SimSwap                   |
| DeepFaceLab      | [https://github.com/iperov/DeepFaceLab](https://github.com/iperov/DeepFaceLab)                   | Very powerful, requires GPU and training setup                        |
| SadTalker        | [https://github.com/OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker)               | Talking-head generation from image + audio                            |
| Live 3D Portrait | [https://github.com/tencent-ailab/LivePortrait](https://github.com/tencent-ailab/LivePortrait)   | Realistic facial animation from still image                           |

### 🌐 SaaS / Online:

| Name        | Link                                               | Notes                                                              |
|-------------|----------------------------------------------------|--------------------------------------------------------------------|
| DeepSwap    | [https://www.deepswap.ai](https://www.deepswap.ai) | Commercial face swapper, good for video memes (Free trial + Paid) |
| HeyGen      | [https://www.heygen.com](https://www.heygen.com)   | Avatar + voice + video generation suite                           |
| Synthesia   | [https://www.synthesia.io](https://www.synthesia.io)| AI avatars with TTS narration, multi-language (Paid)              |
| Reface App  | [https://hey.reface.ai](https://hey.reface.ai)     | Consumer-friendly face swap mobile app                            |
| D-ID        | [https://www.d-id.com](https://www.d-id.com)       | Photo-to-talking-head video from text or voice input              |

---

## 🔧 Other Dev Tools & APIs

| Name           | Link                                                                                                         | Notes                                             |
| -------------- | --------------------------------------------------------------------------------------                       | ------------------------------------------        |
| Hoppscotch     | [https://github.com/hoppscotch/hoppscotch](https://github.com/hoppscotch/hoppscotch)                         | Alternative to Postman                            |
| ToolJet        | [https://github.com/ToolJet/ToolJet](https://github.com/ToolJet/ToolJet)                                     | Build admin panels fast                           |
| Wasp           | [https://github.com/wasp-lang/wasp](https://github.com/wasp-lang/wasp)                                       | Full-stack web app builder with AI support        |
| OpenHands      | [https://github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)                       | Multi-hand detection library                      |
| whisper.cpp    | [https://github.com/ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp)                           | Whisper transcriber (runs on CPU)                 |
| whisper        | [https://github.com/openai/whisper](https://github.com/openai/whisper)                                       | Speech-to-text model from OpenAI                  |
| faster-whisper | [https://github.com/SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)                       | Fast Whisper implementation (CUDA)                |
| LangChain      | [https://github.com/hwchase17/langchain](https://github.com/hwchase17/langchain)                             | Popular framework for RAG pipelines               |
| LlamaIndex     | [https://github.com/jerryjliu/llama_index](https://github.com/jerryjliu/llama_index)                         | Document indexing & retrieval for LLMs            |
| Real-ESRGAN    | [https://github.com/xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)                             | Super-resolution for images, anime, media         |
| ComfyUI        | [https://github.com/comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)                       | Node-based UI for StableDiffusion workflows       |
| diffusers      | [https://github.com/huggingface/diffusers](https://github.com/huggingface/diffusers)                         | HuggingFace's SD/ControlNet backend               |
| ControlNet     | [https://github.com/lllyasviel/ControlNet](https://github.com/lllyasviel/ControlNet)                         | Conditioning system for precise SD image control  |
| Phind-CodeLlama| [https://huggingface.co/Phind/Phind-CodeLlama-34B-v2](https://huggingface.co/Phind/Phind-CodeLlama-34B-v2)   | High-performance coding model from Phind          |


---


## 🗃️ Repos (GitHub + HuggingFace) – Raw List

https://huggingface.co/deepseek-ai/Janus-Pro-7B
https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
https://huggingface.co/Qwen/Qwen2.5-Coder-7B
https://huggingface.co/mistralai/Codestral-22B-v0.1
https://huggingface.co/WizardLMTeam/WizardCoder-15B-V1.0
https://huggingface.co/codellama/CodeLlama-34b-Instruct-hf
https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct
https://huggingface.co/datasets/nvidia/OpenCodeReasoning
https://huggingface.co/datasets/nvidia/Nemotron-CrossThink
https://huggingface.co/Qwen/Qwen1.5-7B-Chat
https://github.com/bytedance/SuperEdit
https://huggingface.co/microsoft/Phi-4-reasoning-plus
https://huggingface.co/deepseek-ai/DeepSeek-Prover-V2-671B
https://huggingface.co/nari-labs/Dia-1.6B
https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2
https://huggingface.co/coqui/XTTS-v2
https://github.com/rhasspy/piper
https://github.com/microsoft/autogen
https://github.com/langchain-ai/langgraph
https://github.com/Kozea/WeasyPrint
https://github.com/pdfme/pdfme
https://github.com/resend/react-email
https://github.com/openai/whisper
https://github.com/ggml-org/whisper.cpp
https://github.com/hoppscotch/hoppscotch
https://github.com/ToolJet/ToolJet
https://github.com/suno-ai/bark
https://github.com/neonbjb/tortoise-tts
https://github.com/coqui-ai/TTS
https://github.com/lllyasviel/FramePack
https://github.com/Picsart-AI-Research/Text2Video-Zero
https://github.com/hpcaitech/Open-Sora
https://github.com/genmoai/mochi
https://huggingface.co/google/gemma-7b/
https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1
https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1
https://github.com/eosphoros-ai/DB-GPT
https://huggingface.co/gaussalgo/T5-LM-Large-text2sql-spider
https://huggingface.co/thangved/text2sql
https://huggingface.co/myshell-ai/OpenVoice
https://huggingface.co/coqui/XTTS-v1
https://huggingface.co/microsoft/Orca-2-13b
https://huggingface.co/tiiuae/falcon-40b-instruct
https://github.com/microsoft/autogen-studio
https://github.com/deepghs/MagicAnimate
https://huggingface.co/ByteDance/MagicEdit
https://huggingface.co/spaces/enzostvs/deepsite
https://github.com/deepfakes/faceswap/
https://github.com/deepinsight/insightface
https://github.com/neuralchen/SimSwap
https://github.com/facefusion/facefusion
https://github.com/iperov/DeepFaceLab
https://github.com/OpenTalker/SadTalker
https://github.com/tencent-ailab/IP-Adapter
https://github.com/tencent-ailab/LivePortrait
https://github.com/wasp-lang/wasp
https://github.com/All-Hands-AI/OpenHands
https://github.com/SYSTRAN/faster-whisper
https://github.com/hwchase17/langchain
https://github.com/jerryjliu/llama_index
https://github.com/xinntao/Real-ESRGAN
https://github.com/comfyanonymous/ComfyUI
https://github.com/huggingface/diffusers
https://github.com/lllyasviel/ControlNet
https://huggingface.co/Phind/Phind-CodeLlama-34B-v2
---

## 🌐 SaaS / Online Tools – Raw List

https://cursor.sh
https://replit.com
https://bolt.ghost.io
https://www.lovable.so
https://windsurf.ai
https://runwayml.com
https://pika.art
https://www.synthesia.io
https://www.heygen.com
https://suno.ai
https://www.deepswap.ai
https://hey.reface.ai
https://www.d-id.com
https://elevenlabs.io
https://play.ht
https://figma.com
https://firebase.google.com


## ⚠️Setup Instructions, scripts, notes, licensing


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
📦 /
├── README.md
├── links.txt
├── bulk_repo_downloader.py
├── /list_comp/
  ├── slebbeog.py
  ├── list1.txt
  ├── list2.txt
  └── results.txt
```

---

## 📜 Notes

- HuggingFace repos use the API (no `git-lfs` needed)
- GitHub repos are cloned with `git`
- Skips already downloaded folders

---

## 🧻 License

MIT – free to use, modify, remix by White People.

---
