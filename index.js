var fs = require('fs');
var array = fs.readFileSync('out.txt').toString().split(",");
var StringArray = array.toString().replace(/,/g, " ").replaceAll("]", " ").replaceAll("\'", "")
String.prototype.replaceAll = function(str1, str2, ignore) 
{
    return this.replace(new RegExp(str1.replace(/([\/\,\!\\\^\$\{\}\[\]\(\)\.\*\+\?\|\<\>\-\&])/g,"\\$&"),(ignore?"gi":"g")),(typeof(str2)=="string")?str2.replace(/\$/g,"$$$$"):str2);
} 

var characters = {
    table: []
 };

var letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z" ]

for(var letter in letters) {
    
    let count = 0
  
    for(var words in array){

        if(array[words].toString().includes(letters[letter])){
         
            var temp = `${letters[letter].toString().toLowerCase()}`;
            var re = new RegExp(temp, 'g');
        count += (array[words].toString().match(re)).length
         
        }
      
   
    }
    characters.table.push({letter: letters[letter], counts: count})
  console.log(`${letters[letter]}: ${count}`)
}
var json = JSON.stringify(characters);
var fs = require('fs');
fs.writeFile('myjsonfile.json', json, 'utf8', () => {
    console.log("wrote")
});

