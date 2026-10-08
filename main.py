from pyscript import document

nicknames = {
    "brunei": "The Land of Unexpected Treasures",
    "cambodia": "Land of the Khmer",
    "indonesia": "The Emerald of the Equator",
    "laos": "The Land of a Million Elephants",
    "malaysia": "Land of Indigenous Malay",
    "myanmar": "The Land of the Golden Pagoda",
    "philippines": "The Pearl of the Orient Seas",
    "singapore": "The Lion City",
    "thailand": "The Land of Smiles",
    "timor-leste": "The Land of Loro Sae",
    "vietnam": "The Land of the Blue Dragon",

}

def show_nickname(e):
    country = document.querySelector("#country").value

    nickname = nicknames.get(
        country, "Please select a country"
    )

    document.querySelector("#result").innerText = nickname