import csv
import sys
import os
from time import sleep
from os.path import join
from .crawler import crawl


sampleRecord = {
    "Measurement": 0,
    "ModifyTime": "2022-11-16 13:58:56",
    "Qty_Unit": "PCS",
    "Vessel_Name": "MONTE VERDE",
    "Container_Size": "",
    "CIF_Unit": "USD",
    "Exporter": "NOT AVAILABLE(AR)",
    "Billing_No": "HLCUBU3220900633",
    "Source": "USA 美国",
    "Foreign_Port": "CHARLESTON,SC",
    "Product_Desc": "ITH BL40 00 XCONSOLIDAT",
    "Country_of_Importers": "",
    "Weight_Unit": "K",
    "RecordType": "Import",
    "FOB": 0,
    "Carrier": "HAPAG LLOYD A G",
    "Importer": "",
    "Place_Of_Receipt": "ARGENTINA",
    "CIF": 56139,
    "Local_Port": "BUENOS AIRES,ARGENTINA",
    "Declaration_Number": "",
    "Flight_No": "",
    "Manifest_Number": "",
    "CreateTime": "2022-11-21 18:39:47",
    "Quantity": 40,
    "FOB_Unit": "",
    "From": "TopeasyCustomsDataCountryTotal2022.dbo.UnitedStates_Import",
    "Origin_Country": "Argentina (AR)",
    "Date": "2022-10-31 00:00:00",
    "Weight": 41200,
    "Measurement_Unit": "",
    "HS_Product": "090240 BLACK TLY FERMENTED TEA NESOI",
    "Id": "543CAB45-F674-49C3-A6C0-1619CD512100",
    "Transport": "VESSEL. CONTAINERIZED.",
    "HS_Code": "090240",
    "Country_of_Exporters": "",
    "Sales_Country": "",
    "Container_Number": ""
}


def main() -> None:
    """ main function """
    cwd = os.getcwd()
    os.makedirs(join(cwd, 'results'), mode=0o755, exist_ok=True)

    if len(sys.argv) > 1 and sys.argv[1] is not None:
        fromPage = int(sys.argv[1]) or 1
        toPage = int(sys.argv[2]) or 100
        fromDate = sys.argv[3] or '2022-01-01'
        toDate = sys.argv[4] or '2022-12-15'
        limit = sys.argv[5] or 50
        # insert URL to the queue
        filename = 'smtso-{}-{}.csv'.format(fromPage, toPage)
        full_file_name = './results/' + filename
        total = 0
        with open(
            full_file_name, mode='w', newline='', encoding='utf-8'
                ) as csv_file:
            fieldnames = sampleRecord.keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            p = fromPage
            while p <= toPage:
                try:
                    records = crawl(p, limit, fromDate, toDate)
                    # print(records)
                    for r in records:
                        total = total + 1
                        writer.writerow(r['_source'])
                except Exception as err:
                    print(str(err))
                p = p + 1
                sleep(15)

        print('Finished')
        print('Total items: %s' % total)
        sys.exit()
    else:
        print("Error! Command need a fromPage, eg: python main.py 1 5")


if __name__ == "__main__":
    main()
