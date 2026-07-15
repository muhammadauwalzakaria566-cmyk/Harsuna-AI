# NER Baseline Test — English vs. Code-Switched vs. Hausa-Heavy

**Date:** July 15, 2026
**Model tested:** `dbmdz/bert-large-cased-finetuned-conll03-english` (Hugging Face default NER pipeline, `aggregation_strategy="simple"`)
**Author:** Muhammad Auwal Zakaria — Harsuna AI

## Purpose

To get first-hand, reproducible evidence of how a standard English-trained NER model behaves as Hausa content increases in a sentence — from pure English, to code-switched (English/Hausa/Pidgin mixed), to Hausa-heavy with minimal English scaffolding. This is a direct, hands-on test of Gap #7 ("LLMs don't speak our languages") and Gap #2 ("Voice/language AI fails on Nigerian accents and code-switching") from the KTB 7-gaps framework — at the token level, not just the sentence level.

---

## Test 1 — Pure English (control)

**Sentences:**
1. "Muhammad Auwal Zakaria lives in Maiduguri, Borno State."
2. "I went to Lagos yesterday to meet Saheed Azeez."
3. "Arewa Pay is building fintech tools for Northern Nigeria."

**Output:**
```
Muhammad Auwal Zakaria -> PER (score: 1.00)
Maiduguri -> LOC (score: 0.97)
Borno State -> LOC (score: 0.89)

Lagos -> LOC (score: 1.00)
Saheed Azeez -> PER (score: 1.00)

Arewa Pay -> ORG (score: 0.99)
Northern Nigeria -> LOC (score: 0.99)
```

**Observation:** Clean, high-confidence results across the board. Even Nigerian names and places score well when surrounded by standard English sentence structure — the model isn't failing on the *entities themselves*, only on the *context* they appear in later.

---

## Test 2 — Code-switched (Hausa / English / Pidgin mixed)

**Sentences:**
1. "Na tafi Maiduguri jiya don in ga Saheed Azeez."
2. "Malam Ahmadu ya ce Arewa Pay zai taimaka wa attajirai a Kano."
3. "I dey go Kano tomorrow to meet Alhaji Musa."

**Output:**
```
Na -> PER (score: 0.84)
Maidug -> MISC (score: 0.53)
Saheed Azeez -> PER (score: 0.99)

Malam Ahmadu -> PER (score: 0.65)
ce Arewa -> ORG (score: 0.64)
Kano -> LOC (score: 0.91)

Kano -> LOC (score: 1.00)
Alhaji Musa -> PER (score: 0.83)
```

**Observations:**
- **"Na" misread as a person (0.84):** "Na" is a Hausa pronoun/verb marker meaning "I" — not a name. The model pattern-matches capitalized sentence-initial words to "probably a name."
- **"Maiduguri" confidence collapsed (0.97 → 0.53) and was mistagged MISC:** Same word, same spelling as Test 1 — the only difference is Hausa words now surround it.
- **Entity boundary error — "ce Arewa" merged into one ORG:** "ce" (Hausa: "said") was incorrectly fused onto "Arewa," and "Pay" was dropped from the entity entirely. The model has no concept of where Hausa grammar ends and the company name begins.
- **Hausa honorific "Malam" lowers confidence:** "Malam Ahmadu" scored lower (0.65) than the equivalent English-context name in Test 1 (1.00). The model doesn't recognize "Malam" as a title the way it would recognize "Mr." or "Dr."
- **Pidgin performed best of the three code-switched sentences** — likely because Pidgin's syntax is closer to English, giving the model more familiar structure to anchor on.

---

## Test 3 — Hausa-heavy (minimal English scaffolding)

**Sentences:**
1. "Yau na je makaranta domin in yi computer training tare da abokina."
2. "Yaran nan suna sha'awar Facebook da WhatsApp sosai."
3. "Gwamnatin Borno ta gina babbar hanya daga Maiduguri zuwa Damaturu."

