# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain.md).

The **Custom Domain** feature in Agency Handy allows users to link their own domain (e.g., `client.yourbusiness.com`) to their workspace. This enables businesses to create a professional, branded experience and make the platform easily accessible to clients and internal users.

#### 

Goals

- Reinforce agency branding through a unique web address.
 
- Enhance professional credibility with a custom domain.
 
- Simplify client and team access using a familiar domain.
 

#### 

Pre-conditions

**Permissions Required:** Only **Super Admins** and **Admins** can configure a custom domain.

**Domain Control:** You must own the domain and have access to modify its DNS settings.

---

#### 

Table of Contents

1. [Accessing the Custom Domain Panel](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain#id-1.-accessing-the-custom-domain-panel)
 
2. [Adding a Custom Domain](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain#id-2.-adding-a-custom-domain)
 
3. [Configuring DNS Settings](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain#id-3.-configuring-dns-settings)
 
4. [Verifying and Saving Domain](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain#id-4.-verifying-and-saving-domain)
 
5. [Monitoring Connection Status](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain#id-5.-monitoring-connection-status)
 
6. [Deleting or Updating Domain](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain#id-6.-deleting-or-updating-domain)
 
7. [Important Notes](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain#important-notes)
 

---

### 

1\. Accessing the Custom Domain Panel

1. Log in to your **Agency Handy** account.
 
2. Navigate to **Workspace Settings**.
 
3. Click on **Custom Domain**.
 

📌 _Only users with administrative access will see this option._

---

### 

2\. Adding a Custom Domain

1. Click on the **\+ Add Custom Domain** button.
 
2. Enter your desired subdomain (e.g., `client.yourbusiness.com`).
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FP2y2U6fn3Zcn2Ks2FATI%252FScreenshot_26.png%3Falt%3Dmedia%26token%3Dcab0d3bf-facc-40ad-abbf-0c25a3dec664&width=768&dpr=3&quality=100&sign=342db5f2&sv=2)
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FmFUBYvTDykcyut9jsi70%252FScreenshot_56.png%3Falt%3Dmedia%26token%3D95ea4b12-3769-49f9-bf51-0a06ffca9a9c&width=768&dpr=3&quality=100&sign=f035aa12&sv=2)
 

⚠️ _Do not use_ `_www_` _as your subdomain. It may cause configuration issues._

---

### 

3\. Configuring DNS Settings

1. Copy the **Type, Name, and Value** provided on the screen.
 
2. Log in to your domain registrar (e.g., GoDaddy, Namecheap, Cloudflare).
 
3. Add a **CNAME record** as instructed.
 
4. If using **Cloudflare**, make sure **Proxy Status** is set to **DNS only** (not proxied).
 

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252F7a8knFtoFhcn1rOhKUhC%252FScreenshot_57.png%3Falt%3Dmedia%26token%3D0bfc1281-bba7-43e6-ae2e-844da9401916&width=768&dpr=3&quality=100&sign=e8feb659&sv=2)

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FiNOi1eA7EZ0Ay7TxgiS7%252FScreenshot_31.png%3Falt%3Dmedia%26token%3Dd73d7a5b-b20b-49bf-bc25-4e2bb884408c&width=768&dpr=3&quality=100&sign=ab67c9b5&sv=2)

Cloudflare DNS Setup

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FPAGAd6Y4cog8oougzBfk%252FScreenshot_30.png%3Falt%3Dmedia%26token%3Deafdeb3e-12e7-4c36-a612-1690bb532c9a&width=768&dpr=3&quality=100&sign=7cb03abe&sv=2)

Add record and save

💡 _Use a DNS propagation tool like_ [_dnschecker.org_](https://dnschecker.org) _to track status._

---

### 

4\. Verifying and Saving Domain

1. After setting up DNS, return to Agency Handy.
 
2. Click **Save Domain**.
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FYAq26HlRB09xALCRFJrW%252FScreenshot_41.png%3Falt%3Dmedia%26token%3D2fb1ec7b-9d42-436f-b871-857aec88bbd1&width=768&dpr=3&quality=100&sign=b3e71086&sv=2)
 
 Save the Custom Domain
 
3. Status will initially show **Disconnected**. Wait 2 minutes to 48 hours.
 
4. Click **Refresh** to check the status.
 

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FuYTunB03J7xvp2AfZUyQ%252FScreenshot_32.png%3Falt%3Dmedia%26token%3D90a87ed7-8ce8-4b45-b0b1-a6958572db86&width=768&dpr=3&quality=100&sign=d7a631e6&sv=2)

Domain Successfully connected

✅ _Once verified, the status will change to_ _**Connected**__._

---

### 

5\. Monitoring Connection Status

- Use tools like [dnschecker.org](https://dnschecker.org) to ensure your domain has fully propagated.
 
- Look for green check marks in all regions for your CNAME record.
 
- DNS changes may take time depending on your registrar and location.
 

---

### 

6\. Deleting or Updating Domain

- To delete your custom domain:
 
 - Click the **Delete** button next to the domain entry.
 
 - Confirm the deletion.
 
 
- The workspace will revert to the default Agency Handy URL.
 
- You may re-add the domain at any time using the same steps.
 

⚠️ _Deleted domains can be added again with proper DNS settings._

---

### 

📝 Important Notes

- **Custom Domain Purpose:** Helps establish a professional and branded web presence for client access.
 
- **Subdomain Rule:** Always use a valid subdomain (e.g., `portal.agencyname.com`) and avoid using `www`.
 
- **DNS Records:** Must add the exact records provided. Incorrect or missing records will prevent connection.
 
- **Cloudflare Users:** Must disable proxy (set to DNS only) for successful verification.
 
- **Verification Time:** Can vary from a few minutes to 48 hours due to DNS propagation delays.
 
- **Admin Access Only:** Configuration rights are limited to Super Admins and Admins.
 
- **No Immediate Connection?** Use DNS tools to troubleshoot and verify record propagation.
 

### 

List of hosting sites with Agency Handy:

- [**Cloudflare**](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain/agencyhandy-hosting-with-cloudflare)
 
- Namecheap
 

[VorherigeSet Up Appearance](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-appearance) [NächsteAgencyHandy Hosting with Cloudflare](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-custom-domain/agencyhandy-hosting-with-cloudflare)

Zuletzt aktualisiert vor 11 Monaten