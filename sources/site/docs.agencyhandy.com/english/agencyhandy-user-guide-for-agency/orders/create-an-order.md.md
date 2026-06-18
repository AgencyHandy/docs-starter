# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/orders/create-an-order.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/orders/create-an-order.md).

# Create an Order

Creating an order is essential for initiating client transactions and facilitating the delivery of products or services. This feature ensures a seamless workflow by providing users with a structured method to input order details, enabling accurate order processing and effective client communication.

## Pre-condition to Use the Feature:

\* Users must have an active account on AgencyHandy and be logged in.&#x20;
\* Users must be Super Admin/Admin to create orders.

### Steps to Use:

\* \*\*Log in to AgencyHandy:\*\* Access your AgencyHandy account using your credentials.&#x20;
\* \*\*Navigate to Orders:\*\* Locate the "Orders" section in the dashboard menu.&#x20;
\* \*\*Initiate Order Creation:\*\* Click the "Create New Order" to start the order creation process.&#x20;
\* \*\*Enter Order Details:\*\* A form will pop up. Fill in the required fields, such as client information, service name, Project Manager (it's optional), order specifics, quantity, price, and any additional details relevant to the order.

<figure><img src="/files/o2p62ZQPMGEUNY2BQMyx" alt=""><figcaption></figcaption></figure>

\* \*\*Review Order Information:\*\* Double-check all entered information for accuracy and completeness.
\* \*\*Submit Order:\*\* Once satisfied with the details, submit the order by clicking the "Submit" or "Create Order" button. Confirmation: You will receive a confirmation message confirming the successful creation of the order.
\* Click the Create button. The Order is created.

### Important Notes:

\* An order has five pre-defined statuses. Pending, Ongoing, In Review, Complete, Cancelled. You can't edit/add a new status.
\* After creating an order (By PM, super admin, admin), all the super admins in a company will get access to the order and send a created order notification to the client.
\* Only the PM, Super Admin, and Admin can change the status.
\* SuperAdmin, Admin, and PM can add employees to an order. The member will get a notification.
\* Super Admin, PM, and Client can send feedback/chat.

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/orders/create-an-order.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.