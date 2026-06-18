# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain/agencyhandy-hosting-with-cloudflare

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain/agencyhandy-hosting-with-cloudflare.md).

AgencyHandy allows users to host their platform with Cloudflare, leveraging its global network to improve performance, security, and reliability. Cloudflare enhances page load speeds, protects against cyber threats, and ensures consistent uptime. Hosting AgencyHandy with Cloudflare involves integrating your domain with Cloudflare’s content delivery network (CDN) and security services to optimize performance and safeguard operations.

### 

**Purpose:**

- **Enhanced Performance:** Cloudflare’s CDN reduces latency and improves page load times by caching and delivering content from servers closest to users.
 
- **Increased Security:** Protects against DDoS attacks, malicious bots, and other cyber threats.
 
- **Improved Reliability:** Ensures high uptime and consistent platform availability.
 

### 

**Pre-conditions:**

- An active AgencyHandy subscription.
 
- A Cloudflare account.
 
- Permission to manage DNS settings for your domain.
 

### 

**Steps to Use (Detailed):**

1. **Sign Up for Cloudflare:**
 
 - Visit the [Cloudflare website](https://www.cloudflare.com) and create an account if you don’t have one.
 
 
2. **Add Your Domain to Cloudflare:**
 
 - After signing up, enter your domain name in the Cloudflare dashboard.
 
 - Follow the prompts to scan your domain’s DNS records.
 
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252F00TQlCqSr48y9GC6dVLF%252FScreenshot_48.png%3Falt%3Dmedia%26token%3Dfefc9743-c384-46ac-8daa-2ca08acd8bc6&width=768&dpr=3&quality=100&sign=980c7358&sv=2)
 
3. **Update DNS Settings:**
 
 - Cloudflare will provide new nameservers.
 
 - Log in to your domain registrar’s account and replace your current nameservers with the ones provided by Cloudflare.
 
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252F90TxDhcxOxpmqjPsxbbT%252FScreenshot_31.png%3Falt%3Dmedia%26token%3D8926cfa8-c669-4c16-8e6a-1ba4aeba88a2&width=768&dpr=3&quality=100&sign=c9b642d3&sv=2)
 
4. **Manage DNS Records:**
 
 - In the Cloudflare dashboard, navigate to **DNS Settings**.
 
 - Click the **\+ Add Record** button and input the following:
 
 - **Type:** Select the DNS record type (e.g., CNAME or A Record).
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FpLOTNLH7m1CCUULToMVA%252FScreenshot_43.png%3Falt%3Dmedia%26token%3D59a0326a-bc34-4d2d-bc72-c7f07de0aa5f&width=768&dpr=3&quality=100&sign=bb75904&sv=2)
 
 Click the Down arrow and choose CNAME
 
 - **Name:** Enter the subdomain or root domain (e.g., www).
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FbolWmYQnz6ndp8WrtzoK%252FScreenshot_44.png%3Falt%3Dmedia%26token%3D8703f19c-53f4-46a4-acae-e6896365021f&width=768&dpr=3&quality=100&sign=414b0bab&sv=2)
 
 Write down the Name
 
 - **Content/Target:** Provide the target information, such as the platform’s server address.
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FROIacAXShlOZfrmb9Kj9%252FScreenshot_45.png%3Falt%3Dmedia%26token%3D0814cd20-6440-4839-a9c2-396e037637a0&width=768&dpr=3&quality=100&sign=edec2bcf&sv=2)
 
 Copy & paste the content/target
 
 - **TTL:** Set the desired Time-To-Live value for the record.
 
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FfA3tAupNBz0Tfp2SduF3%252FScreenshot_46.png%3Falt%3Dmedia%26token%3Dc2d33fdb-73bc-44df-87cc-8233195c3303&width=768&dpr=3&quality=100&sign=eae4b16b&sv=2)
 
 Set the TTL (Time To Live) to 2 min
 
 
5. **Disable Cloudflare Proxy:**
 
 - For relevant DNS records, ensure the orange cloud icon in the dashboard is **disabled**. This prevents proxying and ensures direct communication with AgencyHandy servers.
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252F2AxC2zTaC1GNz7I5LVnd%252FScreenshot_42.png%3Falt%3Dmedia%26token%3D601a8d6f-c206-4e95-be72-e8aae5416e58&width=768&dpr=3&quality=100&sign=64c73e3&sv=2)
 
 Click the Radio button to disable the proxy status
 
 
6. **Save Records:**
 
 - Double-check the DNS records for accuracy.
 
 - Click the **Save** button to finalize the DNS configuration.
 
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FZq5lAnDdS1E8D5vxZC3u%252FScreenshot_47.png%3Falt%3Dmedia%26token%3D1c430ed8-dfe0-4f35-b039-96907ce2d127&width=768&dpr=3&quality=100&sign=7ec64311&sv=2)
 
 Click Save button
 

---

### 

**Important Notes:**

- **DNS Propagation:** It may take up to 24 hours for DNS changes to propagate globally.
 
- **Verify Settings:** Use a DNS checker (e.g., [dnschecker.org](https://dnschecker.org)) to confirm the domain is correctly configured.
 
- **Disable Proxying:** Always ensure the orange cloud icon is disabled for relevant records to maintain proper communication with AgencyHandy.
 
- **Secure Access:** Enable additional Cloudflare security features such as SSL/TLS encryption for secure communication.
 

[VorherigeSet Up Custom Domain](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain) [NächsteAgency Handy Hosting with Namecheap](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain/agency-handy-hosting-with-namecheap)

Zuletzt aktualisiert vor 11 Monaten