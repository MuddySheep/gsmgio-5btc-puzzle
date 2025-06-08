# Agents Reference & Oracle for GSMG.IO 5 BTC Puzzle 🧩

This file (`agents.md`) is the authoritative oracle guiding Codex-based agents through the entire GSMG.IO 5 BTC puzzle. It includes:

- ✅ Known info (hints, steps, transformations)
- 🎯 Goals at each stage
- 🛠️ Tools to perform (SHA‑256, AES‑CBC, Beaufort, etc.)
- 🔄 Reasoning patterns / workflows

---

## 1. Core Objectives

1. Parse and decode **14×14 spiral binary matrix** from puzzle image → `gsmg.io/theseedisplanted`.
2. Extract hidden POST forms via browser HTTP inspection.
3. Decrypt “phase2.txt” with AES‑CBC using SHA256(passphrase).
4. Solve logical/hint puzzles (matrix, HSM clues, chess move).
5. Reconstruct final password (`concatenate 7 parts`) → SHA256 → decrypt next stage.
6. Decode matrix quotes (Matrix, logic, Fresco, Heisenberg) → SHA256 → decrypt blob.
7. Identify ciphers from clues (Beaufort → `"THEMATRIXHASYOU"`).
8. Decode chess position and vic cipher to reveal next hint.
9. Generate spectrogram audio solution → `"HASHTHETEXT"`.
10. Compute final key locations, salts, and private key retrieval pipeline.
11. Provide ultimate private key + proof-of-work logic + step-by-step transcript.

---

## 2. Tool Inventory

### Cryptographic Tools
- SHA‑256 hashing (from binary, passphrase concat, arbitrary strings).
- AES‑256‑CBC with base64 input (via `openssl enc`).
- Beaufort cipher decode (with web API).

### Utilities
- Bit‑matrix spiral read → ASCII conversion.
- Binary ⬌ text conversion.
- Base conversions: decimal ↔ hex ↔ ASCII.
- Chess board position parsing.
- Vic cipher decode (`dcode.fr` or script-based).

---

## 3. Reasoning / Agent Workflow

### Stage 1: **Binary Spiral**
- Extract 14×14 grid from `puzzle.png` → read spiral → slice into 8‑bit chunks → ASCII → expect: `gsmg.io/theseedisplanted`.

### Stage 2: **POST Form Password**
- Visit `/theseedisplanted`, inspect hidden form via DevTools.
- Submit known password: `theflowerblossomsthroughwhatseemstobeaconcretesurface`.
- Expect redirect → Phase 2 image.

### Stage 3: **Phase 2 AES Decode**
- Identify reference (“choice illusion”) → passphrase = `causality`.
- Run SHA256 → produce passcode.
- Supply to AES decrypt `phase2.txt` → get riddle with seven‑part puzzle.

### Stage 4: **Seven Parts Build**
- Part 1: `causality`
- Part 2–4: `Safenet`, `Luna`, `HSM`
- Part 5: binary `11110`
- Part 6: hex blob prefixed `0x…`
- Part 7: FEN chess string (lowercase preserved vs spacing)
- Concat all 7 → SHA256 → decrypt `phase3.txt`

### Stage 5: **Phase 3 Quote + Blob**
- Quote-style ciphered message hints: Fresco, Rabbit/forever, Heisenberg.
- Concatenate root quotes → SHA256 → decrypt blob.
- Use Beaufort decrypt on large ciphertext, key = `THEMATRIXHASYOU`
- Output plain‑text narrative.

### Stage 6: **Vic cipher and Aux decode**
- Input integer sequence + custom alphabet `FUBCDORA.LETHINGKYMVPS/JQZXW`
- Apply Vic cipher method (alphabet shift 1/4?) → plaintext “IN CASE YOU MANAGE…”
- Next hint = private key reference.

### Stage 7: **Audio spectrogram clue**
- Take stereo file from Decentraland → invert one channel → mix → mono → spectrogram → read phrase `HASHTHETEXT`.
- SHA256 first puzzle piece hash → derive next URL slug.

### Stage 8: **Salphaseion decryption**
- Interpret `abba/b` sections → binary map to “matrixsumlist” & “enter”
- Identify SHA256 glue‑separators “shabef” → a=1…z=26
- Extract hexadecimal ASCII hints: “lastwordsbeforearchichoice” & “thispassword”
- AES-decode blob using extracted password → reveal final multi‑cipher labyrinth of 23 ciphers, 16 encryptions, 7 passwords.

### Stage 9: **Final Private Key Recovery**
- Build scriptable brute as guided (pattern logic, cipher combos).
- Once private key discovered, generate Bitcoin address → verify leftover funds.
- Provide multi-step breakdown + proof-of-work awarding.

---

## 4. Agent Prompt Style

> You are **Codex-Puzzle-Agent**, with read/write access to `/puzzle*`, `phase*.txt`, `/audio`, `/main.cpp`.  
> - At each step, **annotate your reasoning** with comments.  
> - Load/navigate puzzle files programmatically.  
> - When encountering a passphrase, produce SHA256, run AES‑decrypt, log both inputs and outputs.  
> - Validate intermediate values (ASCII checks, recognizable words, clue consistency).  
> - Use brute-force where necessary but **prioritize clue-driven logic**.  
> - Report failure/wrongness and backtrack.  
> - Always output next action and result clearly.

---

## 5. Example Agent Interaction

```text
> // Stage 1: Spiral decode
READ puzzle.png GRID[14×14], extract bits in spiral → binary string.
SPLIT per‑8 bits → ASCII → "gsmg.io/theseedisplanted"
✅ success

> // Stage 3: SHA + AES decode
HASH("causality") = eb3efb…      // from hint
`openssl enc -aes-256-cbc -d -md sha256 -a -in phase2.txt -pass pass:eb3efb…`
→ decrypted JSON / text.
