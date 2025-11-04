class ArrayStack {
    constructor(maxSize = 10){
        this.stack = new Array(maxSize)
        this.top = -1
        this.maxSize = maxSize
    }

    push(data) {
        if(this.top >= this.maxSize - 1) {
            throw new Error("Stack overflow")
        }
        this.stack[++this.top] = data
    }

    pop(){
        if(this.isEmpty()){
            throw new Error("Stack underflow")
        }
        return this.stack[this.top--]
    }

    peek(){
        if(this.isEmpty()){
            throw new Error("Stack underflow")
        }
        return this.stack[this.top]
    }

    isEmpty() {
        return this.top === -1
    }

    size(){
        return this.top + 1
    }
}

const stack = new ArrayStack(5);
stack.push(1);
stack.push(2);
stack.push(3);
stack.push(4);
stack.push(5);
stack.pop();
stack.peek();
stack.size();

console.log(stack);