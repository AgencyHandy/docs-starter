# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-emails/setup-smtp

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-emails/setup-smtp.md).

The SMTP (Simple Mail Transfer Protocol) setup in Agency Handy allows you to send emails from your own verified email server instead of the system default. This ensures professional branding, improves deliverability, and gives you more control over your outbound email communications.

### 

What You Can Do

- Connect your workspace with your own SMTP server (e.g., Gmail, Outlook, custom domain)
 
- Send invoices, notifications, and proposals using your verified email
 
- Test your SMTP connection to confirm proper setup
 
- Switch between Custom Domain Email and SMTP Email Provider
 

### 

Why It Matters

- Strengthens brand identity by sending emails from your own domain
 
- Improves trust and deliverability (avoiding “noreply@agencyhandy.com”)
 
- Offers flexibility to use your preferred email infrastructure
 

### 

Who Can Use This

- **SuperAdmins** and **Admins** with Workspace Config permissions
 

---

### 

Getting Started

#### 

1\. Navigate to Email Setup

- Go to **Workspace Config → Email Setup**
 
- Click **SMTP Server**
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FAL8EMMZV5NYmjZyE18eU%252FScreenshot_149.png%3Falt%3Dmedia%26token%3D8c789ae2-c6f5-4c7e-9338-eaa71e01f39f&width=768&dpr=3&quality=100&sign=5aeac5c8&sv=2)
 

#### 

2\. Switch to SMTP Provider

- If you are already using **Custom Email**, a confirmation popup appears:
 
 - Click **Switch to SMTP** to continue
 
 - This will disable existing custom email settings
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FWle4gFhkf1CBQheiLvS1%252FScreenshot_150.png%3Falt%3Dmedia%26token%3D102ce6ee-ab6c-4233-9871-3925ef819be6&width=768&dpr=3&quality=100&sign=c4e500a4&sv=2)
 
 

#### 

3\. Configure SMTP Details

Fill in the required fields:

- **Host Name** (e.g., smtp.gmail.com)
 
- **User Name** (your full email address)
 
- **Password** (app password or SMTP password)
 
- **Port** (e.g., 465 for SSL, 587 for TLS)
 
- **Auto TLS** (optional toggle for security) Click **Save** to store settings.
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FIggA9faohsZ1IcInGtsB%252FScreenshot_151.png%3Falt%3Dmedia%26token%3De19ab50d-4812-48ce-8500-7840fd7339e7&width=768&dpr=3&quality=100&sign=fdbcac4b&sv=2)
 

#### 

4\. Generate the App Password:

Here’s a step-by-step guide:

1. Enable 2-Step Verification (if not already on):
 

- Go to your Google Account: [manage your Google Account](https://myaccount.google.com/security).
 
- Navigate to the "Security" tab on the left.
 
- Under "Signing in to Google," select 2-Step Verification and follow the prompts to turn it on (you'll need your phone).
 
- Once 2-Step Verification is active, go back to the Security section or directly to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
 
- You may need to sign in again.
 
- At the bottom, click Select app and choose the app (e.g., Mail, Other) or type a custom name for the device/app you're connecting.
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252F3PsA7p5sNO656mcKdUGJ%252FScreenshot_106.png%3Falt%3Dmedia%26token%3D6b7c988f-95d7-4cb5-a7e9-dbdf1d2e585f&width=768&dpr=3&quality=100&sign=ce30b0fc&sv=2)
 
- Click Select device, choose your device (or type a custom name).
 
- Click Create. A 16 digit password will be created
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252F43XNbsRgzSGwEyeIT5tt%252FScreenshot_107.png%3Falt%3Dmedia%26token%3D402e7e76-4115-4eea-929a-b38a4b4d9504&width=768&dpr=3&quality=100&sign=28a04fd2&sv=2)
 
- Copy the password & paste it in the SMTP settings in Agency Handy.
 

#### 

5\. Confirm Setup

- A success message confirms: _“SMTP is created successfully.”_
 
- Saved SMTP details (host, username, port) will be displayed
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252F2kIahOUbtrlnCmnIkg4i%252FScreenshot_152.png%3Falt%3Dmedia%26token%3D7db46f40-cdd9-4e10-9ed8-b9434a327f13&width=768&dpr=3&quality=100&sign=7a02c475&sv=2)
 

#### 

6\. Test SMTP Connection

- Click **Test** and enter a receiver email address
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252Fiv95k7YezCTVfE2xn8mc%252FScreenshot_154.png%3Falt%3Dmedia%26token%3Df3b5dcac-9d26-493f-8f8c-dac3cd192e78&width=768&dpr=3&quality=100&sign=163b79d6&sv=2)
 
- Agency Handy sends a test email
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252F9p2pcM3vbRPYuWUSR7od%252FScreenshot_155.png%3Falt%3Dmedia%26token%3Dfe654240-6407-460a-822f-2fcb45f62373&width=768&dpr=3&quality=100&sign=1a91bdf1&sv=2)
 
- Check your inbox for the confirmation message: _“This is a confirmation that your email setup in Agency Handy is working properly.”_
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FShmNUK4Ufu4WTO3dmuxf%252FScreenshot_153.png%3Falt%3Dmedia%26token%3D05233dd1-3693-498b-8ebb-acff65d529c5&width=768&dpr=3&quality=100&sign=b44a4130&sv=2)
 

---

### 

Important Notes

- Use an **App Password** (not your regular login password) if your provider requires it (e.g., Gmail with 2FA).
 
- Only one SMTP setup can be active per workspace.
 
- Emails will no longer use noreply@agencyhandy.com once SMTP is configured.
 
- Incorrect details (host, port, credentials) will block outgoing emails.
 
- Switch between **Custom Domain Email** and **SMTP Email Provider** anytime, but only one can be active.
 
- When switching to a custom email, you have to set the email again.
 

[VorherigeSending a Test Email](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/set-up-emails/sending-a-test-email) [NächsteTax Rates](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/tax-rates)

Zuletzt aktualisiert vor 4 Monaten