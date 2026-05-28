# performance-review-assistant

AI Performance Review Assistant
A performance review tool that aligns employees and managers on goals, tracks progress through the quarter, and generates AI-powered review summaries — replacing inconsistent, time-consuming review cycles with a structured, outcome-driven process.
The Problem
Performance reviews are broken in most organizations:

Employees struggle to articulate impact. In the flow of daily work, contributions get forgotten or poorly summarized at review time.
Managers spend hours writing feedback that's often inconsistent, biased, or misaligned with what the employee actually did.
There's a fundamental misalignment — employees and managers lack shared documentation of goals and expectations, leading to surprise outcomes and wasted effort on both sides.

Core insight: The problem isn't the review itself — it's the absence of continuous, structured alignment throughout the quarter.
How It Works
The tool creates a shared, goal-oriented feedback loop across three stages:
1. Goal Setting (Start of Quarter)
Employees and managers collaboratively define outcome-oriented goals or projects. These become the foundation everything is measured against.
2. Continuous Tracking (During Quarter)

Employees input artifacts, meeting notes, and progress updates against their goals.
Managers provide brief ongoing feedback (1–2 lines) at regular check-in intervals.
Weekly reminders keep both sides engaged without adding overhead.

3. AI-Generated Summary (End of Quarter)
The assistant collates employee data and manager feedback to generate a draft performance summary for both parties — aligned to the employee's goals and objectives, with clear next steps. Both review the summary before a final conversation.
Why AI
Every employee-manager relationship is different. A rule-based system can't account for that variation — but an LLM can:

Semantic similarity over subjective judgment. Reviews are generated from documented outcomes and feedback, not personal bias.
Contextual summarization. The model draws on employee artifacts, manager input, and organizational context (role definitions, HR frameworks, company strategy) to produce reviews grounded in facts.
Actionable next steps. Summaries include growth recommendations aligned to HR-defined career frameworks for the employee's role and level.

Architecture
Model approach: LLM with RAG (Retrieval-Augmented Generation)
The data is individual-specific and limited in scope — primarily summarization from context rather than broad knowledge retrieval. RAG enables the LLM to pull relevant employee information from company databases: role, responsibilities, past reviews, and organizational context.
Data strategy:
The system relies on user-input data initially and uses feedback loops to improve over time. Data flows through three stages — input, ongoing context, and evaluation — with PII protection and bias mitigation considered at each.
StageData SourcesInputEmployee project data, manager feedback, quarterly goalsContextHR data (role, level, past reviews), company vision and strategyOngoingProgress updates and feedback captured during the quarter
Guardrails:

PII protection to prevent employee data leakage
Bias detection on historical data (e.g., labeling past reviews as high/low quality to prevent reinforcing existing bias)

Evaluation Strategy
Pre-launch:

Human review of every generated summary against HR-defined role expectations
Labeled historical reviews (good/bad) used to calibrate output quality and reduce bias
LLM-as-a-judge introduced after human baseline is established, with ongoing human spot-checks

Post-launch:

HR acts as human-in-the-loop, mediating final submitted reviews
Monitoring for mismatches between manager feedback and employee-reported data
Logging of employee engagement (frequency of progress updates through the quarter)
HR maintains updated role and responsibility definitions per employee

Metrics
TypeMetricNorth Star% of successful performance reviews per quarterSuccessTime spent on reviews at end of quarter (target: reduction)SuccessNumber of accurate reviews submitted (aligned to HR standards + employee goals)CounterNumber of rewrites needed on final draftsCounter% of employees providing data during the quarter (low = adoption risk)Counter% mismatch between employee data and manager feedback
MVP Scope
Assumption: HR has defined roles and responsibilities per level, available in the HR database.
In scope:

Employees and managers input quarterly goals at the start of the quarter
Weekly reminders for both parties to log feedback and progress
AI-generated quarterly summary after 3 months
Employee can initiate a review call with manager once summary is ready

Out of scope (future):

AI scheduling review calls or submitting reviews on behalf of employees
AI-generated drafts for intermediary progress stages

Status
🔨 In development — PRD complete, building toward MVP.
Tech Stack

LLM API (with RAG pipeline)
Prompt engineering for role-aware, bias-mitigated summarization
Database integration for HR context retrieval


Built by Shruti Chowdhary — exploring how AI can make workplace processes more aligned, less biased, and less painful.
