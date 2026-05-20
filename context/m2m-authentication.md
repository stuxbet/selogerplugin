# M2M Authentication — AVIV Classified API v4

Source: https://www.developers.aviv-group.com/apis/classifieds-management-v4-4-0-2/docs/m2m-authentication

## Overview

OAuth 2.0 `client_credentials` grant. Exchange credentials for a JWT bearer token, then send it on every API call.

## Prerequisites

- `client_id` and `client_secret` provided by AVIV Group
- An `intermediary_id` identifying the agency the request is made on behalf of
- Audience values:
  - Production: `https://api.aviv-group.com/caas/v4`
  - Sandbox: `https://api.aviv-group.com/sandbox/caas/v4`

## Token endpoint

```
POST https://auth.api.aviv-group.com/oauth/token
Content-Type: application/json
```

Body (JSON, not form-urlencoded):

```json
{
  "client_id": "your_client_id",
  "client_secret": "your_client_secret",
  "grant_type": "client_credentials",
  "audience": "https://api.aviv-group.com/caas/v4",
  "intermediary_id": "your_intermediary_id"
}
```

| Parameter | Required | Description |
|---|---|---|
| `client_id` | Yes | Application's client identifier |
| `client_secret` | Yes | Application's client secret |
| `grant_type` | Yes | Must be `client_credentials` |
| `audience` | Yes | Prod or sandbox audience URL |
| `intermediary_id` | Yes | Identifier of the intermediary agency in your system |

Response:

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 86400,
  "token_type": "Bearer"
}
```

## Using the token

```
GET /caas/v4/<endpoint> HTTP/1.1
Host: api.aviv-group.com
Authorization: Bearer <access_token>
User-Agent: YourApp/1.0 Platform/1.0 Runtime/1.0
```

## Hard rules

1. **`User-Agent` header is mandatory.** Requests without it are blocked by the firewall.
2. **Token caching is mandated.** Tokens are valid for 24 hours and *must* be cached and reused for their full lifetime — do not request a new token per call. Token reuse is verified during sandbox review and is a prerequisite for production access.

## Sandbox

Same token endpoint, different `audience`:

```json
{
  "client_id": "your_client_id",
  "client_secret": "your_client_secret",
  "grant_type": "client_credentials",
  "audience": "https://api.aviv-group.com/sandbox/caas/v4",
  "intermediary_id": "your_intermediary_id"
}
```

Sandbox base URL for API calls: `https://api.aviv-group.com/sandbox/caas/v4`

## Reference snippet (Python)

```python
import requests

token_url = "https://auth.api.aviv-group.com/oauth/token"
payload = {
    "grant_type": "client_credentials",
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "audience": "https://api.aviv-group.com/caas/v4",
    "intermediary_id": "your_intermediary_id",
}
response = requests.post(token_url, json=payload)
access_token = response.json()["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}",
    "User-Agent": "YourApp/1.0 Python/3.12 requests/2.32",
}
```