**Output:**
```
Sentence 1: (no entities detected)

##ha -> MISC (score: 0.55)
Facebook -> ORG (score: 0.68)
WhatsApp -> ORG (score: 0.82)

G -> PER (score: 0.58)
##nat -> ORG (score: 0.43)
Born -> ORG (score: 0.53)
##o -> LOC (score: 0.46)
Maid -> LOC (score: 0.80)
##ug -> MISC (score: 0.62)
##uri -> LOC (score: 0.39)
Damaturu -> LOC (score: 0.73)
```

**Observations:**
- **Total miss on Sentence 1:** Not even "computer training," the one English fragment present, was detected. Full collapse — no entities recognized at all.
- **Subword fragmentation on "sha'awar":** Tokenizer split the Hausa word into pieces, producing a nonsensical `##ha -> MISC` fragment.
- **Global brand names survived:** "Facebook" and "WhatsApp" were still caught — strong enough as standalone signals to punch through, regardless of surrounding language.
- **Catastrophic collapse on Sentence 3 — this is the clearest evidence in the whole test:**
  - "Gwamnatin" (government) shredded into `G` + `##nat`, mistagged as PER then ORG.
  - "Borno" split into `Born` + `##o` — the English-trained tokenizer literally sees the English word "Born" hiding inside "Borno" and anchors on it.
  - **"Maiduguri" — which scored 0.97 as a clean single entity in Test 1 — was torn into three fragments (`Maid` / `##ug` / `##uri`)** in this sentence, with one fragment wrongly tagged MISC. Same word. Same model. The only variable is the surrounding language.
  - Only "Damaturu" survived as one intact token, and even that dropped to 0.73 confidence.

---

## Summary Pattern

The failures are not random noise — they are systematic and explainable:

1. **Confidence drops** on entities the model would recognize perfectly in English, purely because of surrounding Hausa text.
2. **Entity boundaries break** at the seams between Hausa and English/Pidgin — the model cannot tell where one language's grammar ends and a name or organization begins.
3. **Hausa function words get misread as content words** (e.g., "Na" tagged as a person, "ce" absorbed into an organization name).
4. **Hausa honorifics are invisible to the model** ("Malam" is not recognized as a title the way "Mr." or "Dr." would be).
5. **Tokenization itself breaks down** on Hausa words with no English-trained subword mapping — words get sliced at points that coincidentally resemble English substrings ("Born" inside "Borno," "Maid" inside "Maiduguri"), producing fragments the NER head then guesses at based on surface patterns like capitalization.

## Why This Matters for Harsuna AI

This is direct, first-hand, reproducible evidence of Gap #7 ("LLMs don't speak our languages") at the token level, not just the sentence level. It moves the KTB thesis from a documented claim about training data proportions to something demonstrated with real, repeatable output — the same word ("Maiduguri") going from a clean 0.97 LOC tag to a three-way fragmented mistag purely as a function of what language surrounds it.

This is usable, citable material for future Harsuna AI content, research notes, and conversations with people in the African NLP space (Masakhane, HausaNLP, etc.) — concrete evidence, not just assertion.

---

## Follow-Up — Tokenizer-Level Root Cause Test

**Date:** July 15, 2026
**Model tested:** `bert-base-cased` tokenizer (`AutoTokenizer.from_pretrained("bert-base-cased")`)

**Purpose:** The NER tests above showed words fragmenting mid-sentence (e.g., "Maiduguri" → `Maid` / `##ug` / `##uri`; "sha'awar" → a stray `##ha` MISC tag). This follow-up isolates the tokenizer itself, outside of any downstream task, to confirm that fragmentation — not the NER head — is the root cause.

**Words tested and results:**

| Word | Tokens | Fragment count |
|---|---|---|
| Maiduguri | `Maid`, `##ug`, `##uri` | 3 |
| Borno | `Born`, `##o` | 2 |
| Damaturu | `Dam`, `##at`, `##uru` | 3 |
| Gwamnati | `G`, `##wa`, `##m`, `##nat`, `##i` | 5 |
| sha'awar | `s`, `##ha`, `'`, `a`, `##war` | 5 |
| attajirai | `at`, `##ta`, `##ji`, `##rai` | 4 |
| Kano | `Ka`, `##no` | 2 |
| Hausa | `Ha`, `##usa` | 2 |

