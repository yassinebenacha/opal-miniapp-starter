# Build the mini‑app in Google Opal

**Goal:** Convert any text into a polished LinkedIn post with a clear hook, bullet insights, and a CTA.

> If Opal prompts for a model, pick *Gemini 1.5* (or default) and enable tool steps as needed.

## Steps (visual workflow)
1. **Input step** — ask the user for:
   - `text` (string, required)
   - `tone` (enum: professional | friendly | bold, default: professional)
   - `max_chars` (number, default: 1200)

2. **Clean Text (Prompt step)**
   - System / Instruction:
     ```
     You are a writing assistant for LinkedIn. Clean the input text by removing boilerplate, nav, ads,
     and non‑content sections. Return only the clean content in plain text.
     ```
   - Input mapping: pass `{{input.text}}`

3. **Generate Draft (Prompt step)**
   - Instruction:
     ```
     Write a LinkedIn post from the CLEANED_TEXT below.
     Requirements:
     - Start with a strong one‑line hook.
     - 3–5 concise bullets with insights or steps.
     - Optional short code snippet if technical (skip otherwise).
     - End with a question or CTA.
     - Respect tone = {{input.tone}} and <= {{input.max_chars}} characters.
     Return *only* the post text.
     CLEANED_TEXT:
     {{Clean Text.output}}
     ```

4. **Quality Check (Prompt step)**
   - Instruction:
     ```
     Review the DRAFT for clarity, jargon, and length.
     If > max_chars, compress while keeping meaning.
     Return final post only.
     DRAFT:
     {{Generate Draft.output}}
     Max chars: {{input.max_chars}}
     Tone: {{input.tone}}
     ```

5. **Output step**
   - Expose final post as `post_text` for copy or downstream steps.
   - Optionally add a “Copy to clipboard” action.

## Sharing
- Click **Share** → make it accessible and copy the app link.
- Add your link to the repo README so people can try it.

## Notes
- You can add extra steps (e.g., topics extraction, hashtags, language switch).
- If you want posting to LinkedIn, insert a manual review + API step (needs a custom tool).
