# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/services/service-purchase-redirection

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/services/service-purchase-redirection.md).

Service Purchase Redirection allows you to control what happens **after a client purchases a service or completes an intake form**. Instead of leaving users on a static confirmation screen, you can redirect them to an internal page, an external link, or show a custom modal message.

This feature helps you manage user journey flow, move clients to dashboards or lists, provide instructions after purchase, or show a success/failure message based on the outcome. All settings apply **globally for all services** and can be configured inside **Service → Settings → Redirections**.

---

#### 

**What You Can Do**

With Service Redirection you can:

• Redirect clients after successful purchase **before or without intake** • Redirect clients after **post-intake** form submission • Redirect clients **when purchase fails** (payment error, deleted service, coupon error etc.) • Choose redirection modes:  – Custom Modal (default templates provided, HTML editable)  – Internal Page (Dashboard, Orders, Tasks, Invoices, Proposals etc.)  – External Page (any website link) • Enable **Open in New Tab** toggle for pages and links • Edit system modal templates using **HTML Code Editor** • Preview modals before saving • Save configuration changes manually with a **Save/Update button** • Get warning prompts for **Unsaved changes**, **external links**, and **restricted internal pages**

---

#### 

**Why It Matters**

This feature ensures clients don’t get lost after checkout. It helps you provide clarity with post-purchase instructions, onboarding steps, or confirmation messaging. You can route clients to internal workflow pages or trigger guided next actions instead of leaving them idle.

Ideal for: ✔ Smooth onboarding after purchase ✔ Guiding clients to dashboards or task lists ✔ Showing invoice/subscription/payment confirmation ✔ Displaying payment failure notices ✔ Directing users to external funnels or thank-you pages

---

#### 

**Access Location**

You can find Redirection settings under:

**Services → Settings (⚙️ top right) → Redirections tab**

---

#### 

**Getting Started**

1. From the left sidebar click **Services**.
 
2. Click the **Settings (⚙️)** icon at the top-right corner of the page.
 
3. Select the **Redirections** tab.
 
4. You will now see **three redirection configuration areas**:  • For services with pre-intake/no intake  • For services with post-intake form  • For failed purchase scenarios
 
5. Select your preferred redirection method and fill in required fields.
 
6. Click **Update/Save** to apply changes.
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252F70tdhBuXFZQgGgm5dl05%252FScreenshot_38.png%3Falt%3Dmedia%26token%3Dae578a37-6f9a-44d3-ac39-d268dc1a37fe&width=768&dpr=3&quality=100&sign=aa437612&sv=2)
 

---

#### 

**Redirection Type Options**

**1\. External Page**

Use this to redirect clients to any website after purchase or intake completion.

How to configure: • Choose **External Page** from the dropdown • Enter a valid URL (http:// or https://) • Enable **Open Link in New Tab** if needed • System shows a warning before redirecting externally

Recommended for: – Thank-You pages – Funnels or onboarding pages – Knowledge base links – External invoice pages

---

**2\. Internal Page**

Redirect clients to built-in pages inside Agency Handy.

Available destinations: • Dashboard • Service List • Order List • Task List • Invoice List • Proposal List • Subscription List

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FGOSFgJ0YioCJOnJYKRbU%252FScreenshot_32.png%3Falt%3Dmedia%26token%3D9683f1ef-e418-4eee-af81-2d3dff9ee9eb&width=768&dpr=3&quality=100&sign=a70a2bae&sv=2)

Behavior notes: • If selected internal page is not visible to a client due to role/sidebar restriction, system shows a warning • Admin must confirm continuation or change the option • Can open in a new tab if enabled

Good use cases: – Send clients to Dashboard after payment – Push them to tasks after intake – Redirect to Order List to track progress

---

1. **For Failed Purchase – External Page**
 

Redirect clients to an outside website when their payment fails.

Usage: Admins can enter any valid URL (http:// or https://) where the client will be redirected after a failed checkout attempt.

Behavior notes: • A warning is displayed before redirecting users to an external site • "Open link in new tab" toggle available • Useful when routing users to: – A payment help page – A support/FAQ article – An external retry payment link – A custom failure landing page on your website

---

### 

**Custom Modal**

Show a popup with a message immediately after purchase or intake completion.

Available modal templates: • Purchase Success • Purchase Success (Post-Intake) • Purchase Failed

Modal Editor Details: • Uses **HTML Code Editor** • You can modify text, design, styles • Preview available on the right side • Reset to default anytime • Save changes using **Update** button

Use cases: – Show "Payment Successful" with next steps – Show "Thank you for submitting intake" – Display failure message with retry instructions

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252Fr89IFRGyURGx0H3ORQnb%252FScreenshot_39.png%3Falt%3Dmedia%26token%3Dfe7ae3e0-263c-4689-8f07-d31621ecec4e&width=768&dpr=3&quality=100&sign=ba587795&sv=2)

---

#### 

**Redirection Logic**

1. **Pre-Intake or No Intake**  Trigger occurs right after purchase.
 
2. **Post-Intake**  Trigger occurs only after client completes intake form.
 
3. **Failed Purchase**  Used when payment decline or system error occurs:  • Service deleted  • Coupon invalid  • Addon removed  • Package deleted  • API/server failure
 

Each case can have its own redirection configuration.

---

#### 

**Custom Modal Editing Workflow**

1. Go to **Services → Settings → Redirections**
 
2. Scroll to **Custom Modals**
 
3. Click on a modal name to open the editor
 
4. Edit HTML text on the left panel
 
5. Click **Run** to preview
 
6. Click **Update** to save
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FI4OLq2Hj2YkjfHzlLs8D%252FScreenshot_34.png%3Falt%3Dmedia%26token%3Dda941a8c-7930-465b-a6ea-b3e88b024e7a&width=768&dpr=3&quality=100&sign=602dbd12&sv=2)
 

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FcWk2LrDGcmd3Lx7qoJB8%252FScreenshot_40.png%3Falt%3Dmedia%26token%3D046a972b-08a6-4f14-bd25-35d417cd12c5&width=768&dpr=3&quality=100&sign=451d1fc2&sv=2)

![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FpMiWCbZOiaCSwFBPdl99%252FScreenshot_41.png%3Falt%3Dmedia%26token%3D1b29cfb3-8625-4460-825a-b30f93ef42e8&width=768&dpr=3&quality=100&sign=78e9aa6d&sv=2)

If you exit without saving, the system shows an **Unsaved Changes Warning**.

---

#### 

**Important Notes**

• Redirection applies globally for all services (no individual service rules yet). • Only system-provided modal templates exist for now. • External links display a caution alert before redirecting users. • Unsaved edits will trigger a warning when navigating away. • Some internal pages may be disabled if clients don't have access — tooltip will show reason. • Public purchase flows allow secure internal redirection without login interruption.

[VorherigeService Edit Layout](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/services/service-edit-layout) [NächsteCRM](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/crm)

Zuletzt aktualisiert vor 5 Monaten