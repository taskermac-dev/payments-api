# payments-api

Payments service for the Fintech BU. Handles payment capture, refunds, and
idempotency for the checkout flow.

## Features

- Capture card payments with idempotency keys.
- Issue refunds with audit logging.
- Emit payment events for downstream consumers.

## Local development

```sh
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Testing

```sh
pytest
```

## Deployment

Deployed as a container to the shared EKS cluster. Secrets are injected from
the team Vault namespace at startup.
