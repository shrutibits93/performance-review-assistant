AI Performance Review

Context:
Employees struggle to summarize their work impact
Managers spend significant time writing structured feedback
Reviews are often:
•	Inconsistent
•	Biased
•	Low quality

Problem:
Employees and managers are spending significant time on performance reviews without the desired outcome.
Pain points as per context:
1.	There is a challenge for employees to clearly articulate their value contributed – in the ebb and flow of work, sometimes it becomes easy to forget work done and equivalent value
2.	There is a mismatch between what employees and managers articulate despite spending significant time and effort
Core problem: There seems to be a lack of shared alignment or documentation about goals and expectations between employees and managers.

Success would be:
Employees and managers are aligned on what the employee is working on which leads to smoother, higher quality reviews – employees and managers are both satisfied after putting in the time and effort.

Product: How success is achieved
A performance review assistant can help solve the above problems. 
In a tool, employees and managers can agree on few outcome-oriented goals or projects for the employee. These can be tracked over a quarter. Employees and managers can update their progress and feedback regularly with the help of the tracker. 
At the end of the quarter, based on the entries throughout the period, the assistant can provide a draft summary to both employees and managers for review. Managers and employees can both view this summary and meet to finalise based.

Features-
1.	Enter goals at the beginning of the quarter, with check-in dates
2.	Along the quarter, 
a.	employees can input their artifacts and any relevant meeting notes or materials.
b.	Manager can provide 1-2 lines of feedback (ongoing feedback)
3.	At the end of the quarter, AI assistant will provide a summary of performance by collating employee data and manager feedback and present to both employee and manager. 
Summary will contain summary on performance and next steps all in alignment with employees’ goals and objectives. 
Features can be scoped as per priority.

AI Considerations:

Why AI: Since every employee is different and every employee manager is also varied, this provides a feedback based on outcome of the employee and what manager feels from time to time on the outcome. AI can help use semantic similarity to create reviews based on facts and not personal bias. It can also help summarise next steps based on organizational data and HR defined frameworks for roles and levels, which can help provide a clearer path to employees and manager. 

Model:
LLM RAG with appropriate prompting can be used as the data is limited and very individual specific. More of data summarisation is needed from context than company specific information.
RAG is needed so that LLM can get relevant employee information from the company databased – employees’ role, responsibilities, past reviews, etc.

Data Strategy and flow:

Data will be needed at various points of the flow. The strategy is to rely on user-input data initially and move towards user feedback to create a continuous cycle of improvement. Data will need to be considered at various stages – input, ongoing context and feedback, testing and evaluation. At each stage PII and bias will have to be considered.
Input data: Employee project data and manager feedback

Context: 

1.	HR data of employee, past reviews, company specific data like companies’ vision, direction and strategy which can be directly aligned to employees work and value. 
2.	Data input during the quarter 

Considerations: 
1.	I will ensure there are guardrails in place to ensure PII data (employee data) is not leaked 
2.	Past data can lead to bias, appropriate evaluation and testing will be in place

UX flow:
 
<img width="432" height="465" alt="image" src="https://github.com/user-attachments/assets/16aecfc2-960f-499d-b874-62378f9e93f8" />


Metrics:

North Star:
% successful performance reviews in a quarter

Success Metrics:
1.	Amount of time spent on reviews at the end of the quarter
2.	Number of accurate reviews submitted – aligning to HR standards and employee goals

Counter metrics:
1.	Number of rewrites of final drafts
2.	Number of employees providing data during the quarter
3.	% mismatches between employee data and manager feedback

Evaluation:

Pre-launch:
During the testing phase it is very important to have humans test the system. 
1.	Based on HR defined roles and responsibilities, every individual’s review should be vetted by humans. 
2.	While testing the system, it’s important to label the past reviews and data. For example, marking past reviews that were good and bad can help provide context and remove bias.
Post human testing, LLM as a judge can be introduced with humans still evaluating from time to time.
Post-launch: 
HR can be the humans in the loop mediating final reviews submitted by employees and managers. Mismatch between manager feedback and employee data needs to be monitored 
Ongoing Evaluation:
1.	Logging needs to be in place to check how often employees provide continuous progress updates through the quarter
2.	HR needs to keep the roles and responsibilities updated for each employee. 

MVP:

The MVP will build the foundation of this product. Employees and Managers will have a more seamless review experience
Assumption: HR will define the roles and responsibilities, and these are already available in the HR database for every role and level.

In scope:
1.	Ability for Employees and Managers to input quarterly goals at the start of the quarter.
2.	Weekly reminders available for Managers and Employees to input quick feedback and progress. 
3.	Quarterly summary available at the end of 3 months
4.	Ability for Employee to initiate quarterly call with Manager once summary is ready 

Out of scope:
1.	Ability of AI to setup calls for review or submit review on behalf of employees
2.	No drafts provided for intermediary progress stage





