# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/create-a-new-client

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/create-a-new-client.md).

### 

Prerequisites

Review the steps in the [Getting Started](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/getting-started) guide before updating an order. It walks through configuring your API token, and selecting the correct `companyid`, which are all required for the instructions below.

### 

Step 1: Create a New Client

#### 

📍 Endpoint:

`{{URL}}/members/bulk-client`

#### 

🛠️ Set Headers:

Kopieren

```
x-api-key: <API_KEY>
companyId: <COMPANY_ID>
```

#### 

📦 Request Body:

Kopieren

```
[
    {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com",
      "isConvertedClient": false,
      "status": "New",
      "contactNo": "1234567890",
      "source": "website",
      "positionInBoard": 1
    }
]
```

#### 

✅ Success Response:

Kopieren

```
{
  "message": "Lea created successfully",
  "createdMembers": [
    {
      "_id": "NEW_MEMBER_ID",
      "name": "John Doe",
      "status": "New",
      "role": "client"
    }
  ]
}
```

#### 

[Vorherige🚀 Create a New Lead Using API](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/create-a-new-lead-using-api) [NächsteTimesheet](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/timesheet)

Zuletzt aktualisiert vor 4 Tagen