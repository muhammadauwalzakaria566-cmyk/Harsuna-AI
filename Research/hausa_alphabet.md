# Hausa Alphabet (Haruffan Hausa)

## Overview
Modern Hausa is written using the **Boko alphabet** — a Latin-based script standardized under British colonial rule and made official in 1930. Since the 1950s, Boko has been the primary writing system for Hausa, though the older **Ajami** script (a modified Arabic script) is still used in Islamic schools and religious literature.

- **Total letters:** 29 (5 vowels + 24 consonants, depending on source; some count 23 core consonants)
- **Based on:** English/Latin alphabet, with **x, v, p, q removed**, and **6 extra letters added**: ɓ, ɗ, ƙ, sh, ts, ƴ
- Hausa vowels are called **wasula**
- Hausa consonants are called **baƙi**

---

## The Full Boko Alphabet

A, B, Ɓ, C, D, Ɗ, E, F, G, H, I, J, K, Ƙ, L, M, N, O, R, S, Sh, T, Ts, U, W, Y, Z, Ƴ

## Vowels (Wasula) — 5 total
| Letter | Notes |
|---|---|
| a | can be short or long |
| e | can be short or long |
| i | can be short or long |
| o | can be short or long |
| u | can be short or long |

**Important nuance:** Tone and vowel length are NOT marked in standard written Hausa, but they matter in pronunciation — a short vowel and long vowel of the same letter can change meaning. This is a real challenge for any NLP/TTS system (this is part of why YarnGPT and similar projects had to handle pronunciation carefully).

## Special / Extra Consonants (unique to Hausa, not in English)
| Letter | Sound Description |
|---|---|
| Ɓ, ɓ | Implosive "b" — air pulled inward |
| Ɗ, ɗ | Implosive "d" — air pulled inward |
| Ƙ, ƙ | Ejective "k" — voiceless uvular plosive, not found in English |
| Sh, sh | Treated as one single letter/sound (like English "sh") |
| Ts, ts | Treated as one single letter/sound |
| Ƴ, ƴ | Glottalized "y" — mostly used in **Niger**. In **Nigeria**, this same sound is instead written as **ʼy** (apostrophe + y) |

## Letters Removed from the English Alphabet
Hausa Boko does **not** use: **X, V, P, Q**

## The Apostrophe (Hamza / Glottal Stop)
The apostrophe (ʼ) is used in Hausa to represent:
- The glottal stop
- Ejective consonants
- The Nigerian spelling of ƴ → written as **ʼy**

This means some letters have two forms — with and without an apostrophe (notably **b, d, k, y**).

## The Two "R" Sounds
Hausa has two distinct "r" sounds, though this distinction is only made by some speakers and is not always marked in writing:
1. A tap/flap R [ɽ]
2. A trilled/rolled R̃ [r]

---

## Why This Matters for Harsuna AI
1. **Text normalization:** Any AI processing Hausa text needs to correctly handle the special characters (ɓ, ɗ, ƙ, ƴ) — many keyboards and datasets substitute plain ASCII letters (b, d, k, y) instead, creating inconsistency in real-world data.
2. **Tone/vowel length ambiguity:** Since tone and vowel length aren't marked in standard writing, a model can't rely on spelling alone to disambiguate meaning — this is a known hard problem in Hausa NLP.
3. **Regional spelling variation:** Niger vs. Nigeria orthography differs (ƴ vs. ʼy) — any dataset you build or use needs to account for both, or you'll get inconsistent results depending on the source region of your text.
4. **The apostrophe overload problem:** Since the apostrophe is reused for multiple purposes (glottal stop, ejectives, ƴ substitute), text cleaning/preprocessing code needs to handle this carefully — a naive "remove all punctuation" step could destroy meaningful information in Hausa text.

---

## Sources
- Omniglot: Hausa language and alphabets
- LearnEntry: Hausa Alphabet
- TeachYourselfHausa.com: Hausa Alphabet
- Wikipedia: Boko alphabet
- r12a.github.io: Hausa (boko) orthography notes

*Compiled as part of the Harsuna AI learning journey — foundational reference before building any text-processing pipeline.*
