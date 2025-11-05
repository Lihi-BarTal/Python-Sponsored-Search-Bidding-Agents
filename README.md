# 📈 GSP Auction Bidding Agents (Exploration/Exploitation)

**Python Project - Implementation for E-Commerce Models (HW 3)**

## 💡 Overview
This project implements two bidding agents designed to maximize profit in a **Generalized Second Price (GSP) Auction** environment. The focus is on Agent 2, which utilizes a dynamic strategy to compete against unknown agents and maximize revenue.

## 🎯 Solution Approach: Agent 2 (Exploitation via EMA)

**Bidding Agent 2** is designed to learn the competitor's average bidding behavior to propose an optimal bid that wins a spot while paying the minimum required amount (the second price).

### Key Mechanisms:

1.  **Exploration (Warm-up Rounds):**
    * The agent begins with a fixed number of warm-up rounds (`exploration_rounds=1000`).
    * During this stage, the agent bids a static **baseline bid ($v/2.5$)** based on the assumed common strategy of most competitors.
    * **Goal:** Collect initial data points for the true cost (the `payment` made in successful bids).

2.  **Learning Mechanism (Exponential Moving Average - EMA):**
    * The agent updates its belief about the competitor's bid using an **EMA** (with `ema_alpha=0.025`).
    * **Mechanism:** The EMA tracks the average price paid (which equals the runner-up's score/bid), giving **more weight to recent auction outcomes** to quickly adapt to changes in the environment.

3.  **Exploitation (Dynamic Bidding):**
    * After the warm-up, the agent calculates a **Target Score** based on the EMA, adding a small dynamic margin (e.g., `base_margin=0.03`).
    * **Final Bid:** The agent bids just enough to beat the expected runner-up score, but never exceeds the user's maximum valuation ($v$).

## 📂 Project Files

| File Name | Description |
| :--- | :--- |
| **`bidding_agents.py`** | Contains the implementation for both **Agent 1** (Static bid $v/2.5$) and the core **Agent 2** (Dynamic EMA strategy). |
| **`methodology_report.pdf`** | **Detailed Technical Analysis.** PDF document outlining the full strategy, justification for the $v/2.5$ baseline, and the mathematical implementation of the EMA for adapting to opponent behavior. |
