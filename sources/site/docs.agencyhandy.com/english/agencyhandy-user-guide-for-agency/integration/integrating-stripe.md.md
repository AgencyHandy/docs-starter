# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/integrating-stripe.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/integrating-stripe.md).

# Integrating Stripe

Agency Handy’s Stripe Integration enables secure and seamless online payments. Once connected, agencies can send invoices and collect payments directly from within the platform, eliminating manual processing and improving client experience.

### What You Can Do

\* Connect your Stripe account to Agency Handy
\* Accept secure online payments from clients
\* Generate and send invoices that clients can pay via Stripe
\* Automate payment reconciliation and financial tracking
\* Enhance the payment experience with fast, secure transactions

### Why It Matters

\* Reduces friction in payment collection
\* Saves time by automating invoice and payment workflows
\* Offers clients a trusted and familiar payment method
\* Improves financial visibility with real-time reporting and status updates

### Who Can Use This

To set up and manage Stripe Integration, users must:

\* Have an active Agency Handy account
\* Have a verified Stripe account with appropriate permissions
\* Be assigned a SuperAdmin or Admin role within Agency Handy
\* Have access to Integration settings

### Getting Started

1. Access Integration Settings

\* Go to the left sidebar
\* Navigate to Integrations → Stripe Integration<br>

2. Authorize the Integration

\* Click Connect Stripe
\* You’ll be redirected to Stripe’s authorization screen
\* Log into your Stripe account and authorize access
\* Once approved, you’ll be redirected back to Agency Handy<br>

3. Configure Payment Settings

\* Choose currency and preferred payment methods
\* Add optional billing preferences (e.g., tax, invoice prefix)
\* Set default payment terms or due dates<br>

4. Confirm Connection

\* Save and confirm the integration
\* Stripe is now linked to your workspace
\* A confirmation message will appear when successful<br>

5. Test the Integration (Optional)

\* Create a test invoice
\* Send it to yourself or a team member
\* Complete a test payment via Stripe
\* Verify that the invoice status updates in Agency Handy<br>

6. Manage Integration

\* Return to the Stripe Integration panel at any time to:
 \* Update payment settings
 \* Review connection status
 \* Disconnect and re-authorize the integration if needed

### Additional Notes

\* No payment credentials are stored by Agency Handy—Stripe handles all payment security
\* Only one Stripe account can be connected per workspace
\* Disconnected Stripe accounts will pause payment collection until reconnected
\* All invoices linked to Stripe will continue to reflect live status updates from Stripe

<figure><img src="/files/glyfk4zBt0d1bExGoL89" alt=""><figcaption></figcaption></figure>

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/integrating-stripe.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.