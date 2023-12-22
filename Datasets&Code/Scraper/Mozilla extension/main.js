const cheerio = require('cheerio');
const request = require('request');

function readUrls(filename) {

	try {
		// read contents of the file
		const data = fs.readFileSync(filename, 'UTF-8');

		// split the contents by new line
		const lines = data.split(/\r?\n/);
		return lines;
	} catch (err) {
		console.error(err);
	}
}

function readSite(siteUrl) {
	request({
		method: 'GET',
		url: siteUrl
	}, (err, res, body) => {

		if (err) return console.error(err);
		
		let $ = cheerio.load(body);

		//let perms = $(".Permission-description").join()
		
		let perms = [];

		$('.Permission-description').each(function (i, e) {
			perms[i] = $(this).text();
		});

		//let name = $(".AddonTitle");
		let name = $(".RatingManager-legend").children().first().text();
		let summary = $(".Addon-summary").text();
		let usercount = $(".MetadataCard-content").first().text();
		let rating = $(".AddonMeta-rating-title").text().split(" ")[0];
		let version = $(".AddonMoreInfo-version").text();
		let size = $(".AddonMoreInfo-filesize").text();
		let lastupdated = $(".AddonMoreInfo-last-updated").text();
		
		console.log("Reading " + name + "...");
		console.log("\n");
		
		let permsstring = perms.join("; ");
		
		let datastring = "\"" + name + "\"";
		datastring = append(usercount,datastring);
		datastring = append(rating,datastring);
		datastring = append(version,datastring);
		datastring = append(size,datastring);
		datastring = append(lastupdated,datastring);
		datastring = append(summary,datastring);
		datastring = append(permsstring,datastring);
		datastring += "\n";
		
		fs.appendFile('output.csv', datastring, function (err) {
			if (err) throw err;
			console.log('Written to csv!\n');
		}); 
	});
}

function append(str, tostr) {
	return tostr + "," + "\"" + str + "\"";
}

const fs = require('fs');
var urls = readUrls("urls.txt");

fs.writeFile('output.csv', "Name,User,Rating,Version,Size,Last updated,Summary,Permissions\n", function (err) {
	if (err) throw err;
	console.log('Created output.csv!');
}); 


urls.forEach((url) => {
	//console.log(url);
	if(url.length > 5) {
		readSite(url);
	}
});

