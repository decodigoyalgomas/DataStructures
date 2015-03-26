var Stack = function(){

    this.items = []
};

Stack.prototype.size = function(){
	return this.items.length
}
Stack.prototype.isEmpty = function(){
	return this.items.length == 0
}
Stack.prototype.push = function(item){
	this.items.push(item)
}
Stack.prototype.pop = function(item){
	return this.items.pop()
}
Stack.prototype.peek = function(){
	return this.items[this.items.length-1]
}
Stack.prototype.size = function(){
	return this.items.length
}



function revstring(word){
	s = new Stack();
	
	for(var letter in word){
		s.push(word[letter]);
	}
	var reverse =""	;
	
	while( !s.isEmpty() ){
		reverse += s.pop();
	}
	return reverse;
}

function parenthesisParser(symbolString){
	s = new Stack();
	var correspond = true;
	var index = 0;
	
	while( index < symbolString.length && correspond){
		var symbol = symbolString[index];
		
			
		if (symbol == "("){
			s.push(symbol);
		} else {
			if (s.isEmpty()){
				correspond = false;
			} else {
				s.pop();				
			}		
		}
		index++;
	}
	if (correspond && s.isEmpty() ){
		return true;
	} else {
		return false;
	}
	
}

function matches(open, close){
	var opens = "([{";
	var closes = ")]}";
	return opens.indexOf(open) == closes.indexOf(close)
}

function symbolParser(symbolString){
	s = new Stack();
	var correspond = true;
	var index = 0;
	
	while( index < symbolString.length && correspond){
		var symbol = symbolString[index];
		if ( "({[".indexOf(symbol) != -1 ){
			s.push(symbol);
		} else {
			if (s.isEmpty()){

				correspond = false;
			} else {
				var top = s.pop();				
				if (!matches(top, symbol)){

					correspond = false;
				}
			}		
		}
		index++;
	}
	if (correspond && s.isEmpty() ){
		return true;
	} else {
		return false;
	}
	
}
