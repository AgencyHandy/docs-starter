# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/custom-script

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/custom-script.md).

The Custom Script feature allows Admins and SuperAdmins to embed external scripts into their Agency Handy workspace. Use this to add analytics (like Google Analytics), chat widgets, pixels, or any third-party tool—without engineering support.

### 

What You Can Do

- Add tracking scripts such as Google Analytics, Facebook Pixel
 
- Insert SEO or custom scripts in Header or Footer
 
- Target all pages
 
- Manage scripts from a centralized interface
 
- Edit or delete scripts at any time
 

### 

Why It Matters

- Enables self-service integration of analytics and tools
 
- Supports third-party features like live chat or behavioral tracking
 
- Reduces dependency on developers for small code insertions
 
- Gives agencies greater control over how their workspace functions
 

### 

Who Can Use This

To add or manage custom scripts, users must:

- Be a SuperAdmin or Admin
 
- Have access to Workspace Settings
 

### 

Getting Started

1. Open Script Settings
 

- Go to Workspace Config → Custom Script
 
- View the list of added scripts or click Add Script to start
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252F1TdtkVAatAsULDuBPzzo%252FScreenshot_139.png%3Falt%3Dmedia%26token%3D0938624d-847b-4d57-9057-e14857433da4&width=768&dpr=3&quality=100&sign=19b7ccaf&sv=2)
 

1. Add a New Script
 

Each script requires:

- Script Name (free text, required)
 
- Script Location (dropdown: Header or Footer)
 
- Target Page (dropdown: All Pages)
 
- Script Code (HTML/JS code in a text area)
 

1. Save and Apply
 

- Click Save to apply the script immediately
 
- It will load automatically based on the selected location and page
 
 ![](https://docs.agencyhandy.com/~gitbook/image?url=https%3A%2F%2F842362573-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FiedbxyF6rrnGBuHuFME1%252Fuploads%252FxKCOSN581Wp2INgjf2X5%252FScreenshot_141.png%3Falt%3Dmedia%26token%3D00fa715d-1400-4746-9602-e742cf7050d4&width=768&dpr=3&quality=100&sign=6f9630e&sv=2)
 

1. Edit or Delete
 

- Click the 3-dot icon at the right to edit a script
 
- To delete, click the 3-dot icon at the right and select the Delete button.
 
- All changes take effect immediately upon save
 

### 

Platform Behavior

- Scripts are injected directly into the Header or Footer during page load
 
- Target logic applies visibility to either all workspace pages or only Catalog
 
- No sanitization is applied—ensure correctness to avoid workspace issues
 

### 

Important Notes

- Scripts take effect immediately once saved. Always test thoroughly before applying to a live workspace.
 
- Improper or malformed code can break your workspace layout or functionality.
 
- There is no sanitization applied - Agency Handy assumes the inserted script is safe and valid.
 
- Scripts are injected into the workspace header or footer based on your selection.
 
- Target page options include: All Pages . More options coming soon.
 
- All users with SuperAdmin or Admin roles can add, edit, or delete scripts. Deleting a script removes it instantly from the frontend.
 
- Future improvements may include role-based restrictions, script prioritization, and rollback/versioning capabilities.
 
- Test Case Examples:
 
 - Adding a Google Analytics script should render it in the <head> of all pages.
 
 - Editing a script’s location from Header to Footer should relocate it accordingly.
 
 - Saving without required fields (e.g., Script Name) should trigger a validation error.
 
 - Deleting a script should ensure it no longer loads across the workspace.
 
 

[VorherigeEdit Sidebar name](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/sidebar-and-access/edit-sidebar-name) [NächsteCustom Field](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/workspace-config/custom-field)

Zuletzt aktualisiert vor 9 Monaten