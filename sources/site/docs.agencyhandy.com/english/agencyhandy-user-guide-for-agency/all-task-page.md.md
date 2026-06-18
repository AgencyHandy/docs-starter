# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/all-task-page.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/all-task-page.md).

# All Task Page

The \*\*All Task Page\*\* in Agency Handy provides a centralized view of all tasks related to active workflows. Designed for operational transparency and role-based task access, this page helps teams stay aligned on what needs to be done, by whom, and when. It displays tasks from orders that are in \*\*ongoing\*\* or \*\*in-review\*\* status only, with visibility tailored to each user's role.

#### Goals

\* Provide real-time task visibility across relevant orders.
\* Respect role-based access to ensure users see only appropriate tasks.
\* Support intuitive task management with filtering, sorting, and inline controls.

#### Pre-conditions

\*\*Permissions Required:\*\* Task visibility and controls vary by user role.

\*\*Order Status Dependency:\*\* Tasks only appear when associated orders are marked as ongoing or in review.

\*\*\*

#### Table of Contents

1. Accessing the All Task Page
2. Task Visibility by Role
3. Trigger Conditions for Task Appearance
4. Task Deletion Rules
5. Editing Tasks
6. Search, Filter, and Navigation Tools
7. Important Notes

\*\*\*

### 1. Accessing the All Task Page

1. Log in to your \*\*Agency Handy\*\* account.
2. Click on \*\*Tasks\*\* in the left-hand menu.
3. Select \*\*All Tasks\*\* to view the centralized task dashboard.

📌 \*This page reflects tasks from orders that are either in ongoing or in-review states only.\*

\*\*\*

### 2. Task Visibility by Role

#### Superadmin / Admin:

\* Can view and manage \*\*all tasks\*\* across all orders, teams, and statuses.

#### Manager:

\* Sees only tasks linked to orders where they are assigned as the \*\*Manager\*\*.

#### Assignee:

\* Sees only the tasks to which they are \*\*directly assigned\*\*.
\* Cannot view tasks even from their team unless assigned.

\*\*\*

### 3. Trigger Conditions for Task Appearance

Tasks will appear in the All Task Page when the following conditions are met:

\*\*Manual Orders (One-time / Subscription)\*\* are created.&#x20;

\*\*Catalog Orders via Stripe or Manual Methods\*\* are placed.&#x20;

\*\*Proposal is accepted\*\* by the agency.

Tasks remain hidden until:

\* The agency accepts \*\*client-requested tasks\*\*.
\* \*\*Trial orders\*\* are accepted by the agency.
\* Orders with \*\*pending status\*\* (e.g., manual bank payment) are accepted.

\*\*\*

### 4. Task Deletion Rules

\* When an order is deleted, \*\*all associated tasks are automatically removed\*\* from the All Task Page.
\* This deletion is \*\*permanent\*\* and affects visibility for all user roles.

\*\*\*

### 5. Editing Tasks

Tasks listed on the All Task Page can be modified in two ways:

\* ✏️ \*\*Inline Editing:\*\* Edit directly within the task row.
\* 📄 \*\*Modal Editing:\*\* Click into the task to open and update full task details.

\*\*\*

### 6. Search, Filter, and Navigation Tools

The All Task Page is equipped with UI controls to streamline task management:

\* \*\*Search:\*\* Locate tasks by name, assignee, or related order.
\* \*\*Sorting:\*\* Organize tasks by due date, priority, or creation time.
\* \*\*Filters:\*\* Narrow tasks by status, role, or team.
\* \*\*Breadcrumb Navigation:\*\* Maintain contextual awareness while navigating between subtasks, lists, and orders.

\*\*\*

### 📝 Important Notes

\* Tasks are \*\*only shown\*\* for orders that are in an accepted or in-progress state.
\* \*\*Client-requested tasks\*\* require approval and will not appear until accepted.
\* Users only see what their role allows—visibility is filtered dynamically.
\* Deleted orders remove all associated tasks permanently—there is no recovery.
\* PMs do not see tasks unless they are assigned as \*\*Manager\*\* to that order.
\* Task edits can be performed quickly from the row or more deeply in modal views.
\* Changes to orders or task assignments will reflect in \*\*real-time\*\* on the All Task Page.

\*\*\*

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/all-task-page.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.