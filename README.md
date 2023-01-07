<!-- PROJECT LOGO -->
<br />
<div align="center" id="readme-top">
  <a href="https://github.com/tibogeeraerts/api-eindproject">
    <img src="images/logo.png" alt="Logo" width="200" height="150">
  </a>

  <h3 align="center">Eindproject API development</h3>

  <p align="center">
    Gemaakt door Tibo Geeraerts
    <br />
    <a href="https://github.com/tibogeeraerts/api-eindproject"><strong>Bekijk de bestanden »</strong></a>
    <br />
    <br />
    <a href="https://geeraertstibo-api-eindproject.netlify.app/">Front-end website</a>
    ·
    <a href="https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/docs">API docs website</a>
  </p>
</div>



<!-- Inhoudstafel -->
<details>
  <summary>Inhoudstafel</summary>
  <ol>
    <li>
      <a href="#gebouwd-met-">Gebouwd met</a>
    </li>
    <li>
      <a href="#over-dit-project">Over dit project</a>
      <ul>
        <li>
          <a href="#front-end-api">Front-end API</a>
          <ul>
             <li><a href="#login-front-end">Login front-end</li>
             <li><a href="#get-random-quote-front-end">Get random quote</li>
             <li><a href="#get-last-quote-front-end">Get last quote</li>
             <li><a href="#create-quote-front-end">Create quote</li>
             <li><a href="#get-all-quotes-front-end">Get all quotes</li>
             <li><a href="#get-current-admin-front-end">Get current admin</li>
             <li><a href="#get-all-characters-front-end">Get all characters</li>
             <li><a href="#create-admin-front-end">Create admin</li>
             <li><a href="#create-character-front-end">Create character</li>
          </ul>
        </li>
        <li>
          <a href="#back-end-api">Back-end API</a>
          <ul>
             <li><a href="#authorize-back-end">Authorization</li>
             <li><a href="#post-token-back-end">Post token</li>
             <li><a href="#post-custom-quote-back-end">Post custom quote</li>
             <li><a href="#get-all-quotes-back-end">Get all quotes</li>
             <li><a href="#get-random-quote-back-end">Get random quote</li>
             <li><a href="#get-last-quote-back-end">Get last quote</li>
             <li><a href="#put-last-quote-back-end">Put last quote</li>
             <li><a href="#delete-last-quote-back-end">Delete last quote</li>
             <li><a href="#get-current-admin-back-end">Get current admin</li>
             <li><a href="#post-new-admin">Post new admin</li>
             <li><a href="#get-admin-info-back-end">Get admin info</li>
             <li><a href="#delete-admin-met-username-back-end">Delete admin</li>
             <li><a href="#get-characters-back-end">Get characters</li>
             <li><a href="#post-character-back-end">Post character</li>
          </ul>
        </li>
      </ul>
    </li>
    <li>
      <a href="#postman-requests">Postman requests</a>
      <ul>
          <li><a href="#post-token-postman">Post token</li>
          <li><a href="#post-custom-quote-postman">Post custom quote</li>
          <li><a href="#get-all-quotes-postman">Get all quotes</li>
          <li><a href="#get-random-quote-postman">Get random quote</li>
          <li><a href="#get-last-quote-postman">Get last quote</li>
          <li><a href="#put-last-quote-postman">Put last quote</li>
          <li><a href="#delete-last-quote-postman">Delete last quote</li>
          <li><a href="#get-current-admin-postman">Get current admin</li>
          <li><a href="#post-admin-postman">Post admin</li>
          <li><a href="#get-admin-by-username-postman">Get admin info</li>
          <li><a href="#delete-admin-by-username-postman">Delete admin</li>
          <li><a href="#get-character-postman">Get characters</li>
          <li><a href="#post-character-postman">Post character</li>
        </ul>
    </li>
    <li><a href="#contactgegevens">Contactgegevens</a></li>
  </ol>
</details>


## Gebouwd met :

