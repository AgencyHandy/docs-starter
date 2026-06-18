# Source: https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/update-an-order

For the complete documentation index, see [llms.txt](https://docs.agencyhandy.com/llms.txt). This page is also available as [Markdown](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/update-an-order.md).

### 

Prerequisites

Review the steps in the [Getting Started](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/getting-started) guide before updating an order. It walks through configuring your API token, and selecting the correct `companyid`, which are all required for the instructions below.

### 

Endpoint

- **Method:** `PUT`
 
- **Path:** `{{URL}}/orders`
 
- **Query string:** `pid=<projectId>` (required)
 
- **Content-Type:** `multipart/form-data` (use this even when no files are attached to satisfy the `multer` parser)
 

### 

Authorization & Headers

Header

Required

Description

`Authorization`

Yes

Bearer token for the signed-in member. Processed by the `authorization` middleware.

`companyid`

Yes

Mongo ObjectId of the company in which the order exists. Required by most services.

`clientid`

Optional

Real-time client socket id. If supplied, notification payloads include it.

### 

Query Parameters

Name

Type

Description

`pid`

string (ObjectId)

The order / project id that will be updated.

### 

Request Body Schema

Field

Type

Notes

`name`

string (min 2)

Updates the project title.

`deadline`

ISO date

Adjusts the internal due date.

`budget`

number ≥ 0

Total budget figure (matches original currency).

`quantity`

number ≥ 1

Number of units purchased for the package.

`currency`

string

`USD`, `CAD`, `EUR` etc.

`status`

enum

One of `Pending`, `Ongoing`, `Review`, `Completed`, `Cancelled`. Business rules listed below.

`kickoffDate`

ISO date

Project start date.

`notes`

string

Internal notes.

`brief`

string

Client brief / summary.

`assignedProjectManagers`

array

Complete list of project manager member ids. New ids are added to the team; removed ids are deleted from the team. Each id must belong to a `projectManager` role inside the same company.

`repeatCount`

number

Required only for subscription orders when changing recurrence settings.

`repeatDuration`

enum

One of `month`, `week`, `day`, `year`. Required alongside `repeatCount` for subscription orders.

`billingCycleCount`

number

Optional recurring billing limit. Defaults to `0` (no limit).

`billingCycleEvent`

enum

Either `createOrderWithTask` or `noChange`.

`markTasksAsDone`

boolean

**Required** when `status` is `Completed` or `Cancelled`. When `true`, all project tasks are marked done after the status change.

`rejectRequestedTasks`

boolean

Allowed only when `status` is `Completed` or `Cancelled`. When `true`, any client-requested tasks are rejected after the update.

#### 

File Uploads

Attach zero or more files under the `files` field. Every upload is appended to the order's system folder and its byte size is added to the folder's `sizeInBytes`. When files are provided the handler:

1. Uploads each attachment through the standard order upload pipeline.
 
2. Accumulates the uploaded file sizes and increments the folder size atomically.
 
3. Leaves previously uploaded order files untouched.
 

### 

Example JSON Payload

Use this structure when constructing the body (convert the fields to multipart form entries when including files):

Kopieren

```
{
  "name": "Website Redesign",
  "status": "Review",
  "budget": 12000,
  "currency": "USD",
  "quantity": 1,
  "assignedProjectManagers": ["{{PROJECT_MANAGER_ID}}"],
  "repeatCount": 3,
  "repeatDuration": "month",
  "billingCycleEvent": "createOrderWithTask",
  "notes": "Scope finalized with client.",
  "brief": "Launch-ready design refresh."
}
```

### 

Business Rules & Side Effects

- Caller must be an approved member of the `companyid` (`userProjectList` check). Unauthorized members receive `403 PermissionError`.
 
- Orders already marked `Cancelled` or `Completed` cannot be updated (`400 ValidationError`).
 
- Members signed in as `client` cannot cancel an order once it has moved out of `Pending` (`403 PermissionError`).
 
- Status transitions are restricted: `Review` can only follow `Ongoing` or another `Review`. Trying to jump from `Pending` → `Review` returns `400 ValidationError`.
 
- Changing status from `Pending` to any of `Ongoing`, `Review`, or `Completed` marks the project's folder as live (`isLive: true`).
 
- Setting `status` to `Completed` or `Cancelled` requires an explicit `markTasksAsDone` boolean. When `true`, every task in the order is closed; when `false`, tasks remain untouched.
 
- `rejectRequestedTasks` may only be `true` when the order is transitioning to `Completed` or `Cancelled`. If enabled, all outstanding client-requested tasks are rejected after the update.
 
- Moving `status` to `Review`, `Completed`, or `Cancelled` triggers notifications:
 
 - `Review`: notifies the client that a review is needed.
 
 - `Completed`: sends the `orderCompletion` notification to the client.
 
 - `Cancelled`: sends the `orderCancellation` notification to the client.
 
 
- After every successful update, the system fires an `ORDER.UPDATED` webhook event whose payload includes the updated project document plus the current attachment metadata.
 

### 

Responses

HTTP Status

Description

`200 OK`

Update succeeded. Body: `{ "message": "Project has been updated" }`.

`400 ValidationError`

Invalid project id, blocked status transition, or malformed payload. Response contains `fieldName` when relevant.

`403 PermissionError`

Member is not approved, lacks the company role, subscription expired, or a client attempted a forbidden cancel action.

`500 Internal Server Error`

Unhandled exceptions are forwarded to the error middleware and logged via Winston.

### 

Example Request

Kopieren

```
curl --request PUT "{{URL}}/orders?pid={{PROJECT_ID}}" \
  --header "Authorization: Bearer {{ACCESS_TOKEN}}" \
  --header "companyid: {{COMPANY_ID}}" \
  --form "name=Website Redesign" \
  --form "status=Review" \
  --form "budget=12000" \
  --form "assignedProjectManagers[]={{PROJECT_MANAGER_ID}}" \
  --form "repeatCount=3" \
  --form "repeatDuration=month" \
  --form "files=@/path/to/creative-brief.pdf"
```

**Sample success response**

Kopieren

```
{
  "message": "Project has been updated"
}
```

[VorherigeGetting Started](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/getting-started) [Nächste🚀 Create a New Lead Using API](https://docs.agencyhandy.com/english/agencyhandy-user-guide-for-agency/api-integration-guide/create-a-new-lead-using-api)

Zuletzt aktualisiert vor 6 Monaten