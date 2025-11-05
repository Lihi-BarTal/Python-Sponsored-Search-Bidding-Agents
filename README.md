# 📈 GSP Auction Bidding Agents

**Python Project - Dynamic Bidding Strategy (HW 3)**

## 💡 Overview
This project implements dynamic bidding agents designed to maximize profit within a **Generalized Second Price (GSP) Auction** environment. The solution focuses on an adaptive strategy to learn and compete against unknown opponent behaviors.

## 🎯 Core Mechanism: Agent 2 (Exploration/Exploitation)

The key strategy is implemented in Agent 2, which uses a learning approach to dynamically set its bid:

1.  **Exploration:** The agent starts with a static baseline bid ($v/2.5$) for initial rounds to collect competitor data.
2.  **Learning:** It uses **Exponential Moving Average (EMA)** to track the competitor's score (the price paid, `payment`), allowing the agent to adapt quickly to changes in the auction environment.
3.  **Exploitation:** The final bid is set dynamically based on the learned EMA value to secure a win while minimizing cost.

## 📄 Project Files

| File Name | Description |
| :--- | :--- |
| **`bidding_agents.py`** | Implementation of Agent 1 (static $v/2.5$) and the core **Agent 2 (EMA-based dynamic bid)**. |
| **`methodology_report.pdf`** | Detailed report on the strategy. |