[![FastAPI][FastAPI.py]][FastAPI-url]
[![Python][Python.py]][Python-url]
[![Html][Html.html]][Html-url]
[![AlpineJS][Alpine.js]][Alpine-url]
[![Javascript][Bootstrap.css]][Bootstrap-url]


<!-- Over dit project -->
## Over dit project

Ik heb voor dit project gekozen om quotes uit de serie 'The Office' aan de gebruiker weer te geven. Er kan ook een admin worden aangemaakt om de pagina te bewerken. De admin kan ook karakters toevoegen aan de database en deze opvragen via de API. Ik heb gekozen voor deze serie omdat dit één van mijn favoriete series is, en er enrom veel grappige dingen in worden gezegd. De ideale serie om dus grappige quotes uit weer te geven. 

### Front-end API

[![screenshot van API front-end][frontend-screenshot]][frontend-url]

Dit is de home pagina van de front-end API. De layout van de pagina is gemaakt met Bootstrap en de inhoud wordt dynamisch weergegeven op basis van AlpineJS. Er zijn verschillende panelen waar de verschillende GET en POST endpoints van de API zijn. 4 panelen bevatten de GET en POST endpoints voor quotes van 'The Office'. 2 panelen bevatten de endpoints voor de admin, en 2 panelen bevatten de endpoints voor de karakters.

#### Login front-end
![Login front-end][login-frontend]
Bovenaan de pagina kan iemand met een admin username en password inloggen. Eens de admin is ingelogd kan deze ook de admin endpoints gebruiken.

#### Get random quote front-end
![Get random quote knop front-end][getrandomquote-frontend]

Als de gebruiker op deze knop drukt, wordt er een willekeurige quote uit de database gekozen en weergegeven. Er kan oneindig veel op de knop gedrukt worden er zal meestal een nieuwe quote verschijnen. Deze database met quotes bevat voor het grootste deel quotes uit 'The Office' zelf, maar er kunnen ook zelf quotes aan de database worden toegevoegd via de back-end API.

#### Get last quote front-end

![Get last quote knop front-end][getlastquote-frontend]

De get last quote knop kan worden ingedrukt om de laatste quote uit de database weer te geven aan de gebruiker. Deze knop is vooral bedoeld om te kijken of een zelf ingegeven quote in de database staat, aangezien deze helemaal als laatst in de database staat. Deze knop zal zonder aanpassing van de database altijd dezelfde quote weergeven.

#### Create quote front-end

![Create quote knop front-end][postquote-frontend]

De gebruiker kan ook zelf een quote opslaan in de database met de 'Create quote' knop. Er kan in het tekstveld boven de knop zelf een quote worden ingetoetst, en in de database worden opgeslagen door op de knop te drukken. Nadat er op de knop is gedrukt komt er onder de knop ook een bevestiging van welke quote er is opgeslagen in de database.

#### Get all quotes front-end

![Get all quotes knop front-end][getallquotes-frontend]

Deze knop geeft de eerste 50 quotes in de database weer. Dit zijn normaal gezien al de quotes in de database aangezien er bij het opstarten maar 20 quotes in de database worden gezet. Via de back-end API kunnen er quotes worden toegevoegd, maar als er meer dan 50 quotes in totaal zijn worden deze niet meer weergegeven.

#### Get current admin front-end
![Get current admin front-end][getcurrentadmin-frontend]

Als een admin is ingelogd, kan deze zijn eigen username opvragen via deze knop. Dit kan gebruikt worden om te controleren of de gebruiker als juiste gebruiker is ingelogd.

#### Get all characters front-end
![Get all characters front-end][getcharacters-frontend]

Een admin kan karakters aanmaken. Dit is een admin functie omdat het de bedoeling is dat enkel karakters uit de show worden aangemaakt en hier niet zomaar iets komt te staan. Als een admin is ingelogd kan deze een naam ingeven en via de knop deze naam in de database zetten.

#### Create admin front-end
![Create admin front-end][postadmin-frontend]

