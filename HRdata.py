employee_context = (f"""
You are given HR data for employees at a mid-sized technology company operating in SaaS and AI products. The company has engineering, product, data, sales, and operations teams. Below is anonymized employee information across levels.

Employee 1:
Role: Junior Software Engineer
Level: L1
Experience: 1.2 years
Location: Bangalore
Team: Backend Engineering
Skills: Python, REST APIs, SQL
Performance Rating: 3/5
Last Promotion: None
Tenure: 1.2 years
Engagement Score: 6/10
Manager Feedback: Quick learner but needs guidance on system design and code quality.
Attrition Risk: Medium

Employee 2:
Role: Software Engineer
Level: L2
Experience: 3 years
Location: Dublin
Team: Payments Engineering
Skills: Java, Microservices, AWS
Performance Rating: 4/5
Last Promotion: 1 year ago
Tenure: 2.5 years
Engagement Score: 8/10
Manager Feedback: Strong contributor, owns modules independently.
Attrition Risk: Low

Employee 3:
Role: Senior Software Engineer
Level: L3
Experience: 6 years
Location: Bangalore
Team: Platform Engineering
Skills: Distributed Systems, Kubernetes, Go
Performance Rating: 5/5
Last Promotion: 2.5 years ago
Tenure: 4 years
Engagement Score: 7/10
Manager Feedback: High performer, but showing signs of burnout.
Attrition Risk: High

Employee 4:
Role: Data Scientist
Level: L3
Experience: 5 years
Location: London
Team: AI/ML
Skills: Machine Learning, Python, NLP
Performance Rating: 4/5
Last Promotion: 2 years ago
Tenure: 3 years
Engagement Score: 7/10
Manager Feedback: Strong technical skills, needs to improve stakeholder communication.
Attrition Risk: Medium

Employee 5:
Role: Product Manager
Level: L3
Experience: 7 years
Location: Dublin
Team: Payments Product
Skills: Product Strategy, SQL, Agile, Stakeholder Management
Performance Rating: 5/5
Last Promotion: 1.5 years ago
Tenure: 3.5 years
Engagement Score: 9/10
Manager Feedback: Drives high-impact initiatives, excellent cross-functional leadership.
Attrition Risk: Low

Employee 6:
Role: Senior Product Manager
Level: L4
Experience: 10 years
Location: London
Team: Growth
Skills: Experimentation, Data Analytics, Roadmapping
Performance Rating: 4/5
Last Promotion: 3 years ago
Tenure: 5 years
Engagement Score: 6/10
Manager Feedback: Good execution but lacks innovation in strategy.
Attrition Risk: Medium

Employee 7:
Role: Engineering Manager
Level: L5
Experience: 12 years
Location: Bangalore
Team: Platform Engineering
Skills: System Design, Team Leadership, Architecture
Performance Rating: 4/5
Last Promotion: 2 years ago
Tenure: 6 years
Engagement Score: 7/10
Manager Feedback: Strong leader, but team velocity has slowed.
Attrition Risk: Medium

Employee 8:
Role: Director of Engineering
Level: L6
Experience: 15 years
Location: Dublin
Team: Core Infrastructure
Skills: Org Leadership, Distributed Systems, Cloud
Performance Rating: 5/5
Last Promotion: 3 years ago
Tenure: 7 years
Engagement Score: 8/10
Manager Feedback: Strategic thinker, successfully scaled teams.
Attrition Risk: Low

Employee 9:
Role: VP of Product
Level: L7
Experience: 18 years
Location: London
Team: Product Organization
Skills: Product Vision, Stakeholder Alignment, GTM Strategy
Performance Rating: 4/5
Last Promotion: 4 years ago
Tenure: 6 years
Engagement Score: 6/10
Manager Feedback: Strong leadership but slower decision-making recently.
Attrition Risk: Medium

Employee 10:
Role: SVP of Engineering
Level: L8
Experience: 22 years
Location: San Francisco
Team: Global Engineering
Skills: Org Scaling, Technical Strategy, Executive Leadership
Performance Rating: 5/5
Last Promotion: 5 years ago
Tenure: 8 years
Engagement Score: 7/10
Manager Feedback: Drives long-term vision, but org complexity is increasing.
Attrition Risk: Low
""")

