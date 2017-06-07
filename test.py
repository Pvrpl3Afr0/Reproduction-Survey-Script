import random #I'm thinking I'll need random lib for some rng
import time #Might need this?
import pygame #Considering using a graphical interface with pygame, not required#
womanslife = "According to the Pew Research Center, this country only offers abortions to a woman who's life in in danger"
physhealth = "is a country that also offers abortion for a woman's physical health"
mental = "Interestingly, this country offers abortions for the sake of a woman's mental health too."
assault = "offers legal abortions in cases of rape or incest, thankfully."
impairment = "offers abortions if there is fetal impairment"
socioeco = "This country offers legal abortions based on social / economic reasons"
request = ""


countryIndex = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan",
"Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia" "Bosnia and Herzegovina,", "Botswana,", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burma", "Burundi",
"Cambodia", "Cameroon", "Cabo Verde", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Democratic Republic of the Congo", "The Republic of Congo",
"Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Curacao", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor",
"Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "The Gambia",
"Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hong Kong",
"Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
"Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
"Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
"Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Namibia", "Nauru", "Nepal", "Netherlands",
"New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", " Oman", "Pakistan", "Palau", "Palestinian Territories", "Panama", "Papua New Guinea",
"Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
"Samoa", "San Marino", "San Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Sint Maarten",
"Slovakia", "Slovenia", "Solomon Islands", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden",
"Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
"Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Yemen", "Vietnam",
"Zambia", "Zimbabawe"]
continentIndex = ["Africa", "Antarctica", "Asia", "Australia", "Europe", "North America", "South America"]
#Instead of doing this Just make one big multi line List because this is bad
print("Welcome to our Reproductive Rights Survey, made by Marcus Wong and Henry Ramos!")
print("Here, we will ask you a variety of questions in order to inform you about Women's Reproductive Rights around the world.")


username = input("First, let's start with your name: ")
print("Nice to meet you," , username)
print("Okay, so now we'll pick a continent. Please be sure to capitalize the name! I.E Asia instead of asia.")
continentChoice = input("What continent is the country in? If you don't know, pick any!:  ")


if continentChoice == continentIndex[0]:
    print("So you'd like to learn more about ",continentIndex[0], "huh? Interesting!")
elif continentChoice == continentIndex[1]:
    print("So you'd like to learn more about",continentIndex[1], "huh? Cool choice!")
elif continentChoice == continentIndex[2]:
    print("So you'd like to learn more about",continentIndex[2], "huh? Alright!")
elif continentChoice == continentIndex[3]:
    print("So you'd like to learn more about",continentIndex[3], "huh? Cool choice!")
elif continentChoice == continentIndex[4]:
    print("So you'd like to learn more about",continentIndex[4], "huh? Let's do it!")
elif continentChoice == continentIndex[5]:
    print("So you'd like to learn more about",continentIndex[5], "huh? That's where we live!")
elif continentChoice == continentIndex[6]:
    print("So you'd like to learn more about",continentIndex[6], "huh? Interesting!")
else:
    print("Something went wrong, please make sure you spelled and formatted the continent properly!")
asia = ["Afghanistan", "Azerbaijan", "Armenia", "Bahrain", "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China", "Cyprus"]
asia2 = ["Georgia", "India", "Indonesia", "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait"]
asia3 = ["Kyrgyzstan", "Laos", "Lebanon","Malaysia", "Maldives", "Mongolia", "Myanmar", "Burma", "Nepal", "North Korea"]
asia4 = ["Oman", "Pakistan", "Palestine", "Philippines", "Qatar", "Russia", "Saudi Arabia", "Singapore", "South Korea", "Sri Lanka"]
asia5 = ["Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"]
na = ["United States,", "Canada", "Mexico"]
sa = ["Honduras", "Brazil", "Dominican Republic", "Haiti", "Cuba"]
eu = ["England", "Germany", "Spain", "France", "Ireland", "Sweden", "Poland"]
af = ["Egypt", "South Africa", "Morocco", "Congo", "Madagascar"]
au = ["New Zealand", "Fiji", "Guam", "Papua New Guinea", "Marshall Islands"]
countryChoice = input("Which country in your chosen continent would you like to learn about?:")
info = False
while not info:
    print("So you chose", countryChoice, "cool!")
    if countryChoice == "":
        print("Make sure you input something! Otherwise the code will run into an error.")
        info = True
    elif countryChoice == asia[0] or countryChoice == asia[4] or countryChoice == asia[6] or countryChoice == asia3[6] or countryChoice == asia4[3] or countryChoice == asia4[9] or countryChoice == asia5[4]:
        print(womanslife)
        info = True
    elif countryChoice == au[4] or countryChoice == au[3] or countryChoice == af[0] or countryChoice == eu[4] or countryChoice == sa[3] or countryChoice == sa[4]:
        print(womanslife)
        info = True
    elif countryChoice == af[4] or countryChoice == af[3] or countryChoice == asia5[4]:
        print(womanslife)
        info = True
    elif countryChoice == asia3[4]:
        print(physhealth)
        info = True
    elif countryChoice == asia3[3]:
        print(mental)
        info = True
    elif countryChoice == sa[1] or countryChoice == asia[5] or countryChoice == asia2[2] or countryChoice == asia4[0]:
        print(countryChoice, assault)
        info = True
    elif countryChoice == asia[9] or countryChoice == au[0] or countryChoice == asia4[8] or countryChoice == asia5[3] or countryChoice == eu[6] or countryChoice == asia2[7]:
        print(impairment)
        info = True
    elif countryChoice == au[1] or countryChoice == asia2[1] or countryChoice == asia2[6] or countryChoice == eu[0]:
        print(socioeco)
        info = True
    else:
        time.sleep(2)
        print("If you're seeing this message, it means one of two things. Either:")
        time.sleep(2)
        print("The country you input has all aforementioned Reproductive Rights! Everything from saving a woman's life to being purely out of request.")
        time.sleep(3)
        print("OR")
        print("It's possible that the country you input isn't in our index, meaning that we don't have data on it")
        correct = input("Can you verify that this country is what you wanted, and that it's spelled correctly? If you're not sure, call us over!: ")
        if correct == "yes" or correct == "Yes":
            print("Perfect! What this means is that this country has either all aforementioned rights, or simply that they're one of the 58 of 196 countries that allow abortions upon request.")
            info = True
        elif correct == "no" or "No":
            print("If you answered no and this country isn't in our index, that means that unfortunately we weren't able to get the required information in time")
            info = False
        else:
            print("Make sure you input either yes or No!")
print("Thank you for taking our informational program, hopefully you learned a valuable piece of information regaurding a country of your choice.")
time.sleep(5)
print("If you'd like to go again, simply let either Marcus or Henry know. Thanks again!")
