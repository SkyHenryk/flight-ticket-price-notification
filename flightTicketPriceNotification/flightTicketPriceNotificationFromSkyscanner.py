import requests
import json
import datetime
import pprint

class FlightTicketPriceNotificationFromSkyscanner():
    SkyscannerApiKey = "sk-----"
    MailgunApiKey = "key------"
    MailgunSandbox = "sandbox-----"
    MailgunEmail = "-----@-----"
    conditions = [{
        "country": "PL",
        "currency": "PLN",
        "originplace": "WAW",
        "destinationplace": "SEL",
        "outbounddate": "2018-02-09",
        "inbounddate": "2018-02-24",
        "adults": "1",
        "children": "0",
        "infants": "0",
        "stops": "0",
        "notifyMinPrice": "2500",
    }]

    def start(self):

        for condition in self.conditions:
            parsedFlightTicketInfoData = self.parseFlightTicketInfoFromSkyscanner(condition)
            flightTicketInfoData = self.handlingFlightTicketInfo(condition,parsedFlightTicketInfoData)
            self.notifyThoughEmail(condition,flightTicketInfoData)
        pass


    def parseFlightTicketInfoFromSkyscanner(self, condition):
        skyscannerSessionUrl = "http://business.skyscanner.net/apiservices/pricing/v1.0/"
        payload = {
                   "locale": "pl-PL",
                   "locationSchema": "iata",
                   "apikey": self.SkyscannerApiKey,
                   "grouppricing": "on",
                   "cabinclass": "Economy"
                   }
        payload.update(condition)
        headers = {
            'connection': "keep-alive",
            'content-length': "245",
            'content-type': "application/x-www-form-urlencoded",
            'host': "business.skyscanner.net",
            'origin': "http://business.skyscanner.net",
            'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            'cache-control': "no-cache",
        }

        SessionResponse = requests.request('POST', skyscannerSessionUrl, data=payload, headers=headers)
        if isinstance(SessionResponse, str):
            return

        skyscannerPollingUrl = SessionResponse.headers['location']

        querystring = {"apikey": self.SkyscannerApiKey}

        stops = condition.get("stops")
        if stops is not None:
            querystring.update({"stops": stops})

        pollingResponse = json.loads(requests.request("GET", skyscannerPollingUrl, params=querystring).content)
        return pollingResponse


    def handlingFlightTicketInfo(self, condition, parsedFlightTicketInfoData):

        flightTicketInfoArray = []
        itineraries = parsedFlightTicketInfoData.get("Itineraries",[])
        legs = parsedFlightTicketInfoData.get("Legs",[])
        carriers = parsedFlightTicketInfoData.get("Carriers",[])
        agents = parsedFlightTicketInfoData.get("Agents",[])
        places = parsedFlightTicketInfoData.get("Places",[])
        
        for itinerary  in itineraries:

            flightTicketInfo = {}
            flightTicketInfo['searchDate'] = datetime.datetime.utcnow().strftime("%Y-%m-%d")
            firstitemOutbound = itinerary['OutboundLegId']
            firstitemInbound = itinerary['InboundLegId']
            firstitemSeller = itinerary['PricingOptions'][0]['Agents'][0]
            flightTicketInfo["OutboundLegId"] = firstitemOutbound
            flightTicketInfo["InboundLegId"] = firstitemInbound
            flightTicketInfo["price"] = int(itinerary['PricingOptions'][0]['Price'])

            for agent in agents:

                if int(firstitemSeller) == int(agent["Id"]):
                    flightTicketInfo['seller'] = agent["Name"]

            for leg in legs:

                if leg["Id"].find(firstitemOutbound) > -1:
                    firstitemOriginStationNum = leg["OriginStation"]
                    firstitemDestinationStationNum = leg["DestinationStation"]
                    firstitemCarrier = leg["Carriers"][0]
                    flightTicketInfo['outboundDepartTime']= leg['Departure'][11:][:-3]
                    flightTicketInfo['outboundArriveTime'] = leg["Arrival"][11:][:-3]
                    flightTicketInfo['stops'] = len(leg["Stops"])
                    for place in places:
                        if int(place["Id"]) == int(firstitemOriginStationNum):
                            flightTicketInfo['outboundAirportCode'] = place["Code"]
                        if int(place["Id"]) == int(firstitemDestinationStationNum):
                            flightTicketInfo['inboundAirportCode'] = place["Code"]
                    for carrier in carriers:
                        if int(carrier["Id"]) == int(firstitemCarrier):
                            flightTicketInfo['outboundAirline'] = carrier["Name"]
                            flightTicketInfo['outboundAirlinecode'] = carrier["Code"]
                            flightTicketInfo['outboundAirlinecode'] += leg["FlightNumbers"][0]["FlightNumber"]

                if leg["Id"].find(firstitemInbound) > -1:
                    flightTicketInfo['inboundDepartTime'] = leg['Departure'][11:][:-3]
                    flightTicketInfo['inboundArriveTime'] = leg["Arrival"][11:][:-3]
                    for carrier in carriers:
                        if int(carrier["Id"]) == int(firstitemCarrier):
                            flightTicketInfo['inboundAirline'] = carrier["Name"]
                            flightTicketInfo['inboundAirlinecode'] = carrier["Code"][:6]
                            flightTicketInfo['inboundAirlinecode'] += leg["FlightNumbers"][0]["FlightNumber"]

            flightTicketInfo.update(condition)
            flightTicketInfoArray.append(flightTicketInfo)
        pprint.pprint(flightTicketInfoArray)
        return flightTicketInfoArray


    def notifyThoughEmail(self, condition, flightTicketInfoArray):

        notifyMinPrice = condition.get("notifyMinPrice")
        notifyCheckArray = []

        for flightTicketInfo in flightTicketInfoArray:
            price = flightTicketInfo.get("price")
            if price is None:
                continue
            if int(notifyMinPrice) > int(price):
                notifyCheckArray.append(flightTicketInfo)

        if len(notifyCheckArray) > 0:
            emailMsg = "congratulation! The ticket price is less then your minimum price filter. \n"
            emailMsg += json.dumps(notifyCheckArray, sort_keys=True, indent=4)
            requests.post(
                    f"https://api.mailgun.net/v3/{self.MailgunSandbox}.mailgun.org/messages",
                    auth=("api", self.MailgunApiKey),
                    data={"from": f"Mailgun Sandbox <postmaster@{self.MailgunSandbox}.mailgun.org>",
                          "to": self.MailgunEmail,
                          "subject": "congratulation! The ticket price is less then your minimum price filter.",
                          "text": json.dumps(notifyCheckArray, sort_keys=True, indent=4)})
        return notifyCheckArray

if __name__ == '__main__':
    FlightTicketPriceNotificationFromSkyscanner().start()