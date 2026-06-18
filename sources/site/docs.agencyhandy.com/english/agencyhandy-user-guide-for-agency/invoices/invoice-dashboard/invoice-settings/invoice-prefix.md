# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/invoices/invoice-dashboard/invoice-settings/invoice-prefix

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/invoices/invoice-dashboard/invoice-settings/invoice-prefix.md).

The **Invoice Prefix** feature allows agencies to personalize invoice numbering by adding a **static prefix** (e.g., `INV-`, `Agency-`) and choosing a **format** that includes a sequential number (`{{n}}`) and optional date variables (`{{dd}}`, `{{mm}}`, `{{yyyy}}`). This helps businesses maintain **organized, professional, and easily trackable invoices**.

---

### 

**What**

- Customize invoice numbers with a **static prefix** and **predefined formats**.
 
- Sequential invoice numbering with **auto-incrementing counter (**`**{{n}}**`**)**.
 
- Include optional **date variables (**`**{{dd}}**`**,** `**{{mm}}**`**,** `**{{yyyy}}**`**)** for organization.
 
- Live preview feature to see invoice format before applying.
 
- Automatically reset or resume invoice numbers when changing prefixes.
 
- Display formatted invoice numbers in **list views, details pages, and PDFs**.
 

---

### 

**Purpose**

✅ **Easy Tracking** – Keep invoices organized with structured numbering. ✅ **Branding** – Personalize invoices with company name or initials. ✅ **Professionalism** – Maintain a clean, standardized invoice format. ✅ **Automation** – Reduce manual work with automatic numbering.

---

### 

**Pre-conditions**

1. **User Role**: Only **Superadmins and Admins** can configure invoice prefixes.
 
2. **Default Format**: If no custom configuration is set, the system applies:
 
 - **Prefix**: `INV-`
 
 - **Format**: `{{n}}-{{dd}}-{{mm}}-{{yyyy}}`
 
 
3. **Mandatory Variables**: The format must contain `**{{n}}**` (counter).
 
4. **Date Variables Reflect Invoice Date**:
 
 - If manually updated, the **selected invoice date** replaces `{{dd}}-{{mm}}-{{yyyy}}`.
 
 

---

### 

**Steps to Use (Detailed Guide)**

#### 

**1\. Configuring an Invoice Prefix**

**Step 1: Access Invoice Settings**

1. Log in to _Agency Handy_ as **Superadmin/Admin**.
 
2. Navigate to **Settings** → **Invoice Settings**.
 
3. Click **Edit Invoice Prefix**.
 

**Step 2: Add a Prefix**

1. Type a **prefix** (e.g., `INV-`, `Company-`, `Agency-2025`).
 
2. The **prefix supports**:
 
 - Letters
 
 - Numbers
 
 - Spaces
 
 - Special characters
 
 
3. **Examples of Valid Prefixes:**
 
 - `INV-`
 
 - `Company-`
 
 - `Agency 2025-`
 
 

**Step 3: Choose an Invoice Format**

1. Pick a format using the following options:
 
 - `{{n}}` → Auto-incrementing number.
 
 - `{{dd}}` → Invoice day.
 
 - `{{mm}}` → Invoice month.
 
 - `{{yyyy}}` → Invoice year.
 
 
2. **Examples of Predefined Formats:**
 
 - ✅ `{{n}}/{{dd}}/{{mm}}/{{yyyy}}` → _1/23/01/2025_
 
 - ✅ `{{n}}/{{mm}}/{{yyyy}}` → _1/01/2025_
 
 - ✅ `{{n}}/{{yyyy}}` → _1/2025_
 
 - ✅ **Default Format:** `{{n}}-{{dd}}-{{mm}}-{{yyyy}}`
 
 

**Step 4: Preview the Invoice Format**

1. The system **live-previews** how the invoice number will look based on the selected prefix and format.
 
 - **Example:**
 
 - **Prefix**: `Agency-`
 
 - **Format**: `{{n}}/{{dd}}/{{mm}}/{{yyyy}}`
 
 - **Live Preview**: `Agency-1/23/01/2025`
 
 
 

**Step 5: Save the Configuration**

1. Click **Save Changes**.
 
2. The new invoice prefix will apply to all future invoices.
 

---

#### 

**2\. How Invoice Numbers Are Generated**

✅ **Dynamic Replacements in Invoice Numbering:**

- `{{n}}` → Auto-incrementing invoice number.
 
- `{{dd}}` → Invoice creation day.
 
- `{{mm}}` → Invoice creation month.
 
- `{{yyyy}}` → Invoice creation year.
 

✅ **Invoice Number Examples:**

**Prefix**

**Format**

**Generated Invoice**

`INV-`

`{{n}}/{{yyyy}}`

`INV-1/2025`

`Company-`

`{{n}}-{{dd}}-{{mm}}-{{yyyy}}`

`Company-1-23-01-2025`

`Bill-`

`{{n}}/{{mm}}/{{yyyy}}`

`Bill-1/01/2025`

---

#### 

**3\. Number Resetting Rules**

✅ **Counter Reset:**

- If a **new prefix** is entered, the **counter resets to 1**.
 
- **Example:**
 
 - **Prefix**: `Agency-`
 
 - **Invoice Numbers**: `Agency-1`, `Agency-2`
 
 - **Change Prefix to**: `Bill-`
 
 - **New Invoice**: `Bill-1`
 
 

✅ **Counter Resumes for Previously Used Prefixes:**

- If a previously used **prefix** is restored, the counter **resumes from the last value**.
 
- **Example:**
 
 - **Prefix**: `Agency-`
 
 - **Invoice Numbers**: `Agency-1`, `Agency-2`
 
 - **Changed to**: `A-` (**Counter resets to 1**)
 
 - **Changed back to**: `Agency-`
 
 - **Next Invoice**: `Agency-3`
 
 

✅ **Changing Format Without Changing Prefix:**

- If only the **format is updated**, the counter **does NOT reset**.
 
- **Example:**
 
 - **Current Format**: `{{n}}-{{yyyy}}` → _INV-1-2025_
 
 - **Updated Format**: `{{n}}/{{dd}}/{{mm}}/{{yyyy}}`
 
 - **Next Invoice**: `INV-2/23/01/2025`
 
 

---

#### 

**4\. Where Invoice Prefixes Appear**

The full invoice number (**prefix + format**) appears in:

✅ **Invoice List View** ✅ **Invoice Details Page** ✅ **Client-Facing Invoice PDFs & Emails**

---

### 

**Important Notes**

✅ The **prefix field** does NOT accept variables (e.g., `{{n}}`) – only static text is allowed. ✅ `{{n}}` **must be included** in the format. ✅ The **invoice date variables (**`**{{dd}}**`**,** `**{{mm}}**`**,** `**{{yyyy}}**`**) are based on the invoice creation date**. ✅ The **counter resets when the prefix changes** but **resumes if the prefix is restored**. ✅ If a **wrong variable** is entered, an error message **"Invalid variable"** will appear. ✅ **No character limit** for the invoice prefix. ✅ The **prefix is set when the invoice is created**, even if the invoice is in **Draft mode**.

[VorherigeInvoice Settings](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/invoices/invoice-dashboard/invoice-settings) [NächsteCreate an Invoice](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/invoices/invoice-dashboard/create-an-invoice)

Zuletzt aktualisiert vor 1 Jahr