# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/orders/create-tasks-in-an-order.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/orders/create-tasks-in-an-order.md).

# Create Tasks in an Order

Integrating task creation directly into the order form simplifies the workflow and ensures that tasks are associated with specific orders from the outset. This feature enhances efficiency by reducing the need to switch between different sections of the software to create tasks for orders.

## Pre-condition to Use the Feature:&#x20;

\* Users must have an active account on AgencyHandy and be logged in.&#x20;
\* Users must be Super Admin/ Admin/ PM to create tasks.

## Steps to Use:

\* \*\*Log in to AgencyHandy:\*\* Access your AgencyHandy account using your credentials.&#x20;
\* \*\*Navigate to Orders:\*\* Locate the "Orders" section in the dashboard menu. Choose the "Order" in which you want to add tasks.
\* \*\*Add New Task:\*\* Within the Order form, click on the option to add a new task within the task section. A form will pop up.
\* \*\*Enter Task Details:\*\* Provide details for the task, such as title, description, due date, priority, and assignee.&#x20;
\* \*\*Save Task:\*\* Once all necessary details, including tasks, are entered, save the order to finalize the creation or editing process.&#x20;

<figure><img src="/files/7VP8QERYWk5vhh9J48Q7" alt=""><figcaption></figcaption></figure>

### Important Notes:

\* A check box is included in the Task creation form to indicate that client review is required for task completion. By default, it is checked, so the user does not have to select it each time.
\* A notification will be sent to the client when a task is created.
\* PM, Super Admin, and Admin can create a task.
\* Only the admin, super admin, and PM can send and reply to feedback from the clients in a task.
\* Users can see the tasks that are in "in review" and "done" status.
\* When user rejects a task from the in review status, the status changes to the "In Progress."&#x20;
\* Note that, users can't see "In Progress" tasks.

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/orders/create-tasks-in-an-order.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.