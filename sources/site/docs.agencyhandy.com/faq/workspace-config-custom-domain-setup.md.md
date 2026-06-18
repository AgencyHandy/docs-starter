# Source: https://docs.agencyhandy.com/faq/workspace-config-custom-domain-setup.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/faq/workspace-config-custom-domain-setup.md).

# Workspace Config - Custom Domain Setup

#### \*\*Custom Domain Setup in Agency Handy – Frequently Asked Questions\*\*

\*\*\*

#### \*\*1. What is the Custom Domain feature in Agency Handy?\*\*

The Custom Domain feature allows you to link your own website address (e.g., \`client.yourbusiness.com\`) to your Agency Handy workspace. This enhances brand identity, professionalism, and makes it easier for clients to access your platform.

\*\*\*

#### \*\*2. Why should I use a Custom Domain?\*\*

Using a Custom Domain provides:

\* \*\*Brand Reinforcement\*\*: Your domain represents your brand.
\* \*\*Professionalism\*\*: Adds credibility to your workspace.
\* \*\*Ease of Access\*\*: Makes it easy for clients to find and remember your site.

\*\*\*

#### \*\*3. Who can set up a Custom Domain in Agency Handy?\*\*

Only users with Super Admin or Admin access can configure a Custom Domain.

\*\*\*

#### \*\*4. What are the pre-conditions to set up a Custom Domain?\*\*

To set up a Custom Domain, you must:

\* Own a domain name.
\* Have authority to modify DNS settings for that domain.

\*\*\*

#### \*\*5. How do I access the Custom Domain settings?\*\*

1. Log in to your \*\*Agency Handy\*\* account.
2. Navigate to \*\*Workspace Settings\*\*.
3. Click on \*\*Custom Domain\*\*.
4. Press the \*\*+ Add Custom Domain\*\* button.

\*\*\*

#### \*\*6. What should I enter in the domain name field?\*\*

You need to enter your desired subdomain, such as \`client.yourbusiness.com\`.

> ⚠️ \*\*Avoid using "www"\*\* as a subdomain, as it may cause configuration conflicts.

\*\*\*

#### \*\*7. How do I configure the DNS settings?\*\*

1. Copy the \*\*Type, Name, and Value\*\* provided in Agency Handy.
2. Log in to your \*\*domain registrar\*\* or \*\*hosting provider\*\*.
3. Add a \*\*CNAME record\*\* using the information provided.
4. Ensure the \*\*DNS only settings in Proxy Status are OFF\*\*.

\*\*\*

#### \*\*8. What if I use Cloudflare for DNS?\*\*

\* When using \*\*Cloudflare\*\*, ensure that \*\*Proxy Status\*\* is set to \*\*DNS Only\*\*.
\* The cloud icon should be \*\*grey\*\* (not orange).

\*\*\*

#### \*\*9. How do I verify ownership of the domain?\*\*

To verify ownership:

\* Add the provided \*\*DNS record\*\* to your domain settings.
\* Sometimes, verification might also include an \*\*email confirmation\*\*.
\* Click \*\*Save Domain\*\* within Agency Handy.

\*\*\*

#### \*\*10. How long does it take for my domain to connect?\*\*

\* Typically, it takes \*\*2 minutes to 24 hours\*\* for the domain to propagate and connect.
\* You can \*\*refresh\*\* the connection status from your Agency Handy dashboard.

\*\*\*

#### \*\*11. How can I check the status of my custom domain?\*\*

\* Use a \*\*DNS Checker\*\* (e.g., \[dnschecker.org\](https://dnschecker.org)) to monitor the status.
\* If all countries are marked with a \*\*tick\*\*, your domain is live.
\* If not, wait a bit longer and check again.

\*\*\*

#### \*\*12. What should I do if the status shows "Disconnected"?\*\*

If it remains \*\*Disconnected\*\* after 24 hours:

\* Double-check your \*\*CNAME\*\* or \*\*A records\*\*.
\* Ensure \*\*Proxy Status\*\* is off (DNS Only).
\* Verify there are \*\*no conflicting records\*\*.

\*\*\*

#### \*\*13. Can I use "www" as a subdomain?\*\*

No, it is recommended to avoid using "www" as a subdomain to prevent conflicts. Instead, use formats like:

\* \`client.yourbusiness.com\`
\* \`portal.yourbusiness.com\`

\*\*\*

#### \*\*14. What happens if I remove a custom domain?\*\*

If you delete a custom domain:

\* Your workspace will revert to the default \*\*Agency Handy domain\*\*.
\* You can re-add the custom domain anytime.

\*\*\*

#### \*\*15. Can I re-add a deleted custom domain?\*\*

Yes, you can re-add it by providing the same domain name during setup.

\*\*\*

#### \*\*16. How do I troubleshoot connection issues?\*\*

If your domain doesn't connect:

\* Ensure \*\*DNS records\*\* were added correctly.
\* Allow up to \*\*24 hours\*\* for DNS propagation.
\* Use \*\*DNS checking tools\*\* to verify settings.
\* Make sure \*\*Proxy Status\*\* is \*\*Off\*\* in Cloudflare or similar platforms.

\*\*\*

#### \*\*17. What happens if I want to change my domain name?\*\*

If you want to switch to a different domain:

1. Delete the existing custom domain.
2. Add the new domain following the setup steps.

\*\*\*

#### \*\*18. Are there any naming guidelines for the domain?\*\*

\* Only use \*\*subdomains\*\* like \`client.yourbusiness.com\`.
\* Do not use "www" to avoid conflicts.
\* Ensure the name is \*\*valid and properly formatted\*\*.

\*\*\*

#### \*\*19. Can I use the root domain (e.g., \`yourbusiness.com\`) instead of a subdomain?\*\*

No, currently, Agency Handy only supports \*\*subdomains\*\*. Root domains are not recommended for configuration.

\*\*\*

#### \*\*20. How often do I need to verify my DNS settings?\*\*

Generally, you only need to verify once during the initial setup. However, if you make changes to your DNS, you should re-verify to avoid downtime.

\*\*\*

#### \*\*21. What if my domain provider doesn't support CNAME records?\*\*

Most providers support \*\*CNAME\*\* records. If yours does not, consider transferring your domain to a different provider that does.

\*\*\*

#### \*\*22. Is SSL/TLS configured automatically with a custom domain?\*\*

Yes, SSL/TLS encryption is automatically applied once your custom domain is verified and connected.

\*\*\*

#### \*\*23. Do I need to republish my workspace after domain changes?\*\*

No, the workspace updates automatically once the custom domain is verified and connected.

\*\*\*

#### \*\*24. What if I want to remove Agency Handy branding from the custom domain?\*\*

You can upgrade your plan to have a fully \*\*white-labeled experience\*\*, removing Agency Handy branding.

\*\*\*

#### \*\*25. Can I link multiple custom domains to a single workspace?\*\*

Currently, you can only link \*\*one custom domain\*\* per workspace.

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/faq/workspace-config-custom-domain-setup.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.