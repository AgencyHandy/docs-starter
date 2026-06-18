# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-emails/email-template-configuration.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-emails/email-template-configuration.md).

# Email Template Configuration

The Email Templates feature in AgencyHandy allows agencies to configure email templates for various communication scenarios, ensuring consistent and professional correspondence with clients. Agencies can customize templates for client sign-ups, proposal submissions, task reviews, ticket creation, invoice sending, and more.

### \*\*What:\*\*

This feature enables agencies to set up and manage email templates for invoice reminders, subscription reminders, client notifications, and more.

### Purpose:&#x20;

Configuring email templates offers several benefits:

\* Consistency: Email templates ensure consistent communication by standardizing the format and content of client emails.
\* Efficiency: Pre-defined templates save time by eliminating the need to compose emails from scratch for common scenarios.
\* Professionalism: Well-designed templates enhance the agency's professional image and brand consistency in client communications.

### \*\*Pre-conditions:\*\*

\* Users must have administrative access to manage email templates.
\* The sender email and SMTP setup must be configured in AgencyHandy.

### \*\*Steps to Use:\*\*

\*\*Log In to Your AgencyHandy Account:\*\*

\* Access your account using your credentials.

1. \*\*Navigate to Workspace Config:\*\*
 \* On the left-hand menu, click on \*\*Workspace Config\*\*.
2. \*\*Access Email Templates Section:\*\*
 \* Under the \*\*Emails\*\* dropdown, select \*\*Email Template\*\* to view the list of available templates.
3. \*\*View Available Email Templates:\*\*
 \* A variety of templates are displayed, such as:

 \* \*\*Client Sign-up Template\*\*
 \* \*\*Send Proposal Template\*\*
 \* \*\*Task Review Template\*\*
 \* \*\*Send Invoice Template\*\*
 \* \*\*Reminders Template\*\*.

 <figure><img src="/files/TAUfGr04hLTvzti3F45s" alt=""><figcaption></figcaption></figure>
4. \*\*Select a Template to Edit:\*\*
 \* Click on any template to open its configuration page.
5. \*\*Customize the Email Template:\*\*
 \* Update the following fields as needed:

 \* \*\*Sender Email:\*\* Select the email address from which to send it.
 \* \*\*Dynamic Variables:\*\* Add placeholders like {{company\\\_name}}, {{client\\\_name}}, or {{invoice\\\_id}} to personalize emails.
 \* \*\*Subject:\*\* Write a clear and concise subject line.
 \* \*\*Body:\*\* Customize the message body to align with your communication goals.
 \* \*\*Social Media Links:\*\* Add links to your agency's pages to encourage client engagement.

 <figure><img src="/files/BgVdYev3uo3EBoLqBdui" alt=""><figcaption></figcaption></figure>

 <figure><img src="/files/uVhGI8uDLjqfs45wERUV" alt=""><figcaption></figcaption></figure>
6. \*\*Preview and Test the Email Template:\*\*
 \* Use the \*\*Send Test\*\* button to send a test email to verify the template's functionality and layout.
7. \*\*Save Changes:\*\*
 \* After making the necessary updates, click \*\*Save Changes\*\* to apply the modifications.

\*\*\*

### \*\*Important Notes:\*\*

\* Ensure that the sender email is correctly set up in the SMTP configuration.
\* Dynamic variables like {{client\\\_name}} and {{invoice\\\_id}} automatically populate relevant client-specific data in the email.
\* Default templates are available for invoice reminders, subscription reminders, and other notifications, and they can be customized further.
\* Test emails allow you to verify the content and format before sending them to clients.

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-emails/email-template-configuration.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.