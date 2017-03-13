from flightTicketPriceNotification import flightTicketPriceNotificationFromSkyscanner
import unittest

class FlightTicketInfoFromSkyscannerTest(unittest.TestCase):

    def setUp(self):
        self.mainClass = flightTicketPriceNotificationFromSkyscanner.FlightTicketPriceNotificationFromSkyscanner()
        self.condition = self.mainClass.conditions[0]
        self.condition["notifyMinPrice"] = '10000000'
        self.parsedFlightTicketInfoData = {'SessionKey': 'e94555c10b724882b02fd486cbda3b62_rrsqbjcb_06a13f0a788e803fcc56e78802891a26', 'Query': {'Country': 'PL', 'Currency': 'PLN', 'Locale': 'pl-pl', 'Adults': 1, 'Children': 0, 'Infants': 0, 'OriginPlace': '8336', 'DestinationPlace': '7001', 'OutboundDate': '2018-02-09', 'InboundDate': '2018-02-24', 'LocationSchema': 'Default', 'CabinClass': 'Economy', 'GroupPricing': True}, 'Status': 'UpdatesComplete', 'Itineraries': [{'OutboundLegId': '17648-1802091535--32093-0-12409-1802100915', 'InboundLegId': '12409-1802241100--32093-0-17648-1802241400', 'PricingOptions': [{'Agents': [4056756], 'QuoteAgeInMinutes': 27, 'Price': 3200.04, 'DeeplinkUrl': 'http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=GdIj0zlKVz8HduaRC84F3I5UB1K0fipUu9PtnaDg6jxoX%2foBHwiaqjgeZm1%2bnl3N&url=http%3a%2f%2fwww.apideeplink.com%2ftransport_deeplink%2f4.0%2fPL%2fpl-pl%2fPLN%2ftpst%2f2%2f17648.12409.2018-02-09%2c12409.17648.2018-02-24%2fair%2ftrava%2fflights%3fitinerary%3dflight%7c-32093%7c97%7c17648%7c2018-02-09T15%3a35%7c12409%7c2018-02-10T09%3a15%2cflight%7c-32093%7c98%7c12409%7c2018-02-24T11%3a00%7c17648%7c2018-02-24T14%3a00%26carriers%3d-32093%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d3200.04%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26request_id%3d0a36d317-f94b-419c-bd0d-fdd69094c466%26deeplink_ids%3deu-central-1.prod_48aa28baf11627de6bddacc72f03d723%26commercial_filters%3dfalse%26q_datetime_utc%3d2017-03-10T08%3a51%3a25'}, {'Agents': [2627446], 'QuoteAgeInMinutes': 27, 'Price': 3243.99, 'DeeplinkUrl': 'http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=GdIj0zlKVz8HduaRC84F3I5UB1K0fipUu9PtnaDg6jxoX%2foBHwiaqjgeZm1%2bnl3N&url=http%3a%2f%2fwww.apideeplink.com%2ftransport_deeplink%2f4.0%2fPL%2fpl-pl%2fPLN%2fgtbf%2f2%2f17648.12409.2018-02-09%2c12409.17648.2018-02-24%2fair%2ftrava%2fflights%3fitinerary%3dflight%7c-32093%7c97%7c17648%7c2018-02-09T15%3a35%7c12409%7c2018-02-10T09%3a15%2cflight%7c-32093%7c98%7c12409%7c2018-02-24T11%3a00%7c17648%7c2018-02-24T14%3a00%26carriers%3d-32093%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d3243.99%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26request_id%3d0a36d317-f94b-419c-bd0d-fdd69094c466%26deeplink_ids%3deu-central-1.prod_3d1d3ed6d3dfc47b3612c9d8a75b154c%26commercial_filters%3dfalse%26q_datetime_utc%3d2017-03-10T08%3a51%3a27'}, {'Agents': [4045084], 'QuoteAgeInMinutes': 26, 'Price': 3289.14, 'DeeplinkUrl': 'http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=GdIj0zlKVz8HduaRC84F3I5UB1K0fipUu9PtnaDg6jxoX%2foBHwiaqjgeZm1%2bnl3N&url=http%3a%2f%2fwww.apideeplink.com%2ftransport_deeplink%2f4.0%2fPL%2fpl-pl%2fPLN%2ftkpl%2f2%2f17648.12409.2018-02-09%2c12409.17648.2018-02-24%2fair%2ftrava%2fflights%3fitinerary%3dflight%7c-32093%7c97%7c17648%7c2018-02-09T15%3a35%7c12409%7c2018-02-10T09%3a15%2cflight%7c-32093%7c98%7c12409%7c2018-02-24T11%3a00%7c17648%7c2018-02-24T14%3a00%26carriers%3d-32093%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d3289.14%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26request_id%3d0a36d317-f94b-419c-bd0d-fdd69094c466%26deeplink_ids%3deu-central-1.prod_3ed22315b3cadc709c376d183a2df9c2%26commercial_filters%3dfalse%26q_datetime_utc%3d2017-03-10T08%3a51%3a29'}, {'Agents': [1963108], 'QuoteAgeInMinutes': 27, 'Price': 3298.87, 'DeeplinkUrl': 'http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=GdIj0zlKVz8HduaRC84F3I5UB1K0fipUu9PtnaDg6jxoX%2foBHwiaqjgeZm1%2bnl3N&url=http%3a%2f%2fwww.apideeplink.com%2ftransport_deeplink%2f4.0%2fPL%2fpl-pl%2fPLN%2fat24%2f2%2f17648.12409.2018-02-09%2c12409.17648.2018-02-24%2fair%2ftrava%2fflights%3fitinerary%3dflight%7c-32093%7c97%7c17648%7c2018-02-09T15%3a35%7c12409%7c2018-02-10T09%3a15%2cflight%7c-32093%7c98%7c12409%7c2018-02-24T11%3a00%7c17648%7c2018-02-24T14%3a00%26carriers%3d-32093%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d3298.87%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26request_id%3d0a36d317-f94b-419c-bd0d-fdd69094c466%26deeplink_ids%3deu-central-1.prod_aba897a77301c11e9e93430b34e8c673%26commercial_filters%3dfalse%26q_datetime_utc%3d2017-03-10T08%3a51%3a24'}, {'Agents': [3169745], 'QuoteAgeInMinutes': 27, 'Price': 3301.91, 'DeeplinkUrl': 'http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=GdIj0zlKVz8HduaRC84F3I5UB1K0fipUu9PtnaDg6jxoX%2foBHwiaqjgeZm1%2bnl3N&url=http%3a%2f%2fwww.apideeplink.com%2ftransport_deeplink%2f4.0%2fPL%2fpl-pl%2fPLN%2flota%2f2%2f17648.12409.2018-02-09%2c12409.17648.2018-02-24%2fair%2fairli%2fflights%3fitinerary%3dflight%7c-32093%7c97%7c17648%7c2018-02-09T15%3a35%7c12409%7c2018-02-10T09%3a15%2cflight%7c-32093%7c98%7c12409%7c2018-02-24T11%3a00%7c17648%7c2018-02-24T14%3a00%26carriers%3d-32093%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d3301.91%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26request_id%3d0a36d317-f94b-419c-bd0d-fdd69094c466%26deeplink_ids%3deu-central-1.prod_7de206a9301c59dc2eb1ec26440c51c5%26commercial_filters%3dfalse%26q_datetime_utc%3d2017-03-10T08%3a51%3a22%26source_website_id%3damac'}, {'Agents': [3604753], 'QuoteAgeInMinutes': 27, 'Price': 3351.26, 'DeeplinkUrl': 'http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=GdIj0zlKVz8HduaRC84F3I5UB1K0fipUu9PtnaDg6jxoX%2foBHwiaqjgeZm1%2bnl3N&url=http%3a%2f%2fwww.apideeplink.com%2ftransport_deeplink%2f4.0%2fPL%2fpl-pl%2fPLN%2fplk1%2f2%2f17648.12409.2018-02-09%2c12409.17648.2018-02-24%2fair%2ftrava%2fflights%3fitinerary%3dflight%7c-32093%7c97%7c17648%7c2018-02-09T15%3a35%7c12409%7c2018-02-10T09%3a15%2cflight%7c-32093%7c98%7c12409%7c2018-02-24T11%3a00%7c17648%7c2018-02-24T14%3a00%26carriers%3d-32093%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d3351.26%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26request_id%3d0a36d317-f94b-419c-bd0d-fdd69094c466%26deeplink_ids%3deu-central-1.prod_02fea83d04b6bf63fcd6c97e860e9c9d%26commercial_filters%3dfalse%26q_datetime_utc%3d2017-03-10T08%3a51%3a19'}, {'Agents': [4075036], 'QuoteAgeInMinutes': 26, 'Price': 3357.12, 'DeeplinkUrl': 'http://partners.api.skyscanner.net/apiservices/deeplink/v2?_cje=GdIj0zlKVz8HduaRC84F3I5UB1K0fipUu9PtnaDg6jxoX%2foBHwiaqjgeZm1%2bnl3N&url=http%3a%2f%2fwww.apideeplink.com%2ftransport_deeplink%2f4.0%2fPL%2fpl-pl%2fPLN%2ftxpl%2f2%2f17648.12409.2018-02-09%2c12409.17648.2018-02-24%2fair%2ftrava%2fflights%3fitinerary%3dflight%7c-32093%7c97%7c17648%7c2018-02-09T15%3a35%7c12409%7c2018-02-10T09%3a15%2cflight%7c-32093%7c98%7c12409%7c2018-02-24T11%3a00%7c17648%7c2018-02-24T14%3a00%26carriers%3d-32093%26passengers%3d1%26channel%3ddataapi%26cabin_class%3deconomy%26facilitated%3dfalse%26ticket_price%3d3357.12%26is_npt%3dfalse%26is_multipart%3dfalse%26client_id%3dskyscanner_b2b%26request_id%3d0a36d317-f94b-419c-bd0d-fdd69094c466%26deeplink_ids%3deu-central-1.prod_77a1471d0ab2fb95df7f8d04bbd02e1c%26commercial_filters%3dfalse%26q_datetime_utc%3d2017-03-10T08%3a51%3a34'}], 'BookingDetailsLink': {'Uri': '/apiservices/pricing/v1.0/e94555c10b724882b02fd486cbda3b62_rrsqbjcb_06a13f0a788e803fcc56e78802891a26/booking', 'Body': 'OutboundLegId=17648-1802091535--32093-0-12409-1802100915&InboundLegId=12409-1802241100--32093-0-17648-1802241400', 'Method': 'PUT'}}], 'Legs': [{'Id': '17648-1802091535--32093-0-12409-1802100915', 'SegmentIds': [0], 'OriginStation': 17648, 'DestinationStation': 12409, 'Departure': '2018-02-09T15:35:00', 'Arrival': '2018-02-10T09:15:00', 'Duration': 580, 'JourneyMode': 'Flight', 'Stops': [], 'Carriers': [1375], 'OperatingCarriers': [1375], 'Directionality': 'Outbound', 'FlightNumbers': [{'FlightNumber': '97', 'CarrierId': 1375}]}, {'Id': '12409-1802241100--32093-0-17648-1802241400', 'SegmentIds': [1], 'OriginStation': 12409, 'DestinationStation': 17648, 'Departure': '2018-02-24T11:00:00', 'Arrival': '2018-02-24T14:00:00', 'Duration': 660, 'JourneyMode': 'Flight', 'Stops': [], 'Carriers': [1375], 'OperatingCarriers': [1375], 'Directionality': 'Inbound', 'FlightNumbers': [{'FlightNumber': '98', 'CarrierId': 1375}]}], 'Segments': [{'Id': 0, 'OriginStation': 17648, 'DestinationStation': 12409, 'DepartureDateTime': '2018-02-09T15:35:00', 'ArrivalDateTime': '2018-02-10T09:15:00', 'Carrier': 1375, 'OperatingCarrier': 1375, 'Duration': 580, 'FlightNumber': '97', 'JourneyMode': 'Flight', 'Directionality': 'Outbound'}, {'Id': 1, 'OriginStation': 12409, 'DestinationStation': 17648, 'DepartureDateTime': '2018-02-24T11:00:00', 'ArrivalDateTime': '2018-02-24T14:00:00', 'Carrier': 1375, 'OperatingCarrier': 1375, 'Duration': 660, 'FlightNumber': '98', 'JourneyMode': 'Flight', 'Directionality': 'Outbound'}], 'Carriers': [{'Id': 1375, 'Code': 'LO', 'Name': 'LOT', 'ImageUrl': 'http://s1.apideeplink.com/images/airlines/LO.png', 'DisplayCode': 'LO'}], 'Agents': [{'Id': 3512860, 'Name': 'OneTwoTrip', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/otpl.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': False, 'Type': 'TravelAgent'}, {'Id': 1963108, 'Name': 'Mytrip', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/at24.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'BookingNumber': '+48224906969', 'Type': 'TravelAgent'}, {'Id': 2404409, 'Name': 'eSky', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/esky.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': False, 'BookingNumber': '801420303', 'Type': 'TravelAgent'}, {'Id': 2499100, 'Name': 'Flysiesta', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/flpl.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'Type': 'TravelAgent'}, {'Id': 4056756, 'Name': 'Tripsta', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/tpst.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'BookingNumber': '+48223897790', 'Type': 'TravelAgent'}, {'Id': 4075036, 'Name': 'Flighttix.pl', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/txpl.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'BookingNumber': '48588810088', 'Type': 'TravelAgent'}, {'Id': 3604753, 'Name': 'Flipo', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/plk1.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': False, 'Type': 'TravelAgent'}, {'Id': 2627446, 'Name': 'GotoGate', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/gtbf.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'Type': 'TravelAgent'}, {'Id': 4045084, 'Name': 'Tickets.pl', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/tkpl.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'Type': 'TravelAgent'}, {'Id': 3065884, 'Name': 'KILROY', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/krpl.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'Type': 'TravelAgent'}, {'Id': 4040181, 'Name': 'Tije Travel', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/tije.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': False, 'Type': 'TravelAgent'}, {'Id': 2406600, 'Name': 'Etihad Airways', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/etih.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'BookingNumber': '8002277', 'Type': 'Airline'}, {'Id': 3690449, 'Name': 'Qatar Airways', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/qata.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': False, 'BookingNumber': '0097444496666', 'Type': 'Airline'}, {'Id': 1961921, 'Name': 'Asiana Airlines', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/asia.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'BookingNumber': '82226698000', 'Type': 'Airline'}, {'Id': 1939318, 'Name': 'Air France', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/airf.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'BookingNumber': '0969391030', 'Type': 'Airline'}, {'Id': 3051889, 'Name': 'KLM', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/klm1.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'BookingNumber': '0031204747747', 'Type': 'Airline'}, {'Id': 2390482, 'Name': 'Emirates', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/emir.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'BookingNumber': '0097142144444', 'Type': 'Airline'}, {'Id': 3169745, 'Name': 'LOT', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/lota.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': False, 'BookingNumber': '0801703703', 'Type': 'Airline'}, {'Id': 2032127, 'Name': 'British Airways', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/ba__.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'BookingNumber': '08444930787', 'Type': 'Airline'}, {'Id': 3182916, 'Name': 'Lufthansa', 'ImageUrl': 'http://s1.apideeplink.com/images/websites/luft.png', 'Status': 'UpdatesComplete', 'OptimisedForMobile': True, 'BookingNumber': '+48223381300', 'Type': 'Airline'}], 'Places': [{'Id': 17648, 'ParentId': 8336, 'Code': 'WAW', 'Type': 'Airport', 'Name': 'Warszawa Chopina'}, {'Id': 12409, 'ParentId': 7001, 'Code': 'ICN', 'Type': 'Airport', 'Name': 'Seul Incheon'}, {'Id': 8336, 'ParentId': 194, 'Code': 'WAW', 'Type': 'City', 'Name': 'Warszawa'}, {'Id': 7001, 'ParentId': 173, 'Code': 'SEL', 'Type': 'City', 'Name': 'Seul'}, {'Id': 194, 'Code': 'PL', 'Type': 'Country', 'Name': 'Polska'}, {'Id': 173, 'Code': 'KR', 'Type': 'Country', 'Name': 'Korea Południowa'}], 'Currencies': [{'Code': 'PLN', 'Symbol': 'zł', 'ThousandsSeparator': '\xa0', 'DecimalSeparator': ',', 'SymbolOnLeft': False, 'SpaceBetweenAmountAndSymbol': True, 'RoundingCoefficient': 0, 'DecimalDigits': 2}, {'Code': 'KRW', 'Symbol': '₩', 'ThousandsSeparator': ',', 'DecimalSeparator': '.', 'SymbolOnLeft': True, 'SpaceBetweenAmountAndSymbol': False, 'RoundingCoefficient': 0, 'DecimalDigits': 0}]}
        self.handledFlightTicketInfoData = [{"notifyMinPrice": "3300", 'OutboundLegId': '17648-1802091535--32093-0-12409-1802100915', 'InboundLegId': '12409-1802241100--32093-0-17648-1802241400', 'price': 3200, 'seller': 'Tripsta', 'outboundDepartTime': '15:35', 'outboundArriveTime': '09:15', 'stops': '0', 'outboundAirportCode': 'WAW', 'inboundAirportCode': 'ICN', 'outboundAirline': 'LOT', 'outboundAirlinecode': 'LO97', 'inboundDepartTime': '11:00', 'inboundArriveTime': '14:00', 'inboundAirline': 'LOT', 'inboundAirlinecode': 'LO98', 'country': 'PL', 'currency': 'PLN', 'originplace': 'WAW', 'destinationplace': 'SEL', 'outbounddate': '2018-02-09', 'inbounddate': '2018-02-24', 'adults': '1', 'children': '0', 'infants': '0'}]

    def tearDown(self):
        pass

    def test_parseFlightTicketInfoFromSkyscanner(self):
        result = self.mainClass.parseFlightTicketInfoFromSkyscanner(self.condition)
        self.assertGreaterEqual(len(result.get("Itineraries",[])),1)

    def test_handlingFlightTicketInfo(self):
        result = self.mainClass.handlingFlightTicketInfo(self.condition, self.parsedFlightTicketInfoData)
        self.assertGreaterEqual(len(result), 1)

    def test_notifyThoughEmail(self):
        result = self.mainClass.notifyThoughEmail(self.condition, self.handledFlightTicketInfoData)
        self.assertGreaterEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()

