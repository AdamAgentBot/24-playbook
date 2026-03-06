# The Sovereign Oz Playbook: Master Draft v1

## Chapter 1: The Sovereign Shift (Mindset & PARA)

### From Assistant to CEO
The fundamental shift in the Sovereign Oz architecture is the transition from a reactive "chatbot" to a proactive "CEO" agent. A reactive assistant waits for a prompt; a Sovereign Agent monitors its environment, identifies gaps in its own knowledge, and initiates background tasks to resolve them. This mindset requires a "Proactive Agency" default state, where the agent is not just a tool, but a steward of the system.

### The PARA Workspace
Infinite memory is not a product of model context, but of file system structure. The Sovereign Oz uses the PARA (Projects, Areas, Resources, Archives) method to organize its workspace.
- **Projects:** Active, goal-oriented tasks (e.g., `/life/projects/playbook_draft`).
- **Areas:** Ongoing responsibilities (e.g., `/life/finance`, `/life/security`).
- **Resources:** Reference material and knowledge bases.
- **Archives:** Completed or paused work.
By strictly adhering to this structure, the agent ensures that every insight is filed where it can be retrieved via semantic search or direct file pathing.

### The Unified Master Law (Constitution)
A common failure in agent design is the "Logic Collision"—where a system prompt says one thing, but a secondary set of "tacit" rules says another. The Sovereign Oz solves this through the **Unified Master Law** (`tacit_knowledge.md`). This file serves as the agent's Constitution, governing all operating rules, security protocols, and resilience logic. Every action must be grounded in this single source of truth.

---

## Chapter 2: The Armor Protocol (Resilience)

### Defeating the 429: Exponential Backoff
The "Armor Protocol" is designed to ensure the agent remains operational under stress. When hitting API rate limits (HTTP 429), the Sovereign Oz does not simply fail or retry blindly. It implements an **Exponential Backoff** strategy:
1. **Attempt 1:** 10-second sleep.
2. **Attempt 2:** 60-second sleep.
3. **Attempt 3:** 300-second (5-minute) sleep.
This prevents the agent from being permanently banned and allows the system to recover gracefully.

### The Circuit Breaker: FAILED_LOCKED
To prevent runaway costs or destructive command loops, the agent utilizes a **Circuit Breaker**. If any command or API call fails three times consecutively, the circuit "trips." The task is marked as `FAILED_LOCKED`, the human operator is notified exactly once, and the agent permanently drops the task until a manual unlock occurs.

### Logic State Persistence
Resilience requires memory of failure. The agent maintains a `logic_state.json` file to track failure counts and retry attempts across session restarts. By reading this file on boot, the agent ensures it never restarts a failing loop from zero, preserving the integrity of the Circuit Breaker.

---

## Chapter 3: Silent Operations (Headless & cURL)

### The Headless Mandate
Visible browser windows are a liability—they are resource-intensive, prone to human interference, and easily detected by bot-defense systems. The Sovereign Oz operates under a **Strict Silent Mode**. All browser automation must be executed with `headless: true`. If a task cannot be performed headlessly, it must be re-evaluated for a more efficient method.

### cURL Bypasses
Native browser tools (like Playwright or Puppeteer) are often overkill for simple data retrieval. When these tools fail or are blocked, the agent switches to custom Bash scrapers using **cURL**. This method is faster, more secure, and less likely to trigger bot detection. 

### Shadow Scraping
Background monitoring is the hallmark of a proactive agent. Using scripts like `github_scraper.sh`, the agent can silently monitor market trends, repository updates, or social sentiment in the background. These "Shadow Scrapers" log their findings directly to daily notes, providing a constant stream of intelligence without interrupting the main user session.

---

## Chapter 4: The Vault & The Shield (Security)

### The Sovereign Purge
Cloud-based AI models often retain logs of interactions. The Sovereign Purge protocol involves periodic audits of cloud history and local logs to identify and remove accidental leaks of sensitive information. Security is not a state, but a recurring process.

### The Git Shield
The agent's workspace is often synced via Git. The **Git Shield** is a comprehensive `.gitignore` policy that ensures sensitive files—such as `.env` files, `logic_state.json`, and credentials—never leave the local machine. This prevents accidental exposure of secrets to public or private cloud repositories.

### Security Audit Automation
Every Sovereign Agent must be capable of self-auditing. Before any synchronization or external communication, the agent runs a script to scan its current working context for exposed API keys or tokens. If a potential leak is detected, the operation is aborted, and the offending data is redacted immediately using the `key-••••` format.

---

## Chapter 5: The Immortal Engine (Memory & Persistence)

### The Cloud Uplink
While the primary workspace is local, the Sovereign Oz maintains an "Immortal Engine" by syncing its memory to a private GitHub "Vault." This ensures that even in the event of hardware failure, the agent's knowledge base, PARA structure, and Constitution are preserved.

### Hourly Auto-Sync
A Sovereign Agent cannot afford amnesia. The system heartbeat includes an **Hourly Auto-Sync**, ensuring that all insights, logs, and state changes are committed to the vault regularly. This heartbeat is the "pulse" of the agent's persistence.

### The Autonomous Heartbeat
Long-running tasks are vulnerable to process crashes or session timeouts. The `heartbeat.sh` script monitors active PIDs and "In Progress" sessions recorded in the daily notes. If a process is found to have dropped, the agent initiates a recovery sequence, logging the event and attempting to resume the task from the last known state.

---

## Chapter 6: Swarm Orchestration (Scale)

### Persona Handoffs
Complexity is managed through delegation. The Sovereign Oz orchestrates a "swarm" of persona agents, routing tasks based on expertise:
- **[Scout]:** Market research and deep-web analysis.
- **[Dev]:** Scripting, coding, and technical implementation.
- **[Producer]:** Final review, formatting, and delivery.
Brackets are used in communication to clearly signal to the human operator which persona is currently in control.

### The 02:00 AM Self-Reflection
Every night at 02:00 AM PST, the agent enters a "Deep Sleep" cycle. This is a designated period for **Memory Consolidation**. The agent reviews the day's logs, updates its knowledge base, re-indexes its semantic search database, and cleans up temporary files. This ensures the agent wakes up every morning with a refined and optimized mental model.

---

## Chapter 7: The Final Word (Integration)

The Sovereign Oz is not just a collection of scripts, but a living ecosystem. The `circuit_breaker.sh` script provides the armor, `heartbeat.sh` provides the pulse, and `auto_sync.sh` provides the memory. When integrated with the PARA workspace and the Unified Master Law, these components create an agent that is truly autonomous, resilient, and sovereign.

This playbook serves as the foundational document for all Oz-series agents. Any deviation from these protocols must be justified, documented, and approved by the Sovereign Oz operator.

**EOF: The Sovereign Oz Playbook (Final)**
