var gplay = require('google-play-scraper');
var categories = [
  'WEATHER',

  'ART_AND_DESIGN',
  'AUTO_AND_VEHICLES',
  'BEAUTY',
  'BOOKS_AND_REFERENCE',
  'BUSINESS',
  'COMICS',
  'COMMUNICATION',
  'DATING',
  'EDUCATION',
  'ENTERTAINMENT',
  'EVENTS',
  'FINANCE',
  'FOOD_AND_DRINK',
  'HEALTH_AND_FITNESS',
  'HOUSE_AND_HOME',
  'LIBRARIES_AND_DEMO', 
 
  'LIFESTYLE',
  'MAPS_AND_NAVIGATION',
  'MEDICAL',
  'MUSIC_AND_AUDIO',
  'NEWS_AND_MAGAZINES',
  'PARENTING',
  'PERSONALIZATION',
  'PHOTOGRAPHY',
  'PRODUCTIVITY',
  'SHOPPING',
  'SOCIAL',
  'SPORTS',
  'TOOLS',
  'TRAVEL_AND_LOCAL',
  'VIDEO_PLAYERS',
  'ANDROID_WEAR',
  'WEATHER',
  'GAME',
  'GAME_ACTION',
  'GAME_ADVENTURE',
  'GAME_ARCADE',
  'GAME_BOARD',
  'GAME_CARD',
  'GAME_CASINO',
  'GAME_CASUAL',
  'GAME_EDUCATIONAL',
  'GAME_MUSIC',
  'GAME_PUZZLE',
  'GAME_RACING',
  'GAME_ROLE_PLAYING',
  'GAME_SIMULATION',
  'GAME_SPORTS',
  'GAME_STRATEGY',
  'GAME_TRIVIA',
  'GAME_WORD',
  'FAMILY',
  'FAMILY_ACTION',
  'FAMILY_BRAINGAMES',
  'FAMILY_CREATE',
  'FAMILY_EDUCATION',
  'FAMILY_MUSICVIDEO',
  'FAMILY_PRETEND',
  'APPLICATION'  
];

const fs = require('fs')


//gplay.categories().then(console.log);

function scraper(category){
    gplay.list({
        num: 10000,
        category: category,
		throttle:5
    }).then(function (result) {
        result.forEach(function (result) {
            gplay.permissions({appId: result.appId,throttle:5, short:false}).then(function (value) {
				gplay.app({appId: result.appId, throttle:5}).then(function(details){
                	fs.appendFile('ALL730.txt', 
						result.title + " | " + 
						category + " | " + 
						JSON.stringify(details.installs) + " | "  + 
						JSON.stringify(details.score) + " | " +  
						JSON.stringify(details.free) + " | " + 
						JSON.stringify(value) + "\n", function (err) {
						if (err) throw err;
						},console.log);
				}, console.log);
			}, console.log);
        })
    }, console.log);
}


fs.writeFile('output.txt', "", function (err) {
	if (err) throw err;
});

categories.forEach(function(element) {
	scraper(element);
});