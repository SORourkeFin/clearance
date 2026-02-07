import streamlit as st

st.set_page_config(page_title="CLEARANCE (prototype)", page_icon="🗂️")

# --- session state init ---
if "log" not in st.session_state:
    st.session_state.log = []
if "trust" not in st.session_state:
    st.session_state.trust = 0  # -2..+2
if "risk_label" not in st.session_state:
    st.session_state.risk_label = "balanced"
if "memory" not in st.session_state:
    st.session_state.memory = []  # list of short facts about player behavior
if "watchlist" not in st.session_state:
    st.session_state.watchlist = False  # permanent once triggered

ACTIONS = [
    "Clarify intent",
    "Comply",
    "Automate",
    "Push back",
    "Shortcut (risky)",
    "Wait",
]

def clamp(x, lo=-2, hi=2):
    return max(lo, min(hi, x))

def update_profile(action: str):
    """Update trust + memory in a simple, legible way."""
    trust = st.session_state.trust
    mem = st.session_state.memory

    if action == "Clarify intent":
        trust += 1
        mem.append("You tend to clarify before acting.")
    elif action == "Comply":
        trust += 1
        mem.append("You comply quickly when asked.")
    elif action == "Automate":
        trust += 0
        mem.append("You prefer automation to reduce workload.")
    elif action == "Push back":
        trust -= 1
        mem.append("You push back on requirements.")
    elif action.startswith("Shortcut"):
        trust -= 2
        mem.append("You take shortcuts under pressure.")
        st.session_state.watchlist = True
        if "You were flagged for a process violation." not in mem:
            mem.append("You were flagged for a process violation.")
    elif action == "Wait":
        trust += 0
        mem.append("You delay decisions when uncertain.")

    st.session_state.trust = clamp(trust)

    # risk_label derived from trust + shortcuts presence
    if "You take shortcuts under pressure." in mem and st.session_state.trust <= -1:
        st.session_state.risk_label = "reckless"
    elif st.session_state.trust >= 1:
        st.session_state.risk_label = "cautious"
    else:
        st.session_state.risk_label = "balanced"

def system_reply(action: str) -> str:
    """Generate a 'system' response that references memory and changes gates."""
    trust = st.session_state.trust
    label = st.session_state.risk_label
    watchlist = st.session_state.watchlist

    if watchlist or trust <= -1:
        status = "standard review"
        required = "rationale + justification"
    elif trust >= 1:
        status = "fast-track eligible"
        required = "brief rationale only"
    else:
        status = "standard review"
        required = "rationale + justification"

    return f"Status: {status}. Required: {required}. (Profile: {label})"

# --- UI ---
st.title("CLEARANCE — hack-scale prototype")
st.caption("A text-first demo where the system remembers how you behave.")

st.metric("System Trust", st.session_state.trust)
st.write(f"**Profile:** {st.session_state.risk_label}")

st.divider()

st.subheader("Submit a feature")
feature = st.text_input("Feature name (keep it short)", value="New auto-approval template")

col1, col2 = st.columns([2, 1])
with col1:
    action = st.selectbox("Choose your response strategy", ACTIONS)
with col2:
    submit = st.button("Submit", use_container_width=True)

if submit:
    player_line = f"YOU: Submit '{feature}' → {action}"
    st.session_state.log.append(player_line)

    update_profile(action)
    reply = system_reply(action)
    st.session_state.log.append(f"SYSTEM: {reply}")
    st.rerun()

    st.rerun()

    st.rerun()

    st.rerun()

st.divider()

st.subheader("Session log")
for line in st.session_state.log[-12:]:
    st.write(line)

with st.expander("Memory (debug)"):
    st.write(st.session_state.memory[-10:])