roles_context = (f"""
You are given role definitions and responsibilities for employees at a mid-sized SaaS and AI technology company. The organization includes engineering, product, data, and leadership roles across multiple levels. Use this information to analyze responsibilities, career progression, organizational gaps, or decision-making structures.

Employee 1:
Role: Junior Software Engineer
Level: L1
Team: Backend Engineering
Reports To: Software Engineer (L2)
Responsibilities:
- Write and maintain simple backend services and APIs
- Fix bugs and support production issues under guidance
- Participate in code reviews and incorporate feedback
- Learn system design fundamentals and internal tools
- Collaborate with team members on small feature tasks
Scope:
Works on well-defined tasks with clear requirements and supervision

Employee 2:
Role: Software Engineer
Level: L2
Team: Payments Engineering
Reports To: Senior Software Engineer (L3)
Responsibilities:
- Develop and maintain scalable backend services
- Own small to medium features end-to-end
- Write clean, efficient, and testable code
- Participate in design discussions and suggest improvements
- Troubleshoot production issues and ensure system reliability
Scope:
Owns modules independently with moderate complexity

Employee 3:
Role: Senior Software Engineer
Level: L3
Team: Platform Engineering
Reports To: Engineering Manager
Responsibilities:
- Design and build scalable distributed systems
- Lead development of complex features and projects
- Mentor junior engineers and review code
- Drive best practices in performance, reliability, and security
- Collaborate with product and design teams on technical feasibility
Scope:
Owns large systems/components and influences technical direction

Employee 4:
Role: Data Scientist
Level: L3
Team: AI/ML
Reports To: Data Science Manager
Responsibilities:
- Build and deploy machine learning models
- Analyze large datasets to generate insights
- Collaborate with product teams to define ML use cases
- Evaluate model performance and iterate based on feedback
- Communicate findings to technical and non-technical stakeholders
Scope:
Owns end-to-end ML workflows for defined problem areas

Employee 5:
Role: Product Manager
Level: L3
Team: Payments Product
Reports To: Senior Product Manager
Responsibilities:
- Define product requirements and user stories
- Prioritize backlog based on business and customer needs
- Collaborate with engineering, design, and stakeholders
- Analyze user behavior and product performance metrics
- Drive delivery of features from concept to launch
Scope:
Owns a product area or feature set with clear KPIs

Employee 6:
Role: Senior Product Manager
Level: L4
Team: Growth
Reports To: Director of Product
Responsibilities:
- Define product strategy and roadmap for a key domain
- Lead cross-functional initiatives across teams
- Drive experimentation and data-driven decision making
- Mentor junior product managers
- Align stakeholders on product vision and priorities
Scope:
Owns a major product area with business impact

Employee 7:
Role: Engineering Manager
Level: L5
Team: Platform Engineering
Reports To: Director of Engineering
Responsibilities:
- Manage and mentor a team of engineers
- Plan and deliver engineering projects on time
- Ensure system reliability, scalability, and performance
- Partner with product managers on roadmap execution
- Handle team hiring, performance reviews, and career development
Scope:
Owns team delivery and execution quality

Employee 8:
Role: Director of Engineering
Level: L6
Team: Core Infrastructure
Reports To: VP of Engineering
Responsibilities:
- Define technical strategy and architecture for multiple teams
- Scale engineering teams and processes
- Drive cross-team alignment and execution
- Ensure long-term system scalability and reliability
- Partner with product and business leaders on strategic initiatives
Scope:
Owns multiple teams and technical direction at org level

Employee 9:
Role: VP of Product
Level: L7
Team: Product Organization
Reports To: Chief Product Officer
Responsibilities:
- Define product vision and long-term strategy
- Oversee multiple product lines and teams
- Drive alignment between business, product, and engineering
- Own product KPIs including revenue and customer growth
- Represent product organization in executive decisions
Scope:
Owns product portfolio and business outcomes

Employee 10:
Role: SVP of Engineering
Level: L8
Team: Global Engineering
Reports To: CTO
Responsibilities:
- Define engineering vision and organizational strategy
- Oversee all engineering teams and leaders
- Drive large-scale transformation and innovation initiatives
- Ensure alignment with company-wide goals and priorities
- Manage executive stakeholders and board-level communication
Scope:
Owns global engineering organization and long-term technology direction
""")