**Observations:**

- **No Hausa word tested survived as a single token.** Not even "Kano" (a major, globally-referenced city) or "Hausa" (the language's own name) — both split into two fragments. There is no floor of "safe" Hausa vocabulary in this tokenizer; everything gets chopped.
- **Fragment count predicts downstream NER failure.** The two worst performers here — "Gwamnati" (5 fragments) and "sha'awar" (5 fragments) — are the exact two words that produced the clearest mistags in the NER test (Gwamnatin → `G`/`##nat` tagged PER then ORG; sha'awar → a stray `##ha` MISC tag). This is no longer a hypothesis — it's confirmed by two independent tests pointing at the same underlying mechanism.
- **Fragmentation is coincidental, not linguistic.** The tokenizer isn't splitting Hausa words along meaningful roots or morphemes — it's chopping them into whatever substrings happen to overlap with its English-trained vocabulary (e.g., "Borno" → "Born" + "o" because "Born" is a common English word fragment, not because it reflects any real structure in Hausa).

**Conclusion:** NER failures on Hausa/code-switched text are not primarily a weakness in the NER model's classification logic — they are inherited damage from a tokenizer with no Hausa-aware vocabulary. Any real fix has to start at the tokenizer level: training or extending vocabulary on actual Hausa text so common words and morphemes get single-token representation, rather than being reconstructed from accidental English-shaped fragments.

---

## Follow-Up 2 — Paragraph-Level Fragmentation Rate (bert-base-cased)

**Date:** July 15, 2026
**Test text:** 25-word Hausa sentence (news-style): *"Gwamnatin jihar Borno ta sanar da cewa za ta gina sabuwar hanya domin taimaka wa 'yan kasuwa da manoma a yankin arewa maso gabashin Najeriya."*

**Result:**
```
Total words: 25
Total tokens: 56
Average fragments per word: 2.24
```

**Observation:** For comparison, English text typically runs close to 1.0–1.3 tokens per word with this same tokenizer. This real-sentence test confirms the word-level findings above at scale: Hausa text costs roughly **1.7–2x more tokens than English for equivalent content** when processed by an English-trained tokenizer. This has direct compute-cost implications (more tokens = more processing = higher inference cost) on top of the accuracy damage already documented. Content words (sabuwar, hanya, taimaka, kasuwa, manoma, yankin, arewa, gabashin, Najeriya) fragmented 2–3 ways each; only short grammar particles (za, ta, da, wa, a) survived as single tokens — coincidentally, not because the tokenizer recognizes them as Hausa.

---

## Follow-Up 3 — Comparison Against an African-Language-Aware Tokenizer (AfriBERTa)

**Date:** July 15, 2026
**Model tested:** `castorini/afriberta_large` tokenizer

**Purpose:** To test whether a tokenizer trained on African-language text (rather than English-only) actually solves the fragmentation problem documented above — moving from "this is broken" to "here is proof the fix works."

**Result — same word list, side by side:**

| Word | bert-base-cased | AfriBERTa | Improvement |
|---|---|---|---|
| Maiduguri | `Maid`, `##ug`, `##uri` (3 tokens) | `_Maiduguri` (1 token) | 3x fewer fragments |
| Borno | `Born`, `##o` (2) | `_Borno` (1) | 2x fewer |
| Gwamnati | `G`, `##wa`, `##m`, `##nat`, `##i` (5) | `_Gwamnati` (1) | 5x fewer |
| Kano | `Ka`, `##no` (2) | `_Kano` (1) | 2x fewer |
| Hausa | `Ha`, `##usa` (2) | `_Hausa` (1) | 2x fewer |
| sha'awar | `s`, `##ha`, `'`, `a`, `##war` (5) | `_sha`, `'`, `awar` (3) | improved, not fully resolved |

**Observations:**

- **5 of 6 words went from multi-piece fragments to a single clean token** under AfriBERTa. This is not a marginal improvement — it is the difference between a model that has genuinely seen these words in training versus one reconstructing them from coincidental English-shaped scraps.
- **"Gwamnati" improved the most dramatically** — 5 fragments down to 1 — consistent with it being the worst performer across every prior test in this document.
- **"sha'awar" still fragments (3 pieces instead of 5)** — improved, but not fully resolved even by a multilingual African-language tokenizer. This is a specific, narrower remaining gap worth investigating further (possibly related to the apostrophe/hamza handling noted in the Hausa alphabet reference research).

**Conclusion:** This is proof-of-concept, not just theory, that the fix identified above works in practice. A tokenizer trained on real African-language text — AfriBERTa was trained across multiple African languages — resolves most of the fragmentation seen with an English-only tokenizer. This reframes Harsuna AI's technical path: rather than building tokenizer training from zero, the more efficient path is studying, benchmarking against, and potentially extending an existing African-language-aware model, focusing effort on the specific remaining gaps (like apostrophe-containing words) that even AfriBERTa doesn't fully solve.

---

## Follow-Up 4 — Full NER Comparison Against a Community-Trained Model (Masakhane)

**Date:** July 15, 2026
**Model tested:** `Davlan/xlm-roberta-large-masakhaner` — an XLM-RoBERTa large model fine-tuned on the Masakhane MasakhaNER dataset, covering 10 African languages including Hausa.

**Purpose:** To test the same code-switched sentences from the original NER baseline test (Test 2) against a model actually trained on real annotated Hausa NER data, closing the loop from "here is what breaks" to "here is what a properly-trained model gets right — and what it still misses."

**Result — same three sentences, before vs. after:**

| Entity | English-only model (`dbmdz/bert-large-cased-finetuned-conll03-english`) | Masakhane model (`xlm-roberta-large-masakhaner`) |
|---|---|---|
| "Na" (pronoun) | ❌ mistagged PER (0.84) | ✅ correctly ignored |
| "Maiduguri" | ❌ MISC (0.53) | ✅ LOC (1.00) |
| "jiya" (yesterday) | not detected | ✅ DATE (1.00) — new capability, not present in English model at all |
| "ce Arewa" boundary | ❌ incorrectly merged into one ORG (0.64), dropping "Pay" | ✅ fixed — "Arewa Pay" recognized correctly, separate from "ce" |
| "Malam Ahmadu" | PER (0.65), full phrase kept | "Ahmadu" alone tagged PER (1.00) — **"Malam" honorific dropped** |
| "Gwamnatin jihar Borno" (government of Borno state) | Total collapse — 5 fragments, mistagged PER/ORG | Only "Borno" caught as LOC (1.00) — **"Gwamnatin jihar" (the institutional phrase) missed entirely** |
| "arewa maso gabashin Najeriya" (northeast Nigeria) | not detected as a coherent phrase | ✅ LOC (0.99) — full phrase correctly grouped |

**Observations:**

- **The Masakhane model resolves the majority of failures documented in Test 2** — the "Na" mistag, the "ce Arewa" boundary error, and general confidence collapse are all fixed. It also demonstrates a capability the English-only model never had: correctly identifying "jiya" as a DATE entity.
- **Two specific, non-obvious gaps remain even in a model trained on real Hausa NER data:**
  1. **Honorifics are still dropped.** "Malam" (a respect/status title, roughly analogous to "Mr." but with additional cultural weight) is not recognized as part of the person entity, even though the underlying name is correctly tagged.
  2. **Institutional/government phrasing is under-captured.** "Gwamnatin jihar Borno" ("the government of Borno state") is reduced to just "Borno" as a location — the organizational meaning of the surrounding phrase is lost, even though the place name itself is caught correctly.

**Conclusion:** A community-trained model (Masakhane) substantially outperforms an English-only model on Hausa and code-switched text, confirming that real annotated training data — not just better tokenization — closes most of the gap. However, culturally specific categories (honorifics, institutional/government phrasing) remain weak points even in a model built specifically for African languages. This is a concrete, testable, and non-obvious finding — not something read in a paper, but discovered through direct experimentation — and represents a specific, well-defined gap that Harsuna AI could meaningfully target rather than attempting to rebuild general Hausa NER from scratch.
