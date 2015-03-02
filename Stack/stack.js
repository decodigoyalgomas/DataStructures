var Stack = function(){

    this.items = []
};

Stack.prototype.size = function(){return this.items.length}
Stack.prototype.isEmpty = function(){return this.items == []}
Stack.prototype.push = function(item){this.items.push(item)}
Stack.prototype.pop = function(item){ this.items.pop()}
Stack.prototype.peek = function(){return this.items[this.items.length-1]}
Stack.prototype.size = function(){return this.items.length}