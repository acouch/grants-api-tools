# Test Grants.gov SOAP API

To install, `poetry install`.

To get a full list of the available applicant webserivces (also described at [Applicant Web Services
](https://www.grants.gov/web/grants/s2s/applicant/web-services.html), run:

```
poetry run python -mzeep https://ws07.grants.gov/grantsws-applicant/services/v2/ApplicantWebServicesSoapPort?wsdl
```

To get an example opportunity, run `poetry run python client.py`.
