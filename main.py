
import random
import colorama
from colorama import Fore, Back, Style, init

capitals = {
    "Afghanistan": "Kabul",
"Albania": "Tirana",
"Algeria": "Algiers",
"Andorra": "Andorra la Vella",
"Angola": "Luanda",
"Antigua and Barbuda": "St. John's",
"Argentina": "Buenos Aires",
"Armenia": "Yerevan",
"Australia": "Canberra",
"Austria": "Vienna",
"Azerbaijan": "Baku",
"Bahamas": "Nassau",
"Bahrain": "Manama",
"Bangladesh": "Dhaka",
"Barbados": "Bridgetown",
"Belarus": "Minsk",
"Belgium": "Brussels",
"Belize": "Belmopan",
"Benin": "Porto-Novo",
"Bhutan": "Thimphu",
"Bolivia": "Sucre",
"Bosnia and Herzegovina": "Sarajevo",
"Botswana": "Gaborone",
"Brazil": "Brasilia",
"Brunei": "Bandar Seri Begawan",
"Bulgaria": "Sofia",
"Burkina Faso": "Ouagadougou",
"Burundi": "Gitega",
"Cabo Verde": "Praia",
"Cambodia": "Phnom Penh",
"Cameroon": "Yaoundé",
"Canada": "Ottawa",
"Central African Republic": "Bangui",
"Chad": "N'Djamena",
"Chile": "Santiago",
"China": "Beijing",
"Colombia": "Bogotá",
"Comoros": "Moroni",
"Congo (Republic)": "Brazzaville",
"Congo (Democratic Republic)": "Kinshasa",
"Costa Rica": "San José",
"Cote d'Ivoire": "Yamoussoukro",
"Croatia": "Zagreb",
"Cuba": "Havana",
"Cyprus": "Nicosia",
"Czech Republic": "Prague",
"Denmark": "Copenhagen",
"Djibouti": "Djibouti",
"Dominica": "Roseau",
"Dominican Republic": "Santo Domingo",
"Ecuador": "Quito",
"Egypt": "Cairo",
"El Salvador": "San Salvador",
"Equatorial Guinea": "Malabo",
"Eritrea": "Asmara",
"Estonia": "Tallinn",
"Eswatini": "Mbabane",
"Ethiopia": "Addis Ababa",
"Fiji": "Suva",
"Finland": "Helsinki",
"France": "Paris",
"Gabon": "Libreville",
"Gambia": "Banjul",
"Georgia": "Tbilisi",
"Germany": "Berlin",
"Ghana": "Accra",
"Greece": "Athens",
"Grenada": "St. George's",
"Guatemala": "Guatemala City",
"Guinea": "Conakry",
"Guinea-Bissau": "Bissau",
"Guyana": "Georgetown",
"Haiti": "Port-au-Prince",
"Honduras": "Tegucigalpa",
"Hungary": "Budapest",
"Iceland": "Reykjavik",
"India": "New Delhi",
"Indonesia": "Jakarta",
"Iran": "Tehran",
"Iraq": "Baghdad",
"Ireland": "Dublin",
"Israel": "Jerusalem",
"Italy": "Rome",
"Jamaica": "Kingston",
"Japan": "Tokyo",
"Jordan": "Amman",
"Kazakhstan": "Astana",
"Kenya": "Nairobi",
"Kiribati": "Tarawa",
"Korea (North)": "Pyongyang",
"Korea (South)": "Seoul",
"Kuwait": "Kuwait City",
"Kyrgyzstan": "Bishkek",
"Laos": "Vientiane",
"Latvia": "Riga",
"Lebanon": "Beirut",
"Lesotho": "Maseru",
"Liberia": "Monrovia",
"Libya": "Tripoli",
"Liechtenstein": "Vaduz",
"Lithuania": "Vilnius",
"Luxembourg": "Luxembourg City",
"Madagascar": "Antananarivo",
"Malawi": "Lilongwe",
"Malaysia": "Kuala Lumpur",
"Maldives": "Malé",
"Mali": "Bamako",
"Malta": "Valletta",
"Marshall Islands": "Majuro",
"Mauritania": "Nouakchott",
"Mauritius": "Port Louis",
"Mexico": "Mexico City",
"Micronesia": "Palikir",
"Moldova": "Chisinau",
"Monaco": "Monaco",
"Mongolia": "Ulaanbaatar",
"Montenegro": "Podgorica",
"Morocco": "Rabat",
"Mozambique": "Maputo",
"Myanmar": "Naypyidaw",
"Namibia": "Windhoek",
"Nauru": "Yaren",
"Nepal": "Kathmandu",
"Netherlands": "Amsterdam",
"New Zealand": "Wellington",
"Nicaragua": "Managua",
"Niger": "Niamey",
"Nigeria": "Abuja",
"North Macedonia": "Skopje",
"Norway": "Oslo",
"Oman": "Muscat",
"Pakistan": "Islamabad",
"Palau": "Ngerulmud",
"Panama": "Panama City",
"Papua New Guinea": "Port Moresby",
"Paraguay": "Asunción",
"Peru": "Lima",
"Philippines": "Manila",
"Poland": "Warsaw",
"Portugal": "Lisbon",
"Qatar": "Doha",
"Romania": "Bucharest",
"Russia": "Moscow",
"Rwanda": "Kigali",
"Saint Kitts and Nevis": "Basseterre",
"Saint Lucia": "Castries",
"Saint Vincent and the Grenadines": "Kingstown",
"Samoa": "Apia",
"San Marino": "San Marino",
"Sao Tome and Principe": "São Tomé",
"Saudi Arabia": "Riyadh",
"Senegal": "Dakar",
"Serbia": "Belgrade",
"Seychelles": "Victoria",
"Sierra Leone": "Freetown",
"Singapore": "Singapore",
"Slovakia": "Bratislava",
"Slovenia": "Ljubljana",
"Solomon Islands": "Honiara",
"Somalia": "Mogadishu",
"South Africa": "Pretoria",
"South Sudan": "Juba",
"Spain": "Madrid",
"Sri Lanka": "Sri Jayawardenepura Kotte",
"Sudan": "Khartoum",
"Suriname": "Paramaribo",
"Sweden": "Stockholm",
"Switzerland": "Bern",
"Syria": "Damascus",
"Taiwan": "Taipei",
"Tajikistan": "Dushanbe",
"Tanzania": "Dodoma",
"Thailand": "Bangkok",
"Timor-Leste": "Dili",
"Togo": "Lomé",
"Tonga": "Nuku'alofa",
"Trinidad and Tobago": "Port of Spain",
"Tunisia": "Tunis",
"Turkey": "Ankara",
"Turkmenistan": "Ashgabat",
"Tuvalu": "Funafuti",
"Uganda": "Kampala",
"Ukraine": "Kyiv",
"United Arab Emirates": "Abu Dhabi",
"United Kingdom": "London",
"United States": "Washington, D.C.",
"Uruguay": "Montevideo",
"Uzbekistan": "Tashkent",
"Vanuatu": "Port Vila",
"Vatican City": "Vatican City",
"Venezuela": "Caracas",
"Vietnam": "Hanoi",
"Yemen": "Sanaa",
"Zambia": "Lusaka",
"Zimbabwe": "Harare"


}



