# Data Pipeline Design

In this hypothetical challenge, we need to ingest data from a number of sources. Some of those sources will be ingested on a schedule, while others need to be processed in real time when data comes to us. The data is used by both analysts and to API clients.

You will design a system that accomplishes these needs and walk us through your design and tooling decisions.

Whiteboarding tools:

- https://excalidraw.com/

## Product Details

### Data Sources

- Claims: Nightly pull from an external database
- Plans: Sporadic push of data, unknown intervals, into a storage bucket
- Beneficiary: Same type of database, in a different account, with a cross-account data share connection

### Consumers

- Provide an API for other clients to access for their front end applications
- Tableau for internal report creation against the data

---

## Preparing for the Interview

**[Next Steps...](../../next-steps.md)**

