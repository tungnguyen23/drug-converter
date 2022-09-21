import requests
import json
from bs4 import BeautifulSoup
import csv


def scrape(inputs):
    cookies = {
        'idp_session': 'sVERSION_18780ffa9-c750-4b07-bb24-aa114072defb',
        'idp_session_http': 'hVERSION_11833362f-ba29-4a7f-b227-9923d9169ed6',
        'idp_marker': 'b997f225-67af-431f-9b89-ac1bc1ae2451',
        'trackid': '56f52e6f5aa9493197356be41',
        'current_tab': 'drugs',
        'existing_view': '%7B%22viewType%22%3A%22list%22%2C%22drugs%22%3A%7B%22gridView_an%22%3Afalse%2C%22gridView_moa%22%3Atrue%2C%22gridView_ta%22%3Afalse%2C%22gridView_aihpActive%22%3Atrue%2C%22gridView_aihpInactive%22%3Afalse%2C%22gridView_biomarker%22%3Atrue%2C%22gridView_originator%22%3Atrue%2C%22gridView_licensee%22%3Atrue%2C%22gridView_drugs_date%22%3Atrue%7D%2C%22drugSafety%22%3A%7B%22gridView_safetyReport%22%3Atrue%2C%22gridView_safetyReporter%22%3Atrue%2C%22gridView_safetyCases%22%3Atrue%2C%22gridView_safetyAdverseEvents%22%3Afalse%2C%22gridView_safetyCitation%22%3Afalse%2C%22gridView_safetyRecordType%22%3Afalse%2C%22gridView_safetyLanguage%22%3Afalse%2C%22gridView_safetyDate%22%3Atrue%2C%22gridView_safetyUpdateDate%22%3Afalse%7D%2C%22trials%22%3A%7B%22gridView_trialStatus%22%3Atrue%2C%22gridView_TrialDrug%22%3Atrue%2C%22gridView_TrialIndication%22%3Atrue%2C%22gridView_TrialPhase%22%3Atrue%2C%22gridView_TrialBiomarker%22%3Atrue%2C%22gridView_TrialAcronym%22%3Afalse%2C%22gridView_TrialDesign%22%3Afalse%2C%22gridView_TrialNumberOfPatients%22%3Afalse%2C%22gridView_TrialOrganizations%22%3Afalse%2C%22gridView_TrialPatientSegment%22%3Afalse%2C%22gridView_TrialEndDate%22%3Afalse%7D%7D',
        'OptanonAlertBoxClosed': '2022-04-27T06:33:31.068Z',
        '_ga': 'GA1.1.1642299968.1658465888',
        '_gid': 'GA1.3.1876645608.1651041211',
        '_gat_UA-50380846-2': '1',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Wed+Apr+27+2022+15%3A58%3A32+GMT-0400+(Eastern+Daylight+Time)&version=6.10.0&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C0_130358%3A1%2C0_130359%3A1%2C0_261438%3A1%2C0_264205%3A1%2C102%3A1&AwaitingReconsent=false',
        'uvts': 'a1654ed8-9c34-46f7-6713-0efb8a5fad36',
    }

    headers = {
        'authority': 'adisinsight.springer.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'origin': 'https://adisinsight.springer.com',
        'referer': 'https://adisinsight.springer.com/search',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    }

    for search in inputs:
        data = {
            'query.get': search,
            'query': '{"baseQuery":"drug-name:(\\"' + search + '\\")","facets":{"drugs":[],"deals":[],"drugSafety":[],"trials":[],"drugsArchive":[],"patents":[]},"sortBy":{"drugs":"date","deals":"","trials":"","drugSafety":"","drugsArchive":""}}',
            'loadDefaultTab': 'true',
        }

        response = requests.post('https://adisinsight.springer.com/search',
                                cookies=cookies, headers=headers, data=data)
        soup = BeautifulSoup(response.content, "html.parser")

        
        name = soup.find(
            "a", class_="profile-link")

        if name:
            print(name.text.strip().split('-')[0].strip())
        else:
            print(search)
#input list in between scrape (["x",])
#Please refer to the instruction document for the data format
scrape(["SB206 12%",
"KX2-391",
"FMX103",
"BIIB067",
"FYU-981",])