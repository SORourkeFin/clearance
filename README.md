# clearance
A hackathon prototype exploring trust-based review dynamics in AI systems.

# CLEARANCE

**CLEARANCE** is a minimalist, single-mechanic prototype that explores how systems quietly form opinions about users over time.

Instead of reacting only to individual actions, the system builds a *behavioral profile* based on patterns: how often you clarify, comply, push back, or take shortcuts under pressure. That profile then changes what you’re allowed to do next — faster paths, stricter scrutiny, or irreversible flags.

This is not a chatbot and not a narrative game. The focus is the **invisible system**.

---

## What is the core idea?

Most digital systems today don’t just process requests — they **remember behavior**.

CLEARANCE turns that into a playable experience:

- You submit changes into a system
- Each decision subtly shifts trust and risk tolerance
- The system responds differently over time based on *patterns*, not single choices
- Some thresholds are irreversible

The tension comes from realizing that the system is no longer reacting — it is *judging*.

---

## Why this works as a game

The game uses **one mechanic only**:
> *Make a decision → observe how the system changes future constraints*

There are:
- No points
- No visible meters
- No explicit explanations

The “fun” comes from discovery:
- *Why is this harder now?*
- *Why was this fast-tracked earlier?*
- *What did I do to trigger scrutiny?*

---

## Where GenAI fits

GenAI is used as the **adaptive system voice**.

Instead of fixed responses, the system:
- References prior behavior
- Surfaces memory selectively
- Changes tone and requirements dynamically

AI is not used for content generation or storytelling — it is used to simulate **institutional reasoning**.

This makes the experience impossible without AI: the system must *remember, infer, and adapt*.

---

## Hackathon scope & constraints

To keep the concept tight, we intentionally froze scope early:

**We do NOT:**
- Explain system logic to the player
- Visualize trust or risk meters
- Optimize balance or difficulty
- Add multiple mechanics

**We focus on:**
- One irreversible threshold
- One evolving profile
- One visible consequence: changing constraints

---

## Status

This is a hackathon-scale prototype built to demonstrate:
- A novel AI-driven game mechanic
- Systemic storytelling without exposition
- How invisible systems can be made legible through play

---

## Running the prototype locally

Requirements:
- Python 3.9+
- Streamlit

Install dependencies:
```bash
pip install streamlit
