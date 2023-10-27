# Parse grants.gov XML extract.


1. Download latest XML file https://www.grants.gov/web/grants/xml-extract.html 

2. Unzip into this folder, ie `GrantsDBExtractYYYYMMDDv2.xml`

3. Run `xml2csv -i GrantsDBExtractYYYYMMDDv2.xml -m mapping.json -o OUTPUT_FILE_NAME.csv`
