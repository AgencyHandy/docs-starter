# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/create-a-new-lead-using-api

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/create-a-new-lead-using-api.md).

### 

Prerequisites

Review the steps in the [Getting Started](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/getting-started) guide before updating an order. It walks through configuring your API token, and selecting the correct `companyid`, which are all required for the instructions below.

### 

Step 1: Get Client Role ID

#### 

📍 Endpoint:

`{{URL}}/roles?type=company`

#### 

🛠️ Set Headers:

Kopieren

```
x-api-key: <API_KEY>
companyid: <COMPANY_ID>
```

#### 

📥 Response Example:

Kopieren

```
{
  "roles": [
    {
      "_id": "6525994184e9ddd798534535",
      "role": {
        "_id": "6525994184e9ddd79853451e",
        "responsibility": "",
        "name": "client"
      },
      "company": "6525994184e9ddd79853450e",
      "createdAt": "2023-10-10T18:34:41.567Z",
      "updatedAt": "2024-10-01T07:28:48.340Z",
      "__v": 0,
      "type": "company"
    }
  ]
}
```

#### 

📝 What to Do:

- Find the role where `roles[0].role.name === "client"`.
 
- Extract and store the **Client Role ID**:
 
 Kopieren
 
 ```
    const clientRoleId = "ROLE_ID_HERE"; // Replace with actual ID
    ```
 
- **Important:** Ensure you do **not** copy `_id` from `roles[0].role`, but from `roles[0]` itself.
 

### 

Step 2: Create a New Lead

#### 

📍 Endpoint:

`{{URL}}/members/bulk-lead`

#### 

🛠️ Set Headers:

Kopieren

```
x-api-key: <API_KEY>
companyid: <COMPANY_ID>
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
      "role": "ROLE_ID_HERE",
      "isConvertedClient": false,
      "status": "New",
      "contactNo": "1234567890",
      "source": "website",
      "positionInBoard": 1,
      "isConvertedClient": false
    }
  ]
```

#### 

✅ Success Response:

Kopieren

```
{
  "message": "Lead created successfully",
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

❗ Important Tips:

- Ensure `"isConvertedClient": false` is **set** in the request.
 
- Use the correct **Role ID** from Step 3.
 

[VorherigeUpdate an Order](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/update-an-order) [NächsteCreate a New Client](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/create-a-new-client)

Zuletzt aktualisiert vor 4 Tagen