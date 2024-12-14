import java.util.Stack;

class MyQueue {
    private Stack<Integer> stack_in;
    private Stack<Integer> stack_out;

    // Конструктор
    public MyQueue() {
        stack_in = new Stack<>();
        stack_out = new Stack<>();
    }
    
    // queue-ийн ард талд элемент нэмэх
    public void push(int x) {
        stack_in.push(x);
    }
    
    // queue-ийн урд талын элемент устгах
    public int pop() {
        moveElements();
        return stack_out.pop();
    }
    
    // queue-ийн урд талын элементийг харуулах
    public int peek() {
        moveElements();
        return stack_out.peek();
    }
    
    // queue хоосон эсэхийг шалгах
    public boolean empty() {
        return stack_in.isEmpty() && stack_out.isEmpty();
    }

    // stack_out хоосон бол stack_in-ээс шилжүүлэх
    private void moveElements() {
        if (stack_out.isEmpty()) {
            while (!stack_in.isEmpty()) {
                stack_out.push(stack_in.pop());
            }
        }
    }
}
