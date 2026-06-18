# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-emails/setup-email-address.md

\> For the complete documentation index, see \[llms.txt\](https://docs.agencyhandy.com/llms.txt). Markdown versions of documentation pages are available by appending \`.md\` to page URLs; this page is available as \[Markdown\](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-emails/setup-email-address.md).

# Setup Email Address

The Email feature in AgencyHandy allows agencies to configure email settings for their workspace. This includes setting up email addresses from which clients will receive emails and defining the sender name and email.

### Purpose:&#x20;

Setting up workspace email configuration is crucial for the following reasons:

\* \*\*Branding:\*\* Configuring sender names and email allows agencies to maintain brand consistency in their email communications with clients, reinforcing brand identity.
\* \*\*Professionalism:\*\* Providing a personalized sender name and email enhances the professionalism of email communications, building trust and credibility with clients.
\* \*\*Client Engagement:\*\* Using recognizable sender information increases the likelihood of clients engaging with and responding to emails, leading to improved communication and collaboration.

### Pre-condition to Use the Feature:

\* Users must have administrative access to the AgencyHandy workspace to configure email settings.&#x20;
\* Users must first set up a custom domain.
\* Users must set up DKIM & SPF records on the DNS server.&#x20;

### Steps to Use:

\* \*\*Choose a Domain Name:\*\* The first step is to select a domain name for your email address. This could be your personal name, business name, or anything else you prefer. Ensure that the domain name is available for registration.
\* \*\*Register the Domain:\*\* Once you've decided on a domain name, you'll need to register it with a domain registrar. Numerous domain registrars are available online to purchase and manage domain names. Popular registrars include GoDaddy, Namecheap, and Cloudflare Domains. (For documentation purposes, we have selected Cloudflare)
\* \*\*Select an Email Hosting Provider:\*\* After registering your domain name, you'll need to choose an email hosting provider. Several options are available, including Google Workspace (formerly G Suite), Microsoft 365, Zoho Mail, Cloudflare, etc. \\
 \\
 \*\*Pro Tip:\*\* \*\*When selecting a provider, consider factors such as pricing, features, and ease of use.\*\*<br>
\* \*\*Sign Up for Email Hosting:\*\* Once you've chosen an email hosting provider, sign up for an account. You'll typically need to provide your domain name during the signup process. Follow the provider's instructions to set up your account and configure your email settings.

<figure><img src="/files/iBInheOupotNAWJmUMUS" alt=""><figcaption></figcaption></figure>

\* \*\*Access Workspace Settings:\*\* Log in to AgencyHandy and navigate the workspace settings section.&#x20;
\* \*\*Navigate to Email Settings:\*\* Look for the option related to Email Configuration or Email Settings named "Email Setup" within the workspace settings menu.&#x20;

<figure><img src="/files/4g17lPkdXcUYW8wYYHc9" alt=""><figcaption></figcaption></figure>

\* \*\*Set Sender Name & Email:\*\* Enter the desired sender name in the provided field. The name should accurately represent the agency or sender's identity. Enter the sender's custom email address. Ensure the address is valid and associated with the agency or sender domain. Click the Save button.

<figure><img src="/files/rPnDPXUMdhZmxt5sYMuh" alt=""><figcaption><p>Type Sender name &#x26; email and clcik Save</p></figcaption></figure>

\* \*\*Verify Email:\*\* A verification link will be sent to your custom domain email. Click it to verify.

<figure><img src="/files/XNUUmcHnmEMEij6JQZwk" alt=""><figcaption><p>Click Okay to continue process</p></figcaption></figure>

<figure><img src="/files/6XNGYvX9wUxDdwZsAHaI" alt=""><figcaption><p>Click the link to verify</p></figcaption></figure>

<figure><img src="/files/hfG7QtCFgfpIDfohqJnU" alt=""><figcaption></figcaption></figure>

\* \*\*Configure DNS Settings:\*\* To ensure that your custom email addresses work correctly, you'll need to configure your domain's Domain Name System (DNS) settings. This typically involves adding MX (Mail Exchange), DKIM (DomainKeys Identified Mail), and DMARC (Domain-based Message Authentication, Reporting & Conformance) records to your domain's DNS settings, which specify the mail servers responsible for receiving email for your domain. AgencyHandy will provide you with the necessary MX, DKIM, and DMARC records and instructions for configuring them. <br>
\* \*\*Email Status:\*\* Once the sender name and email are configured, save the changes to apply the settings. At first, the status will be "Pending."&#x20;

<figure><img src="/files/WeniNvFAKsJzouvxbn0E" alt=""><figcaption></figcaption></figure>

\* After the DKIM and DMARC records are successfully set and saved, a green tick will appear, indicating that the email has been successfully set up and is ready.

<figure><img src="/files/kk9rl29FkIzUDtXmIE3t" alt=""><figcaption></figcaption></figure>

Your Custom email is set and ready to go.

The DKIM (DomainKeys Identified Mail) & SPF (Sender Policy Framework) Setup feature in AgencyHandy allows agencies to generate and set up DKIM and SPF records for their workspace. These records help prevent email spoofing and enhance email deliverability by verifying the authenticity of the sender's domain.

## Setup DKIM & SPF

### Purpose:&#x20;

Setting up DKIM and SPF records is essential for the following reasons:

\* \*\*Email Security:\*\* DKIM and SPF records add an extra layer of security to email communications, reducing the risk of email spoofing and phishing attacks.
\* \*\*Improved Deliverability:\*\* Authenticating emails with DKIM and SPF records improves deliverability by helping service providers identify legitimate emails, reducing the likelihood of emails being marked as spam.
\* \*\*Brand Trust:\*\* By implementing DKIM and SPF, agencies can build trust with their clients by ensuring that emails from their domain are genuine and trustworthy.

### Pre-condition to Use the Feature:&#x20;

\* Users must have access to the domain's DNS settings to configure DKIM and SPF records.&#x20;

Here's how to set them up:

### DKIM (DomainKeys Identified Mail):

DKIM involves adding cryptographic signatures to your outgoing emails, allowing receiving servers to verify the authenticity of the messages.

\* \*\*Generate DKIM keys:\*\* Start by generating DKIM keys provided by AgencyHadny. These keys typically consist of a public key and a private key pair. \\
 \\
 \*\*Steps to Use:\*\*\\
 \\
 \*\*Workspace Config => Emails => DKIM & SPF Setup => Generate DKIM and SPF records.\*\*
\* \*\*Log In:\*\* Log in to your Cloudflare account and navigate to the DNS settings for your domain.&#x20;
\* \*\*Add SPF Records:\*\* Add a new TXT record with the following values: \\
 \\
 \\- \*\*Type\*\*: Write down the type as \*\*TXT\*\*\\
 \\
 \\- \*\*Record Name/Name:\*\* Copy the name from your SPF Records.\\
 \\
 \\- \*\*Value/ Content:\*\* Copy the value & Paste it to the DNS.\\
 \\
 \\- \*\*TTL (Time To Live):\*\* Set as your provider recommends (2 min)

<figure><img src="/files/hzT9KMsAdmuZO7jIlYNC" alt=""><figcaption><p>Setup SPF Records</p></figcaption></figure>

\* \*\*Add DKIM records:\*\* AgencyHandy provides 3 DKIM Records. To add them to DNS, follow this step:\\
 \\
 \\- \*\*Type\*\*: Write down the type as \*\*CNAME\*\*\\
 \\
 \\- \*\*Record Name/Name:\*\* Copy the name from your SPF Records & paste it.\\
 \\
 \\- \*\*Value/ Content:\*\* Copy the value & Paste it to the DNS.\\
 \\
 \\- \*\*Proxy Status:\*\* Keep it off.\\
 \\
 \\- \*\*TTL (Time To Live):\*\* Set as your provider recommends (2 min)

<figure><img src="/files/VnhvAspKwzKB0L4hSugW" alt=""><figcaption><p>Setup CNAME Records</p></figcaption></figure>

\* \*\*Verify DKIM configuration:\*\* Once DKIM records are added, verify the configuration using tools like DKIMValidator (<https://dmarcian.com/dkim-validator/>) or MXToolbox (<https://mxtoolbox.com/DKIM.aspx>). These tools confirm if your DKIM records are correctly set up for email authentication.&#x20;

### Important Notes:

\* You need to create a custom email first. You can create it from inside your custom domain => email section
\* Your custom domain will be associated with the email.
\* The DKIM & SPF takes time (2 min - 2 hour). Make sure to refresh the page from time to time.

---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the \`ask\` query parameter:

\`\`\`
GET https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-emails/setup-email-address.md?ask=<question>
\`\`\`

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.