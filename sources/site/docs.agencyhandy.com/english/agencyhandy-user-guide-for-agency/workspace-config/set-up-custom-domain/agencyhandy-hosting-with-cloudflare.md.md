# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain/agencyhandy-hosting-with-cloudflare.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain/agencyhandy-hosting-with-cloudflare.md).

# AgencyHandy Hosting with Cloudflare

{% embed url="<https://youtu.be/4PGeGU\_KXao>" %}

AgencyHandy allows users to host their platform with Cloudflare, leveraging its global network to improve performance, security, and reliability. Cloudflare enhances page load speeds, protects against cyber threats, and ensures consistent uptime.\\
Hosting AgencyHandy with Cloudflare involves integrating your domain with Cloudflare’s content delivery network (CDN) and security services to optimize performance and safeguard operations.

### \*\*Purpose:\*\*

\* \*\*Enhanced Performance:\*\* Cloudflare’s CDN reduces latency and improves page load times by caching and delivering content from servers closest to users.
\* \*\*Increased Security:\*\* Protects against DDoS attacks, malicious bots, and other cyber threats.
\* \*\*Improved Reliability:\*\* Ensures high uptime and consistent platform availability.

### \*\*Pre-conditions:\*\*

\* An active AgencyHandy subscription.
\* A Cloudflare account.
\* Permission to manage DNS settings for your domain.

### \*\*Steps to Use (Detailed):\*\*

1. \*\*Sign Up for Cloudflare:\*\*
 \* Visit the \[Cloudflare website\](https://www.cloudflare.com) and create an account if you don’t have one.

2. \*\*Add Your Domain to Cloudflare:\*\*

 \* After signing up, enter your domain name in the Cloudflare dashboard.
 \* Follow the prompts to scan your domain’s DNS records.

 <figure><img src="/files/Xa6H0679OkHoAspUq4w3" alt=""><figcaption></figcaption></figure>

3. \*\*Update DNS Settings:\*\*

 \* Cloudflare will provide new nameservers.
 \* Log in to your domain registrar’s account and replace your current nameservers with the ones provided by Cloudflare.

 <figure><img src="/files/zlZCWeJ6QpNXc1lYLvUk" alt=""><figcaption></figcaption></figure>

4. \*\*Manage DNS Records:\*\*
 \* In the Cloudflare dashboard, navigate to \*\*DNS Settings\*\*.
 \* Click the \*\*+ Add Record\*\* button and input the following:

 \* \*\*Type:\*\* Select the DNS record type (e.g., CNAME or A Record).<br>

 <figure><img src="/files/cPXhrmHTo5qXLhZLuJbZ" alt=""><figcaption><p>Click the Down arrow and choose CNAME<br></p></figcaption></figure>

 \* \*\*Name:\*\* Enter the subdomain or root domain (e.g., www).<br>

 <figure><img src="/files/mh7QL3njroc9j0QRZohP" alt=""><figcaption><p>Write down the Name </p></figcaption></figure>

 \* \*\*Content/Target:\*\* Provide the target information, such as the platform’s server address.<br>

 <figure><img src="/files/wRjbpQCr1egFdxo73DVW" alt=""><figcaption><p>Copy &#x26; paste the content/target</p></figcaption></figure>

 \* \*\*TTL:\*\* Set the desired Time-To-Live value for the record.<br>

 <figure><img src="/files/QFNsCvpi9rwQ6HdTYK8u" alt=""><figcaption><p>Set the TTL (Time To Live) to 2 min </p></figcaption></figure>

5. \*\*Disable Cloudflare Proxy:\*\*
 \* For relevant DNS records, ensure the orange cloud icon in the dashboard is \*\*disabled\*\*. This prevents proxying and ensures direct communication with AgencyHandy servers.\\ <br>

 <figure><img src="/files/gyVaIIew59RdeuM871Iv" alt=""><figcaption><p>Click the Radio button to disable the proxy status<br></p></figcaption></figure>

6. \*\*Save Records:\*\*

 \* Double-check the DNS records for accuracy.
 \* Click the \*\*Save\*\* button to finalize the DNS configuration.

 <figure><img src="/files/wBowMPxxX8potqDRROoM" alt=""><figcaption><p>Click Save button</p></figcaption></figure>

\*\*\*

### \*\*Important Notes:\*\*

\* \*\*DNS Propagation:\*\* It may take up to 24 hours for DNS changes to propagate globally.
\* \*\*Verify Settings:\*\* Use a DNS checker (e.g., \[dnschecker.org\](https://dnschecker.org)) to confirm the domain is correctly configured.
\* \*\*Disable Proxying:\*\* Always ensure the orange cloud icon is disabled for relevant records to maintain proper communication with AgencyHandy.
\* \*\*Secure Access:\*\* Enable additional Cloudflare security features such as SSL/TLS encryption for secure communication.

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain/agencyhandy-hosting-with-cloudflare.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.