Als een gebruiker geen admin account heeft, dan kan deze dit account hier aanmaken. De gebruiker moet hier een naam en wachtwoord ingeven. Als de gekozen gebruikersnaam al bestaat zal hier de volgende melding voor verschijnen.

![Username error front-end][username-error-frontend]

#### Create character front-end
![Create character front-end][postcharacter-frontend]

Een ingelogde admin kan als laatste op de front-end, een karakter aanmaken. Zoals hierboven al vermeld is dit een admin functie, en is enkel de naam van het karakter nodig. Vervolgens kan met de blauwe knop het karakter worden opgeslagen in de database.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Back-end API

[![screenshot van API back-end][backend-screenshot]][backend-url]

Dit is de home pagina van de back-end API. Deze pagina is een interactieve API documentatie voorzien door Swagger UI. Deze interactieve pagina laat toe alle mogelijke eindpunten van de API aan te spreken op één plaats. Hier is te zien dat er 4 eindpunten zijn. 

#### Authorize back-end
Voor sommige zaken wordt er in deze API aan authorizatie gedaan. Dit gebeurd op basis van een OAuth2 token. In de back-end kan er worden ingelogd door op een open slot te drukken zoals hieronder. 

![Unauthorized sign][unauthorized-backend]

Vervolgens worden de normale stappen gevolgd om ergens in te loggen. Enkel een admin username en password volstaan hier.

![Authorization window empty][authorizeblank-backend]
![Authorization window filled][authorizefilled-backend]
![Authorization window response][authorizeresponse-backend]

Na deze stappen te doorlopen veranderd het origineel aangeklikte icoon naar een gesloten slot. Dit geeft aan dat de gebruiker is ingelogd.

![Authorized sign][authorized-backend]:

#### Post token back-end

![Post token back-end][posttoken-backend]

Dit POST endpoint van de API geeft een OAuth2 token terug. Dit token wordt op de achtergrond gebruikt om aan te geven of de request van een admin komt of niet.

#### Post custom quote back-end

![Post custom quote back-end][postquote-backend]

Via dit deel op de pagina kan er een nieuwe quote in de database worden gezet. Om dit te doen moet de gebruiker een POST request doen naar de API met in de body een "content" veld, waarachter een string moet komen, in JSON formaat. Wat de gebruiker in de string zet zal als quote gezien worden en zo in de database worden gezet. De API zal zelf de quote van een ID voorzien in de database.

#### Get all quotes back-end

![Get all quotes back-end][getallquotes-backend]

Via deze dropdown op de pagina kunnen alle quotes in de database worden opgevraagd. Er kan hier zelf worden gekozen bij welke quote er begonnen moet woren (skip), en hoeveel quotes er getoond moeten worden (limit). Als er vervolgens op de blauwe 'execute' knop wordt geklikt, dan zullen de quotes die binnen de geselecteerde parameters vallen weergegeven worden.

#### Get random quote back-end

![Get random quote back-end][getrandomquote-backend]

In dit deel van de docs pagina kan er een willekeurige quote worden gevraagd. Er zijn geen parameters nodig dus er moet enkel op de 'execute' knop worden gedrukt om een quote weer te geven. De quote zelf kan in de teruggestuurde body gelezen worden bij 'content'

#### Get last quote back-end

![Get last quote back-end][getlastquote-backend]

Ook bij deze request zijn er geen parameters nodig. Door hier op de 'execute' knop te drukken wordt de laatste quote uit de database opgevraagt. Als er dus een zelfgemaakte quote in de database is gezet, zal deze hier weergegeven worden.

#### Put last quote back-end

![Update last quote back-end][updatelastquote-backend]

Dit is een put request endpoint. Dit endpoint kan worden gebruikt om de laatste quote in de database aan te passen. Dit kan dus een zelfgemaakte quote zijn, maar ook een standaardquote. Er wordt enkel nieuwe content gevraagd voor deze quote.

#### Delete last quote back-end

![Delete last quote back-end][deletelastquote-backend]

