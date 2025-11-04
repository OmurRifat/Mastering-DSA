class ArrayQueue{
    constructor(size=10){
        this.queue = new Array(size);
        this.size = size;
        this.count = 0;
    }

    enqueue(data){
        if(this.isFull()){
            throw new Error("Queue is full");
        }
        this.queue[this.count++] = data;
    }

    dequeue(){
        if(this.isEmpty()){
            throw new Error("Queue is empty");
        }

        const front = this.queue[0];
        for(let i = 1; i< this.count; i++){
            this.queue[i-1] = this.queue[1];
        }
        this.count--;
        return front;
    }

    peek(){
        return this.count > 0? this.queue[0] : null;
    }

    isEmpty(){
        return this.count ===0;
    }

    isFull(){
        return this.count === this.size;
    }
}