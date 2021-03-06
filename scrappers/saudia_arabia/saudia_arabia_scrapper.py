def scrap(*args, **kwargs):
    print(args, kwargs)
    return {
        "data": [
            {	"airline": "GoAir", "flight_number": "AF-667", "from": "Saudia-Arabia", "to": "New Delhi",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "38706"},
            {	"airline": "GoAir", "flight_number": "AF-621", "from": "Saudia-Arabia", "to": "New Delhi",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "45302"},
            {	"airline": "Indigo", "flight_number": "AF-736", "from": "Saudia-Arabia", "to": "Mumbai",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "20973"},
            {	"airline": "Indigo", "flight_number": "AF-791", "from": "Saudia-Arabia", "to": "Mumbai",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "25761"},
            {	"airline": "Luftahansa", "flight_number": "AF-582", "from": "Saudia-Arabia", "to": "Chennai",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "30740"},
            {	"airline": "Luftahansa", "flight_number": "AF-704", "from": "Saudia-Arabia", "to": "Chennai",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "10545"},
            {	"airline": "Jet Airways", "flight_number": "AF-131", "from": "Saudia-Arabia", "to": "Kolkata",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "45262"},
            {	"airline": "Jet Airways", "flight_number": "AF-987", "from": "Saudia-Arabia", "to": "Kolkata",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "14302"},
            {	"airline": "Air India", "flight_number": "AF-241", "from": "Saudia-Arabia", "to": "Pune",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "19857"},
            {	"airline": "Air India", "flight_number": "AF-475", "from": "Saudia-Arabia", "to": "Pune",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "15259"},
            {	"airline": "Kingfisher", "flight_number": "AF-422", "from": "Saudia-Arabia", "to": "Bangalore",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "42409"},
            {	"airline": "Kingfisher", "flight_number": "AF-816", "from": "Saudia-Arabia", "to": "Bangalore",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "33628"},
            {	"airline": "GoAir", "flight_number": "AF-514", "from": "Saudia-Arabia", "to": "Jammu",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "33654"},
            {	"airline": "GoAir", "flight_number": "AF-914", "from": "Saudia-Arabia", "to": "Jammu",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "13961"},
            {	"airline": "Indigo", "flight_number": "AF-536", "from": "Saudia-Arabia", "to": "Chandigarh",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "40549"},
            {	"airline": "Indigo", "flight_number": "AF-719", "from": "Saudia-Arabia", "to": "Chandigarh",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "1564"},
            {	"airline": "Luftahansa", "flight_number": "AF-516", "from": "Saudia-Arabia", "to": "Lucknow",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "9836"},
            {	"airline": "Luftahansa", "flight_number": "AF-314", "from": "Saudia-Arabia", "to": "Lucknow",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "19516"},
            {	"airline": "Jet Airways", "flight_number": "AF-595", "from": "Saudia-Arabia", "to": "Patna",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "44604"},
            {	"airline": "Jet Airways", "flight_number": "AF-222", "from": "Saudia-Arabia", "to": "Patna",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "30485"},
            {	"airline": "Air India", "flight_number": "AF-306", "from": "Saudia-Arabia", "to": "Bhopal",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "3114"},
            {	"airline": "Air India", "flight_number": "AF-531", "from": "Saudia-Arabia", "to": "Bhopal",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "1756"},
            {	"airline": "Kingfisher", "flight_number": "AF-355", "from": "Saudia-Arabia", "to": "Jaipur",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "44921"},
            {	"airline": "Kingfisher", "flight_number": "AF-602", "from": "Saudia-Arabia", "to": "Jaipur",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "15817"},
            {	"airline": "GoAir", "flight_number": "AF-957", "from": "Saudia-Arabia", "to": "Ahmedabad",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "33028"},
            {	"airline": "GoAir", "flight_number": "AF-411", "from": "Saudia-Arabia", "to": "Ahmedabad",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "23562"},
            {	"airline": "Indigo", "flight_number": "AF-369", "from": "Saudia-Arabia", "to": "Indore",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "29325"},
            {	"airline": "Indigo", "flight_number": "AF-180", "from": "Saudia-Arabia", "to": "Indore",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "10387"},
            {	"airline": "Luftahansa", "flight_number": "AF-470", "from": "Saudia-Arabia", "to": "Bhubneshwar",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "45548"},
            {	"airline": "Luftahansa", "flight_number": "AF-123", "from": "Saudia-Arabia", "to": "Bhubneshwar",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "23284"},
            {	"airline": "Jet Airways", "flight_number": "AF-472", "from": "Saudia-Arabia", "to": "Goa",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "12354"},
            {	"airline": "Jet Airways", "flight_number": "AF-735", "from": "Saudia-Arabia", "to": "Goa",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "2285"},
            {	"airline": "Air India", "flight_number": "AF-204", "from": "Saudia-Arabia", "to": "Ranchi",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "3497"},
            {	"airline": "Air India", "flight_number": "AF-984", "from": "Saudia-Arabia", "to": "Ranchi",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "36348"},
            {	"airline": "Kingfisher", "flight_number": "AF-656", "from": "Saudia-Arabia", "to": "Gangtok",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "21949"},
            {	"airline": "Kingfisher", "flight_number": "AF-308", "from": "Saudia-Arabia", "to": "Gangtok",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "40949"},
            {	"airline": "GoAir", "flight_number": "AF-686", "from": "Saudia-Arabia", "to": "New Delhi",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "9830"},
            {	"airline": "GoAir", "flight_number": "AF-506", "from": "Saudia-Arabia", "to": "New Delhi",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "7693"},
            {	"airline": "Indigo", "flight_number": "AF-751", "from": "Saudia-Arabia", "to": "Mumbai",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "40216"},
            {	"airline": "Indigo", "flight_number": "AF-416", "from": "Saudia-Arabia", "to": "Mumbai",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "47881"},
            {	"airline": "Luftahansa", "flight_number": "AF-992", "from": "Saudia-Arabia", "to": "Chennai",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "13203"},
            {	"airline": "Luftahansa", "flight_number": "AF-702", "from": "Saudia-Arabia", "to": "Chennai",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "2435"},
            {	"airline": "Jet Airways", "flight_number": "AF-517", "from": "Saudia-Arabia", "to": "Kolkata",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "20448"},
            {	"airline": "Jet Airways", "flight_number": "AF-644", "from": "Saudia-Arabia", "to": "Kolkata",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "32408"},
            {	"airline": "Air India", "flight_number": "AF-257", "from": "Saudia-Arabia", "to": "Pune",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "30387"},
            {	"airline": "Air India", "flight_number": "AF-990", "from": "Saudia-Arabia", "to": "Pune",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "10642"},
            {	"airline": "Kingfisher", "flight_number": "AF-509", "from": "Saudia-Arabia", "to": "Bangalore",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "19617"},
            {	"airline": "Kingfisher", "flight_number": "AF-600", "from": "Saudia-Arabia", "to": "Bangalore",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "45441"},
            {	"airline": "GoAir", "flight_number": "AF-583", "from": "Saudia-Arabia", "to": "Jammu",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "6785"},
            {	"airline": "GoAir", "flight_number": "AF-669", "from": "Saudia-Arabia", "to": "Jammu",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "47672"},
            {	"airline": "Indigo", "flight_number": "AF-184", "from": "Saudia-Arabia", "to": "Chandigarh",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "7100"},
            {	"airline": "Indigo", "flight_number": "AF-178", "from": "Saudia-Arabia", "to": "Chandigarh",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "38729"},
            {	"airline": "Luftahansa", "flight_number": "AF-751", "from": "Saudia-Arabia", "to": "Lucknow",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "11632"},
            {	"airline": "Luftahansa", "flight_number": "AF-495", "from": "Saudia-Arabia", "to": "Lucknow",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "41026"},
            {	"airline": "Jet Airways", "flight_number": "AF-781", "from": "Saudia-Arabia", "to": "Patna",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "7420"},
            {	"airline": "Jet Airways", "flight_number": "AF-702", "from": "Saudia-Arabia", "to": "Patna",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "23323"},
            {	"airline": "Air India", "flight_number": "AF-725", "from": "Saudia-Arabia", "to": "Bhopal",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "35236"},
            {	"airline": "Air India", "flight_number": "AF-475", "from": "Saudia-Arabia", "to": "Bhopal",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "30520"},
            {	"airline": "Kingfisher", "flight_number": "AF-801", "from": "Saudia-Arabia", "to": "Jaipur",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "23133"},
            {	"airline": "Kingfisher", "flight_number": "AF-927", "from": "Saudia-Arabia", "to": "Jaipur",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "42555"},
            {	"airline": "GoAir", "flight_number": "AF-505", "from": "Saudia-Arabia", "to": "Ahmedabad",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "6608"},
            {	"airline": "GoAir", "flight_number": "AF-278", "from": "Saudia-Arabia", "to": "Ahmedabad",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "18481"},
            {	"airline": "Indigo", "flight_number": "AF-260", "from": "Saudia-Arabia", "to": "Indore",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "14546"},
            {	"airline": "Indigo", "flight_number": "AF-700", "from": "Saudia-Arabia", "to": "Indore",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "8295"},
            {	"airline": "Luftahansa", "flight_number": "AF-868", "from": "Saudia-Arabia", "to": "Bhubneshwar",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "43509"},
            {	"airline": "Luftahansa", "flight_number": "AF-378", "from": "Saudia-Arabia", "to": "Bhubneshwar",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "4315"},
            {	"airline": "Jet Airways", "flight_number": "AF-207", "from": "Saudia-Arabia", "to": "Goa",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "49450"},
            {	"airline": "Jet Airways", "flight_number": "AF-436", "from": "Saudia-Arabia", "to": "Goa",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "29738"},
            {	"airline": "Air India", "flight_number": "AF-387", "from": "Saudia-Arabia", "to": "Ranchi",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "39487"},
            {	"airline": "Air India", "flight_number": "AF-569", "from": "Saudia-Arabia", "to": "Ranchi",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "7780"},
            {	"airline": "Kingfisher", "flight_number": "AF-748", "from": "Saudia-Arabia", "to": "Gangtok",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "48967"},
            {	"airline": "Kingfisher", "flight_number": "AF-908", "from": "Saudia-Arabia", "to": "Gangtok",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "48535"},
            {	"airline": "GoAir", "flight_number": "AF-757", "from": "Saudia-Arabia", "to": "New Delhi",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "13138"},
            {	"airline": "GoAir", "flight_number": "AF-538", "from": "Saudia-Arabia", "to": "New Delhi",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "42781"},
            {	"airline": "Indigo", "flight_number": "AF-357", "from": "Saudia-Arabia", "to": "Mumbai",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "15437"},
            {	"airline": "Indigo", "flight_number": "AF-773", "from": "Saudia-Arabia", "to": "Mumbai",
                "departure": "18:00", "arrival": "20:00", "duration": "2", "cost": "24852"}
        ]
    }