Dit is het laatste endpoint voor de quotes van deze API. Met deze knop kan de laatste quote uit de database worden verwijderd, totdat de volledige tabel in de database leeg is. Zo kan een custom quote worden verwijderd als de gebruiker dit wilt. Er kunnen ook vooraf gegenereerde quotes worden verwijderd met deze knop.

#### Get current admin back-end

![Get current admin back-end][getcurrentadmin-backend]

Via deze endpoint kan een admin die is ingelogd op de API zijn eigen info opvragen. De info die de admin te zien krijgt is zijn ID in de database en zijn username, het wachtwoord wordt voor veiligheidsredenen niet weergegeven, en is standaard gehashed (onleesbaar voor de mens) in de database.

#### Post new admin back-end

![Post new admin back-end][postadmin-backend]

Aangezien er op deze API enkele beveiligingen zijn geïnstalleerd, waardoor enkel een admin gebruiker alle functionaliteiten heeft, is het handig dat iemand een admin gebruiker kan aanmaken. Dat kan met de post admin knop. Hier worden een username en password gevraagd, en door 'execute' aan te klikken, wordt de gebruiker in de database gezet. Nu kan de gebruiker inloggen met diezelfde gegevens voor admin rechten op de API.

#### Get admin info back-end

![Get admin info back-end][getadmininfo-backend]

Via deze endpoint kan de info van eender welke admin worden opgevraagd. Ook hier worden enkel het database ID en username weergegeven en niet het wachtwoord. Als een gebruiker zijn username bijvoorbeeld vergeten zou zijn, kan hij die op deze manier proberen terugvinden.

#### Delete admin met username back-end

![Delete admin met username back-end][deleteadmin-backend]

Elke admin die aangemaakt kan worden, moet ook kunnen verwijderd, daarom is deze endpoint er. Er kan een username in de URL worden meegegeven, en als deze bestaat, zal de admin volledig uit de database worden verwijderd. Deze endpoint wordt achterliggend ook gebruikt om de testadmins die door 'pytests' worden gebruikt te verwijderen.

#### Get characters back-end

![Get characters back-end][getcharacters-backend]

Elke admin kan karakters van de show toevoegen aan de database, en al deze karakters kunnen worden opgevraagd via deze endpoint.

#### Post character back-end

![Post character back-end][postcharacters-backend]

Als een admin graag zijn favoriete karakter van de show wilt toevoegen aan de database van deze API dan kan dat via deze endpoint. Hier wordt enkel de naam van het karakter gevraagd en via 'execute' wordt deze opgeslagen in de database.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Postman requests

Hier geef ik nog even een korte demonstratie hoe de verschillende endpoints via Postman gebruikt kunnen worden.

### Post token Postman
![Post token with Postman][posttoken-postman]

### Post custom quote Postman
![Post custom quote with Postman][postquote-postman]

### Get all quotes Postman
![Get all quotes with Postman][getall-postman]

### Get random quote Postman
![Get random quote with Postman][getrandom-postman]

### Get last quote Postman
![Get last quote with Postman][getlast-postman]

### Put last quote Postman
![Put last quote with Postman][putlast-postman]

### Delete last quote Postman
![Delete last quote with Postman][deletelast-postman]

### Get current admin Postman
![Get current admin with Postman][getcurrentadmin-postman]

### Post admin Postman
![Post admin with Postman][postadmin-postman]

### Get admin by username Postman
![Get admin by username with Postman][getadmininfo-postman]

### Delete admin by username Postman
![Delete admin by username with Postman][deleteadmin-postman]

### Get character Postman
![Get character with Postman][getcharacters-postman]

### Post character Postman
![Post character with Postman][postcharacter-postman]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Postman requests
![Pytest run][pytest-screenshot]

Om te testen dat al de endpoints van de API werken, is er ook een test bestand gemaakt. Dit bestand wordt gebruikt als het commando pytest wordt ingegeven. De test is geschreven om al de endpoints te testen en na te kijken of de juiste data wordt teruggegeven. Als alles gaat zoals het hoort wordt er een groene succes-boodschap weergegeven in de CLI waar het commando is uitgevoerd.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contactgegevens

