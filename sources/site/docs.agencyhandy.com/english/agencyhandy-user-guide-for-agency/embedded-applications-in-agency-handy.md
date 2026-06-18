# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/embedded-applications-in-agency-handy

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/embedded-applications-in-agency-handy.md).

The **Embedded Application** feature allows Superadmins and Admins to integrate external tools (like Google Docs, Figma, Notion, YouTube, etc.) directly into the Agency Handy interface. These apps can be viewed and accessed without leaving the platform, improving workflow, collaboration, and access control.

---

### 

**What:**

Users can:

- Embed external apps (via iframe or link).
 
- Share apps with team members or clients.
 
- Control who sees what with precise visibility permissions.
 
- Customize sidebar access for quick launching.
 
- Edit or remove embedded apps anytime.
 

---

### 

**Purpose:**

✅ Eliminate switching between platforms. ✅ Enable real-time collaboration on external apps. ✅ Offer role-based access to tools like documents, schedules, designs, and dashboards. ✅ Centralize useful third-party tools for teams and clients inside Agency Handy.

---

### 

**Pre-conditions:**

- Only **Superadmins** and **Admins** can create, edit, or delete embedded apps.
 
- All users must have active roles (Admin, PM, Assignee, Client).
 
- The embed URL must be compatible with iframe or external linking.
 
- Icons for embedded apps should be in a supported format (SVG, PNG, JPG).
 
- Clients can only view shared apps from their sidebars (canvas view).
 
- Sidebar toggles are **user-specific** and personalized.
 

---

### 

**User Journey**

1. Superadmin/Admin adds an app → selects icon → chooses URL/iframe → sets visibility → enables sidebar toggle → Saves.
 
2. Other Admins and Team members see shared apps in grouped view with their own sidebar toggle.
 
3. Clients see only shared apps in their sidebar and access via click.
 

---

### 

**Steps to Use (Detailed Guide)**

**Step 1: Adding a New App**

1. **Navigate to Embedded Apps:**
 
 - From the main interface, locate and click on "Embedded Apps."
 
 
2. **Start Adding:**
 
 - Click the "Add New" button.
 
 
3. **Fill in the App Details:**
 
 - **Title:** Give your app a clear and descriptive name (e.g., "Project Dashboard," "Resource Library").
 
 - **Type:** Select how the app will be displayed:
 
 - **URL:** Opens the app in Agency Handy if the url is sharable and has proper permission.
 
 - **Iframe (Embedded View):** Displays the app directly within AgencyHandy.
 
 
 - **Content URL:** Paste the URL of the web tool you want to integrate.
 
 - **Google Drive Specific (if using Iframe):**
 
 - Ensure the Google Drive folder is set to "Anyone with the link can view."
 
 - Copy the folder link.
 
 - Convert the link to the correct format(sample):
 
 - **From:** `https://drive.google.com/drive/folders/1HAWU4YyOCOMC_NBT3cq-7FOozWITXo11?usp=sharing`
 
 - **To:** `https://drive.google.com/embeddedfolderview?id=1HAWU4YyOCOMC_NBT3cq-7FOozWITXo11`
 
 
 
 - **Youtube Specific (if using URL):**
 
 - Ensure the youtube URL is in the correct format.
 
 - **From:** `https://www.youtube.com/watch?v=iu9a5aJF5ik&ab_channel=FantasyTavern4you`
 
 - **To:** `https://www.youtube.com/embed/iu9a5aJF5ik`
 
 
 
 

**Step 2: Setting Visibility**

1. **Choose Who Can See the App:**
 
 - **Teams:**
 
 - Select "All Team Members" or choose specific members.
 
 - The member's role (e.g., PM, Assignee) is displayed next to their name.
 
 
 - **Clients:**
 
 - Select "All Clients" or choose specific clients.
 
 - Note: Client apps will only appear in the client's sidebar.
 
 
 

**Step 3: Personal Sidebar Toggle (Optional)**

1. **Pin to Your Sidebar:**
 
 - Toggle "Show in your sidebar" to add the app to your personal sidebar for quick access.
 
 - This setting is unique to your profile.
 
 

**Step 4: Saving the App**

1. **Finalize and Save:**
 
 - Click the "Save" button to add the embedded app.
 
 - The app will be organized under its corresponding category (e.g., all Google Docs in one tab).
 
 

---

### 

**App Views by User Role**

**👑 Superadmin/Admin**

- See all embedded apps (yours and others).
 
- Grouped by app type (e.g., Figma, Airtable).
 
- Click on app tab to:
 
 - View content.
 
 - Toggle "Show in Sidebar".
 
 - See who the app is shared with.
 
 - Edit or Delete via the 3-dot menu.
 
 

**🧑‍💼 Team Members (PMs, Assignees)**

- Only view apps shared with them.
 
- Toggle to show/hide from their sidebar.
 
- No edit/delete options.
 
- Click to view embedded app (read-only).
 

**👤 Clients**

- Only apps shared with them appear.
 
- Apps are visible from their **sidebar only**.
 
- Click to open app (canvas size defined by UX).
 
- No edit/delete/sidebar toggle options.
 

---

### 

**Filters & Sorting**

- **Search by Title**
 
- **Filter by Visibility**:
 
 - Shared with all team members
 
 - Shared with specific team members
 
 - Shared with all clients
 
 - Shared with specific clients
 
 
- **Sort Options**:
 
 - Sort by oldest created first (default)
 
 

---

### 

**Important Notes:**

✅ There is **no limit** to how many embedded apps can be added. ✅ Clients and team members can **only view**, not manage apps. ✅ Others can still access apps added by one Admin based on visibility. ✅ **Icons** appear only on the second view page and in the sidebar. ✅ **The canvas layout for clients** is being defined by UX. ✅ Invalid iframe or URL formats will show an error. ✅ Deleted apps are removed for all users instantly. ✅ Personalized **sidebar toggles** apply only to the user toggling it. ✅ **Audit Logs** track who added/edited/deleted apps and when.

---

[VorherigeSlack Integration](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/slack-integration) [NächsteCompany Accounts (B2B)](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/company-accounts-b2b)

Zuletzt aktualisiert vor 1 Jahr