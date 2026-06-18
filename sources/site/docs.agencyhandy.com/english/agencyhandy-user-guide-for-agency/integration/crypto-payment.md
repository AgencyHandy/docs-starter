# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/crypto-payment

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/crypto-payment.md).

Agency Handy’s Crypto Payment option lets you accept cryptocurrency from clients using simple wallet-based transfers. With customizable instructions, manual confirmation, and optional proof of payment, it’s ideal for agencies working with crypto-preferred clients.

### 

What You Can Do

- Enable Crypto Payment as a checkout option
 
- Add wallet details and network-specific instructions
 
- Choose whether to require proof of payment
 
- Accept Bitcoin, Ethereum, USDT, USDC, and more. (Right now, only USDC is acceptable.)
 
- Display instructions in email and invoice views
 
- Manually confirm payment before progressing the order
 
- Control visibility by workspace and service group
 

### 

Why It Matters

- Offer flexible, modern payment options
 
- Customize instructions for each wallet or currency
 
- Avoid missed payments with optional file uploads
 
- Keep invoices and orders aligned with payment verification
 
- Maintain control with manual confirmation flow
 

### 

Who Can Use This

To set up or manage crypto payments, users must:

- Have a Super Admin or Admin role
 
- Access Integrations and Workspace Settings
 
- Have permission to edit service payment options
 

---

### 

Getting Started

#### 

1\. Enable Crypto Payment

- Go to **Integrations**
 
- Click **Crypto Payment**
 
- A wallet setup screen opens with a rich text editor
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252Fwz1hY7fp6OCYd8aNfiQA%252FScreenshot_101.png%3Falt%3Dmedia%26token%3D59033b49-91a0-482d-bca7-88b279dc1de8&width=768&dpr=3&quality=100&sign=760d9477&sv=2)
 

#### 

2\. Enter Wallet Details

Admins can enter:

- **Cryptocurrency Type** (e.g., Bitcoin, Ethereum, USDT, USDC. Right now, only USDC is acceptable.)
 
- **Wallet Address**
 
- **Network Type** (e.g., ERC-20, TRC-20, BTC)
 
- **Additional Instructions** (e.g., memo, tag, support contact, minimum amount)
 
- **Require Proof of Payment** toggle
 
 - If enabled: Clients must upload a file
 
 - If disabled: Payment can proceed without proof
 
 
- Click **Save** to store the setup
 
- Crypto Payment can be edited or disconnected anytime
 
- Input is XSS and HTML sanitized for safety
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FTgfyRAC815gkfS9aaCyN%252FScreenshot_102.png%3Falt%3Dmedia%26token%3D141b68dd-7477-4fc7-a731-2ae094431dc2&width=768&dpr=3&quality=100&sign=57ffeb90&sv=2)
 

---

### 

Client Checkout Flow

#### 

When Clients Choose Crypto Payment

- The system creates:
 
 - **Order** with status: _Pending_
 
 - **Invoice** with status: _Open_
 
 
- Clients are shown wallet info and instructions
 
- A file upload button appears in the invoice (if proof is required)
 
- In the **Catalog**, clients can upload payment proof
 
 - If required and no file is uploaded → no order/invoice
 
 - If not required → order and invoice are created regardless
 
 

---

### 

Manual Confirmation

Admins must manually verify off-platform payment.

- Once confirmed, mark the **Invoice as Paid**
 
- If invoice is marked Paid and order is _Pending_ → order updates to _Ongoing_
 
- If order is already _Completed_ or _Canceled_ → no changes occur
 

---

### 

Email Notifications

#### 

After Order Creation

- Clients receive wallet transfer instructions via email
 
- Based on rich text editor content from crypto setup
 

---

### 

Proposal Integration

- If crypto is configured, “Pay with Crypto” will appear on accepted proposals
 
- Clients can pay in crypto from proposal invoice view
 

---

### 

Additional Notes

- Crypto Payment appears at checkout only if enabled in:
 
 - **Workspace Settings → Payment Methods**
 
 - **Service Grouping → Payment Availability**
 
 
- If disabled in Workspace Settings, crypto won’t appear—regardless of other settings
 
- **USDC** is now a supported currency
 
- If a service does not support USDC, crypto payment is hidden for that service
 
- File uploads are required only if “proof of payment” toggle is on
 
- Clients can view wallet details again from the invoice at any time
 

[VorherigeWise Payment Method](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/wise-payment-method) [NächsteWebhook Management](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/integration/webhook-management)

Zuletzt aktualisiert vor 9 Monaten