# Opal AI Mini‑App Starter — “Article → LinkedIn Post”

A tiny starter project to **showcase a Google Opal mini‑app** that turns an article or text into a concise, engaging **LinkedIn post**.  
It also includes **fallbacks** you can run today if Opal isn’t available in your region (US‑only public beta as of July 24, 2025).

## What this repo contains
- `opal/` — step‑by‑step instructions to recreate the mini‑app in **Google Opal**, with prompts.
- `n8n/` — a simple **n8n** workflow (JSON) that does the same thing, so anyone can run it locally.
- `src/` — a small **Python** script using Gemini to draft a LinkedIn post from text (optional).
- `LICENSE` — MIT.

> ⚠️ **Availability note:** Google states Opal is **US‑only public beta** (blog post dated **July 24, 2025**). If you don’t have access yet, use the **n8n** or **Python** fallback and still share this repo on GitHub while you wait.

---

## Demo idea
## Live Demo
Try it here: [Opal App Link](https://opal.withgoogle.com/?flow=drive:/1Yg3it1e4Os4OF85ja6E_N79N-VPq8f7x&mode=app&shared=true)

### Demo Video
[📺 Watch Demo](Enregistrement%20de%20l'écran%202025-08-15%20194213.mp4)

**Input:** an article URL or raw text  
**Output:** a LinkedIn‑style post (≤ 1300 chars) with a punchy hook, 3–5 bullets, and a CTA.

---

## How to reproduce the Opal mini‑app
See `opal/miniapp_instructions.md` — it contains copy‑paste prompts, step wiring, and sharing notes.

If you can access Opal:
1. Go to `opal.withgoogle.com` → new app → follow the instructions.
2. Share your app and add the link to this README.

If you can’t access Opal yet:
- Import the `n8n/workflow.json` into your local n8n, or
- Run the Python CLI: `python src/draft_linkedin.py --text "..."`

---

## Python quick start (fallback)
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export GEMINI_API_KEY=YOUR_KEY   # Windows: set GEMINI_API_KEY=YOUR_KEY
python src/draft_linkedin.py --text "Paste any article text here"
```

## n8n quick start (fallback)
- Start n8n locally (`docker compose` or `n8n start`).
- Import `n8n/workflow.json`.
- Trigger via the **Webhook** URL and pass `text` in the JSON body.

---

## What to put in your LinkedIn post
- Add a short intro (why you built it) + repo link.
- Include 1–2 screenshots from Opal or n8n.
- Ask a question to spark discussion (e.g., *“Would you add auto‑posting or human‑in‑the‑loop edits?”*).

---

## License
MIT © 2025 — Yassine Ben Acha

---

## Contact Information
### YASSINE BEN ACHA
📞 +212 696 545 641  
✉️ yassinebenacha1@gmail.com  
🌐 [Mon portfolio](votre_lien_portfolio_ici)
