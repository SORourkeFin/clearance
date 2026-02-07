# CLEARANCE — hack-scale prototype

A text-first prototype exploring **trust-based review dynamics**: the system remembers how you behave, updates a “trust” score, and changes what it requires from you over time.

This was built as a solo hackathon project for the **Supercell Global AI Game Hack** (AI Tech Open Challenge).

---

## What it is

**CLEARANCE** is a minimalist “approval simulator”:

- You submit a feature request
- You choose a response strategy (clarify, comply, automate, push back, shortcut, wait)
- The system updates a **trust score** and a **risk profile**
- The next response changes based on that history (fast-track vs stricter review)

It’s not a chatbot and not a narrative game. The core mechanic is **stateful judgment**: the system becomes more permissive or more demanding depending on your pattern of behavior.

---

## Core idea (why it matters)

Most systems don’t just evaluate *your request* — they evaluate *you* (implicitly or explicitly):

- Past behavior becomes a proxy for risk
- “Trust” gates speed, scrutiny, and permissions
- A single risky move can permanently shift how you’re treated

CLEARANCE turns that invisible dynamic into a playable, inspectable prototype.

---

## Demo path (30 seconds)

Use the default feature name (or any text) and run:

1) **Clarify intent → Submit**  
   - Trust increases  
   - Profile shifts toward **cautious**  
   - System shows **fast-track eligible** (brief rationale only)

2) **Shortcut (risky) → Submit** (twice)  
   - Trust drops  
   - Profile becomes **reckless**  
   - System requires **rationale + justification** (stricter review)

This is the “aha”: the same request gets different treatment because *you* changed.

---

## How to run locally

### Requirements
- Python 3.9+
- Streamlit

### Install
```bash
python3 -m pip install streamlit
