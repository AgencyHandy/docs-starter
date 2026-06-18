# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/getting-started

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/getting-started.md).

### 

**Step 1: Generate an API Key**

1. Go to: `{{workspaceUrl}}/workspace-config?tab=api-keyGenerate`
 
2. Copy the **API key**.
 

### 

Step 2: Get Company Id

#### 

📍 Endpoint:

Kopieren

```
{{URL}}/accounts/companies
```

#### 

🛠️ Set Headers:

Kopieren

```
x-api-key: <API_KEY>
```

#### 

📥 Response Example:

Kopieren

```
{
  "message": "Companies associated with API token.",
  "companies": [
    {
      "_id": "6525994184e9ddd79853450e",
      "name": "onethread123",
      "logo": "",
      "extraSmallLogo": "",
      "largeLogo": ""
    }
  ]
}
```

#### 

📝 What to Do:

- Extract the **Company ID** from the response: `companies[0]._id`.
 
- Store the ID for later use:
 
 Kopieren
 
 ```
    const companyid = "COMPANY_ID_HERE"; // Replace with actual ID
    ```
 

[VorherigeAPI Integration Guide](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide) [NächsteUpdate an Order](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/update-an-order)

Zuletzt aktualisiert vor 1 Stunde