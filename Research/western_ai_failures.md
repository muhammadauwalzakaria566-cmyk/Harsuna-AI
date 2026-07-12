# Evaluation Log: Hausa Machine Translation Gaps

This file documents real, observed failures in existing AI translation models when handling Hausa — collected as part of the Harsuna AI research process. Each entry is a factual record: what was tested, what the model produced, what was actually correct, and why the gap likely occurred.

The goal is not to criticize existing tools, but to build an honest, evidence-based picture of where Hausa language technology currently falls short — which is the starting point for any real improvement.

---

## Entry 1: Tire Safety Instruction (Logistics Domain)

**Date:** July 12, 2026
**Model tested:** Helsinki-NLP/opus-mt-en-ha (via Hugging Face `transformers`)
**Task:** English → Hausa translation

**Input (English):**
> "Please check your truck tires before leaving Kano tomorrow morning."

**Model output (Hausa):**
> "Don Allah ka kalli motarka kafin ka bar Kano gobe."

**Correct translation (native speaker verified):**
> "Dan Allah ka kalli tayar motarka kafin ka bar Kano gobe da safe."

### Observed Errors

1. **Spelling error in common phrase:** The model produced "Don Allah" instead of the correct "Dan Allah" (a standard Hausa phrase meaning "please"). Likely cause: token-level confusion with the English name/title "Don," which shares spelling but not meaning.

2. **Dropped word — "tires":** The word "tayar" (tires) was omitted entirely. The model translated "truck" (mota) but lost the more specific noun. This is a **meaningful omission**, not a stylistic simplification — the resulting sentence tells the reader to check their vehicle in general, not the specific safety-critical component (tires) that was actually mentioned.

3. **Dropped detail — "morning":** "Tomorrow" (gobe) was translated, but "morning" (da safe) was dropped, losing part of the original time specification.

### Why This Likely Happened
Machine translation models learn patterns from training data. Common, general phrases (like "check your car") are likely far more frequent in Hausa training data than specific technical terms (like "check your tires"). When a model is less confident about a specific word, it tends to default to a simpler, more frequently-seen pattern rather than the precise term — effectively dropping detail it hasn't seen enough examples of.

### Why This Matters
In a general conversation, this kind of omission might go unnoticed. In a safety-relevant or instructional context — such as logistics, healthcare, or technical instructions — dropping a specific noun like "tires" changes a precise instruction into a vague one. The sentence still reads as fluent, grammatically correct Hausa, which makes the error harder to catch without a native speaker reviewing the output.

---

## Notes on Methodology
- All test sentences are evaluated by direct comparison against a native Hausa speaker's translation (self-verified, given the author's own fluency)
- Entries will be added as more tests are run across different domains (everyday conversation, technical instructions, news-style text, etc.)
- The goal over time is to build a small but rigorous evaluation set — not to claim any single model is "bad," but to identify concrete, reproducible patterns in where Hausa NLP currently has gaps

---

*Part of the Harsuna AI research process — a project by Khalifa TechBridge.*
