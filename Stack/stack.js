var Stack = function(){

    this.items = []
};

Stack.prototype.size = function(){return this.items.length}
Stack.prototype.isEmpty = function(){return this.size() == 0 }
Stack.prototype.push = function(item){this.items.push(item)}
Stack.prototype.pop = function(item){ return this.items.pop()}
Stack.prototype.peek = function(){return this.items[this.items.length-1]}
Stack.prototype.size = function(){return this.items.length}



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