from zeep import Client

trainingWsdl = 'https://trainingws.grants.gov:443/grantsws-applicant/services/v2/ApplicantWebServicesSoapPort?wsdl'
prodWsdl = 'https://ws07.grants.gov/grantsws-applicant/services/v2/ApplicantWebServicesSoapPort?wsdl'
FundingOpportunityNumber = 'OIA-MAP2024'
packageId = 'PKG00212468'
client = Client(wsdl=prodWsdl)
nofo = client.service.GetOpportunityList(None,{'FundingOpportunityNumber':FundingOpportunityNumber})
print(nofo)

nofo = client.service.GetOpportunityList(packageId)
print(nofo)