Tibo Geeraerts - [@geeraerts_tibo](https://twitter.com/geeraerts_tibo) - r0882113@student.thomasmore.be

Front-end link: [https://geeraertstibo-api-eindproject.netlify.app/](https://geeraertstibo-api-eindproject.netlify.app/)

Hosted API link: [https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/docs](https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/docs)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[FastAPI.py]: https://img.shields.io/badge/-%F0%9F%97%B2%20FastAPI-019486?style=for-the-badge
[FastAPI-url]: https://fastapi.tiangolo.com/
[Python.py]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[Html.html]: https://img.shields.io/badge/HTML-E54C21?style=for-the-badge&logo=html5&logoColor=white
[Html-url]: https://www.w3schools.com/html/
[Alpine.js]: https://img.shields.io/badge/Alpine.js-77C1D2?style=for-the-badge&logo=javascript&logoColor=white
[Alpine-url]: https://alpinejs.dev/
[Bootstrap.css]: https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com/

[frontend-screenshot]: images/front-end-screenshot.png
[frontend-url]: https://geeraertstibo-api-eindproject.netlify.app/
[login-frontend]: images/login-front-end.jpg
[username-error-frontend]: images/username-error-frontend.jpg
[getrandomquote-frontend]: images/getrandomquote-front-end.jpg
[getlastquote-frontend]: images/getlastquote-front-end.jpg
[postquote-frontend]: images/postquote-front-end.jpg
[getallquotes-frontend]: images/getallquotes-front-end.jpg
[getcurrentadmin-frontend]: images/getcurrentadmin-front-end.jpg
[postadmin-frontend]: images/postadmin-front-end.jpg
[getcharacters-frontend]: images/getcharacters-front-end.jpg
[postcharacter-frontend]: images/postcharacter-front-end.jpg

[backend-screenshot]: images/back-end-screenshot.png
[backend-url]: https://api-eindproject-service-tibogeeraerts.cloud.okteto.net/docs
[postquote-backend]: images/postquote-back-end.jpg
[getallquotes-backend]: images/getallquotes-back-end.jpg
[getrandomquote-backend]: images/getrandomquote-back-end.jpg
[getlastquote-backend]: images/getlastquote-back-end.jpg
[posttoken-backend]: images/posttoken-back-end.png
[updatelastquote-backend]: images/updatelastquote-back-end.png
[deletelastquote-backend]: images/deletelastquote-back-end.png
[getcurrentadmin-backend]: images/getcurrentadmin-back-end.png
[postadmin-backend]: images/postadmin-back-end.png
[getadmininfo-backend]: images/getadmininfo-back-end.png
[deleteadmin-backend]: images/deleteadmin-back-end.png
[getcharacters-backend]: images/getcharacters-back-end.png
[postcharacters-backend]: images/postcharacter-back-end.png

[authorizeblank-backend]: images/authorize-blank-back-end.jpg
[authorizefilled-backend]: images/authorize-filled-back-end.jpg
[authorizeresponse-backend]: images/authorize-response-back-end.jpg
[unauthorized-backend]: images/unauthorized-back-end.jpg
[authorized-backend]: images/authorized-back-end.jpg

[posttoken-postman]: images/postman-posttoken.jpg
[postquote-postman]: images/postman-postquote.jpg
[getall-postman]: images/postman-getall.jpg
[getrandom-postman]: images/postman-getrandom.jpg
[getlast-postman]: images/postman-getlast.jpg
[putlast-postman]: images/postman-putquote.jpg
[deletelast-postman]: images/postman-deletequote.jpg
[getcurrentadmin-postman]: images/postman-getadmin.jpg
[postadmin-postman]: images/postman-postadmin.jpg
[getadmininfo-postman]: images/postman-getadmininfo.jpg
[deleteadmin-postman]: images/postman-deleteadmin.jpg
[getcharacters-postman]: images/postman-getcharacters.jpg
[postcharacter-postman]: images/postman-postcharacter.jpg

[pytest-screenshot]: images/pytest.jpg