import os
import random  # Import random module for random.choice
from colorama import Fore, Style, init

# Initialize colorama (for cross-platform compatibility)
init()

def colorize_ascii_top_green_white_blue(ascii_art):
    colored_art = ""
    # Split the ASCII art into lines
    lines = ascii_art.split("\n")
    
    # Apply colors to different parts of the ASCII art (two lines per color)
    for i, line in enumerate(lines):
        if i % 6 < 2:  # First 2 lines red
            colored_art += Fore.RED + line + Style.RESET_ALL + "\n"
        elif i % 6 < 4:  # Next 2 lines blue
            colored_art += Fore.BLUE + line + Style.RESET_ALL + "\n"
        else:  # Next 2 lines white
            colored_art += Fore.WHITE + line + Style.RESET_ALL + "\n"

    return colored_art

# ASCII Art (This can be modified to be any text art you want)
ascii_art = """
 ██████╗ █████╗ ██████╗ ██╗████████╗ █████╗ ██╗          ██████╗ ██╗   ██╗███████╗███████╗███████╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔══██╗██║         ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗
██║     ███████║██████╔╝██║   ██║   ███████║██║         ██║  ███╗██║   ██║█████╗  ███████╗███████╗█████╗  ██████╔╝
██║     ██╔══██║██╔═══╝ ██║   ██║   ██╔══██║██║         ██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║     ██║   ██║   ██║  ██║███████╗    ╚██████╔╝╚██████╔╝███████╗███████║███████║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                                  
 [Made By Morvixent] ---> https://github.com/Morvixent
"""

# Get the ASCII art with applied colors
ascii_art_with_color = colorize_ascii_top_green_white_blue(ascii_art)

# Print the colored ASCII art
print(ascii_art_with_color)


def ask_question(asked_countries, country_list):
    # If all countries have been asked, reset the asked countries list
    if len(asked_countries) == len(country_list):
        print("\nYou've answered all the countries. Let's restart the questions.")
        asked_countries.clear()

    # Randomly pick a country from the dictionary, excluding those already asked
    remaining_capitals = list(set(country_list) - asked_countries)
    country, capital = random.choice(remaining_capitals)
    
    # Ask the user to guess the capital
    answer = input(f"What is The Capital of {country}? ").strip()
    
    # Check if the answer is correct
    if answer.lower() == capital.lower():
        # Correct answer: green color
        print("\033[92mCorrect!\033[0m")  # \033[92m is green, \033[0m resets color
    else:
        # Wrong answer: red color
        print(f"\033[91mWrong! The Correct Answer Is {capital}.\033[0m")  # \033[91m is red
    
    # Add the country to the list of asked countries
    asked_countries.add((country, capital))

def main():
    # Clear the terminal screen before printing the ASCII art
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Print the colored ASCII art
    print(ascii_art_with_color)
    
    asked_countries = set()  # Set to keep track of asked countries
    country_list = list(capitals.items())  # Create a list of country-capital pairs
    
    # Ask the user how many capitals they want to guess
    while True:
        try:
            num_questions = int(input("How Many Capitals Do You Want To Guess? (Enter 0 for infinite): "))
            if num_questions < 0:
                print("Please enter a positive number or 0 for infinite.")
                continue
            break
        except ValueError:
            print("Please Enter A Valid Number.")
    
    # Infinite loop if the user wants to guess an infinite number of capitals
    if num_questions == 0:
        print("You can keep guessing capitals forever! Type 'exit' to stop.")
        while True:
            ask_question(asked_countries, country_list)
            # Check if the user wants to exit
            exit_check = input("Do you want to continue? Type 'exit' to stop or press Enter to continue: ").strip().lower()
            if exit_check == 'exit':
                break
    else:
        # Ask the specified number of questions
        for _ in range(num_questions):
            ask_question(asked_countries, country_list)

if __name__ == "__main__":
    main()
